# basic file writing using psychopy
# parity judgement task (even vs odd number discrimination)
# using both ExperimentHandler and TrialHandler
# attempts to write anyway in case of crash
# written by Tom Verguts, Feb 2018
from psychopy import data, visual, event, core, gui, os
visual_targets = range(1,8)
targets_responses = []
data_file="experimental_data.csv"
directory_to_write_to = "/Users/tom/Documents/pythonfiles/psychopy/lesson12/"
already_exists = True
myDlg = gui.Dlg(title=u"get subject info")
myDlg.addField("number? ")
while already_exists:
    myDlg.show()
    number = myDlg.data[0]
    filename = directory_to_write_to + "experimental_data_" + number + ".csv"
    if not os.path.isfile(filename):
        already_exists = False

thisExp = data.ExperimentHandler(dataFileName=data_file)
for loop in visual_targets:
    if loop%2 == 0:
        correct_response = 'f' # even numbers, press f
    else:
        correct_response = 'j' # odd numbers, press j
    targets_responses.append({'target':loop, 'correct_response':correct_response})
# shakearound(targets_responses) # Here you can add code from Lesson 11 (randomization) to shake around the list according to one's experimental desires
trials = data.TrialHandler(targets_responses, nReps=1, method='random')
win = visual.Window([400,400])
experiment_timer = core.Clock()
thisExp.addLoop(trials)
for trial in trials: # a TrialHandler object is iterable
    experiment_timer.reset()
    the_text = visual.TextStim(win, text=trial['target'], color='white')
    the_text.draw()
    win.flip()
    trial_continue = True
    while trial_continue:
        response=event.getKeys()
        if response:
            trial_continue = False
    rt = experiment_timer.getTime()
    accuracy = 0
    if response[0]==trial['correct_response']:
        accuracy = 1
    trials.addData('response', response[0])
    trials.addData('accuracy', accuracy)
    trials.addData('RT',rt)
    thisExp.nextEntry()
thisExp.saveAsWideText(data_file, appendFile=False)
thisExp.abort()
win.close()
core.quit()