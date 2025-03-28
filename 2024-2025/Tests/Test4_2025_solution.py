# A catch-the-dots task loosely inspired 
# by Baranes et al. (2014, Frontiers in Neuroscience)
# by Tom Verguts, Feb 2025

import numpy as np
import pandas as pd
from psychopy import visual, gui, event, data, core
import os, time

n_block = 1
n_trial_per_block = 6
n_trials = n_block*n_trial_per_block

# on the next two lines are the two factors of the design
speed_levels     = np.array([0, 1, 2]) # easy, medium, hard
direction_levels = np.array([0, 1])    # left-to-right, right-to-left
n_speed          = speed_levels.size # 3
n_direction      = direction_levels.size # 2
n_levels         = n_speed*n_direction # 3*2 = 6
n_rep = int(n_trial_per_block/(n_levels)) # how often the repeat all possible trials in a block
basic_trials= np.array(range(n_levels))
step_size = 2/50
max_n_step = np.floor(2/step_size)

# from abstract to concrete variables
wait_times= np.array([.2, .1, .02]) # in sec
start_pos = np.array([-1, +1])
move_step = np.array([+1, -1])

# construction of the design matrix
factor_speed     = np.floor(basic_trials/n_direction) % n_speed
factor_direction = np.floor(basic_trials/1)           % n_direction
design_matrix    = np.column_stack([factor_speed, factor_direction])
full_design_matrix = np.tile(design_matrix, (n_rep, 1))

# make full trial matrix
trial_array = np.ones((n_trials, 2))*np.nan
for block_loop in range(n_block):
    check = False  # check that the order constraints are satisfied
    while not check:
        np.random.shuffle(full_design_matrix)
        if (full_design_matrix[0, 0] == 0) and (full_design_matrix[-1, 0] == 2):
            check = True
    trial_numbers = np.array(range(n_trial_per_block)) + block_loop*n_trial_per_block
    trial_array[trial_numbers,:] = full_design_matrix

participant_info = {"name": "tom", "number": 0, "gender": ["m", "f", "other", "prefer not to say"]}
already_exists = True
while already_exists:
    gui.DlgFromDict(participant_info, title = "Catch the dots!")
    print(participant_info) 
    file_path = os.path.join(os.getcwd(), "data_subject"+str(participant_info["number"]))
    if not os.path.isdir(file_path):
        os.mkdir(file_path)
    file_name = os.path.join(file_path, "subject" + str(participant_info["number"]))
    if not os.path.isfile(file_name  + ".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
    print(file_name + ".csv")

name = participant_info["name"].capitalize()
participant_info.pop("name") # for a GDPR compatible data file

# the cross-table...
trial_pd = pd.DataFrame.from_records(trial_array)
trial_pd.columns = ["speed", "direction"]
print(pd.crosstab(trial_pd.speed, trial_pd.direction))

# and finally, the trialhandler and experimenthandler
trial_list = pd.DataFrame.to_dict(trial_pd, orient = "records")
trials = data.TrialHandler(trial_list, nReps = 1, method = "sequential", extraInfo = participant_info)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = participant_info)
thisExp.addLoop(trials)

win      = visual.Window(size = (600, 600), color = (0, 1, 0), units = "norm")
dot      = visual.Circle(win, size = 0.1, pos = (0, 0), color = (1, 0, 0)) 
left_bar = visual.Rect(win, width = 1/50, height = 15/50, pos = (-5/50, 0), fillColor = "black")
right_bar= visual.Rect(win, width = 1/50, height = 15/50, pos = (+5/50, 0), fillColor = "black")

welcome_text = ("Welcome to the experiment, " + name + "!\n"
                                            + "In this experiment, you must "
                                            + "press a key when the dot is between the bars.\n"
                                            + "Press Space to start the experiment.")
break_text = "Take a break!\n Press Space to continue."
goodbye_text  = ("Thanks for participating, " + name + "!\n"
                + "Press Space to end the experiment.")
show_text_stim = visual.TextStim(win, height = 0.1, color = "black", text = "nothing")                                             

def communication(text):
    show_text_stim.text = text
    show_text_stim.draw()
    win.flip()
    event.waitKeys(keyList = "space")

# here starts the experiment
communication(welcome_text)

for trial in trials:
    pressed     = False  # at the start of each trial, the subject has not pressed yet
    max_reached = False  # 
    dot.pos = (start_pos[int(trial["direction"])], 0)
    acc = 0
    counter = 0
    while not pressed and not max_reached:
        counter += 1
        left_bar.draw()
        right_bar.draw()
        dot.pos = (dot.pos[0] + step_size*move_step[int(trial["direction"])], 0)
        dot.draw()
        win.flip()
        k = event.waitKeys(maxWait = wait_times[int(trial["speed"])], keyList = ["space", "escape"])
        if k is not None:
            pressed = True
            if k[0] == "escape":
                break
            if abs(dot.pos[0]) < 5/50: # from -5 to +5% is ok
                acc = 1
                feedback = "Well done " + name + "!"
            else:
                acc = 0
                feedback = "Try to be more accurate, " + name + "!"
        if counter >= max_n_step: # you can also use dot.pos but I find it cleaner with a counter
            max_reached = True
    if k is not None:
        if k[0] == "escape":
            break
    if not pressed:
        acc = 0
        feedback = "Are you still awake, " + name + "?"
    trials.addData("location", start_pos[int(trial["direction"])] + counter*step_size*move_step[int(trial["direction"])])
    trials.addData("press", int(pressed)) # pressed is boolean
    trials.addData("acc", acc)
    trials.addData("block", np.floor(trials.thisTrialN/n_trial_per_block))
    communication(feedback)
    if not ((trials.thisTrialN + 1) % n_trial_per_block) and trials.thisTrialN < n_trials -1:
        communication(break_text)
    thisExp.nextEntry()

if k is not None:
    if k[0] != "escape":
        communication(goodbye_text)
win.close()