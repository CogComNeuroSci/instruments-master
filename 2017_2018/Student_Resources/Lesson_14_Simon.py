############
## Import ##
############

from psychopy import core, visual, event
import random
import csv

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

output_folder = r'\Users\Pieter\Documents\Vakantiejob code\scripts lessen'
if (platform.system() == 'Windows'): 
    output_folder = 'C:' + output_folder

os.chdir(output_folder) 

##############################
## Configuration parameters ##
##############################

## Below, we have a code for a Simon task
## Because the Simon task is probably (hopefully) well known, we will not elaborate on the set-up of this task
## If you are thinking right now 'Huh? What's a Simon task?'
    # Google is your friend!
    # Keep in mind that Google is also your friend if you do know the Simon task...

my_window = visual.Window(fullscr = True, units = 'height', color = "white")

COLORS =["red","green"]

POS_CONGR = ["right","left"]
POS_INCONGR = ["left","right"]

fixation_cross = "+"
fixation = visual.TextStim(my_window, text=fixation_cross,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)

part_1_text = "Press the RIGHT arrow when the circle is colored RED"
instructions1 = visual.TextStim(my_window, text=part_1_text,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)

part_2_text = "Press the LEFT arrow when the circle is colored GREEN"
instructions2 = visual.TextStim(my_window, text=part_2_text,units='norm',height=0.07, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)

## Below, we define the time parameters
    ## We just define three numbers to simulate a countdown later on in the experiment
        ## This may not be the most elegant way, but there is only one question that really matters:
            # 'does it work?'
                ## If the answer to that question is 'yes', you are doing fine

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

## The randomisation of this experiment is pretty straightforward
    ## We make a large list that has 'COLORS' (["red","green"]) 100 times in it
    ## We make two smaller lists
        ## One that contains CONGRUENT circle positions 50 times (["right","left"])
        ## One that contains INCONGRUENT circle positions 50 times (["left","right"])
        ## We create a large list by merging (combining) these two smaller lists
            ## Thus, we have two large lists, which consists of 200 items each (100 times 2 items)
    ## When our computations on these lists are done, we have one large list with 200 items in it
        ## Each item is actually a pair of elements
            ## The left element in the pair represents the color
            ## The right element in the pair represents the position
            ## Note that Python DOES NOT says that 'trial_parameters' consists of 400 items
                ## This because the pairs are seen by Python as single elements within 'trial_parameters'
                ## This single element however is a list
                ## We can access the elements of the list (and we will do this later in the code)
                ## However, for Python, 'trial_parameters' consists of 200 items (although we know it has 400 words in it)

COLORS = COLORS*100

POS_CONGR = POS_CONGR*50
POS_INCONGR = POS_INCONGR*50
POS = POS_CONGR+POS_INCONGR

for i in range(len(COLORS)):
    needed = (COLORS[i],POS[i])
    trial_parameters.append(needed)

print type(trial_parameters), trial_parameters

## We randomize the order of the trials
## The function 'random.shuffle()' is used for this
## Note that we do not have to create a new variable: simply applying 'random.shuffle()' on trial_order should do the trick
## What these lines of codes exactly do is the following:
    ## 'range(len(trial_parameters))' is actually a list which runs from 0 to x, with x the length of 'trial_parameters' - 1
        ##  ! This because Python starts counting at 0, and not at 1 !
        ## So, we will have a list which goes from 0 to 199 (with steps of 1), yielding a list with a length of 200 (the same as 'len(trial_parameters)')
        ## We assign this list to a new variable called 'trial_order'
    ## Then, we shuffle this variable (the order becomes random)
    ## So, when the list originally was (0,1,2,...,199) is now becomes (for instance) (65,12,99,...,3)
    ## This property is used to select random items from 'trial_parameters'
        ## ' for trial_index in trial_order: '
            ## this for loop creates a variable 'trial_index' specific for this for loop, which has the same values as 'trial_order'
            ## Looking at our previous example, trial_order might be (65,12,99,...,3) after shuffling
            ## This means that in the first loop, trial_index will be 65, in the second loop it will be 12 etc.
            ## By doing so, we can randomly select items from 'trial_parameters'
            ## Why not use 'trial_order' directly?
                ## Because we want to work in a loop, so by using trial_index, we ensure that we can still work in a loop, but without missing an item in trial_parameters
                    ## This because 'trial_order' (obviously) has the same length as 'trial_parameters', so we never miss an item
## Understanding these two lines of code is imperative to understanding the randomization of the experiment
    ## Please make sure that 'trial_order' and the loop with 'trial_order' is crystal clear to you

trial_order = range(len(trial_parameters))
random.shuffle(trial_order)

##########################
## Experiment execution ##
##########################

## Below we draw the instructions on screen
## These instructions were defined earlier, so we only have to write the .draw() function
## The instructions disappear from screen as soon as a key is pressed

instructions1.draw()
my_window.flip()
event.waitKeys()

instructions2.draw()
my_window.flip()
event.waitKeys()

## The while loop below simply draws the numbers on screen, and then waits one second
## This is used to simulate a countdown
## The loop is actually an infinite loop (the condition 'While True' is always met), but when using the 'break', we can escape

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

## Here, we write the data to a file row by row
## The difference with the other way (using a variable like 'experiment_data = []') is that the data is written away each trial
## The advantage here is that when an error occurs (or the program is shut down / or the computer breaks down / or a power outage occurs...), the data is still written away
## In other words: the loop does not have to be completed before the data is stored, as it is secured after each trial 
## When we use the following approach:
    ## data = []
        ## data.append(answer)
## The data may be lost when the loop is ended in an unconventional fashion (e.g. when the computer is shut down unexpectedly

## The code for this 'trial-level' data writing approach is again pretty straightforward:
    ## First, ! before the experimental loop !, we open a file, and we define that the following 'write' action have impact on this opened file
        ## To open a file, we first define the name (probably, you are already familiar with this)
        ## Next, we define the mode argument
            ## 'w' stands for 'write', and is used to write data (synomym: add new data to a file)
            ## 'r' stands for 'read', and is mainly used when you want to open an external file in Python (e.g. for data analysis/manipulation)
            ## 'a' stands for 'append', which (similar to the function 'append()') adds new info to the end of the file
            ## 'r+' is a special one, as it is used to both read and write a file
        ## Here, we use 'w', as our main objective is writing new data to a file
        ## 'As f' means that you will refer to the file "Simon_Exp_Subject_%02d.txt" as 'f' into your code
            ## This makes your code more transparent, and is easier for others to follow
# Because this block is about writing data, we skip to the line of code stating: 'writer = csv.writer(f, delimiter='\t')'
## We define a 'writer', which contains the function 'csv.writer()'
    ## This function writes away the data to the file 'f' (remember that 'f' actually stands for the .txt file we defined earlier)
    ## The delimiter '\t' stands for the way the data is seperated:
        ## Usually, two main ways are used 'csv' and '\t'
            ## csv stands for 'comma seperated values':
                ##green,right,right
            ## '\t' stands for values seperated by tab
                ## green    right   right
            ## What you want to use is up to you, as this is a choice which has no direct impact on the data 
## The final line of the write code writes away the data as rows to your file
    ## The order in which the data is written away is arbitrary (defined by you), and how the values are seperated (tabs or commas) is also up to you

## We provide a short overview of the meaning of the rest of the code between the 'with open' and 'core.quit()'
    ## We select a random item from 'trial_parameters', based on the shuffled 'trial_order' we mentioned earlier
        ## For example, when the first element in 'trial_order' is 45, we select item 45 from 'trial_parameters'
            ## Keep in mind that this item is actually a list, which contains two variables
            ## Each item in that specific list is then used to define the properties of this specific trial 
    ## From 'trial_parameters', we create two new variables: 'color_word' and 'position_word'
        ## 'color_word' represents the color of the drawn circle, and is defined by taking the first element ([0]) of a specific item in 'trial_parameters'
        ## 'position_word' represents the position of the drawn circle, and is defined by taking the second element ([1]) of that same specific item in 'trial_parameters'
## In the following, we reorganise some variables using if-statement to write the relevant data away properly
## Also,we use if-statement to write away the position of the circle in that trial to our file, and we define the position of the circle
## We then draw the circle and wait for a response
    ## Keep in mind that the loop can be broken by pressing 'escape'
## The reactiontime is also measured and written
## We check whether the response is correct or not 
    ## Note that we set 'correct' as '-1' by default
        ## In that way we can notice when something went wrong with the data writing (as correct should be '0' or '1', if it happens to be '-1', something is off)
    ## Mind how the 'and' and 'or' statements were used in the if-statement 

with open("Simon_Exp_Subject_%02d.txt" %subject_id, 'w') as f:
    for trial_index in trial_order:

        color_word = trial_parameters[trial_index][0]
        position_word = trial_parameters[trial_index][1]

        color = []
        if color_word == "red":
            color.append("red")
        else:
            color.append("green")

        position = []
        pos_number = []
        if position_word == "right":
            position.append("right")
            pos_number.append(.5)
        else:
            position.append("left")
            pos_number.append(-.5)

        circle = visual.Circle(my_window, radius = .10, pos=(pos_number[0],0), fillColor = color_word)

        fixation.draw()
        my_window.flip()
        time.sleep(.5)

        circle.draw()
        my_window.flip()
        t1 = int(round(time.time() * 1000))

        answer = event.waitKeys()
        t2 = int(round(time.time() * 1000))

        reactiontime= int(t2 - t1)

        if answer[0] in ['Escape','escape', 'esc']:
            break

        correct = -1

        if (color_word == 'red' and answer[0] == 'right') or (color_word == 'green' and answer[0] == 'left'):
            correct = 1
        else:
            correct = 0

        writer = csv.writer(f, delimiter='\t')
        writer.writerow([trial_index, color[0], position[0], answer, reactiontime, correct])
        
        my_window.flip(clearBuffer = True)
        time.sleep(.5)

my_window.close()
core.quit()

#########
## END ##
#########
