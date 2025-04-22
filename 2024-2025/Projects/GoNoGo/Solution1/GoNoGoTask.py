##Project IEP course
##Go/NoGo Task
##Author: Vincent Hoofs

from psychopy import visual, gui, data, core, event
import numpy, os, pandas

##Challenges
challenge1 = True #True/False
challenge2 = True
challenge3 = True

##Settings
NTrialsPerBlock = 60 #10 is the minimum nr of trials needed for presenting all types of trials. The value here should a multiplication of 10
NBlocks = 3

if challenge3: 
    PossibleCueDurations = numpy.random.exponential(.3, 100) #An exponential distribution has mean β and variance β2 . β (the scale parameter) is .3 here (if checking the mean and variance of the array, you also find a numpy.mean of about .3 and a numpy.var of about .09)
else:
    PossibleCueDurations = numpy.array([.5, .4, .3, .2, .1]) #Uniform means that each result is equally likely to occur

##File management & dlg box
DirectoryToWriteTo = os.getcwd() + '/GoNoGodata/' #Create data folder (if this does not yet exist) #os.getcwd() is where your script is saved
if not os.path.isdir(DirectoryToWriteTo):
    os.mkdir(DirectoryToWriteTo)

info = {'ParticipantNr': 0, 'age': 0, 'gender' : ['male','female','x']} #Dictionary for dlg box ... I collect all data here that is typically needed for a method section in a paper

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'GoNoGoTask') #Present a dlg box
    FileName = DirectoryToWriteTo + 'GoNoGoTask_Participant' + str(info['ParticipantNr'])
    if not dlg.OK: #Quit the experiment if 'Cancel' is selected
        core.quit()
    if not os.path.isfile(FileName + '.csv'): #Only escape the while loop if ParticipantNr is unique
        AlreadyExists = False
    else:
        dlg2 = gui.Dlg(title = 'Error') #If the ParticipantNr is not unique, present an error msg
        dlg2.addText('This ParticipantNr is in use already, please select another')
        dlg2.show() #For this dlg method we need the .show() for presenting

ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info) #ExperimentHandler: a class for keeping track of multiple loops/handlers

##Randomnization
MinimumNrOfTrials = 10 #One cue is followed by 80% Go and 20% NoGo signals, while this is reversed for the other cue (20% Go and 80% NoGo signals). For all conditions following the correct probabilities, you need a minumum of at least 10 trials (see the schematic overview below)
CueArray = numpy.repeat([0,1], (MinimumNrOfTrials / 2))
SignalArray = numpy.concatenate((CueArray[1:], [CueArray[0]]))
CorrectResponseArray = numpy.copy(SignalArray) #It is the color of the signal that decides the correct response
MinimalTrialArray = numpy.column_stack([CueArray, SignalArray, CorrectResponseArray]) #An array with the minimum of 10 trials

#CueArray, SignalArray
#[[0        0]
# [0        0]
# [0        0]
# [0        0]
# [0        1] <- in 20% of the cue = 0 trials, it's followed by signal = 1
# [1        1]
# [1        1]
# [1        1]
# [1        1]
# [1        0] <- in 20% of the cue = 1 trials, it's followed by signal = 0

BlockArray = numpy.tile(MinimalTrialArray, (int((NTrialsPerBlock/MinimumNrOfTrials)),1)) #All trials for a block
FullExperimentArray = numpy.ones(((NBlocks*NTrialsPerBlock), numpy.shape(BlockArray)[1] + 3)) #An array with 'placeholders'. It has a length (nr of rows) that corresponds with the total nr of trials

for BlockNr in range(NBlocks): #Here we fill the 'placeholder' array (FullExperimentArray)
    TrialNrArray = numpy.arange(len(BlockArray)) + (BlockNr * len(BlockArray)) #The latter part of this statement is a strategy to change the start and end point of TrialNrArray. The intercept change is BlockNr * len(BlockArray). E.g.,: For the first block, TrialNrArray is [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19], for the second it is [20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39]
    numpy.random.shuffle(BlockArray)
    FullExperimentArray[TrialNrArray, 0 : numpy.shape(BlockArray)[1]] = BlockArray #For these rows - defined by TrialNrArray - replace columns 0:3 of FullExperimentArray with the content of BlockArray
    FullExperimentArray[TrialNrArray, numpy.shape(BlockArray)[1] + 1] = BlockNr + 1 #Add block nr (Python starts indexing at 0)
    FullExperimentArray[TrialNrArray, numpy.shape(BlockArray)[1] + 2] = numpy.arange(len(BlockArray)) + 1 #Add trial nr
    for TrialNr in range(BlockNr * NTrialsPerBlock, (BlockNr+1) * NTrialsPerBlock): #We add PossibleCueDurations here. We iterate over each single trial here and simply add the value at position [0] after reshuffling each time
        numpy.random.shuffle(PossibleCueDurations)
        FullExperimentArray[TrialNr, numpy.shape(BlockArray)[1]] = abs(round(PossibleCueDurations[0], 2)) #Round up to 2 decimals to keep the FullExperimentArray interpretable if printing... The abs is just to be completely sure that no negative value can occur

StaircaseArray = numpy.repeat(numpy.nan, 10) #Not needed for the randomnization, we need this for challenge2

##Validate the randomnization
FullExperimentDataFrame = pandas.DataFrame.from_records(FullExperimentArray) #Numpy arrays ('trial matrix') -> DataFrame (this is an in-between before we can create crosstabs)
FullExperimentDataFrame.columns = ['Cue', 'Signal', 'CorrectResponse', 'CueDuration', 'BlockNr', 'TrialNr'] #The colum names of the DataFrame
print(pandas.crosstab(FullExperimentDataFrame.Cue, FullExperimentDataFrame.Signal)) #With this crosstab you can check whether the 80-20% probabilities for cues and signals are ok

#An overview of all the conversions that are taking place:
#NUMPY ARRAY(1) --> PANDAS DATAFRAME(2) --> LIST OF DICTS(3) --> TRIALHANDLER(4)
#   PANDAS.DATAFRAME.FROM_RECORDS
#What we just did: (1) --> (2)

##TrialHandler
TrialList = pandas.DataFrame.to_dict(FullExperimentDataFrame, orient = 'records') #DataFrame -> list of dictionaries (this is the input for the TrialHandler)

#An overview of all the conversions that are taking place:
#NUMPY ARRAY(1) --> PANDAS DATAFRAME(2) --> LIST OF DICTS (3) --> TRIALHANDLER(4)
#           PANDAS.DATAFRAME.TO_DICT(DATAFRAME, ORIENT = 'RECORDS')
#What we just did: (2) --> (3)

##Initialize clock, response, window, and stimuli properties
RTClock = core.Clock() #Initialize the clock
ResponseButton = ['space'] #Give in the response key here
ResponseButton.append('escape')

win = visual.Window([1000, 1000], units = 'norm')
HorizontalCue = visual.Rect(win, width = .3, height = .6, fillColor = 'grey')
VerticalCue = visual.Rect(win, width = .6, height = .3, fillColor = 'grey')
msg = visual.TextStim(win, text = '', color = 'black', height = .1)

CueOptions = numpy.array([HorizontalCue, VerticalCue]) #Helps to convert the 0's and 1's from the randomnization into actually presented cue stimuli

if challenge1:
    if info['ParticipantNr'] % 2 == 0: #Vary Cue and Probability across participants
        SignalOptions = numpy.array(['green', 'red']) #In 80% of the cases, cue-0 is followed by signal-0, and cue-1 is followed by signal-1. Here we decide what signal-0/signal-1 corresponds to (green/red)
        CorResp = numpy.array([ResponseButton[0], '']) #space - ''
    else:
        SignalOptions = numpy.array(['red', 'green'])
        CorResp = numpy.array(['', ResponseButton[0]]) #''-space. If swopping signal-0/signal-1 colors, we also need to change to swop the CorResp array. Otherwise, red-'' and green-space is not maintained
else:
    SignalOptions = numpy.array(['green', 'red'])
    CorResp = numpy.array([ResponseButton[0], '']) #space - ''

##welcome and instructions
msg.text = 'Welcome to this experiment!\n\nYou will be presented with horizontal and vertical shapes\n\nYour task: If these shapes turn \'green\', press {0},\nif these turn \'red\', do not press any button!\n\nPress {0} to start with the experiment'.format(ResponseButton[0])
msg.draw()
win.flip()
event.waitKeys(keyList = ResponseButton[0])

###Experiment (practice and main phase)
MaxWaitWindow = 2
AccuracySum = 0 #To prevent 'NameError: name 'AccuracySum' is not defined'
ExpPhases = numpy.array(['practice','main'])
for ExpPhase in range(len(ExpPhases)):
    if ExpPhases[int(ExpPhase)] == 'practice':
        trials = data.TrialHandler(TrialList[3:8], nReps = 1, method = 'random') #Without 'random' you have the exact same sequence of trials in the practice as in the main experiment. We just took 5 trials from the TrialList for the practice
        ThisExp.addLoop(trials) #Here you connect the TrialHandler with the ExperimentHandler
        msg.text = 'Let\'s practice now\n\nPress {} to continue'.format(ResponseButton[0])
    else:
        trials = data.TrialHandler(TrialList, nReps = 1, method = 'sequential') #Sequential because the trials have already been randomnized
        ThisExp.addLoop(trials) #Here you connect the TrialHandler (with overwritten 'trials' now) with the ExperimentHandler
        msg.text = 'We start the main phase now\n\nPress {} to continue'.format(ResponseButton[0])

    msg.draw()
    win.flip()
    event.waitKeys(keyList = ResponseButton[0])

        #An overview of all the conversions that are taking place:
        #NUMPY ARRAY(1) --> PANDAS DATAFRAME(2) --> LIST OF DICTS (3) --> TRIALHANDLER(4)
        #                                     TRIALS = DATA.TRIALHANDLER(TRIALLIST, ...)
        #What we just did: (3) --> (4)

    for trial in trials:
        trials.addData('ExpPhase', ExpPhases[int(ExpPhase)]) #To register the experiment phase in the data file
 
        msg.text = '+' #Fixation cross, the instructions for programming were: 'The trial starts with the presentation of a fixation cross for 0.8 seconds'
        msg.draw()
        win.flip()
        core.wait(.8)

        win.flip() #Blank screen, the instructions for programming were: 'followed by a blank screen for 0.5 seconds'
        core.wait(0.5)
        
        CueOptions[int(trial['Cue'])].lineColor = 'black' #Cue
        CueOptions[int(trial['Cue'])].draw()
        win.flip()
        core.wait(trial['CueDuration'])

        CueOptions[int(trial['Cue'])].lineColor = SignalOptions[int(trial['Signal'])] #Signal
        CueOptions[int(trial['Cue'])].draw()
        win.flip()
        
        RTClock.reset()
        keys = event.waitKeys(keyList = ResponseButton, maxWait = MaxWaitWindow)
    
        if keys: #'Truthy variable' (= a value that is considered True when encountered in a Boolean context). This statement is to prevent for TypeError: 'NoneType' object is not subscriptable
            trials.addData('RT', int(RTClock.getTime() * 1000))
            if keys[0] == 'escape': #To escape the trial loop
                break
            PerformedResponse = keys[0]
        else:
            trials.addData('RT', -999) #A clear value that shows that no RT has been measured (there was no response to base RT on)
            PerformedResponse = ''
            
        accuracy = (PerformedResponse == CorResp[int(trial['CorrectResponse'])]) * 1 #The *1 converts False/True to 0/1
        if accuracy and ExpPhases[int(ExpPhase)] == 'main': #We only use the AccuracySum for the feedback in the main phase. We need to prevent here for correct responses in the practice phase biasing the calculation
            AccuracySum += 1 #We reset it directly after the block feedback was presented

        msg.text = numpy.array(['error','correct'])[accuracy]
        trials.addData('PerformedResponse', PerformedResponse)
        trials.addData('accuracy', msg.text)

        msg.draw()
        win.flip()
        core.wait(1)

        if challenge2 and ExpPhases[int(ExpPhase)] == 'main':
            StaircaseArray = numpy.concatenate((StaircaseArray,[accuracy]))[1:] #First you add accuracy to StaircaseArray. Then you index, by which you delete the first value of the array

            if not numpy.any(StaircaseArray == numpy.nan): #Postpone the staircase procedure till after the first 10 trials have been performed
                if numpy.sum(StaircaseArray) < 7: #If less than 70% is correct of the last 10 trials, increase the MaxWaitWindow
                    MaxWaitWindow += .02
                elif numpy.sum(StaircaseArray) > 7: #if it's above 70%, decrease the MaxWaitWindow
                    MaxWaitWindow -= .02

            trials.addData('StaircaseArray', numpy.sum(StaircaseArray))
            trials.addData('MaxWaitWindow', MaxWaitWindow)
            trials.addData('MaxWaitWindowAdjustment', (MaxWaitWindow - 2)) #Just to track how big the adjustment has been

        if int(trial['TrialNr']) == NTrialsPerBlock:
            msg.text = 'You responsed correct to {0:.0%} of the trials in this block\n\nPress {1} to continue'.format((AccuracySum/NTrialsPerBlock), ResponseButton[0])
            msg.draw()
            win.flip()
            event.waitKeys(keyList = ResponseButton[0])
            
            AccuracySum = 0 #Reset directly after block feedback

            if not int(trial['BlockNr']) == NBlocks:
                msg.text = 'You can take a break now\n\nPress {} to continue'.format(ResponseButton[0])
                msg.draw()
                win.flip()
                event.waitKeys(keyList = ResponseButton[0])

        ThisExp.nextEntry()

    if keys:
        if keys[0] == 'escape': #To escape the ExpPhase loop
            break

ThisExp.close() #Let the ExperimentHandler know that its job is done

##Goodbye msg
msg.text = 'Thank you for participating!\n\nPress {} to end the experiment'.format(ResponseButton[0])
msg.draw()
win.flip()
event.waitKeys(keyList = ResponseButton[0])

win.close()