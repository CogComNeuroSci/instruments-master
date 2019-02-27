# Code for Stroop task randomization
# Blocked randomization, congruency

import pandas
import numpy


# constants

## number of blocks
nBlocks = 10

## number of trials per block
nBlockTrials = 48


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


# determine the congruency and even out the congruent and incongruent trials

## deduce the congruence
CongruenceBoolean = numpy.array(ColorWord == FontColor)
Congruence = CongruenceBoolean*1

## combine arrays in trial matrix
DesignBalanced = numpy.column_stack([ColorWord, FontColor, UniqueTrials, Congruence])

## extract the congruent trials
CongruentTrials = DesignBalanced[DesignBalanced[:,3] == 1,:]

## how many times do we need to repeat these trials to even out the congruent and incongruent trials
nRepsCongruent = int((DesignBalanced.shape[0]-CongruentTrials.shape[0])/CongruentTrials.shape[0] - 1)

## repeat the congruent trials to even out the congruent and incongruent trials
CongruentTrials = numpy.tile(CongruentTrials, (nRepsCongruent, 1))

## create a unblanced design that evens out the congruent and incongruent trials
DesignUnbalanced = numpy.concatenate((DesignBalanced, CongruentTrials), axis=0)


# make the design for one block

## number of balanced design repetitions per block
nRepsBalanced = int(nBlockTrials/Nunique)

## repeat the 4-by-4 design
blockTrialsBalanced = numpy.tile(DesignBalanced, (nRepsBalanced, 1))

## number of unbalanced design repetitions per block
nRepsUnbalanced = int(nBlockTrials/DesignUnbalanced.shape[0])

## repeat the unbalanced design
blockTrialsUnbalanced = numpy.tile(DesignUnbalanced, (nRepsUnbalanced, 1))

# make the trial stucture for the entire experiment

## number of trials in the experiment
ntrials = nBlocks * nBlockTrials

## make empty trial matrix
trials = numpy.ones((ntrials,7)) * numpy.nan


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## is this a balanced or unbalanced block?
    if (blocki)%2 == 0:
        blockTrials = blockTrialsBalanced
    else:
        blockTrials = blockTrialsUnbalanced
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:4] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 4] = blocki+1
    
    ## store the block type
    trials[currentTrials, 5] = (blocki+1)%2
    
    ## store the correct response
    trials[currentTrials, 6] = trials[currentTrials, 1]     ## correct answer determined by font color


# Validation and export

## creating pandas dataframe from numpy array
trials = pandas.DataFrame.from_records(trials)

## name the columns
trials.columns = ["ColorWord", "FontColor", "StimType", "Congruence", "Block", "Balance", "CorAns"]

## cross table validation
print("Block randomization")
print(pandas.crosstab(trials.Congruence, trials.Balance))
print(pandas.crosstab(trials.Congruence, trials.Block))
print("Correct answers")
print(pandas.crosstab(trials.FontColor, trials.CorAns))
print(pandas.crosstab(trials.Block, trials.StimType))

## export
trials.to_csv(path_or_buf = "CE8_4_output_arrays.csv", index = False)
