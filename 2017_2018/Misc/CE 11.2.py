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


# add a dummy column for the block number, instruction and correct answer
dataFrame["Block"] = -1
dataFrame["Instruction"] = "m"
dataFrame["CorAns"] = "m"


# make empty data frame that will contain all the trials
AllTrials = pandas.DataFrame(columns = ["ColorWord","FontColor","Block","Instruction","CorAns"])


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
    
    ## fill in the instruction and correct answer
    if (i+1)%2 == 0:
        Random["Instruction"] = "typical"
        Random["CorAns"] = Random["ColorWord"]
    else:
        Random["Instruction"] = "atypical"
        Random["CorAns"] = Random["FontColor"]
    
    ## add the current block to the file with all the trials
    AllTrials = AllTrials.append(Random)


# determine the correct response button
AllTrials["CorAns"].replace(["red","blue","green","yellow"], ["d","f","j","k"],inplace = True)


# cross table validation
print("Block randomization")
print(pandas.crosstab(AllTrials.ColorWord, [AllTrials.FontColor, AllTrials.Block]))
print("Block instructions")
print(pandas.crosstab(AllTrials.Instruction, AllTrials.Block))
print("Correct answers")
print(pandas.crosstab(AllTrials.CorAns, [AllTrials.Instruction, AllTrials.FontColor]))
print(pandas.crosstab(AllTrials.CorAns, [AllTrials.Instruction, AllTrials.ColorWord]))