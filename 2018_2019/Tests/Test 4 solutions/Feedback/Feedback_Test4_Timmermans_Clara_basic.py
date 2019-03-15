# This is the script for test 4, basic version
# 06/03/2019 by Clara Timmermans

# Import modules #

from psychopy import data, visual, event, core, gui, os
import pandas, numpy


# Initalize window #

win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height])


# Initialize variables #

##set working directory
my_directory = os.getcwd()
directory_to_write_to = my_directory + "/data/"

## data file
data_file = "Test4_"

## dialogue box
info = {"Name": "","Participant number": 0, "Age": 18, "Gender": ['Female', 'Male', 'Other'],"Hand preference": ['Left-handed', 'Right-handed', 'Ambidexter']}

my_clock = core.Clock()
text_width = 0.5

# Constants
## number of blocks
nBlocks = 12

## number of trials per block
nBlockTrials = 60

## calculate nReps
nDirections = 2
nPositions = 3
nUnique = nDirections * nPositions

nReps = int(nBlockTrials/nUnique)

# Design 
Design_pos = [{"Stimulus": "<", "Position": (-0.5,0), "Correct answer": "left", "Congruency": "congruent"},\
               {"Stimulus": "<", "Position": (0,0), "Correct answer": "down", "Congruency": "neutral"}, \
               {"Stimulus": "<", "Position": (0.5,0), "Correct answer": "right", "Congruency": "incongruent"}, \
               {"Stimulus": ">", "Position": (-0.5,0), "Correct answer": "left", "Congruency": "incongruent"}, \
               {"Stimulus": ">", "Position": (0,0), "Correct answer": "down", "Congruency": "neutral"}, \
               {"Stimulus": ">", "Position": (0.5,0), "Correct answer": "right", "Congruency": "congruent"}]

Design_dir = [{"Stimulus": "<", "Position": (-0.5,0), "Correct answer": "left", "Congruency": "congruent"},\
               {"Stimulus": "<", "Position": (0,0), "Correct answer": "left", "Congruency": "neutral"}, \
               {"Stimulus": "<", "Position": (0.5,0), "Correct answer": "left", "Congruency": "incongruent"}, \
               {"Stimulus": ">", "Position": (-.5,0), "Correct answer": "right", "Congruency": "incongruent"}, \
               {"Stimulus": ">", "Position": (0,0), "Correct answer": "right", "Congruency": "neutral"}, \
               {"Stimulus": ">", "Position": (0.5,0), "Correct answer": "right", "Congruency": "congruent"}]


# Data file #

already_exists = True
while already_exists:
    
    ## display gui for participant number
    myDlg = gui.DlgFromDict(info, title = "Info")
    number = str(info["Participant number"])
    name = info["Name"]
    
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    ## determine file name
    file_name = directory_to_write_to + data_file + "_subject_" + number
    
    ## verify whether this file name already exists
    if not os.path.isfile(file_name + ".csv"):
        already_exists = False
    else:
        infoDlg2=  gui.Dlg(title = "Error")
        infoDlg2.addText("Try another participant number")
        infoDlg2.show()

## remove name of participant from the dialog box information (anonimity)
info.pop("Name")

## Experimenthandler
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


# Graphical elements #
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the task!\n"+
                                                "Arrows will be presented on the screen.\n"+
                                                "You have to respond to either the direction of the arrow \n" +
                                                "or the position of the arrow \n" +
                                                "Push the spacebar to proceed to the instructions").format(name),
                                    wrapWidth = win_width*text_width)
instruct_pos        = visual.TextStim(win,text=("Indicate as quickly as possible where the arrow\n" +
                                                "is presented on the screen. \n" +
                                                "When presented left: press the left key \n" +
                                                "When presented right: press the right key \n" +
                                                "When presented in the middle of the screen: \n" +
                                                "press the down key \n" +
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
instruct_dir        = visual.TextStim(win,text=("Indicate as quickly as possible where the arrow\n" +
                                                "is directed on the screen. \n" +
                                                "When directed to the right (>): press the right key \n" +
                                                "When directed to the left (<): press the left key \n" +
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

def announce_blockstart(bloknr):
    if bloknr < 9:
        instructions = instruct_dir
    else:
        instructions = instruct_pos
    instructions.draw()
    win.flip()
    event.waitKeys(keyList = "space")

def choose_trials(bloknr):
    # create the trials
    if bloknr < 9:
        Design_block = Design_dir 
    else:
        Design_block = Design_pos
    trials = data.TrialHandler(trialList = Design_block, nReps = nReps , method = "random")  
    
    # Esther: fillRandom was hier nog net iets beter dan random
    
    thisExp.addLoop(trials)
    return trials

# to make sure that participants don't press a button that does not belong to the response options
def keys(bloknr):
    if bloknr < 9:
        keys = event.waitKeys(keyList = ["right","left"])
    else:
        keys = event.waitKeys(keyList = ["down","right","left"])
    return keys

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

block = 0
while block < nBlocks:
    announce_blockstart(block)
    
    trials = choose_trials(block)
    
    # start of the trial loop
    for trial in trials:
        
        ## display the arrow on the screen
        stimulus.text = trial["Stimulus"]
        stimulus.pos = trial["Position"]
        stimulus.draw()
        win.flip()
        
        ## wait for the response
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        Keys =keys(block)
        
        ## calculate accuracy
        accuracy = 1*(Keys[0]==trial["Correct answer"])
        
        ## store the information in the ExperimentHandler
        trials.addData("RT", my_clock.getTime())
        trials.addData("response", Keys[0])
        trials.addData("Accuracy", accuracy)
        trials.addData("Trial nr", block * nBlockTrials)
        thisExp.nextEntry()
    block += 1
    
# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()

