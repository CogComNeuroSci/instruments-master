# A task similar to the BART (balloon analog risk task)
# by Tom Verguts, Feb 2024

import numpy as np
import pandas as pd
from psychopy import visual, gui, event, data
import os, time

n_block = 1
n_trial_per_block = 16
n_trials = n_block*n_trial_per_block
initial_size = 2/50
size_levels    = np.array([1/50, 5/50]) # from % to norm system
explode_levels = np.array([1, 2, 3, 4])
n_size_levels = size_levels.size
n_explode     = explode_levels.size
n_levels      = n_size_levels*n_explode
n_rep = int(n_trial_per_block/(n_levels))
basic_trials= np.array(range(n_levels))
start_time, wait_time = 0.5, 1
escape = False
 
factor_size   = np.floor(basic_trials/n_explode) % n_size_levels
factor_explode= np.floor(basic_trials/1) % n_explode
design_matrix = np.column_stack([factor_size, factor_explode])
full_design_matrix = np.tile(design_matrix, (n_rep, 1))

# make full trial matrix
trial_array = np.ones((n_trials, 2))*np.nan
for block_loop in range(n_block):
    check = False
    while not check:
        np.random.shuffle(full_design_matrix)
        comparison = np.diff(full_design_matrix[:,1])
        if sum(comparison == 0) == 0:
            check = True
    trial_numbers = np.array(range(n_trial_per_block)) + block_loop*n_trial_per_block
    trial_array[trial_numbers,:] = full_design_matrix

participant_info = {"name": "tom", "gender": ["m", "f", "other"], "number": 0}
already_exists = True 
while already_exists:
    gui.DlgFromDict(participant_info, title = "BART experiment", order = ["name", "gender", "number"])
    file_name = os.path.join(os.getcwd(), "subject" + str(participant_info["number"]) + ".csv")
    if not os.path.isfile(file_name):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

name = participant_info["name"].capitalize()
participant_info.pop("name")


trial_pd = pd.DataFrame.from_records(trial_array)
trial_pd.columns = ["balloon_size", "explosion"]
print(pd.crosstab(trial_pd.balloon_size, trial_pd.explosion))

trial_list = pd.DataFrame.to_dict(trial_pd, orient = "records")
trials = data.TrialHandler(trial_list, nReps = 1, method = "sequential", extraInfo = participant_info)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = participant_info)
thisExp.addLoop(trials)

win = visual.Window(size = (600, 400), color = (1, 0, 0))
balloon = visual.Circle(win, size = 0, color = (0, 1, 0))
show_text = visual.TextStim(win, height = 0.05, text = " ")

welcome_text = ("Welcome to the experiment, " + name + "!\n"
                                            + "In this experiment, you must "
                                            + "press a key before the balloon explodes.\n"
                                            + "Press Space to start the experiment.")
break_text = "Take a break!\n Press Space to continue."
goodbye_text  = ("Thanks for participating, " + name + "!\n"
                + "Press Space to end the experiment.")

show_text_stim = visual.TextStim(win, height = 0.05, text = "nothing")                                             

def communication(text):
    show_text_stim.text = text
    show_text_stim.draw()
    win.flip()
    event.waitKeys(keyList = "space")

# here starts the experiment
communication(welcome_text)

for trial in trials:
    pressed = False
    exploded = False
    balloon.size = initial_size
    counter = 0
    event.clearEvents()
    while not pressed and not exploded:
        balloon.draw()
        win.flip()
        k = event.waitKeys(maxWait = wait_time)
        if k:
            pressed = True
            if k[0] == "escape":
                escape = True
                break
        if counter == explode_levels[int(trial["explosion"])] and not pressed:
            exploded = True
        counter += 1
        balloon.size = balloon.size + size_levels[int(trial["balloon_size"])]

    if k: # to escape from the experiment
        if escape:
            break
    trials.addData("press", int(pressed))
    trials.addData("score", (1-exploded)*explode_levels[int(trial["explosion"])])
    trials.addData("block", np.floor(trials.thisTrialN/n_trial_per_block))
    if exploded:
        feedback_text = "KABOOM!\n Press Space for the next trial."
    else:
        feedback_text = "well done!\n Press Space for the next trial."
    communication(feedback_text)
    if not ((trials.thisTrialN + 1) % n_trial_per_block) and trials.thisTrialN < n_trials -1:
        communication(break_text)
    thisExp.nextEntry()
    
if not escape:
    communication(goodbye_text)

win.close()