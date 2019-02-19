# Code for Stroop task randomization
# Blocked randomization

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

## convert to a data frame to easily add a dummy column for the block number
dataFrame = pandas.DataFrame.from_dict(Design)
dataFrame["Block"] = -1


# make the design for one block

## each block consists of 80 trials, or 5 repetitions of the 16 unique trials in the design
blockTrials = pandas.concat([dataFrame]*nReps, ignore_index = True)

## extract the trial indices
index = list(blockTrials.index)


# make the trial stucture for the entire experiment

## make empty data frame that will contain all the trials
trials = pandas.DataFrame(columns = ["ColorWord","FontColor","Block"])


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## randomize the trial order
    numpy.random.shuffle(index)
    blockTrials = blockTrials.iloc[index]
    
    ## fill in the block number (starting from 1 instead of 0)
    blockTrials["Block"] = blocki+1
    
    ## add the current block to the file with all the trials
    trials = trials.append(blockTrials)


# Validation and export

## cross table validation
print(pandas.crosstab(trials.ColorWord, [trials.FontColor, trials.Block]))

## export
trials.to_csv(path_or_buf = "CE8_1_output_dataframe.csv", index = False)
