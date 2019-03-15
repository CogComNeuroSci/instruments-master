# import modules
from psychopy import visual, event, core, gui, event, data
import time, pandas, os
import numpy as np


## INITIALIZATION ##

# escape option
if event.getKeys(keyList="esc"):
    core.quit()

# set the directory
my_directory = os.getcwd()

# initialize dialog box
info = {"Participant name": " ", "Participant number": 0, "Age": 0, "Gender": ["male", "female"], "Handedness": ["left", "right", "ambidexter"]}

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary=info, title="Lexical Decision Task")
    
    # construct the name of the folder that will hold the data
    directory_to_write_to = my_directory + "/data"
    
    # create the folder 'data' if it doesn't exist yet
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)

    # construct the name of the data file
    file_name = "Test4_subject_" + str(info["Participant number"])
    
    # check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        already_exists = False
    else:
        # if the data file name has already been used, ask the participant to call the researcher
        myDlg2 = gui.Dlg(title = "Participant number already exists")
        myDlg2.addText("Please call the experimentor")
        myDlg2.show()

# extract the name of the participant from the dialog box information
subject_name = info["Participant name"]

# remove the name of the participant from the dialog box information for anonimity
info.pop("Participant name")


# initialization of basic experiment constants
win = visual.Window(size=[1000,700], units="norm")
my_clock = core.Clock()
nBlocks = 12
nBlockTrials = 60

# initialization of stimulus presentation
Arrow = visual.TextStim(win, text=" ")

## INSTRUCTIONS ##

Welcome = visual.TextStim(win, text = "Welcome to the experiment {0}!".format(info["Participant name"]))
Welcome.draw()
win.flip()
event.waitKeys(keyList=["space"])

Instructions = visual.TextStim(win, text = " ", height = 0.05)


## TRIAL CHARACTERISTICS ##

# definition of core trial characteristics
StimOriOptions = np.array(["<", ">"])
StimPosOptions = np.array([(-1,0),(0,0),(1,0)])

RespOptions = np.array(["left", "down", "right"])

# determine number of unique trials
nStimOriOptions = len(StimOriOptions)           # 2
nStimPosOptions = len(StimPosOptions)           # 3
nUnique = nStimOriOptions * nStimPosOptions     # 6
UniqueTrials = np.array(range(nUnique))         # [0 1 2 3 4 5]

# create the arrays for the factorial design (3*2)
StimOri = [0, 1, 0, 1, 0, 1]
StimPos = [0, 1, 2, 0, 1, 2]

# store arrays in factorial-design trial matrix
Design = np.column_stack([StimOri, StimPos])


## BLOCK DESIGN ##

# make the design for one block
nReps = int(nBlockTrials/nUnique)
BlockTrials = np.tile(Design, (nReps, 1))        # repeat the design for every block


## FULL-EXPERIMENT DESIGN ##

# determine total number of trials
nTrials = nBlocks * nBlockTrials

# create an empty trial matrix
trials = np.ones((nTrials, 14)) * np.nan

# provide the random trial order per block and store the core trial characteristics
for blocki in range(nBlocks):
    np.random.shuffle(BlockTrials)                              # shuffle the 60 trials for this block
    CurrentTrials = np.array(range(nBlockTrials)) + blocki*nBlockTrials         # current trial number for the full experiment
    trials[CurrentTrials, 0] = info["Participant number"]
    trials[CurrentTrials, 1] = info["Age"]
    trials[CurrentTrials, 2] = info["Gender"]
    trials[CurrentTrials, 3] = info["Handedness"]
    trials[CurrentTrials, 4] = blocki+1                                     # fill in the block number
 #   trials[CurrentTrials, 5] = CurrentTrials[blocki]                # store the within-block trial number
 #   trials[CurrentTrials, 6] = CurrentTrials[blocki]                # store the cumulative trial number
    trials[CurrentTrials, 7] = BlockTrials[CurrentTrials, 0]    # store the stimulus orientation
    trials[CurrentTrials, 8] = BlockTrials[CurrentTrials, 1]    # store the stimulus position
    if BlockTrials[CurrentTrials] == [0, 0] or [1, 2]:        # store the congruence
        trials[CurrentTrials, 9] = 0            # congruent
    elif BlockTrials[CurrentTrials] == [0, 2] or [1, 0]:
        trials[CurrentTrials, 9] = 1            # incongruent
    else: 
        trials[CurrentTrials, 9] = 2            # neutral
    if (blocki+1)%3 == 0:                                       # store the correct response
        trials[CurrentTrials, 10] = trials[CurrentTrials, 1]    # determined by orientation (1/3)
    else:
        trials[CurrentTrials, 10] = trials[CurrentTrials, 0]    # determined by position (2/3)


# intra-block trial loop and stimulus presentation
for b in range(nBlocks):
    if (b+1)%3 == 0:
        Instructions.text = "In dit experiment verschijnt er een pijltje op elke trial. \n" + "Reageer op de oriëntatie van het pijltje door op het linker, onderste (midden) of rechter pijltje op uw toetsenbord te drukken. \n" + "Druk op de spatiebalk om te beginnen"
    else: 
        Instructions.text = "In dit experiment verschijnt er een pijltje op elke trial. \n" + "Reageer op de positie van het pijltje door op het linker, onderste (midden) of rechter pijltje op uw toetsenbord te drukken. \n" + "Druk op de spatiebalk om te beginnen"
    Instructions.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    
    for triali in range(nBlockTrials):
        StimOri_copy = trials[CurrentTrials, 7].copy()             # copy the numerical stimulus orientation array
        StimOri_int = StimOri_copy.astype(int)                        # convert values to integers
        Arrow.text = StimOriOptions[StimOri_int[trials[triali+(b*60), 7]]       # define the stimulus orientation to be presented based on the earlier randomized stimulus-orientation list
        Arrow.pos = StimPosOptions[trials[triali+(b*60), 8]]            # define the stimulus position
        
        Arrow.draw()                                 # draw the stimulus and prepare for response
        event.clearEvents(eventType="keyboard")
        win.flip()
        my_clock.reset()
    
        keys = event.waitKeys(keyList=["left", "down", "right"])     # store the response
        if keys[0] == "left":       
            trials[triali+(b*60), 11] = 0
        elif keys[0] == "down":
            trials[triali+(b*60), 11] = 1
        else: 
            trials[triali+(b*60), 11] = 2

        trials[triali+(b*60), 12] = int(trials[triali+(b*60), 10] == trials[triali+(b*60), 11])        # store the accuracy
        trials[triali+(b*60), 13] = my_clock.getTime()                                                # store the reaction time


## GOODBYE ##
Goodbye = visual.TextStim(win, text = "Thank you for participating {0}!".format(info["Participant name"]))
Goodbye.draw()
win.flip()
event.waitKeys(keyList=["space"])


## VALIDATION AND EXPORTATION ##

# create a pandas dataframe from numpy array
Trials = pandas.DataFrame.from_records(trials)

# name the columns
Trials.columns = ["Participant_no", "Age", "Gender", "Handedness", "Block_no", "Trial_no", "Trial_no_cumulative", "Stimulus_orientation", "Stimulus_position", "Congruence", "CorResp", "Resp", "Acc", "RT"]

# print a cross table
print(pandas.crosstab(Trials.Block_no, Trials.Stimulus))

# export the .cvs file
np.savetxt(file_name, Trials, fmt="%.2d", delimiter = "\t")

# print the trials
print(Trials)

core.quit()