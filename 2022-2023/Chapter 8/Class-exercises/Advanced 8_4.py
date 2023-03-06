import numpy as np
import pandas as pd
from psychopy import data
import os

# randomization across participants
## determing the participant number (will later be done via the GUI)
participant = 1

## importing stimuli
dfStimuli = pd.read_csv("dfStimuli.txt", sep = '\t', header = None, encoding = 'latin-1')

## this first 6 columns contain the words and the last 6 columns contain the matched non-words
#print(dfStimuli.shape)
#print(dfStimuli)

## Latin square to counterbalance 6 lists over 6 conditions, across participants
latSq = [   [1, 2, 6, 3, 5, 4],
            [2, 3, 1, 4, 6, 5],
            [3, 4, 2, 5, 1, 6],
            [4, 5, 3, 6, 2, 1],
            [5, 6, 4, 1, 3, 2],
            [6, 1, 5, 2, 4, 3]]

## assigning participant to order (n = 36)
listOrder = np.array(latSq[int(participant)%6])


# initialize all variables and arrays
ncenter         = 3     ## position on the screen: left, middle, right
nspace          = 2     ## spacing of the letters: narrow or broad
nword           = 2     ## words versus nonwords
nblock          = 5     ## number of blocks
nreps_design    = 20    ## number of repetitions of the ncenter * nspace design within each block (only words or only non-words)

nconditions     = ncenter * nspace          ## the two crossed factors in the design (will later be doubled for the words and non-words)
ndesign         = nconditions * nword       ## each condition will be presented with a word and its matched non-word

blockLength     = ndesign * nreps_design    ## number of trials in a block
ntrials         = blockLength * nblock      ## number of trials in the entire experiment

nListItems      = int(ntrials/nconditions/nword)    ## number of words (and matched non-words) in each of the 6 stimulus columns we read in at the top of the script

## derived arrays
centers         = np.array(range(ncenter))                              ## 0: left, 1: middle, 2: right
spacing         = np.array(range(nspace))                               ## 0: narrow, 1: broad
word_nonword    = np.array(range(nword))                                ## 0: word, 1: non-word
conditions      = np.array(range(nconditions))                          ## 0 to 5: crossing of centers and spacing
listItems       = np.array(range(nListItems))                           ## 0 to 99: index for the words (and matched non-words) in the 6 stimulus columns
emptyArray      = np.ones((nconditions,1)) * -1                         ## empty array to later feed in the stimulus numbers per block
blockTrials     = np.array(range(blockLength))                          ## 0 to 239: all the trials in a block

## make empty trial matrix
trials          = np.ones((ntrials,9)) * -1


# randomize the word order in each list (for each participant)
randomstim      = np.ones((nListItems,nconditions)) * -1

for list in range(nconditions):
    np.random.shuffle(listItems)
    randomstim[:,list] = listItems


# make the factorial design
factorCenter    = np.floor(conditions / nspace)
factorSpacing   = np.floor(conditions / 1) % nspace


for thisblock in range(nblock):
    
    ## select the unique trials for this block
    uniqueStim = randomstim[np.array(range(nreps_design)) + (thisblock*nreps_design),:]
    
    ## generate some trial numbers
    thisblock_trials = np.array(range(blockLength))
    thisblock_trials_words = np.array(range(int(blockLength/nword)))
    thisblock_trials_nonwords = thisblock_trials_words + int(blockLength/nword)
    
    ## combine arrays in block matrix
    thisblock_design = np.column_stack([factorCenter, factorSpacing, conditions, listOrder, emptyArray, emptyArray, emptyArray, emptyArray, emptyArray])
    
    ## repeat the design for the number of repetitions per block
    thisblock_design = np.tile(thisblock_design, (nreps_design, 1))
    
    ## add in the stimulus indices
    thisblock_design[:,4] = np.reshape(uniqueStim, (1,np.product(uniqueStim.shape)))
    
    ## repeat the design for the words and the nonwords
    thisblock_design = np.tile(thisblock_design, (nword, 1))
    
    ## change the words lists to the nonwords lists for the nonwords
    thisblock_design[thisblock_trials_nonwords,3] = thisblock_design[thisblock_trials_nonwords,3] + nconditions
    
    ## code the trials as word and nonword trials
    thisblock_design[:,5] = np.repeat(word_nonword,nconditions*nreps_design)
    
    ## shuffle the trials in this block
    np.random.shuffle(blockTrials)
    
    ## reoder the trial in this block in the random order
    thisblock_design = thisblock_design[blockTrials,]
    
    ## add the trial numbers for this block
    thisblock_design[:,6] = thisblock_trials
    thisblock_design[:,7] = thisblock_trials + (thisblock*blockLength)
    thisblock_design[:,8] = thisblock
    
    ## store the trials for this block in the experiment array
    trials[thisblock_trials + (thisblock*blockLength),:] = thisblock_design

#print(trials)


## creating pandas dataframe from numpy array
dataframe = pd.DataFrame.from_records(trials)

## name the columns
dataframe.columns = ['Center', 'Spacing', 'Condition', 'listMapping', 'stimulusIndex', 'Word', 'blockTrial', 'Trial', 'Block']

print(pd.crosstab(dataframe.Center, dataframe.Spacing))
print(pd.crosstab([dataframe.Center, dataframe.Spacing], dataframe.Condition))
print(pd.crosstab(dataframe.Condition, dataframe.listMapping))
print(pd.crosstab([dataframe.stimulusIndex, dataframe.Condition] , dataframe.Block))
print(pd.crosstab([dataframe.stimulusIndex, dataframe.Condition] , dataframe.Word))


