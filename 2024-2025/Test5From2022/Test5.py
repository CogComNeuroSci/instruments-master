##import modules
from psychopy import visual, gui, event, core, data
import os, numpy, random, time, pandas

##file management & dlg box
MyDirectory = os.getcwd()

DirectoryToWriteTo = MyDirectory + '/data/' #Create data folder (if this does not yet exist)
if not os.path.isdir(DirectoryToWriteTo):
    os.mkdir(DirectoryToWriteTo)

info = {'ParticipantNr':'', 'age':'','gender':['male','female','x'],'handedness':['right','left','ambidexter']} #Dictionary for dlg box

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'Task Switching Task') #Present a dlg box
    FileName = DirectoryToWriteTo + 'task_switching_subj' + info['ParticipantNr']

    if not dlg.OK: #Quit the experiment if 'Cancel' is selected
        core.quit()

    if not os.path.isfile(FileName + '.csv'): #Only escape the while loop if ParticipantNr is unique
        AlreadyExists = False
    else:
        dlg2 = gui.Dlg(title = 'Error') #If the ParticipantNr is not unique, present an error msg
        dlg2.addText('This ParticipantNr is in use already, please select another')
        dlg2.show()

ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info) #ExperimentHandler: a class for keeping track of multiple loops/handlers

##design & randomnization
NrOfBlocks = 4 #NrOfBlocks should be 2 or multiplications of 2 (the nr of possible block types)
NrOfTrialsPerBlock = 32 #NrOfTrialsPerBlock should be 8 or multiplications of 8 (the nr of unique trials)

FixDurOptions = numpy.array([0.5, 1]) #These three variables need to be taken into account when creating the design
TargetShapeOptions = numpy.array(['triangle', 'square'])
TargetColorOptions = numpy.array(['blue', 'green'])

UniqueTrialsArray = numpy.array(range((len(FixDurOptions) * len(TargetShapeOptions) * len(TargetColorOptions))))

FixDur = numpy.floor(UniqueTrialsArray / (len(FixDurOptions) * len(FixDurOptions))) #0-0-0-0-1-1-1-1
TargetShape = numpy.floor(UniqueTrialsArray / len(FixDurOptions)) % len(FixDurOptions) #0-0-1-1-0-0-1-1
TargetColor = numpy.floor(UniqueTrialsArray / 1) % len(FixDurOptions) #0-1-0-1-0-1-0-1

UniqueTrialIdentifier = numpy.array(range(len(UniqueTrialsArray))) #By adding this to UniqueTrialsArray, we get a unique identifier for each unique trial (needed for the randomnization procedure later)
BlockNr = numpy.repeat(numpy.nan, len(UniqueTrialsArray)) #Just a 'placeholder' to be added to the matrix
UniqueTrialsArray = numpy.column_stack([FixDur, TargetShape, TargetColor, UniqueTrialIdentifier, BlockNr]) #One repetition of all unique trials
BlockTrialsArray = numpy.tile(UniqueTrialsArray, (int((NrOfTrialsPerBlock/len(UniqueTrialsArray))),1)) #Contains the trials for an entire block now

FullExperimentTrialsArray = numpy.ones(((NrOfBlocks*NrOfTrialsPerBlock), numpy.shape(BlockTrialsArray)[1])) #An array with 'placeholders'. It has the nr of rows of the entire experiment, and the same nr of columns as BlockTrialsArray

for BlockNr in range(NrOfBlocks): #The actual randomnization of the trials per block takes place here
    FullExperimentTrialsArray_CurrentRowNrs = numpy.array(range(len(BlockTrialsArray))) + (BlockNr * len(BlockTrialsArray)) #First repeat, this array will be from 0-31 (covers first block). Second repeat, this array will have an intercept change of 32, so from 32-63 (covers second block) ...

    stop = True
    while stop:
        numpy.random.shuffle(BlockTrialsArray)
        if numpy.sum(numpy.diff(BlockTrialsArray[:,3]) == 0) == 0: #Only stop shuffling if there are no trial repetitions
            stop = False
    
    FullExperimentTrialsArray[FullExperimentTrialsArray_CurrentRowNrs, :] = BlockTrialsArray #Store the trials for this block in the FullExperimentTrialsArray array
    FullExperimentTrialsArray[FullExperimentTrialsArray_CurrentRowNrs, 4] = BlockNr + 1 #Fill in the block nr (Python starts at 0)

AccuracyArray = numpy.repeat(numpy.nan, len(FullExperimentTrialsArray)) #An additional array that is needed for creating block feedback later (not relevant for randmonization)

##validate the randomization
FullExperimentTrialsArrayDataFrame = pandas.DataFrame.from_records(FullExperimentTrialsArray) #Create DataFrame first
FullExperimentTrialsArrayDataFrame.columns = ['FixDur', 'TargetShape', 'TargetColor', 'UniqueTrialIdentifier', 'BlockNr'] #Add column names
print(pandas.crosstab([FullExperimentTrialsArrayDataFrame.TargetShape, FullExperimentTrialsArrayDataFrame.TargetColor], FullExperimentTrialsArrayDataFrame.FixDur)) #Print the cross table validation
FullExperimentTrialsArrayDataFrame.to_csv(path_or_buf = 'DataFrame_test5.csv', index = False) #Save as .csv

##TrialHandler
TrialList = pandas.DataFrame.to_dict(FullExperimentTrialsArrayDataFrame, orient = 'records') #Convert dataframe to list of dictionaries
trials = data.TrialHandler(TrialList, nReps = 1, method = 'sequential') #Sequential because the trials have already been randomnized
ThisExp.addLoop(trials)

##initialize clock, response, window, and stimuli properties
RTClock = core.Clock() #Initialize the clock

ResponseButtons = ['u','i','escape'] #Changes in this variable should accordingly change the instructions and accuracy determination

win = visual.Window(size = (1000, 1000), units = 'norm', color = 'white')
msg = visual.TextStim(win, text = '', color = 'black')
fix = visual.TextStim(win, text = '+', height = 0.1, color = 'black')
TargetStimulus = visual.Polygon(win, size = 0.5)
TaskReminder = visual.TextStim(win, height = 0.1, color = 'black', pos = (0, 0.4))
feedback = visual.TextStim(win, text = '', height = 0.2)

##def(s)
def FeedbackRotationAndPresentation():
    feedback.text = numpy.array(['error','correct','too slow'])[accuracy] #For this array: [0] = 'error', [1] = 'correct', [-1] = 'too slow'
    feedback.color = numpy.array(['red','yellow','red'])[accuracy]
    for rotations in range(60):
        feedback.ori = 360 - (rotations * 6)
        feedback.draw()
        win.flip() #This takes 16ms. Checks revealed a total duration of 0.9975993998814374 - 0.9982555999886245 - 1.0008912000339478 - ...

##welcome and instructions
msg.height = 0.05 #Height should be relatively small to ensure that the instructions fit the screen
msg.text = 'Welcome to this experiment!\n\nIn this experiment you need to respond\nto the shape or color of the stimulus\non the screen.\n\nAt the start of each of the {0} blocks,\nan information screen will tell you what\nyou need to respond to.\n\nIf you see \'Shape Task\', you need to\nidentify the shape (triangle/square) of the\nstimulus in that entire block.\n\nWhen you see \'Color Task\', you need to\nidentify the color (blue/green) of the\nstimulus in that entire block.\n\nFor responding, you can use the \'{1}\'\nfor triangle/blue and \'{2}\' for\n square/green.\n\nAfter each block, there will be a short break.\n\nDo you have any questions?\n\nGood luck!\n\n[Press space to continue]'.format(NrOfBlocks, ResponseButtons[0], ResponseButtons[1])
msg.draw()
win.flip()
event.waitKeys(keyList = 'space')

##experimental task
for trial in trials:

    ##information screen - ShapeBlock/ColorBlock follows
    if trials.thisN % NrOfTrialsPerBlock == 0: #Only present this screen at the start of a new block
        if int(info['ParticipantNr']) % 2 == 0:
            BlockType = numpy.tile(['ShapeTask', 'ColorTask'], int((NrOfBlocks/2)))[int((trials.thisN/NrOfTrialsPerBlock))] #ABAB
        else:
            BlockType = numpy.tile(['ColorTask', 'ShapeTask'], int((NrOfBlocks/2)))[int((trials.thisN/NrOfTrialsPerBlock))] #BABA
        if trials.thisN >= NrOfTrialsPerBlock: #Only from the second block onwards TaskSwitchText should be filled
            TaskSwitchText = 'Task switch needed! '
        else:
            TaskSwitchText = ''
        msg.height = 0.08
        msg.text = '{0}In this block you need to\nperform the {1}\n\n[Press space to continue]'.format(TaskSwitchText, BlockType[:-4] + ' Task')
        msg.draw()
        win.flip()
        event.waitKeys(keyList = 'space')

    trials.addData('BlockTypeString', BlockType)

    ##fixation cross on a blank screen (ITI)
    fix.draw()
    win.flip()
    core.wait(FixDurOptions[int(trial['FixDur'])])
    
    ##target stimulus
    TaskReminder.text = BlockType[:-4] #Which stimulus dimension need to be responded to? (Regards the text above the target stimulus)
    TaskReminder.draw()
    
    TargetStimulus.edges = trial['TargetShape'] + 3 #TargetShape is 0 for triangle and 1 for square
    TargetStimulus.color = TargetColorOptions[int(trial['TargetColor'])]
    TargetStimulus.draw()
    fix.draw()
    win.flip()
    RTClock.reset()
    keys = event.waitKeys(keyList = ResponseButtons, maxWait = 1.2)
    RT = int((RTClock.getTime() * 1000)) #In ms
    trials.addData('TargetShapeString', TargetShapeOptions[int(trial['TargetShape'])])
    trials.addData('TargetColorString', TargetColorOptions[int(trial['TargetColor'])])

    ##correct response
    if BlockType == 'ShapeTask':
        CorrectResponse = ResponseButtons[int(trial['TargetShape'])] #TargetShape is 0 for triangle and 1 for square
    else:
        CorrectResponse = ResponseButtons[int(trial['TargetColor'])] #TargetColor is 0 for blue and 1 for green

    ##accuracy
    if keys == None: #In case of a miss
        accuracy = -1
        RT = numpy.nan
    elif keys[0] == ResponseButtons[2]: #'escape'
        break
    else: #This else statement is met in case of correct or an error
        AccuracyArray[trials.thisN] = accuracy = int(keys[0] == CorrectResponse) #Will need the AccuracyArray for the block feedback

    trials.addData('RT', RT)
    trials.addData('accuracy', accuracy)
    trials.addData('AccuracyString', numpy.array(['error','correct','too slow'])[accuracy])

    ##feedback event
    FeedbackRotationAndPresentation() #Actual code is moved away (see def(s) section at start of script)

    ##block feedback & self-paced break
    if (trials.thisN + 1) % NrOfTrialsPerBlock == 0:
        msg.height = 0.08
        msg.text = 'You responded correct to {}% of the trials in this block]\n\n[Press space to continue]'.format(int((numpy.sum(AccuracyArray[range(((trials.thisN + 1) - NrOfTrialsPerBlock), (trials.thisN + 1))] == 1)/ NrOfTrialsPerBlock) * 100))
        msg.draw()
        win.flip()
        event.waitKeys(keyList = 'space')

        if (trials.thisN + 1) == len(TrialList):
            msg.text = 'The experiment is finished!\n\nThanks for participating!\n\n[Press space to finish the experiment]'
        else:
            msg.text = 'You can take a break now\n\n[Press space to continue]'
        msg.draw()
        win.flip()
        event.waitKeys(keyList = 'space')
    
    ThisExp.nextEntry() #Let the ExperimentHandler proceed to the next trial

ThisExp.close() #Let the ExperimentHandler know that its job is done
win.close()