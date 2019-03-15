# Import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy as np
from numpy import random
import os
import platform

#Set the current working directory
my_directory = os.getcwd()

#Initialize window and clock
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height])

my_clock = core.Clock()

#Create dialog box
info = {"Name": "", "Participant number": str(0), "Age": str(0), "Gender": ["Male", "Female", "Other"], "Handpreference": ["Left", "Right", "Ambidexter"]}

#Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary=info, title = "Test4")        #Display dialog box
    
    # Esther: /data was eigenlijk voldoende
    
    directory_to_write_to = my_directory + "/data_Test4"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"])
    if not os.path.isfile(file_name+ ".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title= "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, let's get started!")
subject_name = info["Name"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

#Graphical elements
Welcome = visual.TextStim(win, text =( "Hi {}, \n" +
                                       "Welcome to this experiment!\n" + 
                                       "Use the arrows on your keyboard to either indicate the position of the arrow on the screen, \n" +
                                       "or to indicate the orientation of the arrow on the screen. \n\n" +
                                       "Push the space bar to proceed.").format(subject_name))

# Esther: deze instructies zeggen eigenlijk niets over het verschil tussen de blokinstructies

Instruction = visual.TextStim(win, text =("Push left ('left arrow') or \n" + 
                                           "Push right ('right arrow') or \n" +
                                           "Push down ('down arrow'). \n\n" +
                                           "Push the space bar to start the experiment."))
Goodbye = visual.TextStim(win, text = ("This is the end of the experiment. \n\n" +
                                        "Thank you for your participation!"))
Stimulus        = visual.TextStim (win,text="")

#Welcome and instructions
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

Instruction.draw()
win.flip()
event.waitKeys(keyList = "space")

#Constants
## Number of blocks
nBlocks = 12

## Number of trials per block
nTrialsBlock = 60

## Number of design repetitions per block
nReps = int(nTrialsBlock/ (2*3))

# Make design based on the core trial characteristics
## Make the 2 x 3 factorial design

Orientations = ["<", ">"]
Positions = ["pos = (-0.5, 0)", "pos = (0,0)", "pos = (0.5, 0)"]    # Esther: enkel de horizontale coordinaten waren hier voldoende
Design = data.createFactorialTrialList({"OrientationArrow": Orientations, "PositionArrow": Positions})

# Esther: oei, je overschrijft hier je vorige experiment handler door een nieuwe, dus de gegevens van je proefpersoon zullen niet opgeslagen worden
# Esther: en je gebruikt je geplande filenaam niet

# Make trial structure for the entire experiment
## Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = "Test4_output_handlers")

## Loop over the 12 blocks to randomize each block seperately
for blocki in range(nBlocks):
    
    #Make the design for one block
    ## Completely random trial order
    TrialsBlock = data.TrialHandler(Design, nReps = nReps, method = "fullRandom")
    
    ##Add block to the ExperimentHandler
    thisExp.addLoop(TrialsBlock)
    
    for trial in TrialsBlock:
        ##Store blocknumber
        TrialsBlock.addData("Block", blocki+1)
        
        ##Instruction and correct answer
        if (blocki+1)%3 == [1, 2, 3, 4]:
            TrialsBlock.addData("Instruction", "Position")
            CorAns = trial["PositionArrow"]
        else:
            TrialsBlock.addData("Instruction", "Orientations")
            CorAns = trial["OrientationArrow"]
        CorAns = CorAns.replace("<", "curses.KEY_LEFT")
        CorAns = CorAns.replace(">", "curses.KEY_RIGHT")
        CorAns = CorAns.replace("Position_Left", "curses.KEY_LEFT")
        CorAns = CorAns.replace("Position_Right", "curses.KEY_RIGHT")
        CorAns = CorAns.replace("Position_Center", "curses.KEY_DOWN")

        
        ##Display stimuli on screen
        Stimulus.text = trial["OrientationArrow"]
        Stimulus.position = trial["PositionArrow"]  # Esther: dit zal niet marcheren
        Stimulus.draw()
        win.flip()
        
        ##Wait for response
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["curses.KEY_LEFT", "curses.KEY_RIGHT", "curses.KEY_DOWN"]) # ESther: gevonden op het internet? Maar dan is er wel een library nodig?
        
        TrialsBlock.addData("response", keys[0])
        accuracy = 1*(keys[0] == correct [trial["Number"]-1])
        TrialsBlock.addData("Acc", accuracy)
        TrialsBlock.addData("RT", my_clock_getTime())   # Esther: best de RT meteen vastleggen in plaats van dit uit te stellen tot later
        
        ##Proceed to next trial
        thisExp.nextEntry()


# ESther: zorg dat de proefpersoon ook op het einde weten op welke toets ze moeten drukken

# say goodbye to the participant
Goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()


