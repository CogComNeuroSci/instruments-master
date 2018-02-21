"""
Simon task implementation with ExperimentHandler
Esther De Loof, february 2018

"""

# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy as np
from numpy import random
import os
import platform

# set the directory
my_directory = "/Users/esther/Documents/Research/IEP"
if platform.system() == "Windows":
    my_directory = "C:" + my_directory
os.chdir(my_directory) 

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing
n_blocks    = 2
n_trials    = 4
stim_size   = 0.2
position    = [-0.8,0.8]
letters     = ["f","j"]
fix_time    = 0.5
deadline    = 1.5
FB_time     = 1
text_width  = 0.9
my_clock    = core.Clock()
FB_options  = ["Wrong!","Correct!","Too slow!"]
info        = {"Participant number": 0, "Name": "", "Session": 0}

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Simon task")
    file_name = my_directory + "/Simon_experiment_subject_" + str(info["Participant number"]) + "_data"
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, let's get started!")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# Within-subjects design
Design = data.createFactorialTrialList({"Letter": [0,1], "Position": [0,1]})

# graphical elements
stimulus        = visual.TextStim(win,text="")
fixation        = visual.TextStim(win,text="+")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the Simon task!\n"+
                                                "Respond to the letter\n"+
                                                "and ignore its location.\n\n"+
                                                "Push the space bar to proceed.").format(info["Name"]),
                                   wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (letter 'f') when the letter 'f' appears\n"+
                                                "Push right (letter 'j') when the letter 'j' appears\n\n"+
                                                "Push the space bar to start the experiment."),
                                   wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                   wrapWidth = win_width*text_width)
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
feedbackTrial   = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
feedbackBlock   = visual.TextStim(win,text="",wrapWidth = win_width*text_width)

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
for block in range(n_blocks):
    
    blockstart.text = ( "Welcome to part {} of 2!\n\n"+
                        "Push the space bar to start.").format(block+1)
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    experiment = data.TrialHandler(trialList = Design, nReps = n_trials/4, name = "Exp", method = "random")  # this will set the global seed - for the whole exp
    thisExp.addLoop(experiment)
    
    # start of the trial loop
    for trial in experiment:
        
        ## determine the color of the left and right square
        trial_let = trial['Letter']
        trial_pos = trial['Position']
        
        ## display the fixation cross on the screen
        fixation.draw()
        win.flip()
        core.wait(fix_time)
        
        ## display the square on the screen
        stimulus.pos = [position[trial_pos],0]
        stimulus.text = letters[trial_let]
        stimulus.draw()
        fixation.draw()
        win.flip()
        
        ## wait for the response or response deadline
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        while my_clock.getTime() < deadline:
            keys = event.getKeys(keyList = ["f","j"])
            if len(keys) != 0:
                break
        
        ## determine the RT, ACC and the congruence of the current trial
        if len(keys) != 0:
            experiment.addData("RT", my_clock.getTime())
            experiment.addData("CONG", int(trial_let == trial_pos))
            if keys[0] == "f" and trial_let == 0:
                experiment.addData("ACC", 1)
                feedbackTrial.text = FB_options[1]
            elif keys[0] == "j" and trial_let == 1:
                experiment.addData("ACC", 1)
                feedbackTrial.text = FB_options[1]
            else:
                experiment.addData("ACC", 0)
                feedbackTrial.text = FB_options[0]
        else:
            experiment.addData("ACC", 0)
            feedbackTrial.text = FB_options[2]
        
        ## display the feedback text
        feedbackTrial.draw()
        win.flip()
        core.wait(FB_time)
        
        thisExp.nextEntry()
        
        # end of the trial loop

    # end of the block loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()