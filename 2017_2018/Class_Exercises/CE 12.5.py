"""
Class Exercise 12.5
It is checked whether the directory and file already exists: the program keeps on querying
until a non-existent (directory, session) combination is provided
version with random color combination (to check out createFactorialTrialList)
The full list is presented twice, but trial-to-trial repetitions are not allowed
And incongruent trials are presented twice as often
"""
import os, random
from psychopy import gui, data, visual, event, core
import numpy as np

def shake_around():
    global targets_colors
    frequencies = [1]*len(visual_targets) + [2]*len(visual_targets) # for red and green trials
    for loop in range(len(targets_colors)): # want to loop through an integer here
        if frequencies[loop]>1:
            for freq_loop in range(frequencies[loop]-1):
                targets_colors.append(targets_colors[loop])
    check = False # to enter at least once into the while loop
    while not check:
        random.shuffle(targets_colors)
        check = True
        for loop in range(len(targets_colors)-1):
            if targets_colors[loop]==targets_colors[loop+1]:
                check = False

## check dir to write to
directory_to_write_to = "/Users/tom/Documents/pythonfiles/psychopy/lesson12/"
already_exists = True
myDlg = gui.Dlg(title=u"get subject info")
myDlg.addField("What is your last name? ")
while already_exists:
    myDlg.show()
    name = myDlg.data[0]
    if not os.path.isfile(directory_to_write_to + name):
        filename = directory_to_write_to + name + ".csv"
        already_exists = False
    else:
        print("This file already exists! Choose another name.")
thisExp = data.ExperimentHandler(dataFileName=filename)

## main experiment now
visual_targets = range(1,8)
correct_response = [["f","j"][x%2] for x in visual_targets]
factors = {"target": visual_targets, "color": ["red", "green"]}
targets_colors = data.createFactorialTrialList(factors) # targets_colors is now a list of dicts
shake_around()
trials = data.TrialHandler(targets_colors, nReps=1, method="sequential") # not to spoil result from previous line
win = visual.Window([400,400])
experiment_timer = core.Clock()
thisExp.addLoop(trials)
for trial in trials: # a TrialHandler object is iterable
    experiment_timer.reset()
    the_text = visual.TextStim(win, text=trial["target"], color=trial["color"])
    the_text.draw()
    win.flip()
    trial_continue = True
    while trial_continue:
        response=event.getKeys()
        if response:
            trial_continue = False
    rt = experiment_timer.getTime()
    accuracy = 0
    if response[0]==correct_response[trial["target"]-1]:
        accuracy = 1
    trials.addData("response", response[0])
    trials.addData("accuracy", accuracy)
    trials.addData("RT",rt)
    thisExp.nextEntry()
thisExp.saveAsWideText(filename, appendFile=False)
thisExp.abort()
win.close()
core.quit()