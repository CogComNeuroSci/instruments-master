# Lesson 12, data file manipulations
# Class Exercise 12.3
import os
from psychopy import gui, data, visual, event, core

## check dir to write to
directory_to_write_to = "/Users/tom/Documents/pythonfiles/psychopy/lesson12/"
already_exists = True
myDlg = gui.Dlg(title=u"get subject info")
myDlg.addField("What is your last name? ")
myDlg.addField("What is your session number? ")
while already_exists:
    myDlg.show()
    name = myDlg.data[0]
    number = myDlg.data[1]
    if not os.path.isdir(directory_to_write_to + name):
        directory_to_write_to = directory_to_write_to + name
        os.mkdir(directory_to_write_to + name)
        filename = directory_to_write_to + "/experimental_data_session_" + number + ".csv"
    else:
        filename = directory_to_write_to + name + "/experimental_data_session_" + number + ".csv"
    if not os.path.isfile(filename):
        already_exists = False
    else:
        print("This file already exists! Choose another name.")
thisExp = data.ExperimentHandler(dataFileName=filename)

def final_words():
    end_text = visual.TextStim(win, text="That's all!\nThanks a lot for participating.")
    end_text.draw()
    win.flip()
    event.waitKeys()

## main experiment now
first_number = 1
last_number = 7
visual_targets = range(first_number,last_number+1)
correct_response = [["f","j"][x%2] for x in visual_targets]
factors = {"target": visual_targets, "color": ["red", "green"]}
targets_colors = data.createFactorialTrialList(factors)
# shakearound(targets_responses) # Here you can add code from Lesson 11 (randomization) to shake around the list according to one's experimental desires
trials = data.TrialHandler(targets_colors, nReps=2, method="random")
win = visual.Window([400,400])
experiment_timer = core.Clock()
break_timer = core.Clock()
break_text = visual.TextStim(win, text="Take a break!\nPress any key to continue")
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
    if trials.thisN == len(targets_colors)-1:
        break_timer.reset()
        break_text.draw()
        win.flip()
        event.waitKeys()
        break_time = break_timer.getTime()
        trials.addData("break time",break_time)
thisExp.saveAsWideText(filename, appendFile=False)
thisExp.abort()
final_words()
win.close()
core.quit()