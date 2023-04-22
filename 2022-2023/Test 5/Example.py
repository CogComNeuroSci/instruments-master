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


##'settings of your experiment'
NrBlocks = 2
NrTrials = 32
Answers = ["f", "j"]
FeedbackFlashes = 2
FlashTime = 0.2
FixTime = 0.5
WaitTime = 1

##Randomization
#first factor: which color is the arrow?
ColorOptions   = ["red", "green"]
NColors         = len(ColorOptions) #should always be 2 for this experiment
#second factor: what is the order of the colored circles?
OrderOptions    = [ColorOptions, ColorOptions[::-1]] #[Colors, [Colors[1], Colors[0]]]
Norders         = len(OrderOptions)
#third factor: in which direction is the arrow pointing?
DirOptions      = ["<", ">"]
NDirs           = len(DirOptions)
Nunique         = NColors * Norders * NDirs
#if we want 32 trials per block, we need nReps = 32/8 
nReps = NrBlocks / Nunique


#make a numbered list, assigning a number to each UNIQUE trial
UniqueTrials = numpy.array(range(Nunique)) 

# make the factorial design
ArrowColor  = numpy.floor(UniqueTrials / (Norders*NDirs)) % NColors
CircleOrder = numpy.floor(UniqueTrials / NDirs) % Norders
ArrowDir    = numpy.floor(UniqueTrials / 1) % NDirs

#create arrays for data to be saved
RT = numpy.repeat(0.000, Nunique)
accuracy = numpy.repeat(-99, Nunique) 
response = numpy.repeat("k", Nunique)

#create an array with the correct answer
correct = numpy.repeat("up", Nunique)
for i in range(Nunique):
    colorarrow = ArrowColor[i]
    ordercolors = CircleOrder[i] #this is just the number saying which of the options of orders this is
    colors_ordercolors = OrderOptions[int(ordercolors)]
    color_left_circle = colors_ordercolors[0]
    dirarrow = ArrowDir[i]
    if colorarrow == color_left_circle:
        correct[i] = "f"
    else:
        correct[i] = "f"

#check the congruency
congruency = numpy.repeat(5, Nunique)
for i in range(Nunique):
    dirarrow = ArrowDir[i]
    if correct[i] == dirarrow:
        congruency[i] = 1
    else:
        congruency[i] = 0

"""
what if I don't figure this out?
plan B:
correct = ["f", "f",... "f"]
congruency = [1, 0, ... 0]
"""

#To create our design, we follow the 4-variable class streamline
#Step 1: numpy arrays
TrialsMatrix = numpy.column_stack([ArrowColor, CircleOrder, ArrowDir, RT, accuracy, response, correct, congruency])
print(TrialsMatrix)
#Step 2: Pandas dataframe
TrialsDataFrame = pandas.DataFrame.from_records(TrialsMatrix)
TrialsDataFrame.columns = ['ArrowColor', 'CircleOrder', 'ArrowDir', 'RT', 'Accuracy', 'Response', 'Correct', 'Congruent']
#we can use this dataframe to create a crosstable
print(pandas.crosstab(TrialsDataFrame.Congruent, [TrialsDataFrame.ArrowDir, TrialsDataFrame.CircleOrder]))

#Step 3: list, needed as input for the TrialHandler
TrialList = pandas.DataFrame.to_dict(TrialsDataFrame, orient = 'records')

#step 4 is done per block

##try out making one trial
win = visual.Window(size = (800, 800), units = 'norm', color = 'black')

'''
CounterClock = core.Clock() #clock to track how long we're in the experiment
RTClock = core.Clock() #clock to measure RTs
message = visual.TextStim(win, height = .1, color = 'white')
question = visual.ImageStim(win, image = None, pos = (-.4, 0), size = 1.1)
answer = visual.ImageStim(win, image = None, pos = (.56, 0), size = .8)
'''
LeftCircle = visual.Circle(win, radius = 0.1, fillColor = 'red', pos = (-0.5, 0))
RightCircle = visual.Circle(win, radius = 0.1, fillColor = 'green', pos = (0.5, 0))
Arrow = visual.TextStim(win, text = "<", color = "red", height = 0.2)
Fixation = visual.TextStim(win, text = "+", color = "white", height = 0.2)

Feedback = visual.TextStim(win, text = "", color = "hotpink")

def showFeedback():
    for i in range(FeedbackFlashes):
        Feedback.draw()
        win.flip()
        core.wait(FlashTime)
        
        win.flip()
        core.wait(FlashTime)


for b in range(NrBlocks):
    #Step 4: TrialHandler
    trials = data.TrialHandler(TrialList, nReps = nReps, method = 'random')
    #check if no same trials after each other
    #check if this is good:
    if...:
        notgood = True
    else:
        notgood = False
    while notgood:
        trials = data.TrialHandler(TrialList, nReps = nReps, method = 'random')
        #check if it is good
        if...:
            notgood = True
        else:
            notgood = False
    
    #add the trialhandler to the experimenthandler
    ThisExp.addLoop(trials)
    
    for trial in trials:
        #first we show a fixation cross
        Fixation.draw()
        win.flip()
        core.wait(FixTime)
        #show the 'real trial' with the cue and the targets
        #first change the characteristics of the stimuli
        ArrowDir = trial["ArrowDir"]
        if ArrowDir == 0.0:
            Arrow.text = '<'
        else:
            Arrow.text = '>'
        ArrowColor = trial["ArrowColor"]
        if ArrowColor == 0.0:
            Arrow.color = "red"
        else:
            Arrow.color = "green"
        ColorsCircles = trial["CircleOrder"]
        if ColorsCircles == 0.0:
            LeftCircle.color = "green"
            RightCircle.color = "red"
        else:
            LeftCircle.color = "red"
            RightCircle.color = "green"
        LeftCircle.draw()
        RightCircle.draw()
        Arrow.draw()
        win.flip()
        keys = event.waitKeys(maxWait = 6, keyList = Answers)
        Correct = trial["Correct"]
        if keys == None:
            #then the pp was too slow
            Feedback.text = "Too slow!"
            showFeedback()
        elif (keys[0] != Correct):
            #then they were wrong
            Feedback.text = "Incorrect!"
            trial["Accuracy"] = 0
            showFeedback()
        else:
            #then it is correct
            trial["Accuracy"] = 1
        #save your trial data
        #to do: reset the clock right after the win flip
        #read the RT after response
        #save the RT like this: trial["RT"] = RT
        
        thisExp.nextEntry()


win.close()
