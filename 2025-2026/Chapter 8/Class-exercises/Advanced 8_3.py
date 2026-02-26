import numpy as np
import pandas as pd
from psychopy import data
import os

# determing the participant number (will later be done via the GUI)
participant = 1


# initialize all variables and arrays
ntiming         = 2     ## number of timings of the sound (before or after)
ngo             = 2     ## number of trial types (go versus no-go)
nlateral        = 2     ## number of response hands (left versus right)
nsound          = 20    ## smallest design for 70-15-15 percent combination (14-3-3)
nemo            = 36    ## number of unique emotional sounds per emotion type
nblock          = 16    ## number of blocks
nreps_design    = 6     ## number of repetitions of the unique trials
nreps_emo       = 4     ## number of times the emotional sounds are repeated

design          = ntiming * ngo * nlateral * nsound
ntrials         = design * nreps_design
trialsPerBlock  = int(ntrials/nblock)

## derived arrays
timing          = np.array(range(ntiming))
go              = np.array(range(ngo))
lateral         = np.array(range(nlateral))
sound           = np.array(range(nsound))
emosounds       = np.array(range(nemo))+1
blocks          = np.array(range(nblock))
factorDesign    = np.array(range(design))

## make empty trial matrix
trials      = np.ones((ntrials,10)) * -1
trials[:,0] = range(ntrials)


# make the factorial design
factorTiming    = np.floor(factorDesign / (nsound*nlateral*ngo))
factorGo        = np.floor(factorDesign / (nsound*nlateral)) % ngo
factorLateral   = np.floor(factorDesign / nsound) % nlateral
factorSound     = np.floor(factorDesign / 1) % nsound

## combine all the unique trials
unique_trials   = np.column_stack([factorTiming, factorGo, factorLateral, factorSound, factorDesign])


# fill in the trials matrix
replication_counter = 0
for rep_i in range(nreps_design):
    
    ## list the indexes for this replication block
    these_rep_trials = np.array(range(design)) + (rep_i*design)
    
    ## shuffle the unique trials
    np.random.shuffle(unique_trials)
    
    ## insert the new order into the trial matrix
    trials[these_rep_trials,1:6] = unique_trials
    
    ## add the replication number
    trials[these_rep_trials,6] = rep_i

## add the block number
trials[:,7] = np.repeat(blocks, trialsPerBlock)

## add the sound stimulus number
trials[trials[:,4]<14,8] = 0
trials[trials[:,4]>13,8] = 1
trials[trials[:,4]>16,8] = 2

## add the number of the sound stimulus
neutralTrials   = trials[trials[:,8]==0,0] 
happyTrials     = trials[trials[:,8]==1,0] 
sadTrials       = trials[trials[:,8]==2,0] 

## loop over the four repetitions of the unique emotion sounds
for soundrep_i in range(nreps_emo):
    
    ## indices for this repetition of the sounds
    these_soundrep_trials = np.array(range(nemo)) + (soundrep_i*nemo)
    
    ## shuffle the unique sounds for the happy sounds
    np.random.shuffle(emosounds)
    
    ## fill in the happy sounds in the trial matrix
    trials[np.isin(range(ntrials), happyTrials[these_soundrep_trials]),9] = emosounds
    
    ## shuffle the unique sounds for the sad sounds
    np.random.shuffle(emosounds)
    
    ## fill in the sad sounds in the trial matrix
    trials[np.isin(range(ntrials), sadTrials[these_soundrep_trials]),9] = emosounds

## fill in the neutral sounds in the trial matrix
trials[np.isin(range(ntrials), neutralTrials),9] = 0

#print(trials)
#print(trials[1,:])


## creating pandas dataframe from numpy array
dataframe = pd.DataFrame.from_records(trials)

## name the columns
dataframe.columns = ['trial_nr', 'timing', 'go_nogo', 'lateralization', 'sound', 'unique_trial', 'trial_repeat', 'block_nr', 'soundType', 'soundStim']

print(pd.crosstab(dataframe.timing, [dataframe.go_nogo, dataframe.lateralization]))
print(pd.crosstab(dataframe.unique_trial, [dataframe.timing, dataframe.go_nogo, dataframe.lateralization]))
print(pd.crosstab(dataframe.trial_repeat, dataframe.block_nr))
print(pd.crosstab(dataframe.soundType, dataframe.soundStim))
