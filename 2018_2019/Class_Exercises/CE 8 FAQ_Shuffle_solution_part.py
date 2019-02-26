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

# now randomize: 10 blocks with 80 trials in each block
for block in range (nb_blocks):
    np.random.shuffle(Stroop_array_full)
    
    RANDOM = Stroop_array_full
    
    print(RANDOM)