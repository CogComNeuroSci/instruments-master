# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 09:29:00 2019

@author: esther
"""

# Test 4, a solution

# import modules
from psychopy import core, gui, data
import os, numpy


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
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"]) + "_Export2" + ".csv"
    
    ## check whether the name of the data file has already been used
    if not os.path.isfile(file_name):
        
        ## if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        ## if the data file name has already been used, ask the participant to inser a different participant number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

## declare all levels of the factors
ArrowOptions    = ["<",">"]
PositionOptions = [-0.5,0.5,0]
RespOptions     = ["left","right","down"]

## determine the number of levels for the factors
Narrows         = len(ArrowOptions)
Npositions      = len(PositionOptions)

## determine the number of unique trials
Nunique         = Narrows * Npositions
UniqueTrials    = numpy.array(range(Nunique)) 

## make the 2-by-3 factorial design
Arrow           = numpy.floor(UniqueTrials / Npositions)
Position        = numpy.floor(UniqueTrials / 1) %  Npositions

## make the block structure
############################

# make an empty array for the RTs
RT              = numpy.ones((Nunique,1)) * numpy.nan

## combine arrays in trial matrix
trials          = numpy.column_stack([Arrow, Position, UniqueTrials, RT])

## initialize clock
my_clock        = core.Clock()

## trial loop
trialcounter = 0
while trialcounter < trials.shape[0]:
    
    # wait a bit
    core.wait(0.1)
    
    ## store the response information
    trials[trialcounter,3] = my_clock.getTime()
        
    trialcounter = trialcounter + 1

# Export as a comma separated file
numpy.savetxt(file_name, trials, delimiter = ',') 
