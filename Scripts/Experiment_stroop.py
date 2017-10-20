###############
## Importing ##
###############

from psychopy import microphone, sound, core, visual, event
import random
import pandas

import os
import platform 
import time

#########################
## Identification data ##
#########################

subject_id = 1

################
## Set folder ##
################

output_folder = r'\Users\Pieter\Documents\Vakantiejob code\scripts lessen\Stroop data files'
if (platform.system() == 'Windows'): 
    output_folder = 'C:' + output_folder

os.chdir(output_folder) 

##############################
## Configuration parameters ##
##############################

my_window = visual.Window(size=(1000,800), units = 'pix', color = "white")

WORDS = ["P U R P L E", "B R O W N" ,"R E D","B L U E","G R E E N"]
COLORS =["purple", "brown","red","blue","green"]

part_1_text = "Say the WORD that is presented on the screen"
instructions1 = visual.TextStim(my_window, text=part_1_text,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)

part_2_text = "Say the COLOR of the text presented on the screen"
instructions2 = visual.TextStim(my_window, text=part_2_text,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)

time1 = '1'
time2 = '2'
time3 = '3'

timing1 = visual.TextStim(my_window, text=time1,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)
timing2 = visual.TextStim(my_window, text=time2,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)
timing3 = visual.TextStim(my_window, text=time3,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)

######################################
## Generate experimental conditions ##
######################################

trial_parameters = []

for i in range(len(WORDS)):
    for j in range(len(COLORS)):
        if i != j:
            trial_parameters.append( (i,j) )

trial_order = range(len(trial_parameters))
random.shuffle(trial_order)

############################################################
## Generate PsychoPy components                           ##
## To do: find out how to interface with the microphone   ##
##  Ideally we should detect the onset of speech and take ##
##  that as a reaction time. The offset of speech could   ##
##  be used as a trigger to initiate the next word pair   ##
############################################################

word_stim = visual.TextStim(my_window,"", height = 30)

instructions = visual.TextStim(my_window,"")

#########################################################
## Here comes the code that runs the actual experiment ##
## and makes use of the components defined previously  ##
#########################################################

experiment_data = []

############################################################
## Part one, say the word that is presented on the screen ##
############################################################

instructions1.draw()
my_window.flip()
event.waitKeys()

################
## Count down ##
################

while True:
    timing3.draw()
    my_window.flip()
    time.sleep(1)

    timing2.draw()
    my_window.flip()
    time.sleep(1)

    timing1.draw()
    my_window.flip()
    time.sleep(1)

    break

for trial_index in trial_order:
    
    word_index  = trial_parameters[trial_index][0]
    color_index = trial_parameters[trial_index][1]

    word_stim.color = COLORS[color_index]
    word_stim.text = WORDS[word_index]

    word_stim.draw()
    my_window.flip()

    answer = event.waitKeys()

    if answer[0] in ['Escape','escape', 'esc']:
        break

    experiment_data.append( (1, trial_index, word_index, color_index, answer))

##########################################################################
## Part two : say the color of the word that is presented on the screen ##
##########################################################################

instructions2.draw()
my_window.flip()
event.waitKeys()

################
## Count down ##
################

while True:
    timing3.draw()
    my_window.flip()
    time.sleep(1)

    timing2.draw()
    my_window.flip()
    time.sleep(1)

    timing1.draw()
    my_window.flip()
    time.sleep(1)

    break

for trial_index in trial_order:
    word_index  = trial_parameters[trial_index][0]
    color_index = trial_parameters[trial_index][1]

    word_stim.color = COLORS[color_index]
    word_stim.text = WORDS[word_index]

    word_stim.draw()
    my_window.flip()

    answer = event.waitKeys()

    if answer[0] in ['Escape','escape', 'esc']:
        break

    experiment_data.append( (2, trial_index, word_index, color_index,answer))

my_window.close()

#################
## Export data ##
#################

my_df = pandas.DataFrame(experiment_data, columns = ["phase", "trial_index","word_index","color_index","Answer"])

my_df.to_csv(output_folder + "\\" + "StroopExp_Subject_%02d.txt" %subject_id, sep = '\t')

#########
## END ##
#########
