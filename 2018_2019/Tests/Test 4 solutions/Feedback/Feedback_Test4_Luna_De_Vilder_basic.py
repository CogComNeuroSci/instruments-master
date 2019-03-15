# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy as np
from numpy import random
import os
import platform
from psychopy import data
import pandas

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height], units = "norm")

# initializing

my_clock    = core.Clock()
info        = {"Participant number": str(0), "Name": "", "Age": "", "Gender": ["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"]}

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test4")
    
    # Esther: /data volstond hier
    
    directory_to_write_to = my_directory + "/data_Test4_"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"]) + "_data"
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

# graphical elements
stimulus          = visual.TextStim(win,text="")
Welcome           = visual.TextStim(win, text = "Welcome " + subject_name + "!\n\nPress the space bar to continue.")
Instructions      = visual.TextStim(win, text = "OK", height = 0.05)
VoorInstructies   = visual.TextStim(win, text = "Bij dit experiment zal je pijltjes zien verschijnen op het scherm. De instructies volgen straks. Let op dat je de instructies telkens goed leest aangezien deze soms veranderen doorheen het experiment. Druk op spatie om verder te gaan.", height = 0.05)
Block_start       = visual.TextStim(win, text = "OK")
Feedback          = visual.TextStim(win, text = "OK")
Goodbye           = visual.TextStim(win, text = "Goodbye!")

# welcome and instructions
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

VoorInstructies.draw()
win.flip()
event.waitKeys(keyList = "space")


# constants

## number of blocks
nBlocks = 12

## number of trials per block
nBlockTrials = 60

## number of design repetitions per block
nReps = int(nBlockTrials/(2*3))
print(nReps)

# make the design based on the core trial characteristics

## make the 2-by-3 factorial design
arrays = ["<",">"]
position_arrays = [(-0.75,0), (0,0), (0.75,0)]
Design = data.createFactorialTrialList({"Arrays": arrays, "Position": position_arrays})
print(Design)

# determine the congruency (and other derived properties)
#
## convert to a data frame to easily add dummy columns
#dataFrame = pandas.DataFrame.from_dict(Design)
#
## convert to a data frame to easily add dummy columns
#Balanced = pandas.DataFrame.from_dict(Design)
#Balanced["Congruence"] = -1
#Balanced["Balanced"] = 1
#Balanced["CorAns"] = Balanced["Arrays", "Position"]
#
## determine the correct response button
#Balanced["CorAns"].replace(["<",">"], ["(-0.75,0)", ""(0,0), "(0.75,0)"]["left","right","down"]) #, inplace = True)
#
## deduce the congruence
#Balanced.loc[Balanced["<"] == Balanced["(-0.75,0)"], "Congruence"] = Congruent
#Balanced.loc[Balanced[">"] == Balanced["(0.75,0)"], "Congruence"] = Congruent
#Balanced.loc[Balanced["<"] == Balanced["(0.75,0)"], "Congruence"] = Incongruent
#Balanced.loc[Balanced[">"] == Balanced["(-0.75,0)"], "Congruence"] = Incongruent
#Balanced.loc[Balanced[">", "<"] == Balanced["(0,0)"], "Congruence"] = Neutraal

## loop over the 12 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    # make the design for one block
    
    ## completely random trial order
    blockTrials = data.TrialHandler(Design, nReps = nReps, method = "fullRandom")
    
    ## add the block to the ExperimentHandler
    thisExp.addLoop(blockTrials)
    
    #range(nBlocks).addData("Block", blocki+1)
    
    # announce what block is about to start
#    Block_start.text = "Block " + str(blocki+1) + " will start when you press the space bar."
#    Block_start.draw()
#    win.flip()
    
    # Esther: pas op, hier heb je slechts drie blokken waarop de alternatieve constructie komt: 9, 10, en 11
    
    if (blocki+1) <= 8:
        Instructions.text = ("Reageer op de richtig van het pijltje (links of rechts)\n" + 
        "door op de pijltjestoetsen te drukken.\n" +
        "Druk links als het pijltje naar links wijst, en rechts als het pijltje naar rechts wijst." +
        " Druk op spatie om blok " + str(blocki+1) + " te starten.")
    else:
        Instructions.text = ("Reageer op de positie van het pijltje (links, midden of rechts)\n" + 
        "door op de pijltjestoetsen te drukken.\n" +
        "Druk links als het pijltje links staat, rechts als het pijltje rechts staat en onder als het pijltje in het midden staat." +
        " Druk op spatie om blok " + str(blocki+1) + " te starten.")
        
    ## display the Instructions
    Instructions.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    for trial in blockTrials:
        
        ## store the block number
        # blockTrials.addData("Trial", trial+1)
        blockTrials.addData("Block", blocki+1)
        
        stimulus.pos = trial["Position"]
        stimulus.text = trial["Arrays"]
        stimulus.draw()
        win.flip()
        
        ## wait for the response
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["right","down", "left"])
        
        blockTrials.addData("response", keys[0])
        blockTrials.addData("RT", my_clock.getTime())
        
        ## fill in the instruction and correct answer
        if (blocki+1) <= 8: 
            blockTrials.addData("Instruction", "ResponseArrays")
            CorAns = trial["Arrays"]
        else:
            blockTrials.addData("Instruction", "ResponsePositionArrays")
            CorAns = trial["Position"]
        CorAns = CorAns.replace("<","left")
        CorAns = CorAns.replace(">","right")
        CorAns = CorAns.replace("(-0.75,0)","left")
        CorAns = CorAns.replace("(0,0)","down")
        CorAns = CorAns.replace("(0.75,0)","right")
        blockTrials.addData("CorAns", CorAns)
        
        thisExp.nextEntry()
        # end of the trial loop

# display the goodbye message
Goodbye.draw()
win.flip()
core.wait(1)

# close the experiment window
win.close()
