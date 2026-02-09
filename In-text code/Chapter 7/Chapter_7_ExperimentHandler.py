# basic file writing using psychopy
# parity judgement task (even vs odd number discrimination)
# using both ExperimentHandler and TrialHandler
# written by Tom Verguts, Feb 2018

from psychopy import data, visual, event, core
import os

data_file = os.path.join(os.getcwd(), 'data', 'experimental_data') # no need to add an extension; experimenthandler will do that
thisExp = data.ExperimentHandler(dataFileName=data_file)

visual_targets = [digit for digit in range(1,8)]
targets_responses = []
for loop in visual_targets:
    if loop%2 == 0:
        correct_response = 'f' # even numbers, press f
    else:
        correct_response = 'j' # odd numbers, press j
    targets_responses.append({'target':loop, 'correct_response':correct_response})
trials = data.TrialHandler(targets_responses, nReps=1, method='random')
thisExp.addLoop(trials)

win = visual.Window([400,400])
experiment_timer = core.Clock()

for trial in trials: # a TrialHandler object is iterable
    the_text = visual.TextStim(win, text=trial['target'], color='white')
    the_text.draw()
    win.flip()
    experiment_timer.reset()
    response = event.waitKeys()
    rt = experiment_timer.getTime()
    trials.addData('response', response[0])
    trials.addData('RT',rt)
    thisExp.nextEntry()

win.close()
core.quit()