##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##
##   Code with me session: Test 4 2022-2021   ##
##                                            ##
##   Instruments of Experimental Psychology   ##
##              Ghent University              ##
##          Academic year 2024-2025           ##
##                                            ##
##             Brent Vernaillen               ##
##   =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=  ##

##   Description   ##

#   This is a possible solution to test 4 of a couple of years ago. The script was written
#   during the code with me session on 06/03/2025

## Import the relevant modules
from psychopy import data, gui, visual, core, event
import random, os, pandas
import numpy as np

##------------------------------------------------------------------------------##
##                               Experiment Setup                               ##
##------------------------------------------------------------------------------##

# Factors
letters = ['A', 'B', 'C']
locations = [-0.5, 0, 0.5]
colors = ['black', 'green']

# responding
allowedKeys = ['f', 'j', 'q']
respDeadline = 2 # in seconds
feedbackTime = 0.3 # in seconds

# window
winH = 700
winW = 1000
winC = 'gray'

# Control
nBlocks = 2
nTrials = 36
nRepsBlock = 2

# Directory
Home = os.getcwd()

## Dlg box

# What information would we like to record from the participant?
info = {'Participant number':0,  
        'Full name': 'Brent Vernaillen',
        'Gender':'',
        'Age': 0, 
        'Handedness': ['Right', 'Left', 'Both']}

# Keep asking for a number in case it already exists
already_exists = True
while already_exists:
    
# display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="CodeWithMe")
    sub = info["Participant number"]
    
    # determine the file name
    file_name = os.path.join(Home, f"Test4_subject_{str(sub)}.csv")
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False

# Create response mapping based on the first letter of the name
if info['Full name'][0] in ['A', 'B', 'C']:
    mapping = {'green': 'j', 'black': 'f'}
    mappingID = 0
else:
    mapping = {'green': 'f', 'black': 'j'}
    mappingID = 1

# Data
output_file_name = f"Test4_subject_{info['Participant number']}"

# Create window
win = visual.Window(size = [winW, winH], color = winC, units = 'norm')

# Stimuli
targetStim = visual.TextStim(win, text = 'Some Text', height = 0.2, color = 'red', pos = (-0.5, -0.5))

# Function
def Say(text = 'Some Text', wait = feedbackTime):
    textElement = visual.TextStim(win, text = text, color = 'black', height = 0.1)
    textElement.draw()
    win.flip()
    
    if wait == 'Key':
        event.waitKeys()
    else:
        core.wait(wait)

# Present instructions
Say(f"Welcome {info['Full name'].split()[0]}!", wait = 'Key')
Say(f"press {mapping['black']} for black or {mapping['green']} for green", wait = 'Key')

# Create unique trials/conditions
trial_list = data.createFactorialTrialList({"Target": letters, "Location": locations, "Color": colors})

##----------------------------------------------------------------------------##
##                               Practice Phase                               ##
##----------------------------------------------------------------------------##

# Select 4 trials for practice form all unique trials
trial_list_practice = random.sample(trial_list, 4)

# Initiate some variables
Practice = True                     # Should we practice?
correct_counter = 0                 # How many correct trials were there?
nTries = 0                          # How many times did the subject try?

# Define experiment handler
thisExp = data.ExperimentHandler(dataFileName = output_file_name)

# Keep going until at least 2 correct
while Practice and nTries < 3:
    
    # Create trial handler
    trials_P = data.TrialHandler(trial_list_practice, nReps = 1, method = "random")
    thisExp.addLoop(trials_P)
    
    # Announce practice
    Say('This is a practice block.\n\nPress any key to start', wait = 'Key')
    
    # Start practice loop
    for trialP in trials_P:
        
        # Update the target
        targetStim.text = trialP['Target']
        targetStim.pos = (0, trialP['Location'])
        targetStim.color = trialP['Color']
        
        # Present the target
        targetStim.draw()
        win.flip()
        
        # Collect response
        keys = event.waitKeys(maxWait = respDeadline, keyList = allowedKeys)
        
        # In case of no response
        if not keys:
            keys = ['No response']
        
        # Check for quit
        if keys[0] == 'q':
            Practice = False
            break
        
        # Determine accuracy and provide feedback
        if mapping[trialP['Color']] == keys[0]:     # Correct key was pressed
            correct = 1
            Say('Correct!')
        
        elif keys[0] == 'No response':              # No key was pressed
            correct = 0
            Say('Too slow!')
        
        else:                                       # Wrong key was pressed
            correct = 0
            Say('Incorrect!')
        
        # Add the relevant data
        trials_P.addData("Response", keys[0])
        trials_P.addData("Subject", info['Participant number'])
        trials_P.addData("Accuracy", correct)
        trials_P.addData("BlockType", 0)
        trials_P.addData("mapping", mappingID)
        
        # Go to next trial
        thisExp.nextEntry()
        
        # Update correct trial  counter
        correct_counter += correct
    
    # Update number of tries
    nTries += 1
    
    # Check if practice was passed
    if correct_counter > 1:
        Practice = False

##----------------------------------------------------------------------------##
##                           Experimental Phase                               ##
##----------------------------------------------------------------------------##

# In case participant did not quit the experiment
if keys[0] != 'q':
    
    # Loop over all blocks
    for block in range(nBlocks):
        
        # Announce the block start and remind the participant of the correct mapping
        Say('The next block will start now\n\nPress any key to continue', wait = 'Key')
        Say(f"Press {mapping['black']} for black or {mapping['green']} for green\n\npress any key to start", wait = 'Key')
    
        ## Prevent trial repetitions
        
        # Initiate the emtpy trial list to store everything in
        trialListClean = []
        
        # For each repetition of the 18 unique trials, we check for repeats
        for rep in range(nRepsBlock):
            
            # Initiate repeats variable as true
            repeats = True
            
            # Reshuffle as long as there are repeats
            while repeats:
                
                # Shuffle trial_list
                np.random.shuffle(trial_list)
                
                # For the first set, we only check if there were no repeats
                if rep == 0:
                    
                    # Are all elements different from the subsequent element?
                    if not any([trial_list[i] == trial_list[i+1] for i in range(len(trial_list)-1)]):
                        repeats = False
                        trialListClean += trial_list # Add these non-repeating trials to the clean list
                
                # For the subsequent reps we additionally check if the first element of the new rep and the last
                # element of the last rep are different. We do this because joining the two lists together
                # might accidentally create a repetition
                else: 
                    if (not any([trial_list[i] == trial_list[i+1] for i in range(len(trial_list)-1)])) and (
                        trialListClean[-1] != trial_list[0]):
                        repeats = False
                        trialListClean += trial_list
        
        # Create trial handler
        # nreps is 1 instead of 2 because we already doubled the amount of unique trials before in the loop
        # We also use 'sequential' because we already shuffled in the previous loop, and additional randomization
        # might introduce repeats.
        trials_R = data.TrialHandler(trialListClean, nReps = 1, method = "sequential")
        
        # Couple experiment- and trial handler
        thisExp.addLoop(trials_R)
        
        # Validation (same number of repeats per condition)
        dataFrame = pandas.DataFrame.from_dict(trialListClean)
        print(pandas.crosstab(dataFrame.Location, [dataFrame.Target, dataFrame.Color]))
        
        # Trial loop
        for trialR in trials_R:
            
            # Update the target
            targetStim.text = trialR['Target']
            targetStim.pos = (0, trialR['Location'])
            targetStim.color = trialR['Color']
            
            # Present the target
            targetStim.draw()
            win.flip()
            
            # Collect response
            keys = event.waitKeys(maxWait = respDeadline, keyList = allowedKeys)
            
            # In case of no response
            if not keys:
                keys = ['No response']
            
            # Check for quit
            if keys[0] == 'q':
                break
            
            # Determine accuracy
            if mapping[trialR['Color']] == keys[0]: # Correct
                correct = 1
                Say('Correct!')
            
            elif keys[0] == 'No response':          # Slow
                correct = 0
                Say('Too slow!')
            
            else:                                   # Incorrect
                correct = 0
                Say('Incorrect!')
            
            # Determine congruency
            if (trialR['Target'] == 'A' and trialR['Location'] == (0, -0.5)) or (
               trialR['Target'] == 'B' and trialR['Location'] == (0, 0)) or (
               trialR['Target'] == 'C' and trialR['Location'] == (0, 0.5)):
                congruency = 'Congruent'
            
            else:
                congruency = 'Incongruent'
            
            # Add the relevant data
            trials_R.addData("Response", keys[0])
            trials_R.addData("Subject", info['Participant number'])
            trials_R.addData("Accuracy", correct)
            trials_R.addData("BlockType", 1)
            trials_R.addData("BlockNr", block + 1)
            trials_R.addData("mapping", mappingID)
            trials_R.addData("Congruency", congruency)
            
            # Go to next trial
            thisExp.nextEntry()
        
        # In case of quit
        if keys[0] == 'q':
            break

# Close the window
win.close()