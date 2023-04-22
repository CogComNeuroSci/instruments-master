##import modules
from psychopy import visual, gui, event, data, core
import numpy, pandas, os

##File management and dlg box
DirectoryToWriteTo = os.getcwd() + '\Data'
#Create data folder (if this does not yet exist)
if not os.path.isdir(DirectoryToWriteTo):
    os.mkdir(DirectoryToWriteTo)
info = {'ParticipantNr': numpy.random.randint(0,999), 'Name': 'Fien Goetmaeckers', 'age': '', 'gender': ["woman", "man", "other"]} 
#ParticipantNr proposes a random number such that the experimenter (you) has to change this less often

AlreadyExists = True
while AlreadyExists:
    dlg = gui.DlgFromDict(dictionary = info, title = 'Example')
    FileName = DirectoryToWriteTo + '\Participant' + str(info['ParticipantNr'])
    #If cancel is selected, the experiment is quitted
    if not dlg.OK: 
        core.quit()
    #Only leave the while loop if the ParticipantNr is unique
    if not os.path.isfile(FileName + '.csv'): 
        AlreadyExists = False
    #If the ParticipanatNr has been used, show an error gui
    else:
        dlg2 = gui.Dlg(title = 'Error')
        dlg2.addText('This ParticipantNr is already in use, please select another')
        dlg2.show()

name = info["Name"].split()[0]
info.pop("Name")

#we create the experimenthandler with the created name and the participant's (anonymous) info
ThisExp = data.ExperimentHandler(dataFileName = FileName, extraInfo = info)

##settings of your experiment
NrBlocks = 2
NrTrials = 32
Answers = ["f", "j", "escape"]
FeedbackFlashes = 2
FlashTime = 0.2
FixTime = 0.5
WaitTime = 1

##Randomization
#first factor: which color is the arrow?
ColorOptions   = ["red", "green"]
NColors         = len(ColorOptions) #should always be 2 for this experiment
#second factor: what is the order of the colored circles?
LeftColorOptions = ColorOptions #we just save which circle is the left one
NLeftColors      = len(LeftColorOptions)
#third factor: in which direction is the arrow pointing?
DirOptions      = ["<", ">"]
NDirs           = len(DirOptions)
Nunique         = NColors * NLeftColors * NDirs
#if we want 32 trials per block, we need nReps = 32/8 
nReps = int(NrTrials / Nunique)
#make a numbered list, assigning a number to each UNIQUE trial
UniqueTrials = numpy.array(range(Nunique)) 

# make the factorial design
ArrowColor  = numpy.floor(UniqueTrials / (NLeftColors*NDirs)) % NColors
LeftColor   = numpy.floor(UniqueTrials / NDirs) % NLeftColors
#in these ^ two lists, 0 means red, 1 means green
ArrowDir    = numpy.floor(UniqueTrials / 1) % NDirs
#in this ^ list, 0 means left, 1 means right

#create arrays for data to be saved
RT = numpy.repeat(0.000, Nunique)
accuracy = numpy.repeat(-99, Nunique) 

#create the numpy array showing the correct answer (0 for left/f and 1 for right/j)
#0 if ArrowColor == LeftColor or 1 if ArrowColor != LeftColor
Correct = numpy.array(ArrowColor != LeftColor) * 1

#create the numpy array showing the congruency (0 for IC, 1 for C)
#0 if ArrowDir != Correct or 1 if ArrowDir == Correct
Congruent = numpy.array(ArrowDir == Correct) * 1
"""
what if I don't figure this out?
plan B: just write it down yourself! 
you'll lose some points, but at least you can move on
correct = [0, 0, 1, ... 0]
congruency = [1, 0, ... 0]
"""
#To create our design, we follow the 4-variable class streamline
#Step 1: numpy arrays
TrialsMatrix = numpy.column_stack([UniqueTrials, ArrowColor, LeftColor, ArrowDir, RT, accuracy, Correct, Congruent])
#already create one block
BlockMatrix = numpy.tile(TrialsMatrix, (nReps, 1))
#Step 2-4 are done per block (in the block loop)

##we create all visual elements
win = visual.Window(size = (800, 800), units = 'norm', color = 'black')

RTClock = core.Clock() #clock to measure RTs
message = visual.TextStim(win, height = .1, color = 'white')

LeftCircle = visual.Circle(win, radius = 0.1, fillColor = 'red', pos = (-0.5, 0))
RightCircle = visual.Circle(win, radius = 0.1, fillColor = 'green', pos = (0.5, 0))
Arrow = visual.TextStim(win, text = "<", color = "red", height = 0.2)
Fixation = visual.TextStim(win, text = "+", color = "white", height = 0.2)

Feedback = visual.TextStim(win, text = "", color = "hotpink")

#function showing the flashing of the feedback
def showFeedback():
    for i in range(FeedbackFlashes):
        Feedback.draw()
        win.flip()
        core.wait(FlashTime)
        
        win.flip()
        core.wait(FlashTime)

##Welcome and instruction screens
message.text = "Welcome " + name + "!\n" + "Press space to continue."
message.draw()
win.flip()
event.waitKeys(keyList = "space")

message.text = "Respons which circle has the same color as the middle arrow. Press 'f' for left, 'j' for right."
message.draw()
win.flip()
event.waitKeys(keyList = "space")

for b in range(NrBlocks):
    #we create the trial matrix
    #before we accept the BlockMatrix, we check if every consecutive trail is different
    AllDifferent = False
    while AllDifferent != True:
        numpy.random.shuffle(BlockMatrix) #shuffle the trials in this block
        #see if two consecutive trials have the same unique TrialNumber, given by UniqueTrials,
        #which is saved in the first column (column 0) of BlockMatrix
        comparison = numpy.diff(BlockMatrix[:,0]) 
        if sum(comparison == 0) != 0:
            #then at least one consecutive pair has a difference of 0
            AllDifferent = False 
        else:
            AllDifferent = True #the loop will end
    print(BlockMatrix)
    #Step 2: Pandas dataframe
    BlockDataFrame = pandas.DataFrame.from_records(BlockMatrix)
    BlockDataFrame.columns = ['TrialNumber', 'ArrowColor', 'LeftColor', 'ArrowDir', 'RT', 'Accuracy', 'Correct', 'Congruent']
    #we can use this dataframe to create a crosstable
    print(pandas.crosstab(BlockDataFrame.Congruent, [BlockDataFrame.ArrowDir, BlockDataFrame.LeftColor]))
    #Step 3: list, needed as input for the TrialHandler
    TrialList = pandas.DataFrame.to_dict(BlockDataFrame, orient = 'records')
    #Step 4: TrialHandler
    trials = data.TrialHandler(TrialList, nReps = 1, method = 'sequential')
    #add the trialhandler to the experimenthandler
    ThisExp.addLoop(trials)
    
    for trial in trials:
        #first we show a fixation cross
        Fixation.draw()
        win.flip()
        core.wait(FixTime)
        
        ##show the 'real trial' with the cue and the targets
        #first change the characteristics of the stimuli
        Arrow.text = DirOptions[int(trial["ArrowDir"])] 
        '''
        #the longer (easier to understand) version of the line above:
        ArrowDir = trial["ArrowDir"]
        if ArrowDir == 0.0:
            Arrow.text = '<' #which is DirOptions[0]
        else:
            Arrow.text = '>' #which is DirOptions[1]
        '''
        Arrow.color = ColorOptions[int(trial["ArrowColor"])]
        '''
        #the longer (easier to understand) version of the line above:
        ArrowColor = trial["ArrowColor"]
        if ArrowColor == 0.0:
            Arrow.color = "red" #which is ColorOptions[0]
        else:
            Arrow.color = "green" #which is ColorOptions[1]
        '''
        LeftCircle.color = LeftColorOptions[int(trial["LeftColor"])]
        RightCircle.color = LeftColorOptions[int(trial["LeftColor"]) - 1] 
        #this ^ will give the other option in the LeftColorOptions list
        '''
        LeftColor = trial["LeftColor"]
        if LeftColor == 0.0:
            LeftCircle.color = "red" #which is LeftColorOptions[0]
            RightCircle.color = "green" #which is LeftColorOptions[0-1] = LeftColorOptions[-1] (so the last one)
        else:
            LeftCircle.color = "green" #which is LeftColorOptions[1]
            RightCircle.color = "red"  #which is LeftColorOptions[1-1] = LeftColorOptions[0]
        '''
        #now we show the correct stimili belonging to this trial
        LeftCircle.draw()
        RightCircle.draw()
        Arrow.draw()
        win.flip()
        RTClock.reset()
        keys = event.waitKeys(maxWait = 6, keyList = Answers)
        RT = round(RTClock.getTime(), 3)
        if keys == None:
            #then the pp was too slow
            Feedback.text = "Too slow!"
            showFeedback()
        elif keys[0] == "escape":
            break
        elif (keys[0] == 'f' and trial["Correct"] == 1) or (keys[0] == 'j' and trial["Correct"] == 0):
            #then they were wrong
            Feedback.text = "Incorrect!"
            trial["Accuracy"] = 0
            trial["Answer"] = keys[0]
            showFeedback()
        else:
            #then it is correct
            trial["Accuracy"] = 1
            trial["Answer"] = keys[0]
        
        trial["RT"] = RT
        ThisExp.nextEntry()
    
    #make sure pp exit the block structure after having pressed escape
    if key[0] == "espace":
        break
    
    #after one block, show an information screen
    if (b+1) == NrBlocks:
        #then you show the end text scren
        message.text = "Thank you " + name + " for participating. Press space to exit the experiment."
    elif (b+1) * 2 == NrBlocks: #halfway for even NrBlocks
        #then you show the middle text screen
        message.text = "You reached the middle of the experiment. Press space to continue."
    elif (b+1) * 2 - 1 == NrBlocks: #over halfway for uneven NrBlocks
        message.text = "You are over  halfway. Press space to continue."
    else: 
        message.text = "Take a break. Press space to continue."
    message.draw()
    win.flip()
    event.waitKeys(keyList = "space")

win.close()
