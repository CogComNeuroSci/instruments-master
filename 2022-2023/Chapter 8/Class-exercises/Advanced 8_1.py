import numpy as np
import pandas as pd
from psychopy import data
import os


# initialize all variables and arrays
nstim_mini      = 4     ## number of unique stimuli in each mini block
nincentives     = 2     ## number of incentive structures (2 incentivized and 2 not incentivized)
nrewards        = 4     ## number of unique reward blocks

nreps_stim      = 8     ## number of repetitions of the unique stimuli in the mini block
nreps_incent    = 2     ## number of repetitions of the incentives within one mini block
nreps_reward    = 2     ## number of repetitions of the reward
nreps_subblock  = 2     ## number of subblocks within each reward block

## derived numbers
ntrials         = int((nstim_mini * nreps_stim) * nreps_subblock * (nrewards * nreps_reward))
nstim           = nstim_mini * nreps_subblock * (nrewards * nreps_reward)

## derived arrays
uniquestim      = np.array(range(nstim_mini))
stimuli         = np.array(range(nstim))
rewards         = np.array(range(nrewards))

mini_block      = np.repeat(uniquestim, nreps_stim)
reward_block    = np.repeat(rewards, nreps_reward)

## make empty trial matrix
trials          = np.ones((ntrials,9)) * -1
trials[:,0]     = range(ntrials)


# stimulus shuffling (different order for each participant)
np.random.shuffle(stimuli)


# reward block shuffling (different order for each participant)
np.random.shuffle(reward_block)


# fill in the trials matrix
mini_block_counter = 0
## loop over the 8 reward blocks
for reward_block_i in range(len(reward_block)):
    
    ## fill in each of the subblocks (2 mini blocks)
    for subblock_i in range(nreps_subblock):
        
        ## what are the current mini block stimuli
        stimi = stimuli[np.array(range(nstim_mini)) + nstim_mini*mini_block_counter]
        
        ## what are the current mini block trials
        triali = np.array(range(len(mini_block))) + len(mini_block)*mini_block_counter
        
        ## choose two trials that will be incentivized
        random_incentives = np.random.choice(nstim_mini, int(nstim_mini/nincentives), replace = False)
        
        ## mini block shuffling
        np.random.shuffle(mini_block)
        
        ## Store the trial characteristics
        trials[triali,1] = reward_block_i                                           ## cumulative cue block number
        trials[triali,2] = subblock_i                                               ## first or second subblock
        trials[triali,3] = reward_block[reward_block_i]                             ## type of reward block
        trials[triali,4] = stimi[mini_block]                                        ## number of the stimulus that is presented
        trials[triali,5] = np.isin(mini_block, random_incentives)*1                 ## is the trial incentivized or not (0/1)
        trials[triali,6] = trials[triali,5] + (trials[triali,3]%2)*nincentives     ## color of the frame
        trials[triali,7] = mini_block                                               ## correct response
        trials[triali,8] = mini_block_counter                                       ## correct response
        
        ## update the mini_block counter
        mini_block_counter += 1


#print(trials[0:64,])
#print(trials[64:120,])


## creating pandas dataframe from numpy array
dataframe = pd.DataFrame.from_records(trials)

## name the columns
dataframe.columns = ['trial_nr', 'reward_block_nr', 'sub_block_nr', 'reward_block_type', 'stim_nr', 'incentive_type', 'frame_color', 'CorResp', "mini_block_nr"]

print(pd.crosstab([dataframe.reward_block_type,dataframe.incentive_type], dataframe.frame_color))
print(pd.crosstab(dataframe.reward_block_type,dataframe.CorResp))
print(pd.crosstab(dataframe.incentive_type,dataframe.mini_block_nr))
