# basic file writing using psychopy
# parity judgement task (even vs odd number discrimination)
# using both ExperimentHandler and TrialHandler
# attempts to write anyway in case of crash
# note: to keep subject data anonymous, the subject's name is NOT used in the file name
# only the subject's number is used
# subject's name is asked only for greeting purposes
# written by Tom Verguts, Feb 2019

from psychopy import data, visual, event, core, gui, os

info = {"Participant number": 0, "Name": "Tom", "Session": 0}

data_file = "experimental_data_"
directory_to_write_to = os.getcwd() + "/data/"

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(info, title = u"get subject info")
    number = str(info["Participant number"])
    filename = directory_to_write_to + data_file + number
    if not os.path.isfile(filename + ".csv"):
        already_exists = False

thisExp = data.ExperimentHandler(dataFileName = filename)

visual_targets = range(1,8)
targets_responses = []
for loop in visual_targets:
    if loop%2 == 0:
        correct_response = 'f' # even numbers, press f
    else:
        correct_response = 'j' # odd numbers, press j
    targets_responses.append({'target':loop, 'correct_response':correct_response})

trials = data.TrialHandler(targets_responses, nReps = 1, method = 'random')
thisExp.addLoop(trials)

win = visual.Window([400,400])
experiment_timer = core.Clock()

for trial in trials: # a TrialHandler object is iterable
    the_text = visual.TextStim(win, text = trial['target'], color = 'white')
    the_text.draw()
    win.flip()
    experiment_timer.reset()
    response = event.waitKeys()
    rt = experiment_timer.getTime()
    accuracy = 0
    if response[0] == trial['correct_response']:
        accuracy = 1
    trials.addData('response', response[0])
    trials.addData('accuracy', accuracy)
    trials.addData('RT',rt)
    thisExp.nextEntry()

win.close()
core.quit()