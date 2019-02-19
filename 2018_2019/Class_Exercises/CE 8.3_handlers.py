# Code for Stroop task randomization
# Blocked randomization with two instructions, no repetitions

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


# make the design for one block

## convert to a data frame to easily add dummy columns
dataFrame = pandas.DataFrame.from_dict(Design)
dataFrame["StimType"] = range(dataFrame.shape[0])

## each block consists of 80 trials, or 5 repetitions of the 16 unique trials in the design
blockTrials = pandas.concat([dataFrame]*nReps, ignore_index = True)

## extract the trial indices
index = list(blockTrials.index)


# make the trial stucture for the entire experiment
 
## Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = "CE8_3_output_handlers")


## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    # fill in the random trial order per block
    
    stopcriterium = 0
    while stopcriterium != 1:
    
        ## suggest a shuffle
        numpy.random.shuffle(index)
        blockTrials = blockTrials.iloc[index]
        
        ## calculate the difference between subsequent values 
        comparison = blockTrials['StimType'].diff()
        
        ## adjust the stopcriterium when necessary
        if sum(comparison == 0) == 0:
            stopcriterium = 1
    
    ## convert dataframe to list of dictionaries
    trial_list = pandas.DataFrame.to_dict(blockTrials, orient = "records")
    
    ## completely random trial order
    blockTrialsHandler = data.TrialHandler(trial_list, nReps = 1, method = "sequential")
    
    ## add the block to the ExperimentHandler
    thisExp.addLoop(blockTrialsHandler)
    
    for trial in blockTrialsHandler:
        
        ## store the block number
        blockTrialsHandler.addData("Block", blocki+1)
        
        ## fill in the instruction and correct answer
        if (blocki+1)%2 == 0:
            blockTrialsHandler.addData("Instruction", "atypical")
            CorAns = trial["ColorWord"]
        else:
            blockTrialsHandler.addData("Instruction", "typical")
            CorAns = trial["FontColor"]
        CorAns = CorAns.replace("red","d")
        CorAns = CorAns.replace("blue","f")
        CorAns = CorAns.replace("green","j")
        CorAns = CorAns.replace("yellow","k")
        blockTrialsHandler.addData("CorAns", CorAns)
        
        ## proceed to the next triall
        thisExp.nextEntry()


# Validation and export

## Note that we can't validate the design before executing it, we can only look at the output file
