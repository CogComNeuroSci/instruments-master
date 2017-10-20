from psychopy import visual, event, core
import os
import random
import pandas as pd
import numpy as np
import platform 
import time

from random import randint

################
## Set folder ##
################

mydirectory = '/Users/Pieter/Documents/Vakantiejob code/scripts lessen'
if (platform.system() == 'Windows'): 
    mydirectory = 'C:' + mydirectory

os.chdir(mydirectory) 

#########################
## Identification data ##
#########################

subject_id = 2

###############
## Constants ##
###############

PROPORTION_VALID   = 0.8
PROPORTION_INVALID = 0.1
PROPORTION_NEUTRAL = 0.1
N_TRIALS = 100

ISI_DURATION = 1
CUE_DURATION = 1
FIXATION_DURATION = 1

BOX_SIZE = 140
BOX_POSITION = 300

LEFT_CUE = 0
RIGHT_CUE = 1
NEUTRAL_CUE = 2

TARGET_LEFT = -1
TARGET_RIGHT = 1

############################################
## Generate the parameters for each trial ##
############################################

n_valid_trials = int(PROPORTION_VALID*N_TRIALS)
n_invalid_trials = int(PROPORTION_INVALID*N_TRIALS)
n_neutral_trials = int(PROPORTION_NEUTRAL*N_TRIALS)

trial_parameters = []
for i in range(n_valid_trials):
    if i%2 == 0:
        trial_parameters.append((1, LEFT_CUE,TARGET_LEFT))
    else:
        trial_parameters.append((1, RIGHT_CUE,TARGET_RIGHT))

for i in range(n_invalid_trials):
    if i%2 == 0:
        trial_parameters.append( (2, LEFT_CUE, TARGET_RIGHT))
    else:
        trial_parameters.append( (2, RIGHT_CUE, TARGET_LEFT))

for i in range(n_neutral_trials):
    if i%2 == 0:
        trial_parameters.append( (3, NEUTRAL_CUE, TARGET_LEFT))
    else:
        trial_parameters.append( (3, NEUTRAL_CUE, TARGET_RIGHT))

trial_order =  range(len(trial_parameters))
random.shuffle(trial_order)

##################################
## Generate PsychoPy components ##
##################################

my_window = visual.Window( fullscr = False, units = 'pix', color = (-1,-1,-1))

fixation_cross = visual.TextStim(my_window,"+")
left_cue = visual.TextStim(my_window,"<<<")
right_cue = visual.TextStim(my_window,">>>")
neutral_cue = visual.TextStim(my_window,"<.>")
cue_list = [left_cue, right_cue, neutral_cue]

left_box = visual.Rect(my_window, width = BOX_SIZE, height = BOX_SIZE, pos=(-BOX_POSITION,0))
right_box  = visual.Rect(my_window, width = BOX_SIZE, height = BOX_SIZE, pos=(BOX_POSITION,0))

target_stimulus = visual.Polygon(my_window, edges = 5, radius = BOX_SIZE/4, fillColor="#12A04A")


welcome = "Welcome in this Posner cueing task! \n \nFocus on the arrows in the middle. \n \nUse the left and right arrows to answer. \n \nThe first 10 trials are exercise. \n \nPress any key to exit."
Message1 = visual.TextStim(my_window, text=welcome,units='pix', height= BOX_SIZE/4, color='White',pos=[0,0], alignHoriz='center',flipHoriz=False)
Message1.draw()
my_window.flip()
event.waitKeys()

#######################
## Experimental loop ##
#######################

# Used as a check
# The number of congruent, incongruent and neutral trials should stay the same

data_val = []

for trial_index in trial_order:
    which_val = trial_parameters[trial_index][0]
    data_val.append(which_val)

data_cue = []

for trial_index in trial_order:
    which_cue = trial_parameters[trial_index][1]
    data_cue.append(which_cue)

data_target_loc = []

for trial_index in trial_order:
    target_loc = trial_parameters[trial_index][2]
    data_target_loc.append(target_loc)

data_pos = []

for trial_index in data_target_loc:
    target_stimulus.pos = (trial_index*BOX_POSITION,0)
    needed = np.array(target_stimulus.pos)
    data_pos.append(needed)

data_trial = np.column_stack((data_val, data_cue, data_target_loc))
data = data_trial.tolist()

print ('%%%')
print len(data), type(data), data
print ('%%%')

## Please note that append is a destructive command
## This means that the command .append does NOT create a new variable, it merely edits an already existing variable 
##  Therefore, the code 
    ## NewData = data.append([0,1])
    ## print NewData
##  would return 'None', as NewData actually does not exist
##  Only data exists, and this variable is modified by the append (or extend) function
##  Because of this, the code
    ## data.append([0,1])
    ## print len(data), data
##  Will return the old 'data', and [0,1] will be added at the end!

experiment_data = []
trial_index = 0

while trial_index < len(data):
    congruency = data[trial_index][0]
    which_cue = data[trial_index][1]
    target_loc = data[trial_index][2]
    if target_loc == -1:
        target_stimulus.pos = (-300*1,0)
    else:
        target_stimulus.pos = (300*1,0)

    fixation_cross.draw()
    left_box.draw()
    right_box.draw()
    my_window.flip()
    core.wait(FIXATION_DURATION)
    
    cue_list[which_cue].draw()
    left_box.draw()
    right_box.draw()
    my_window.flip()
    core.wait(CUE_DURATION)
    
    left_box.draw()
    right_box.draw()
    target_stimulus.draw()
    cue_list[which_cue].draw()
    my_window.flip()

    event.clearEvents()
    answer = event.waitKeys()

## An optional block of code
##  Think what would be the advantages/disadvantages of uncommenting this block

##    if congruency == 1:
##        congruency = 'valid'
##   if congruency == 2:
##        congruency = 'invalid'
##    if congruency == 3:
##        congruency = 'neutral'

##    if which_cue == 0:
##        which_cue = 'neutral'
##    if which_cue == 1:
##        which_cue = 'right'
##    if which_cue == 2:
##        which_cue = 'left'

    if target_loc == -1:
        target_loc = 'left'
    if target_loc == 1:
        target_loc = 'right'

    if answer[0] in ['Escape','escape', 'esc']:
        break

    accuracy = []

    if answer[0] in ['left','right']:

        if answer[0] == target_loc:
            accuracy.append(1)
            data.remove(data[trial_index])
        elif answer[0] != target_loc:
            accuracy.append(0)
            number = randint(0, len(data))
            needed = ([data[trial_index][0],data[trial_index][1]])
            data.insert(number, needed)

        experiment_data.append([congruency, which_cue, target_loc,answer[0],accuracy[0]])
    
    elif answer[0] not in ['left','right']:
        my_window.flip(clearBuffer=True)
        
        instructions = "Wrong key was pressed! \n \nOnly the left and right arrow should be used! \n \nPress any key to continue"
        warningMessage = visual.TextStim(my_window, text=instructions,units='pix', height= BOX_SIZE/4, color='White',pos=[0,0], alignHoriz='center',flipHoriz=False)
        warningMessage.draw()
        my_window.flip()

        accuracy.append('wrong key')
        
        number = randint(0, len(data))
        needed = ([data[trial_index][0],data[trial_index][1]])
        data.insert(number, needed)
        
        experiment_data.append([congruency, which_cue, target_loc,answer[0],accuracy[0]])
        event.waitKeys()
        
    trial_index += 1

#####################
## export the data ##
#####################

print (len(experiment_data)), (experiment_data)
print (len(data))

expData = pd.DataFrame(experiment_data, columns = ['Congr', 'Cue','Target','Key','Acc'])
print (expData)

expData.to_csv("PosnerExp_subject%02d.txt" %subject_id, sep = '\t')

#########
## END ##
#########
