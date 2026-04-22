# RSVP project

# modules

from psychopy import gui, data, visual, core, event
import os, random
import numpy as np
import pandas as pd

# Set up working directory
# Including: 
# Set up folder to save data

wk_dir = os.getcwd()
results_folder = 'RSVP_results'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)


# Get partiicpant information

info = {"Participant number": 0, "Age": 0, "Gender" : ""}

ppt_number_taken = True
while ppt_number_taken:
    infoDlg = gui.DlgFromDict(dictionary = info, title = 'Participant information')
    ppt_number = str(info['Participant number'])
    behavioural_file = results_folder + '/' + ppt_number + '.csv'
    if not os.path.isfile(behavioural_file):
        ppt_number_taken = False
    else:
        dlg2 = gui.Dlg(title = 'Error') 
        dlg2.addText('Please try a different participant number.')
        dlg2.show()

# Set up window and text stimulus

win = visual.Window(fullscr= True, units = 'norm')
stim = visual.TextStim(win, text = '')
mouse = event.Mouse(visible = False, newPos = (0,0)) # hide the mouse

# Experiment Handler

ThisExp = data.ExperimentHandler(dataFileName = behavioural_file, extraInfo = info)

# Design
# Idea: Scaling eg., changing number of blocks or number of trials etc

nr_blocks = 2
nr_trials = 6 # total 4*101 = 404
nr_totaltrials = nr_blocks * nr_trials
nr_practice = 2

# From the description of the task
# Color of the cross: red, yellow, green, black
# Target letter: K, L, D, S
# Distractors: digits from 1 to 9

fixcross_colours = np.array(['red', 'yellow', 'green', 'black'])
targets = ['K', 'L', 'D', 'S']

# Create array for colour of the fixation cross across the full experiment

exp_fixcross = np.tile(np.vstack(np.arange(len(fixcross_colours))), (int((nr_totaltrials/len(fixcross_colours))),1))

# Create array for saving up experiment information i.e., rows = number of trials, columns = each elements shown in RSVP + fixation cross

exp_trialinfo = np.ones((nr_totaltrials,15)) # array with ones

# Create trials

# Fixation cross

exp_trialinfo[np.arange(nr_totaltrials), 0:1] = exp_fixcross # we already know the colours of the fixation cross

# Elements shown

for row in np.arange(len(exp_trialinfo)):
    for column in range(1, exp_trialinfo.shape[1]):
        while True:
            exp_trialinfo[row, column] = random.randint(1,9)
            if not exp_trialinfo[row, column] == exp_trialinfo[row,(column-1)]: #Ask for a new random integer as long as this does not differ from the preceding one
                break

# However, right now we are only showing digits
# In 95% of the trials, we are showing one target instead of one digit
# Targets can only be shown in the 1, 3 or 6 position of the sequence (NB: not starting from 0 because the first column in our DF is the color of the fixation cross)
# Therefore, we need to select 95% of the rows of our dataframe, and change the values of columns 1, 3, 6 to something different that later in our trials will become the target

nrtrials_withtarget = int(.95*nr_totaltrials)
trials_withtarget = random.sample(range(nr_totaltrials), nrtrials_withtarget)

for i in trials_withtarget:
    exp_trialinfo[i, random.choice([1,3,6])] = random.choice([10,11,12,13]) # the last digit is the index for targets, in the case of indexing K, we need it to be 0 i.e., we need numbers that end with 0,1,2,3
    
# Make it a pd object

exp_trialinfo_df = pd.DataFrame.from_records(exp_trialinfo)

# Name columns

exp_trialinfo_df.columns = ['fixcross_color', 'element1', 'element2', 'element3', 'element4', 'element5', 'element6',
'element7', 'element8', 'element9', 'element10', 'element11', 'element12', 'element13', 'element14']

print(exp_trialinfo_df)

# Create the practice trials
# Just select a random subset of rows from the dataframe we have
# NB it could be the case that there are no target trials

practice_trialinfo_df = exp_trialinfo_df.sample(nr_practice)

# Add a column stating the trial type (practice/experimental)

exp_trialinfo_df['trialtype'] = 'experiment'
practice_trialinfo_df['trialtype'] = 'practice'

# Convert the df to dictionaries to use them to present stimuli

practice_triallist =  pd.DataFrame.to_dict(practice_trialinfo_df, orient = 'records')
experiment_triallist = pd.DataFrame.to_dict(exp_trialinfo_df, orient = 'records')

# Create rating scales for post-experimental questionnaire

scale_yesno = visual.RatingScale(win, low = 0, high = 1, marker = 'slider', textSize = 1,
    tickMarks = [0, 1], stretch = 1.5, showValue = False,
    labels = ['Yes', 'No'])
    
scale_colours = visual.RatingScale(win, low = 0, high = 3, marker = 'slider',  textSize = 1,
    tickMarks = [0, 1, 2, 3], stretch = 1.5, showValue = False,
    labels = ['Yellow', 'Green', 'Black', 'Red'])

# Experiment sequence
# Introduction
# Instructions
# Practice trials
# Experiment in blocks (with a pause screen, progress experiment with spacebar)
# Post-experimental questionnaire (mouse click response): 1- Performance (if no = exp ends, if yes = 2 follow up questions)


# Trial sequence
# Fixation cross for 90 ms
# One element of a 14-length list every 90 ms
# 10 ms blank screen between presentations
# After sequence: Keyboard response for what letter they have seen
# After response: Feedback (correct/error) + letter for 500 ms/if not response (spacebar) NONE for 1000 ms
# ITI: 1500 ms of a blank screen

RTclock = core.Clock()

def run_trial(trial, trials):
    
    # Fixation cross
    
    stim.text = '+'
    stim.color = fixcross_colours[int(trial['fixcross_color'])]
    stim.draw()
    win.flip()
    
    core.wait(2) 
    
    # Sequence
    
    sequence = []
    corans = ''
    accuracy = ''
    for i in range(14):
        stim.color = 'white'
        stim.text = int([trial['element1'], trial['element2'], trial['element3'], trial['element4'], trial['element5'], trial['element6'],
            trial['element7'], trial['element8'], trial['element9'], trial['element10'], trial['element11'], trial['element12'], trial['element13'], trial['element14']][i])
        if int(stim.text) >= 10:
            print(stim.text)
            print(targets[(int(stim.text[1]))])
            stim.text = targets[(int(stim.text[1]))]
            corans = stim.text.lower()
        if corans == '':
            conans = 'space' 
        stim.draw()
        win.flip()
        core.wait(.9)
        win.flip()
        core.wait(.1)
        sequence.append(stim.text)
    
    stim.text = 'What letter did you see?'
    stim.draw()
    win.flip()
    
    RTclock.reset()
    keys = event.waitKeys(keyList = ['k', 'l', 'd', 's', 'space', 'esc'])
    RT = round(RTclock.getTime() * 1000)
    
    corans = 'space' if corans == '' else corans
    
    if keys[0] == 'escape':
        print('Experiment escaped')
        win.close()
    elif keys[0].upper() in targets:
        stim.text = keys[0].upper()
        stim.draw()
        win.flip()
        core.wait(0.5)
        if keys[0] == corans:
            stim.text = 'Correct'
            accuracy = 'correct'
        else:
            stim.text = 'Error'
            accuracy = 'incorrect'
        stim.draw()
        win.flip()
        core.wait(0.5)
    elif keys[0] == 'space': # In this code, we also 
        stim.text = 'NONE'
        accuracy = 'space'
        stim.draw()
        win.flip()
        core.wait(1)
    
    win.flip()
    core.wait(1.5) # ITI
    
    # Store data
    
    trials.addData('fixcross_color', fixcross_colours[int(trial['fixcross_color'])])
    trials.addData('sequence', sequence)
    trials.addData('key_pressed', keys[0])
    trials.addData('correct_response', corans)
    trials.addData('accuracy', accuracy)
    trials.addData('RT', RT)
    
    
    
# Experiment sequence

# Introduction

stim.text= 'Introduction'
stim.draw()
win.flip()
event.waitKeys(keyList = ['space'])

# Instructions

stim.text='Instructions'
stim.draw()
win.flip()
event.waitKeys(keyList = ['space'])

# Practice trials

p_trials = data.TrialHandler(practice_triallist, nReps = 1, method = 'random')
ThisExp.addLoop(p_trials)

for trial in p_trials:
    
    run_trial(trial, p_trials)
    ThisExp.nextEntry()

stim.text='End practice'
stim.draw()
win.flip()
event.waitKeys(keyList = ['space'])

# Experimental trials

e_trials = data.TrialHandler(experiment_triallist, nReps = 1, method = 'random')
ThisExp.addLoop(e_trials)

e_counter = 0
e_break = (nr_totaltrials/nr_blocks) + 1

for trial in e_trials:
    e_counter += 1
    if e_counter == e_break:
        e_counter = 0
        stim.text='Break'
        stim.draw()
        win.flip()
        event.waitKeys(keyList = ['space'])
        run_trial(trial, e_trials)
    else:
        run_trial(trial, e_trials)
    ThisExp.nextEntry()
# Post-experimental questionnaire

stim.text= 'End of experiment. Start of ratings.'
stim.draw()
win.flip()
event.waitKeys(keyList = ['space'])

scale_yesno.reset()
while scale_yesno.noResponse:
    stim.text = 'Did you feel or think during the experiment that you performed better or worse after different colors?'
    stim.draw()
    scale_yesno.draw()
    win.flip()
e_trials.addData('Rating_BetterPerformanceAfterParticularColor?', ['Yes','No'][int(scale_yesno.getRating())])

if scale_yesno.getRating() == 0:
    scale_colours.reset()
    while scale_colours.noResponse:
        stim.text = 'After which color(s) did you feel/think you performed better?'
        stim.draw()
        scale_colours.draw()
        win.flip()
    e_trials.addData('Rating_FeelBetterAfterParticularColor?', ['Yellow', 'Green', 'Black', 'Red'][int(scale_colours.getRating())])

    scale_colours.reset()
    while scale_colours.noResponse:
        stim.text = 'After which color(s) did you feel/think you performed worse?'
        stim.draw()
        scale_colours.draw()
        win.flip()
    e_trials.addData('Rating_WorsePerformanceAfterParticularColor?', ['Yellow', 'Green', 'Black', 'Red'][int(scale_colours.getRating())])
        
stim.text= 'End of experiment.'
stim.draw()
win.flip()
event.waitKeys(keyList = ['space'])

win.close()

    
