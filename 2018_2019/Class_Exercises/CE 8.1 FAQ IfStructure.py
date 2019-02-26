# Code for Stroop task randomization
# Blocked randomization

import pandas
import numpy


# constants

## number of blocks
nBlocks = 10

## number of trials per block
nBlockTrials = 80


# make the design based on the core trial characteristics

## declare all levels of the factor
ColorOptions = numpy.array(["red","blue","green","yellow"])

## determine the number of levels for the factor
Ncolors = len(ColorOptions)
Nunique = Ncolors * Ncolors

## determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

## make the 4-by-4 factorial design
ColorWord = numpy.floor(UniqueTrials / Ncolors)
FontColor = numpy.floor(UniqueTrials / 1) %  Ncolors

## combine arrays in trial matrix
Design = numpy.column_stack([ColorWord, FontColor])


# make the design for one block

## number of design repetitions per block
nReps = int(nBlockTrials/Nunique)

## repeat the 4-by-4 design five times
blockTrials = numpy.tile(Design, (nReps, 1))

## fill in the block number (starting from 1 instead of 0)
blocknr = numpy.repeat(-1, blockTrials.shape[0])

## add the block numbers to the trial matrix
trials = numpy.column_stack([blockTrials, blocknr])


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## randomize the trial order
    numpy.random.shuffle(trials)
    
    ## insert the block number
    trials[:,2] = blocki
    
    if blocki == 0:
        AllTrials = trials
    else:
        AllTrials = numpy.vstack((AllTrials, trials))


# Validation and export

## creating pandas dataframe from numpy array
trials = pandas.DataFrame.from_records(AllTrials)

## name the columns
trials.columns = ["ColorWord", "FontColor", "Block"]

## cross table validation
print(pandas.crosstab([trials.ColorWord, trials.FontColor], trials.Block))

## export
trials.to_csv(path_or_buf = "CE8_1_output_arrays_ifstructure.csv", index = False)
