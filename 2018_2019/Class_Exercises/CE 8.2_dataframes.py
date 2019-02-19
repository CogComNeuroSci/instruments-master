# Code for Stroop task randomization
# Blocked randomization with two instructions

from psychopy import data
import pandas
import numpy


# constants

## number of blocks
nBlocks = 10

## number of trials per block
nBlockTrials = 80

## number of design repetitions per block
nReps = int(nBlockTrials/(4*4))


# make the design based on the core trial characteristics

## make the 4-by-4 factorial design
colors = ["red","blue","green","yellow"]
Design = data.createFactorialTrialList({"ColorWord": colors, "FontColor": colors})

## convert to a data frame to easily add dummy columns
dataFrame = pandas.DataFrame.from_dict(Design)
dataFrame["Block"] = -1
dataFrame["Instruction"] = "m"
dataFrame["CorAns"] = "m"


# make the design for one block

## each block consists of 80 trials, or 5 repetitions of the 16 unique trials in the design
blockTrials = pandas.concat([dataFrame]*nReps, ignore_index = True)

## extract the trial indices
index = list(blockTrials.index)


# make the trial stucture for the entire experiment

## make empty data frame that will contain all the trials
trials = pandas.DataFrame(columns = ["ColorWord","FontColor","Block","Instruction","CorAns"])


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## randomize the trial order
    numpy.random.shuffle(index)
    blockTrials = blockTrials.iloc[index]
    
    ## fill in the block number (starting from 1 instead of 0)
    blockTrials["Block"] = blocki+1
    
    ## fill in the instruction and correct answer
    if (blocki+1)%2 == 0:
        blockTrials["Instruction"] = "atypical"
        blockTrials["CorAns"] = blockTrials["ColorWord"]
    else:
        blockTrials["Instruction"] = "typical"
        blockTrials["CorAns"] = blockTrials["FontColor"]
    
    ## add the current block to the file with all the trials
    trials = trials.append(blockTrials)

## determine the correct response button
trials["CorAns"].replace(["red","blue","green","yellow"], ["d","f","j","k"], inplace = True)


# Validation and export

## cross table validation
print("Block randomization")
print(pandas.crosstab(trials.ColorWord, [trials.FontColor, trials.Block]))
print("Block instructions")
print(pandas.crosstab(trials.Instruction, trials.Block))
print("Correct answers")
print(pandas.crosstab(trials.CorAns, [trials.Instruction, trials.FontColor]))
print(pandas.crosstab(trials.CorAns, [trials.Instruction, trials.ColorWord]))

## export
trials.to_csv(path_or_buf = "CE8_2_output_dataframe.csv", index = False)
