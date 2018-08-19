# basic file writing using psychopy
# parity judgement task (even vs odd number discrimination)
# using both ExperimentHandler and TrialHandler
# attempts to write anyway in case of crash
# written by Tom Verguts, Feb 2018
# compact version
from psychopy import data, visual, event, core
import random
visual_targets = range(1,8)
targets_responses = []
data_file="experimental_data.csv"
thisExp = data.ExperimentHandler(dataFileName=data_file)
correct = [["f", "j"][loop%2] for loop in range(1,8)] # even numbers, press f
for loop in visual_targets: # visual_targets = 1, ..., 7
    targets_responses.append({'target':loop, 'correct_response':correct[loop-1]})
random.shuffle(targets_responses)
trials = data.TrialHandler(targets_responses, nReps=1, method='random')
win = visual.Window([400,400])
experiment_timer = core.Clock()
thisExp.addLoop(trials)
for trial in trials: # a TrialHandler object is iterable
    experiment_timer.reset()
    the_text = visual.TextStim(win, text=trial['target'], color='white')
    the_text.draw()
    win.flip()
    response = event.waitKeys()
    rt = experiment_timer.getTime()
    accuracy = [response[0]==trial['correct_response']]
    trials.addData('response', response[0])
    trials.addData('accuracy', accuracy)
    trials.addData('RT',rt)
    thisExp.nextEntry()
thisExp.saveAsWideText(data_file, appendFile=False)
thisExp.abort()
win.close()
core.quit()