# N-back task
# by Ricardo Alejandro, March 2024

import numpy as np
import pandas as pd
from psychopy import visual, gui, event, data, core
import os, time

n_blocks = 3                                        
n_letter_reps_block = 2                                         # number of times a letter is repeated in a block
letters = np.array(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
n_trials_per_block = n_letter_reps_block * (len(letters))       # number of trials per block
n_trials = n_blocks * n_trials_per_block                        # number of trials in total

prop_no_trials = 0.7                                                # proportion of NO n-back trials
n_no_trials = int(np.round(n_trials_per_block * prop_no_trials))    # number of NO n-back trials
n_nback_trials = n_trials_per_block - n_no_trials                   # number of n-back trials

stim_duration = 0.5
isi_duration = 2

back_levels = np.array([1, 2, 3])                               # number of "n-back" levels

## collect participant info
participant_info = {"name": "ric", "number": 0, "gender": ["m", "f", "other"]}
already_exists = True
while already_exists:
    gui.DlgFromDict(participant_info, title = "N-back Task", order = ["name", "number", "gender"])
    file_name = os.path.join(os.getcwd(), "subject" + str(participant_info["number"]))
    if not os.path.isfile(file_name  + ".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
participant_number = participant_info["number"] 
name = participant_info["name"].capitalize()        # capitalize for the greeting
participant_info.pop("name")                        # for a GDPR compatible data file

# random or latin square order of blocks:
block_order = 'random'
if (block_order == 'latin_square'):
    latin_sq = [[1, 2, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
                [1, 3, 2],
                [2, 1, 3]]
    nback_order = np.array(latin_sq[(int(participant_number) % 6) - 1])
else:
    nback_order = np.array([1, 2, 3])
    np.random.shuffle(nback_order)

## trials creation and randomization

# block id (block number per trial)
block_ids = np.repeat(np.arange(start=1, stop=n_blocks+1), n_trials_per_block)

# trial type (which n-back) per trial
nback_type = np.repeat(nback_order, n_trials_per_block)

# (n_trials x n_blocks) array with 1 (nback) or 0 (no trial)
is_nback = np.ones((n_trials_per_block, len(back_levels))) * np.nan
for index, back_level in enumerate(nback_order):
    # populate array with an "n_nback_trials" number of ones
    # making sure that the n-back trial doesn't happen at the first n positions
    # (e.g., 1st trial in 1-back, 1st or 2nd trial in 2-back)
    nback_trials_level = np.zeros(n_trials_per_block)
    nback_trials_level[back_level : back_level+n_nback_trials] = 1
    np.random.shuffle(nback_trials_level[back_level : ])
    
    is_nback[:, index] = nback_trials_level
#reshape as column array
is_nback = (is_nback.reshape(-1, 1, order='F')).astype(int)

# array for trial stimuli:
trial_stim = np.empty((n_trials_per_block, len(back_levels)), dtype=str)
for block_id in range(n_blocks):
    # populate with 'n_letter_reps_block' repetitions of each letter per block
    trial_stim[:, block_id] = np.tile(letters, n_letter_reps_block)
    # and mix them
    np.random.shuffle(trial_stim[:, block_id])
trial_stim = trial_stim.reshape(-1, 1, order='F')
#make sure that n-back is happening when it's supposed to happen:
for index, element in enumerate(trial_stim[::-1]):
    # iterate the array from end to start
    rev_index = (len(trial_stim)-1) - index
    current_nback_type = nback_type[rev_index]
    if (is_nback[rev_index] == 1):      # if this is supposed to be an n-back trial
        trial_stim[rev_index - current_nback_type] = element    # set the n-back element the same as the current one
    else:   # otherwise (if it's not supposed to be an n-back trial)
        while (trial_stim[rev_index - current_nback_type] == element):  
            # choose a random letter and assign it
            trial_stim[rev_index - current_nback_type] = np.random.choice(letters)
# collect all the trials' information in one matrix
trials_matrix = np.column_stack([block_ids, trial_stim, is_nback, nback_type])
trials_df = pd.DataFrame.from_records(trials_matrix)
trials_df.columns = ['block_ids', 'trial_stim', 'is_nback', 'nback_type']
print(trials_df)
# add trialhandler and experimenthandler
trial_list = pd.DataFrame.to_dict(trials_df, orient = "records")
trials = data.TrialHandler(trial_list, nReps = 1, method = "sequential", extraInfo = participant_info)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = participant_info)
thisExp.addLoop(trials)

#visual settings
win = visual.Window(size = (800, 600), color = (0, 0, 0))
show_stim = visual.TextStim(win, height = 0.05, text = " ")
#texts
welcome_text = ("Welcome to the N-back experiment, " + name + "!\n"
                + "In this experiment, you must "
                + "press a key if you think that the current letter is the same"
                + " as the one presented N trials ago.\n"
                + "Press Space to see the instructions for the first block.")
break_text = "Take a break!\n Press Space to continue."
goodbye_text  = ("Thanks for participating, " + name + "!\n"
                + "Press Space to end the experiment.")
show_text = visual.TextStim(win, height = 0.05, text = "nothing")                                             
## Functions
def communication(text):
    show_text.text = text
    show_text.draw()
    win.flip()
    event.waitKeys(keyList = "space")
def stim_presentation(letter):
    show_stim.text = letter
    show_stim.draw()
    win.flip()
########## Experiment
communication(welcome_text)
experiment_timer = core.Clock()
show_block_msg = True
## block trials
for trial in trials:
    # (if applicable) show instructions for this block
    if show_block_msg:
        block_text = ("Block " + str(trial["block_ids"]) + "\n\n"
                    + "Task: " + str(trial["nback_type"]) + "-back.\n\n"
                    + "Press a key if you think the letter you see is the same as the one "
                    + "presented" + str(trial["nback_type"]) + " trial(s) ago.\n\n"
                    + "Press space to start")
        communication(block_text)
        trials.addData('communication', 'welcome or block')
        show_block_msg = False
    ##present the letter
    stim_presentation(trial['trial_stim'])
    core.wait(stim_duration)
    ##present the ISI
    experiment_timer.reset()
    stim_onset = core.getTime()
    trial_acc = 0
    pressed = False
    response = "none"
    rt = 999
    while ((core.getTime() - stim_onset) < isi_duration) and (not pressed):
        stim_presentation("")
        #wait for response
        k = event.getKeys()
        if (len(k) > 0): # if there was a key press
            rt = experiment_timer.getTime()
            pressed = True
            response = k[0]
            if k[0] == "escape":
                core.quit()
            if (int(trial["is_nback"])) == 1: # key presses are only correct in N-back trials
                trial_acc = 1
        elif (not (int(trial["is_nback"]))) and (not pressed): # if there was no key press, was it a NO n-back trial?
            trial_acc = 1 # no key press, no N-back trial, then this trial was correct
        elif (not (int(trial["is_nback"]))) and (pressed):
            trial_acc = 0

    # log trial data:
    trials.addData('response', response)
    trials.addData('trial_acc', trial_acc)
    trials.addData('RT',rt)
    ## show break message after a block
    if not ((trials.thisTrialN + 1) % n_trials_per_block) and (trials.thisTrialN < n_trials -1):
        trials.addData('communication', 'break')
        communication(break_text)
        show_block_msg = True
    thisExp.nextEntry()
# goodbye message
communication(goodbye_text)
win.close()
core.quit()