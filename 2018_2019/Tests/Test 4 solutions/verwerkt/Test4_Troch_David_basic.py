# import
from psychopy import data, visual, event, core, gui, os
import pandas, random, numpy

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing
my_clock     = core.Clock()
info         = {"Participant number": str(0), "Name": "", "Age": 0, "Gender":"m, f, third gender", "Handedness": "L, R, ambidextrous"}
nBlocks      = 12
nBlockTrials = 60

# stimuli
S1 = visual.TextStim(win, pos = (-0.5 , 0), text = "<")
S2 = visual.TextStim(win, pos = (0, 0), text = "<")
S3 = visual.TextStim(win, pos = (0.5, 0), text = "<")
S4 = visual.TextStim(win, pos = (-0.5 , 0), text = ">")
S5 = visual.TextStim(win, pos = (0, 0), text = ">")
S6 = visual.TextStim(win, pos = (0.5, 0), text = ">")

# Text elements
welcome     = visual.TextStim(win, text = "Welcome, {0}!".format(str(info["Name"])))
proceed     = visual.TextStim(win, text = "Press the spacebar to continue.")
instructdir = visual.TextStim(win, text = "Here you have to respond to the direction of the arrow. Press the left arrow key when the arrow on the screen points to the left and press the right arrow key when the arrow points to the right.")
instructpos = visual.TextStim(win, text = "Now you have to react to the position of the arrow. Press the left arrow key when the arrow on the screen is on the left, press the down key when the arrow is in the middle and the right arrow key when the arrow is located on the right.")
goodbye     = visual.TextStim(win, text = "Thank you for participating in this experiment!")

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test4")
    directory_to_write_to = my_directory + "/data_Test4"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
subject_name = info["Name"]

# Simple version of the trials


# number of blocks
nBlocks = nBlocks

# number of trials per block
nBlockTrials  = nBlockTrials

## number of design repetitions per block
nReps = int(nBlockTrials/(2*3))


# make the design based on the core trial characteristics

## make the 2-by-3 factorial design
Design = data.createFactorialTrialList({"Direction": Directions, "Position": Positions})
Directions = ["<", ">"]
Positions = [(-0.5, 0), (0, 0), (0.5, 0)]

# make the trial stucture for the entire experiment
 
## Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = "Test4_output_handlers")


## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    # make the design for one block
    
    ## completely random trial order
    blockTrials = data.TrialHandler(Design, nReps = nReps, method = "fullRandom")
    
    ## add the block to the ExperimentHandler
    thisExp.addLoop(blockTrials)
    
    for trial in blockTrials:
        
        ## store the block number
        blockTrials.addData("Block", blocki+1)
        
        
        
        ## proceed to the next trial
        thisExp.nextEntry()
