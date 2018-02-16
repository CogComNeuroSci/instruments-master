# Code for Stroop task randomization
# by Esther De Loof & Tom Verguts, feb 2018

from psychopy import data
import pandas
import random


# constants
## number of blocks
nBlocks = 10
## number of design repetitions per block
nReps = 5


# make the 4-by-4 factorial design in data frame format
colors = ["red","blue","green","yellow"]
Design = data.createFactorialTrialList({"ColorWord": colors, "FontColor": colors})
dataFrame = pandas.DataFrame.from_dict(Design)


# add a dummy column for the block number
dataFrame["Block"] = -1


# make empty data frame that will contain all the trials
AllTrials = pandas.DataFrame(columns = ["ColorWord","FontColor","Block"])


# make a block
## each block consists of 80 trials, or 5 repetitions of the 16 unique trials in the design
Extended = pandas.concat([dataFrame]*nReps, ignore_index = True)

## extract the trial indices
index = list(Extended.index)


# loop over the 10 blocks to randomize each block separately
for i in range(nBlocks):
    
    ## randomize the trial order
    random.shuffle(index)
    Random = Extended.iloc[index]
    
    ## fill in the block number (starting from 1 instead of 0)
    Random["Block"] = i+1
    
    ## add the current block to the file with all the trials
    AllTrials = AllTrials.append(Random)


# cross table validation
print(pandas.crosstab(AllTrials.ColorWord, [AllTrials.FontColor, AllTrials.Block]))