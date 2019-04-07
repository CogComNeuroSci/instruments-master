# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 09:29:00 2019

@author: esther
"""

# Test 4, a solution

# import modules
from psychopy import core, gui, data
import os


# file management and participant info

## set the directory
my_directory = os.getcwd()

## construct the name of the folder that will hold the data
directory_to_write_to = my_directory + "/data"
    
## if the folder doesn't exist yet, make it
if not os.path.isdir(directory_to_write_to):
    os.mkdir(directory_to_write_to)

## initialize the participant information dialog box
info = {"Participant name":"Incognito", "Participant number":0, "Age":0, "Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"]}

## make sure the data file has a novel name
already_exists = True
while already_exists:
    
    ## present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    ## construct the name of the data file
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"]) + "_Export1"
    
    ## check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        
        ## if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        ## if the data file name has already been used, ask the participant to inser a different participant number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

## extract the name of the participant from the dialog box information
subject_name = info["Participant name"]

## remove the name of the participant from the dialog box information (anonimity!)
info.pop("Participant name")

## start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name!)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

## declare all levels of the factors
ArrowOptions    = ["<",">"]
PositionOptions = [-0.5,0.5,0]
RespOptions     = ["left","right","down"]

## create the factorial trial list
trial_list = data.createFactorialTrialList({"Position": PositionOptions, "Arrow": ArrowOptions})

## create the trials for the entire experiment via the TrialHandler
trials = data.TrialHandler(trialList = trial_list, nReps = 10, method = "fullRandom")
thisExp.addLoop(trials)

## initialize clock
my_clock        = core.Clock()

## trial loop
for trial in trials:
    
    # wait a bit
    core.wait(0.1)
    
    ## store the response information in the ExperimentHandler
    trials.addData("RT", my_clock.getTime())
    
    ## let the ExperimentHandler proceed to the next trial
    thisExp.nextEntry()

## let the experimentHandler know its job is done
thisExp.close()
