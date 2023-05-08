##import modules
from psychopy import visual, gui, event, core, data
import os, numpy, random, time, pandas

##speedy mode
speedy = False #True/False. For piloting purposes (not required to incorporate)

##file management & dlg box
info = {'ParticipantNr':0, 'ParticipantName':'', 'age':0, 'SelfReportedGender':['male','female','x'], 'handedness':['right','left','ambidexter']} #Dictionary for dlg box

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'Visual Search Task Task') #Present a dlg box
    if not os.path.isdir(os.getcwd() + '/ParticipantData/'): #Create this folder if it does not exist yet
        os.mkdir(os.getcwd() + '/ParticipantData/')
    FileName = os.getcwd() + '/ParticipantData/' + 'XSearchTask_Participant' + str(info['ParticipantNr'])

    if not dlg.OK: #Quit the experiment if 'Cancel' is selected
        core.quit()

    if not os.path.isfile(FileName + '.csv'): #Only escape the while loop if ParticipantNr is unique
        AlreadyExists = False
    else:
        dlg2 = gui.Dlg(title = 'Error') #If the ParticipantNr is not unique, present an error msg
        dlg2.addText('This ParticipantNr is in use already, please select another')
        dlg2.show()

ParticipantName = info['ParticipantName'].split()[0].capitalize()
info.pop('ParticipantName') #GDPR

ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info) #To use the ExperimentHandler (a class for keeping track of multiple loops/handlers)

##design & randomnization
NrOfBlocks = 2
NrOfTrialsPerBlock = 24
ResponseButtonsList = ['f','j'] #Changes in this variable should accordingly change the instructions
ResponseButtonsList.append('escape') #Just to make sure that escape is also tracked

#These two variables need to be taken into account when creating the design
TrialOptions = numpy.array(["XO      +      OO","OX      +      OO","OO      +      XO","OO      +      OX"]) #4 types of trials
AreYouReadyDurationOptions = numpy.array([.8,1,1.2]) #3 durations in seconds

UniqueTrialsArray = numpy.array(range(len(TrialOptions) * len(AreYouReadyDurationOptions))) 

#Create the factorial design
AreYouReadyDurations = numpy.floor(UniqueTrialsArray / len(TrialOptions)) % len(AreYouReadyDurationOptions) #0-0-0-0-1-1-1-1-2-2-2-2
TrialTypes = numpy.floor(UniqueTrialsArray / 1) % len(TrialOptions) #0-1-2-3-0-1-2-3-0-1-2-3

#Combine arrays in trial matrix
BlockNr = numpy.repeat(0, len(UniqueTrialsArray)) #Just a 'placeholder' array to be added to the matrix. The 0s will be overwritten
CorResp = numpy.copy(BlockNr) #Also just a placeholder
UniqueTrialsArray = numpy.column_stack([AreYouReadyDurations, TrialTypes, BlockNr, CorResp]) #The size of this array corresponds to one repetition of all unique trials (TrialTypes and AreYouReadyDurations columns are already informative)

if info['ParticipantNr'] % 2 == 0: #Here we are filling the CorResp column
    UniqueTrialsArray[:, 3] = numpy.floor(UniqueTrialsArray[:, 1] / 2) #Even participants should respond to "XO+OO","OX+OO" with the 'left button', to other targets with the 'right button'. We code this by making sure that TrialTypes 0 and 1 lead to 0, and 2 and 3 lead to 1
else:
    UniqueTrialsArray[:, 3] = UniqueTrialsArray[:, 1] % 2 #Odd participants should respond to "XO+OO","OO+XO" with the 'left button', to others with the 'right button'. We code this by making sue that 0 and 2 lead to 0, and 1 and 3 to 1

BlockTrialsArray = numpy.tile(UniqueTrialsArray, (int((NrOfTrialsPerBlock/len(UniqueTrialsArray))),1)) #The size of this array corresponds to all trials within a single block (TrialTypes, AreYouReadyDurations, CorResp columns are already informative)

FullExperimentTrialsArray = numpy.ones(((NrOfBlocks*NrOfTrialsPerBlock), numpy.shape(BlockTrialsArray)[1])) #An array with placeholders. It has the nr of rows of the entire experiment, and the same nr of columns as BlockTrialsArray

for BlockNr in range(NrOfBlocks): #The actual randomnization of the trials per block takes place here
    FullExperimentTrialsArray_CurrentRowNrs = numpy.array(range(len(BlockTrialsArray))) + (BlockNr * len(BlockTrialsArray)) #For the first block, the array is 0-23, for the second, 24-47, for the third, 48-71, ...

    numpy.random.shuffle(BlockTrialsArray) #Without shuffling we have the exact same order for each series of 12 trials... Thanks to the looping here, we have different trial orders between blocks
    FullExperimentTrialsArray[FullExperimentTrialsArray_CurrentRowNrs, :] = BlockTrialsArray #Store the trials for this block in the FullExperimentTrialsArray array
    FullExperimentTrialsArray[FullExperimentTrialsArray_CurrentRowNrs, 2] = BlockNr + 1 #Fill in the block nr (Python starts at 0)

##validate the randomization
FullExperimentTrialsArrayDataFrame = pandas.DataFrame.from_records(FullExperimentTrialsArray) #Create DataFrame first. This DataFrame is needed for the crosstab and for creating the dictionairy input (i.e., TrialListMainExperiment) of the TrialHandler of the main experiment
FullExperimentTrialsArrayDataFrame.columns = ['AreYouReadyDurations', 'TrialTypes', 'BlockNr', 'CorResp'] #Add column names to FullExperimentTrialsArrayDataFrame
print(pandas.crosstab(FullExperimentTrialsArrayDataFrame.TrialTypes, FullExperimentTrialsArrayDataFrame.AreYouReadyDurations)) #Print the cross table validation

PracticeArrayDataFrame = pandas.DataFrame.from_records(UniqueTrialsArray) #This DataFrame is needed for creating the dictionaire input (i.e., TrialListPractice) of the TrialHandler of the practice phase (contains all the unique trials, 1x)
PracticeArrayDataFrame.columns = ['AreYouReadyDurations', 'TrialTypes', 'BlockNr', 'CorResp'] #Add column names to PracticeArrayDataFrame

##TrialHandler
TrialListMainExperiment = pandas.DataFrame.to_dict(FullExperimentTrialsArrayDataFrame, orient = 'records') #Convert dataframe to list of dictionaries (this will be the input for the TrialHandler of the main experiment)
TrialListPractice = pandas.DataFrame.to_dict(PracticeArrayDataFrame, orient = 'records') #We are doing the same conversion here, now for the practice phase (this will be the input for the TrialHandler of the practice phase)

##Initialize clock, response, window, and stimuli properties
RTClock = core.Clock() #Initialize the clock

win = visual.Window(size = [800, 800], units = 'norm', colorSpace = 'rgb', color = 'yellow')
MessageToParticipant = visual.TextStim(win, text = '', height = .07, color = 'black')
AreYouReadyMessage = visual.TextStim(win, text = 'Are you ready?', height = .1, color = 'black')
TrialInformation = visual.TextStim(win, text = '', height = .1, color = 'black')
box = visual.Rect(win, size = [.2, .2], lineColor = 'black', fillColor = 'yellow')
feedback = visual.TextStim(win, text = '', color = 'black', height = .1)

##Present the welcome text, task instructions, practice start text
WelcomeText = 'Hi {}!\n\nWelcome to this experiment!\n\nWe will explain the task to you on the next screen.\n\n[Press space to continue]'.format(ParticipantName)
InstructionsText = 'In this task, you will see the message \'Are you ready\' in each trial.\n\n'\
'Next, you need to respond to the location of the X as fast and accurate as possible.\n\nPress {0} with your left index finger if the X is presented left {1}, '\
'press {2} with your right index finger if the X is presented right {1}.\n\nGood luck!\n\n[Press space to continue]'.format(ResponseButtonsList[0].upper(), ['at the screen', 'within the box'][info['ParticipantNr'] % 2], ResponseButtonsList[1].upper())
PracticeStartText = 'We start with a short practice phase now.\n\n[Press space to continue]'

for message in [WelcomeText, InstructionsText, PracticeStartText]:
    MessageToParticipant.text = message
    MessageToParticipant.draw()
    win.flip()
    if not speedy:
        event.waitKeys(keyList = ['space'])

##Present the experiment
for ExperimentPhase in ['practice','main']:
    if ExperimentPhase == 'practice':
        trials = data.TrialHandler(TrialListPractice, nReps = 1, method = 'random') #We need to randomnize here, because this wasn't done yet (in contrast to TrialListMainExperiment)
        ThisExp.addLoop(trials) #As 'trials' can differ, we here tell whether the information from TrialListPractice or TrialListMainExperiment should be presented in the trials loop + we can set nReps and method (btw, here the ExperimentHandler and TrialHandler are connected to each other)
    else:
        MessageToParticipant.text = 'The practice phase is finished, we start with the main experiment now.\n\nThere are {} blocks in total, you will receive a short break after each block.\n\n'\
        'Remember, try to respond as fast and accurate as possible.\n\nGood luck!\n\n[Press space to continue]'.format(NrOfBlocks)
        MessageToParticipant.draw()
        win.flip()
        if not speedy:
            event.waitKeys(keyList = ['space'])

        trials = data.TrialHandler(TrialListMainExperiment, nReps = 1, method = 'sequential')
        ThisExp.addLoop(trials) #As 'trials' can differ, we here tell whether the information from TrialListPractice or TrialListMainExperiment should be presented in the trials loop + we can set nReps and method (btw, here the ExperimentHandler and TrialHandler are connected to each other)
    
    for trial in trials:
        trials.addData('PerformedTask', ['ScreenTask','BoxTask'][info['ParticipantNr'] % 2]) #Register the performed task
        trials.addData('ExperimentPhase', ExperimentPhase) #Register the experiment phase

        AreYouReadyMessage.draw()
        win.flip()
        if not speedy:
            core.wait(AreYouReadyDurationOptions[int(trial['AreYouReadyDurations'])])

        trials.addData('AreYouReadyDurationOptions', (AreYouReadyDurationOptions[int(trial['AreYouReadyDurations'])]*1000)) #Register the duration of the 'are you ready'-screen, written in full, in ms

        TrialInformation.text = TrialOptions[int(trial['TrialTypes'])]
        trials.addData('TrialType', TrialInformation.text.replace(' ', '')) #Register the trial information, written in full... Instead of .replace() you can also use TrialOptionsWithoutSpaces = numpy.array(["XO+OO","OX+OO","OO+XO","OO+>OX"]) and trials.addData('TrialInformation', TrialOptionsWithoutSpaces[int(trial['TrialTypes'])]) to get rid of the spaces

        box.pos = [-.285, 0] #I tried some X-values to obtain decent allignment, it's perfectly fine for the test if the targets are not exactly in the middle of the box
        box.draw() #Draw the boxes first, otherwise it will cover the trial information
        box.pos *= -1
        box.draw()
        TrialInformation.draw()
        win.flip()
        
        if not speedy:
            RTClock.reset()
            keys = event.waitKeys(keyList = ResponseButtonsList, maxWait = 2)
            RT = round(RTClock.getTime() * 1000) #In ms

            if keys: #'Truthy variable' (= a value that is considered True when encountered in a Boolean context)
                if keys[0] == 'escape': #To escape the trial loop
                    break
                else:
                    trials.addData('PerformedResponse', keys[0]) #Register which button was pressed
                    accuracy = (keys[0] == ResponseButtonsList[int(trial['CorResp'])]) * 1
                    feedback.text = ['error','correct'][accuracy]
                    feedback.color = ['red','green'][accuracy]
            else:
                feedback.text = 'too late'
                feedback.color = 'red'
                RT = -1 #Will overwrite the value of RT in case of a too late response

            trials.addData('RT', RT) #Register RT
            trials.addData('Accuracy', feedback.text) #Register the accuracy, written in full

        trials.addData('CorrectResponse', ResponseButtonsList[int(trial['CorResp'])]) #Register what would have been the correct response

        feedback.draw()
        win.flip()
        if not speedy:
            core.wait(.75)

        ThisExp.nextEntry() #Let the ExperimentHandler proceed to the next trial (now it knows that next .addData() calls correspond to the next trial)

        if ExperimentPhase == 'main' and (trials.thisN + 1) % NrOfTrialsPerBlock == 0:
            if not trials.thisN == len(TrialListMainExperiment)-1: #Participants should receive another msg after the last block has finished
                MessageToParticipant.text = 'You can have a break now.\n\n[Press space to continue]'
            else:
                MessageToParticipant.text = 'Thank you for participating!\n\n[Press space to finish the experiment]'
            MessageToParticipant.draw()
            win.flip()
            if not speedy:
                event.waitKeys(keyList = ['space'])

    if not speedy:
        if keys:
            if keys[0] == 'escape': #To escape the ExperimentPhase loop
                break

ThisExp.close() #Let the ExperimentHandler know that it's finished
win.close()