"""
parity judgement task implementation with ExperimentHandler
Esther De Loof, february 2018

"""

# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy as np
from numpy import random
import os
import platform
import pandas
import random

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
numbers     = range(1,8)
colors      = ["red","green"]
text_width  = 0.9
my_clock    = core.Clock()
info        = {"Participant number": 0, "Name": "", "Session": 0}

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Parity Judgement Task")
    directory_to_write_to = my_directory + "/" + info["Name"]
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
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# graphical elements
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the parity judgement task!\n"+
                                                "Respond to the number\n"+
                                                "and ignore its color.\n\n"+
                                                "Push the space bar to proceed.").format(info["Name"]),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (letter 'f') for even numbers or\n"+
                                                "Push right (letter 'j') for odd numbers \n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

def announce_blockstart():
    if block == 0:
        blockstart.text = ("Welcome to the practice block!\n\n"+
                           "Push the space bar to start.")
    else:
        blockstart.text = ( "Welcome to the experiment!\n\n"+
                            "Push the space bar to start.").format(block)
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
def randomize():
    
    # Within-subjects design
    Design = data.createFactorialTrialList({"Number": numbers, "Color": colors})
    
    # Add accuracy via data frame
    dataFrame = pandas.DataFrame.from_dict(Design)
    dataFrame["CorAns"] = dataFrame["Number"] % 2
    dataFrame["CorAns"].replace([0,1], ["f","j"], inplace = True)
    
    # Convert dataframe back to list of dictionaries
    trial_list = pandas.DataFrame.to_dict(dataFrame, orient = "records")
    
    # create the trials
    if block == 0:
        trial_list = [trial_list[i] for i in random.sample(numbers,4)]
        trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "random")
    else:
        trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "random")
        thisExp.addLoop(trials)
    
    return trials

def output():
    global acc
    if block > 0:
        trials.addData("response", keys[0])
        trials.addData("RT", my_clock.getTime())
        
        if keys[0] == trial["CorAns"]:
            trials.addData("ACC", 1)
        else:
            trials.addData("ACC", 0)
            
        thisExp.nextEntry()
        
    else:
        if keys[0] == trial["CorAns"]:
            acc += 1

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
block = 0
while block < 2:
    
    # announce the block start
    announce_blockstart()
    
    # randomization
    trials = randomize()
    
    # accuracy tracker
    acc = 0
    
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
        
        ## register the output
        output()
        
    # end of the trial loop
        
    # update the block number
    if (block == 0 and acc == 4) or block > 0:
        block += 1
# end of the block loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")