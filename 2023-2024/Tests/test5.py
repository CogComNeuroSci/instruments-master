##import modules
from psychopy import visual, gui, event, core, data
import os, numpy, random, time, pandas, random

##speedy mode
speedy = False #True/False. For piloting purposes. Not required to incorporate according to the test instructions.

##file management & dlg box
info = {'Participant number': random.randint(0,999), 'age': 0, 'Handedness': ['right','left','ambidexter']} #Dictionary for dlg box

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'Parity/Color Task') #Present a dlg box

    if not os.path.isdir(os.getcwd() + '/LetterNumberTaskData/'): #Create this folder if it does not exist yet
        os.mkdir(os.getcwd() + '/LetterNumberTaskData/')
    FileName = os.getcwd() + '/LetterNumberTaskData/' + 'ParticipantNr_' + str(info['Participant number'])

    if not dlg.OK: #Quit the experiment if 'Cancel' is selected
        core.quit()

    if not os.path.isfile(FileName + '.csv'): #Only escape the while loop if ParticipantNr is unique
        AlreadyExists = False
    else:
        dlg2 = gui.Dlg(title = 'Error') #If the ParticipantNr is not unique, present an error msg
        dlg2.addText('Select another participant number!')
        dlg2.show()

ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info) #To use the ExperimentHandler (a class for keeping track of multiple loops/handlers)

##design & randomnization
NrOfBlocks = 3
NrOfTrialsPerBlock = 48
ResponseButtonsList = ['f','j'] #Changes in this variable should accordingly change the instructions
ResponseButtonsList.append('escape') #Just to make sure that escape is also tracked

#These variables need to be taken into account when creating the design
TaskOptions = numpy.array(['LETTER','NUMBER']) #2 questions
NumberOptions = numpy.array([1,2,3,4,5,6]) #6 numbers
LetterOptions = numpy.array(['A','B','E','C']) #4 letters (2*6*4 = 48 unique trials) #With this specific order A-B-E-C it was easier to infer the correct response via the modulo (goal: left for vowel, right for consonant)

UniqueTrialsArray = numpy.array(range(len(TaskOptions) * len(NumberOptions) * len(LetterOptions))) 

#Create the factorial design
tasks = numpy.floor(UniqueTrialsArray / (len(NumberOptions) * len(LetterOptions))) % len(TaskOptions) #[0-0-0-...-1-1-1]
numbers = numpy.floor(UniqueTrialsArray / len(LetterOptions)) % len(NumberOptions) #[0-0-0-0-1-1-1-1-2-2-2-2-...]
letters = numpy.floor(UniqueTrialsArray / 1) % len(LetterOptions) #[0-1-2-3-0-1-2-3-...]

#Combine arrays in trial matrix
CorResp = numpy.repeat(0, len(UniqueTrialsArray)) #Just a 'placeholder' array to be added to the matrix. The 0s will be overwritten

UniqueTrialsArray = numpy.column_stack([tasks, numbers, letters, CorResp, UniqueTrialsArray]) #The size of this array corresponds to one repetition of all unique trials
BlockTrialsArray = numpy.tile(UniqueTrialsArray, (int(NrOfTrialsPerBlock/len(UniqueTrialsArray)),1)) #The size of this array corresponds to all trials within a single block

FullExperimentTrialsArray = numpy.ones(((NrOfBlocks*NrOfTrialsPerBlock), numpy.shape(BlockTrialsArray)[1] + 1)) #An array with placeholders. It has the nr of rows of the entire experiment, and the same nr of columns as BlockTrialsArray + 1 (the + 1 is to add the block nr)

for BlockNr in range(NrOfBlocks): #The actual randomnization of the trials per block takes place here
    FullExperimentTrialsArray_CurrentRowNrs = numpy.array(range(len(BlockTrialsArray))) + (BlockNr * len(BlockTrialsArray)) #CHANGE!!! ALSO OTHER VERSION TEST!!! For the first block the array is 0-35, for the second 36-71

    stop = True
    while stop:
        numpy.random.shuffle(BlockTrialsArray) #Without shuffling we have the exact same order for each series of trials... Thanks to the looping here, we have different trial orders between blocks

        if numpy.sum(numpy.diff(BlockTrialsArray[:,4]) == 0) == 0: #Check whether the column with unique trial identifiers (the last one of this array) is not repeated between two subsequent lines
            stop = False #With this approach, we also prevent for trial repetitions after scaling up to e.g., 96 trials per block

    FullExperimentTrialsArray[FullExperimentTrialsArray_CurrentRowNrs, :numpy.shape(BlockTrialsArray)[1]] = BlockTrialsArray #Store the trials of a block in FullExperimentTrialsArray
    
    for TrialNr in range((BlockNr * len(BlockTrialsArray)), (len(BlockTrialsArray) * (BlockNr+1))): #Here we decide what the CorResp (4th column/column nr 3) should be
        if FullExperimentTrialsArray[TrialNr, 0] == 0: #Letter task
            FullExperimentTrialsArray[TrialNr, 3] = FullExperimentTrialsArray[TrialNr, 2] % 2 #The CorResp is decided by letters. A/E = vowel, B/C = consonant. Thanks to the order of LetterOptions (A-B-E-C), we can now go via the modulo
        else: #Number task
            FullExperimentTrialsArray[TrialNr, 3] = NumberOptions[int(FullExperimentTrialsArray[TrialNr, 1])]  % 2 #Take modulo of the number. If it's even, CorResp = 0, if it's odd, CorResp = 1

    FullExperimentTrialsArray[FullExperimentTrialsArray_CurrentRowNrs, numpy.shape(BlockTrialsArray)[1]] = BlockNr + 1 #Python starts counting at 0

##validate the randomization
FullExperimentTrialsArrayDataFrame = pandas.DataFrame.from_records(FullExperimentTrialsArray) #Create DataFrame first. This DataFrame is needed for the crosstab and for creating the dictionairy input (i.e., TrialListMainExperiment) of the TrialHandler of the main experiment
FullExperimentTrialsArrayDataFrame.columns = ['tasks', 'numbers', 'letters', 'CorResp', 'UniqueTrialsArray', 'BlockNr'] #Add column names to FullExperimentTrialsArrayDataFrame
print(pandas.crosstab([FullExperimentTrialsArrayDataFrame.letters, (FullExperimentTrialsArrayDataFrame.numbers)], [FullExperimentTrialsArrayDataFrame.tasks])) #Print the cross table validation

##TrialHandler
TrialListExperiment = pandas.DataFrame.to_dict(FullExperimentTrialsArrayDataFrame, orient = 'records') #Convert dataframe to list of dictionaries (this will be the input for the TrialHandler of the main experiment)

##Initialize clock, response, window, and stimuli properties
RTClock = core.Clock() #Initialize the clock

win = visual.Window(size = [850, 850], units = 'norm', color = 'yellow')

MessageToParticipant = visual.TextStim(win, text = '', height = .07, color = 'black')

FixationCross = visual.TextStim(win, text = '+', height = .1, color = 'black')
TaskTypeText = visual.TextStim(win, text = '', pos = [0,0.2], height = .1, color = 'black')
NumberPlusLetterText = visual.TextStim(win, text = '', height = .1, color = 'black')
MappingText = visual.TextStim(win, text = '', pos = [0,-0.2], height = .06, color = 'gray')
feedback = visual.TextStim(win, text = '', color = 'black', height = .1)
RatingScaleQuestionText = visual.TextStim(win, text = 'How much did you like participating in this experiment?', pos = [0,0.2], height = .1, color = 'black')
MyRatingScale = visual.RatingScale(win, low = 0, high = 100, marker = 'slider', tickMarks = [0, 100], stretch = 1.5, tickHeight = 1.5, labels = ['0','100'], textColor = 'black', lineColor = 'black', markerColor = 'black')
RatingAndThanksText = visual.TextStim(win, text = '', color = 'black', height = .1)

##Function for the rating scale question and thank you msg
def RatingAndThanks():
    MyRatingScale.reset()
    while MyRatingScale.noResponse:
        RatingScaleQuestionText.draw()
        MyRatingScale.draw()
        win.flip()
    if MyRatingScale.getRating() >= 50:
        RatingAndThanksText.text = 'Happy to read about the positive experience!\n\nThank you for participating!\n\n[Press space to finish the experiment]'
    else:
        RatingAndThanksText.text = 'Sorry to read that you did not like the experiment!\n\nThank you for participating!\n\n[Press space to finish the experiment]'
    RatingAndThanksText.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

##Present the welcome text, task instructions, practice start text
WelcomeText = 'Hi!\n\nWelcome to this experiment!\n\nWe will explain the task to you on the next screen.\n\n[Press space to continue]'
InstructionsText = f'In each trial, you will either be asked whether a particular stimulus (for instance 3C) is \'even or odd\' (Number Task; 3 is odd) or whether it is \'a vowel or consonant\' (Letter Task; C is a consonant).\n\nIn the Number Task, you need to press left ({ResponseButtonsList[0]}) if it\'s even and right ({ResponseButtonsList[1]}) if it\'s odd.\n\n In the Letter Task, you need to press left ({ResponseButtonsList[0]}) if it\'s a vowel and right({ResponseButtonsList[1]}) if it\'s a consonant.\n\nGood luck!\n\n[Press space to start with the experiment]'

if not speedy:
    for message in [WelcomeText, InstructionsText]:
        MessageToParticipant.text = message
        MessageToParticipant.draw()
        win.flip()
        if not speedy:
            event.waitKeys(keyList = ['space'])

##Present the experiment
trials = data.TrialHandler(TrialListExperiment, nReps = 1, method = 'sequential') #We already took care of the shuffling
ThisExp.addLoop(trials) #We here tell that the information from TrialListExperiment should be presented in the trials loop

accuracy = RT = FixationCrossDuration = AccuracyCount = 0 #Most of these are needed to prevent for error messages if speedy is activated (accuracy is also needed for other purposes)

for trial in trials:

    FixationCross.draw()
    win.flip()    
    if not speedy:
        core.wait(FixationCrossDuration)
        FixationCrossDuration = random.choice([0.6, 0.75, 0.9]) #Randomly select a fixation cross duration (no need to incorporate this in the randomnization)

    TaskTypeText.text = TaskOptions[int(trial['tasks'])]
    TaskTypeText.draw()

    NumberPlusLetterText.text = str(NumberOptions[int(trial['numbers'])]) + LetterOptions[int(trial['letters'])]
    NumberPlusLetterText.draw()

    MappingText.text = ['<---VOWEL   CONSONANT--->','<---EVEN   ODD--->'][int(trial['tasks'])]
    MappingText.draw()

    win.flip()
    if not speedy:
        RTClock.reset()
        keys = event.waitKeys(keyList = ResponseButtonsList, maxWait = 2.7)
        RT = [-999, round(RTClock.getTime() * 1000)][bool(keys)] #If keys == True (truthy variable), RT = getTime() value, otherwise it's -999
        
        if keys:
            if keys[0] == 'escape':
                break
            else:
                accuracy = (keys[0] == ResponseButtonsList[int(trial['CorResp'])]) * 1
                feedback.text = ['error','correct'][accuracy]
                feedback.color = ['black','blue'][accuracy]
                AccuracyCount += 1 #We need this variable for the accuracy calculation at the very end of the experiment
        else:
            accuracy = 0
            feedback.text = 'too late'
            feedback.color = 'black'

    feedback.draw()
    win.flip()
    
    if not speedy:
        core.wait(1)

    for AddData in [trials.addData('BlockNr', trial['BlockNr']), trials.addData('FixationCrossDuration', FixationCrossDuration*1000), trials.addData('TaskTypeText',TaskTypeText.text.lower()), trials.addData('number',NumberOptions[int(trial['numbers'])]), trials.addData('letter',LetterOptions[int(trial['letters'])]), trials.addData('Accuracy',feedback.text), trials.addData('RT',RT)]:
        AddData

    ThisExp.nextEntry() #Let the ExperimentHandler proceed to the next trial (now it knows that next .addData() calls correspond to the next trial)

    if not speedy:
        if ((trials.thisN + 1) % NrOfTrialsPerBlock == 0):
                MessageToParticipant.text = f'This is the end of block {int(trial["BlockNr"])} of {NrOfBlocks}.\n\n. You can have a break now if you want.\n\n[Press space to continue]' #THIS INFORMATION NEEDS TO BE COMMUNICATED! DESCRIBE IN TEST!
                MessageToParticipant.draw()
                win.flip()
                event.waitKeys(keyList = ['space'])

if not speedy:
    MessageToParticipant.text = f'In this experiment, you performed {int((AccuracyCount/len(TrialListExperiment)))}% of the trials correctly.\n\nThanks for participating!\n\n[Press space to go the very last part of the experiment (a short question)]'
    MessageToParticipant.draw()
    win.flip()
    event.waitKeys(keyList = ['space'])

if not speedy:
    RatingAndThanks()

ThisExp.close() #Let the ExperimentHandler know that it's finished
win.close()