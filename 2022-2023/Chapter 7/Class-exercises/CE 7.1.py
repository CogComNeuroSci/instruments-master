"""
parity judgement task implementation with ExperimentHandler
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

# graphical elements
stimulus        = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the parity judgement task!\n"+
                                                "Respond to the number\n"+
                                                "and ignore its color.\n\n"+
                                                "Push the space bar to proceed.").format(subject_name),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (letter 'f') or\n"+
                                                "Push right (letter 'j') \n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# create the trials
trials = data.TrialHandler(trialList = Design, nReps = 1, name = "Exp", method = "random")  # this will set the global seed - for the whole exp
thisExp.addLoop(trials)

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
    keys = event.waitKeys(keyList = ["f","j"])
    
    trials.addData("response", keys[0])
    trials.addData("RT", my_clock.getTime())
    
    thisExp.nextEntry()
# end of the trial loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()