"""
CE 9.6: a Stroop task implementation
Esther De Loof and Tom Verguts, december 2017

"""

# import modules
from psychopy import visual, event, core, gui
import numpy as np
from numpy import random

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing
n_blocks    = 2
n_prac      = 4
n_trials    = 16
text_width  = 0.9
text_size   = 0.075
fix_time    = 0.5
deadline    = 1
FB_time     = 1
colWords    = ["red","blue","green","yellow"]
respOptions = ["d","f","j","k"]
FB_options  = ["Wrong answer!","Correct","Too slow! Try to respond faster."]
my_clock    = core.Clock()

# graphical elements
fixation        = visual.TextStim(win,text="+",color="black")
stimulus        = visual.TextStim(win,text="",color="black")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the Stroop task!\n"+
                                                "Push the space bar to proceed.").format(info["Name"]),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
instruct        = visual.TextStim(win,text=(    "In this experiment you will see color words (red, blue, green and yellow)\n"+
                                                "presented in a random ink color (red, blue, green and yellow color).\n"+
                                                "You have to respond to the ink color of the stimulus\n"+
                                                "and ignore the meaning of the written word.\n"+
                                                "You can use the following four response buttons\n"+
                                                "(from left to right; use the index and middle finger of your left and right hand):\n"+
                                                "d, f, j and k.\n"+
                                                "If the ink color is red, press the leftmost button d.\n\n"+
                                                "If it's blue, press f.\n"+
                                                "If it's green, press j.\n"+
                                                "If it's yellow, press k.\n\n"+
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n"+
                                                "By all means ignore the meaning of the words,\n"+
                                                "you should only respond to the ink color.\n\n"+
                                                "Push the space bar to start the experiment."),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
start_prac      = visual.TextStim(win,text=(    "This is the start of the practice phase.\n\n"+
                                                "Push the space bar to proceed."),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
start_exp       = visual.TextStim(win,text=(    "This is the start of the experiment.\n\n"+
                                                "Push the space bar to proceed."),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width, height = text_size, color = "black")
feedbackTrial   = visual.TextStim(win,text="",wrapWidth = win_width*text_width, height = text_size, color = "black")
goodbye         = visual.TextStim(win,text=(    "The is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
for block in range(n_blocks):

    ## enable the practice phase
    if block == 0:
        start = -n_prac
    else:
        start = 0

    # start of the trial loop
    for trial in range(start,n_trials):
        
        if trial == -n_prac and block == 0:
            ## announce start of the practice phase
            start_prac.draw()
            win.flip()
            event.waitKeys(keyList = "space")
        elif trial == 0 and block == 0:
            ## announce start of the actual experiment
            start_exp.draw()
            win.flip()
            event.waitKeys(keyList = "space")
        if trial == 0:
            ## announce the number of the block
            blockstart.text = ( "Now starts part {} of {}!\n\n"+
                                "Push the space bar to start.").format(block+1, n_blocks)
            blockstart.draw()
            win.flip()
            event.waitKeys(keyList = "space")
        
        ## RT, ACC and COR for storing the trial information
        RT  = -1
        ACC = -1
        COR = -1
        
        ## determine the ink color and color word
        trial_col   = random.randint(0,len(colWords))
        trial_word  = random.randint(0,len(colWords))
        
        ## determine the correct answer
        COR = trial_col
        
        ## display the fixation cross on the screen
        fixation.draw()
        win.flip()
        core.wait(fix_time)
        
        ## display the word on the screen
        stimulus.text   = colWords[trial_word]
        stimulus.color  = colWords[trial_col]
        stimulus.draw()
        win.flip()
        
        ## wait for the response or response deadline
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        while my_clock.getTime() < deadline:
            keys = event.getKeys(keyList = respOptions)
            if len(keys) != 0:
                break
        
        ## determine the RT and ACC
        if len(keys) != 0:
            RT = my_clock.getTime()
            if COR == respOptions.index(keys[0]):
                ACC = 1
            else:
                ACC = 0
            feedbackTrial.text  = FB_options[ACC]
        else:
            feedbackTrial.text  = FB_options[2]
        
        ## feedback message
        feedbackTrial.draw()
        win.flip()
        core.wait(FB_time)

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()