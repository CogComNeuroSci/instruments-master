# Code for Stroop task randomization
# Blocked randomization, congruency

from psychopy import data
import pandas


# constants

## number of blocks
nBlocks = 10

## number of trials per block
nBlockTrials = 48


# make the design based on the core trial characteristics

## make the 4-by-4 factorial design
colors = ["red","blue","green","yellow"]
Design = data.createFactorialTrialList({"ColorWord": colors, "FontColor": colors})


# determine the congruency (and other derived properties)

## convert to a data frame to easily add dummy columns
Balanced = pandas.DataFrame.from_dict(Design)
Balanced["Congruence"] = -1
Balanced["Block"] = -1
Balanced["Balanced"] = 1
Balanced["CorAns"] = Balanced["FontColor"]
Balanced["StimType"] = range(Balanced.shape[0])

## determine the correct response button
Balanced["CorAns"].replace(["red","blue","green","yellow"], ["d","f","j","k"], inplace = True)

## deduce the congruence
Balanced.loc[Balanced["ColorWord"] == Balanced["FontColor"], "Congruence"] = 1
Balanced.loc[Balanced["ColorWord"] != Balanced["FontColor"], "Congruence"] = 0


# even out the congruent and incongruent trials

## extract the congruent trials
CongruentTrials = Balanced.loc[Balanced["Congruence"] == 1,]

## how many times do we need to repeat these trials to even out the congruent and incongruent trials
nRepsCongruent = int((Balanced.shape[0]-CongruentTrials.shape[0])/CongruentTrials.shape[0] - 1)

## repeat the congruent trials to even out the congruent and incongruent trials
CongruentTrials = pandas.concat([CongruentTrials]*nRepsCongruent, ignore_index = True)

## create a unblanced design that evens out the congruent and incongruent trials
Unbalanced = CongruentTrials.append(Balanced, ignore_index=True)

## adapt the balancedness info of the unbalanced trials 
Unbalanced["Balanced"] = 0


# make the design for one block

## number of balanced design repetitions per block
nRepsBalanced = int(nBlockTrials/(4*4))

## repeat the 4-by-4 design
blockTrialsBalanced = pandas.concat([Balanced]*nRepsBalanced, ignore_index = True)

## number of unbalanced design repetitions per block
nRepsUnbalanced = int(nBlockTrials/Unbalanced.shape[0])

## repeat the unbalanced design
blockTrialsUnbalanced = pandas.concat([Unbalanced]*nRepsUnbalanced, ignore_index = True)

## extract the trial indices
index = list(blockTrialsBalanced.index)


# make the trial stucture for the entire experiment

## make empty data frame that will contain all the trials
trials = pandas.DataFrame(columns = ["ColorWord","FontColor","Congruence","Block","Balance","CorAns","StimType"])


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## is this a balanced or unbalanced block?
    if (blocki)%2 == 0:
        blockTrials = blockTrialsBalanced
    else:
        blockTrials = blockTrialsUnbalanced
    
    ## fill in the block number (starting from 1 instead of 0)
    blockTrials["Block"] = blocki+1
    
    ## add the current block to the file with all the trials
    trials = trials.append(blockTrials)


# Validation and export

## cross table validation
print("Block randomization")
print(pandas.crosstab(trials.Congruence, trials.Balance))
print(pandas.crosstab(trials.Congruence, trials.Block))
print("Correct answers")
print(pandas.crosstab(trials.FontColor, trials.CorAns))

## export
trials.to_csv(path_or_buf = "CE8_4_output_dataframe.csv", index = False)
