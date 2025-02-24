"""
parity judgement task implementation with ExperimentHandler
and a practice block; CE 7.5
Esther De Loof & Tom Verguts, february 2019

"""

# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy as np
from numpy import random
import os
import platform

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height], units = "norm")

# initializing
colors      = ["red","green"]
text_width  = 0.9
my_clock    = core.Clock()
info        = {"Participant number": str(0), "Name": "", "Session": 0}

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Parity Judgement Task")
    directory_to_write_to = my_directory + "/data_ParityJudgementTask"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/ParityJudgementTask_subject_" + str(info["Participant number"]) + "_Session_" + str(info["Session"]) + "_data"
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, let's get started!")
subject_name = info["Name"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# Within-subjects design
Design = [{"Number": 1, "Color": "red"}, {"Number": 2, "Color": "red"}, {"Number": 3, "Color": "red"}, {"Number": 4, "Color": "red"},\
          {"Number": 1, "Color": "green"}, {"Number": 2, "Color": "green"}, {"Number": 3, "Color": "green"}, {"Number": 4, "Color": "green"} ]

correct = [["f", "j"][loop%2] for loop in range(1,5)] # even numbers, press f

# graphical elements
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    f"Hi {subject_name},\n"+
                                                "Welcome to the parity judgement task!\n"+
                                                "Respond to the number\n"+
                                                "and ignore its color.\n\n"+
                                                "Push the space bar to proceed."),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (letter 'f') or\n"+
                                                "Push right (letter 'j') \n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

def announce_blockstart(blocknr):
    if blocknr == 0:
        blockstart.text = ("Let's do the practice block!\n\n"+
                           "Push the space bar to start.")
    else:
        blockstart.text = ( "Let's start the main part of the experiment!\n\n"+
                            "Push the space bar to start.")
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")

def choose_trials(bloknr):
    # create the trials
    if bloknr == 0:
        Design_block = Design[3:7] # four randomly chosen items; a random mechanism could be included here
    else:
        Design_block = Design
    trials = data.TrialHandler(trialList = Design_block, nReps = 1, method = "random")  
    thisExp.addLoop(trials)
    return trials

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

block = 0
while block < 2:
    announce_blockstart(block)
    
    trials = choose_trials(block)
    acc_block = 0
    # start of the trial loop
    for trial in trials:

        ## display the number on the screen
        stimulus.color = trial["Color"]
        stimulus.text = trial["Number"]
        stimulus.draw()
        win.flip()
    
        ## wait for the response
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["f","j", "esc"], maxWait = 2)
        if keys == None: # in case of no response
            keys = ["t"] # t for too late
        if keys[0] == "esc":
            break
        trials.addData("response", keys[0])
        accuracy = 1*(keys[0]==correct[trial["Number"]-1])
        acc_block += accuracy
        trials.addData("Acc", accuracy)
        trials.addData("RT", my_clock.getTime())
    
        thisExp.nextEntry()
        #trials.next()
    # end of the trial loop
    if (block == 1) or (acc_block == 4):
        block += 1
    
# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()