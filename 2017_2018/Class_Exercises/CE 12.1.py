# some operating system (os) manipulations
# Text exercise 12.8: with actual experiment attached
# It is checked whether the directory and file already exists: the program keeps on querying
# until a non-existent directory, session combination is provided
# version with random color combination (to check out createFactorialTrialList)
# accuracy is ignored here
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

## main experiment now
visual_targets = range(1,8)
targets_responses = []
factors = {"target": visual_targets, "color": ["red", "green"]}
targets_responses = data.createFactorialTrialList(factors)
# shakearound(targets_responses) # Here you can add code from Lesson 11 (randomization) to shake around the list according to one's experimental desires
trials = data.TrialHandler(targets_responses, nReps=1, method='random')
win = visual.Window([400,400])
experiment_timer = core.Clock()
thisExp.addLoop(trials)
for trial in trials: # a TrialHandler object is iterable
    experiment_timer.reset()
    the_text = visual.TextStim(win, text=trial['target'], color=trial['color'])
    the_text.draw()
    win.flip()
    trial_continue = True
    while trial_continue:
        response=event.getKeys()
        if response:
            trial_continue = False
    rt = experiment_timer.getTime()
    trials.addData('response', response[0])
    trials.addData('RT',rt)
    thisExp.nextEntry()
thisExp.saveAsWideText(filename, appendFile=False)
thisExp.abort()
win.close()
core.quit()