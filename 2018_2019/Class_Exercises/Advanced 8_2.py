import numpy as np
import pandas as pd
from psychopy import data
import os

# determing the participant number (will later be done via the GUI)
participant = 1


# initialize all variables and arrays
nstim_mini  = 3     ## number of unique stimuli in each mini block
nhands      = 2     ## number of response hands
ncue        = 2     ## number of instruction cues

nreps_stim  = 2     ## number of repetitions of the unique stimuli in the mini block
nreps_hand  = 3     ## number of repetitions of the response hand mappings per cue block
nreps_cue   = 6     ## number of repetitions of each cue block

## derived numbers
ntrials     = int((nstim_mini * nreps_stim) * (nhands * nreps_hand) * (ncue * nreps_cue))
nstim       = nstim_mini * (nhands * nreps_hand) * (ncue * nreps_cue)

## derived arrays
triplet     = np.array(range(nstim_mini))
hands       = np.array(range(nhands))
cues        = np.array(range(ncue))
stimuli     = np.array(range(nstim))

mini_block  = np.repeat(triplet, nreps_stim)
hand_block  = np.repeat(hands, nreps_hand)

## make empty trial matrix
trials      = np.ones((ntrials,13)) * -1
trials[:,0] = range(ntrials)
trials[:,8] = trials[:,0]%(len(hand_block)*len(mini_block))
trials[:,9] = trials[:,0]%len(mini_block)


# stimulus shuffling (different order for each participant)
np.random.shuffle(stimuli)


# determine the order of the cue blocks
## revert the order for half of the participants
if participant%2 == 1:
    cues = np.flip(cues,0)

## let the cue switch for every block
cue_blocks = np.tile(cues, nreps_cue)


# fill in the trials matrix
mini_block_counter = 0
for cue_block_i in range(len(cue_blocks)):
    
    ## response hand shuffling
    np.random.shuffle(hand_block)
    
    ## fill in each of the hand blocks
    for hand_block_i in range(len(hand_block)):
        
        ## mini block shuffling
        shuffling = 1
        while shuffling:
            
            ## shuffle the stimuli in the mini block
            np.random.shuffle(mini_block)
            
            ## calculate the difference
            comparison = np.diff(mini_block)
            
            ## check whether there was a repeition
            if sum(comparison == 0) == 0:
                shuffling = 0
        
        ## select the stimuli for this mini-block
        stimi = stimuli[np.array(range(nstim_mini)) + nstim_mini*mini_block_counter]
        
        ## fill in the details for this mini_block
        triali = np.array(range(len(mini_block))) + len(mini_block)*mini_block_counter
        
        trials[triali,1] = cue_block_i                      ## cumulative cue block number
        trials[triali,2] = cue_blocks[cue_block_i]          ## stimulus position during instructions
        trials[triali,3] = hand_block_i                     ## cumulative hand mapping block number within this cue block
        trials[triali,4] = hand_block[hand_block_i]         ## response hand mapping
        trials[triali,5] = mini_block_counter               ## cumulative mini_block counter
        trials[triali,6] = stimi[mini_block]                ## stimulus position during instructions
        if hand_block[hand_block_i] == 0:
            trials[triali,7] = mini_block                   ## correct response button for first response mapping
        else:
            trials[triali,7] = mini_block + nstim_mini      ## correct response button for second response mapping
        trials[triali,10] = stimi[0]
        trials[triali,11] = stimi[1]
        trials[triali,12] = stimi[2]
        
        ## update the mini_block counter
        mini_block_counter += 1
        

#print(trials[range(20),:])
#print(trials[range(400,ntrials),:])

## creating pandas dataframe from numpy array
dataframe = pd.DataFrame.from_records(trials)

## name the columns
dataframe.columns = [   'trial_nr', 'cue_block_nr', 'cue_block_type', 'hand_block_nr', 'hand_block_type', 'mini_block_nr', 'stimulus_nr', 'CorResp', 'trial_cueblock_nr', 'trial_miniblock_nr',\
                        'stim1', 'stim2', 'stim3']

print(pd.crosstab(dataframe.hand_block_type, dataframe.CorResp))
print(pd.crosstab(dataframe.stimulus_nr, dataframe.CorResp))
print(pd.crosstab(dataframe.cue_block_type, dataframe.hand_block_type))

## export (just to be able to check the randomization)
dataframe.to_csv(path_or_buf = "A8_2.csv", index = False)


# Convert dataframe to list of dictionaries
trial_list = pd.DataFrame.to_dict(dataframe, orient = "records")
print(trial_list)

# completely random trial order
trials = data.TrialHandler(trial_list, nReps = 1, method = "sequential")

# what is the current working directory
my_home_directory = os.getcwd()

# determine the path for the stimuli folder
stim_folder = my_home_directory + "/stimuli"

# change directories to the stimulus folder
os.chdir(stim_folder)

# get the names of the all the files in the directory
files = os.listdir()
print(len(files))
print(files)

# how to access the right picture on each trial
for triali in trials:
    
    if triali["trial_cueblock_nr"] == 0:
        if triali["cue_block_type"] == 0:
            pass #(one set of instructions: ACC versus RT)
        else:
            pass #(other set of instructions: ACC versus RT)
    
    if triali["trial_miniblock_nr"] == 0:
        print(files[int(triali["stim1"])])
        print(files[int(triali["stim2"])])
        print(files[int(triali["stim3"])])
        
        if triali["hand_block_type"] == 0:
            pass # sdf
        else:
            pass # jkl
    
    print(files[int(triali["stimulus_nr"])])
