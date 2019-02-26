# Chapter 8/ Class excercises

# import
import numpy as np

# experiment characteristics
Colour = ["Red","Green","Blue","yellow"]
nb_blocks = 10
nb_trials = 80

# total number of unique trials
lenCol = len (Colour)
Unique_trials = lenCol*lenCol

# make a trialmatrix with numbers from 0 to 3
Number_of_trials = np.array(range(Unique_trials))
ColourWord       = np.floor(Number_of_trials/lenCol)
ColourFont       = np.floor(Number_of_trials)%lenCol

# add everything together
Stroop_array     = np.column_stack([Number_of_trials,ColourWord,ColourFont])

# repeat the matrix
Stroop_array_full= np.tile(Stroop_array,(5,1))

# make empty trial matrix
trials = np.ones((nb_trials*nb_blocks,4)) * np.nan

for block in range(nb_blocks):
    
    ## trial number for this block
    currentTrials = np.array(range(nb_trials)) + block*(nb_trials)
    
    ## randomize the trial order
    np.random.shuffle(Stroop_array_full)
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:3] = Stroop_array_full
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 3] = block+1

print(trials)