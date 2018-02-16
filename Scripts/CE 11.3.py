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
dataFrame["StimType"] = range(dataFrame.shape[0])


# make empty data frame that will contain all the trials
AllTrials = pandas.DataFrame(columns = ["ColorWord","FontColor","Block","Instruction","CorAns","StimType"])


# make a block
## each block consists of 80 trials, or 5 repetitions of the 16 unique trials in the design
Extended = pandas.concat([dataFrame]*nReps, ignore_index = True)

## extract the trial indices
index = list(Extended.index)


# loop over the 10 blocks to randomize each block separately
for i in range(nBlocks):
    
    stopcriterium = 0
    while stopcriterium != 1:
    
        ## suggest a shuffle
        random.shuffle(index)
        Suggestion = Extended.iloc[index]
        
        ## check whether there are two consecutive trials with the same stimulus
        current     = Suggestion.iloc[range(Suggestion.shape[0]-1)]
        subsequent  = Suggestion.iloc[range(1,Suggestion.shape[0])]
        
        comparison  = current["StimType"] == subsequent["StimType"]
        
        ## adjust the stopcriterium when necessary
        if comparison.sum() == 0:
            stopcriterium = 1
    
    ## randomize the trial order
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


# no same consecutive trials check
print("Consecutive trials check")
current     = AllTrials.iloc[range(AllTrials.shape[0]-1)]
subsequent  = AllTrials.iloc[range(1,AllTrials.shape[0])]
comparison  = current["StimType"] == subsequent["StimType"]
blocks      = range(1,nBlocks)
blockStarts = [x * Extended.shape[0] for x in blocks]
print(blockStarts)
comparison.drop(comparison.index[blockStarts], inplace = True)
print(comparison.sum())