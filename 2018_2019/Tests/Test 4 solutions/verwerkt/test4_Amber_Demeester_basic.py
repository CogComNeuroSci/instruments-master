# Amber Demeester - Test 4 IEP

# import modules

from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy as np
from numpy import random
import os
import platform
import time

# set the directory
my_directory = os.getcwd()

#initializing
info        = {"Participant number": str(0), "Name": "", "Participant number": 0, "age": 0, "gender": ["male","female","third gender"], "hand preference": ["left","right","ambidexter"]}

# create a dialog box
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "test4")
    directory_to_write_to = my_directory + "/test4"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "test4_subject_" + str(info["Participant number"]) + ".csv"
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

# initialize the window
win = visual.Window(size = [1000,700], units = "norm")

# initialize the variables
nblocks     =  4
ntrials     = 20
my_clock = core.Clock()
participant = info["Participant number"]
welcome_message = visual.TextStim(win, text = "Welkom {}".format(subject_name) +"\n\nPress <space> to continue")
stimulus = visual.TextStim(win, text = ">", pos = (0,0))
instructies = visual.TextStim(win, text = "ok")
goodbye = visual.TextStim(win, text = "Thank you")




#testen
#eerst de welkom
welcome_message.draw()
win.flip()
event.waitKeys(keyList = "space")

# instructies + stimulus
block = 0
trial = 0
for block in range(nblocks):
    #eerste soort blok
    instructies.text = "Het is de bedoeling dat je u focust op de richting van de stimulus. Reageer met de pijltjestoetsen of de stimulus naar links of naar rechts wijst."
    instructies.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    for trial in range (ntrials):
        
        if trial%2:
            stimulus.text = "<"
            stimulus.position = (0,0)
        else :
            stimulus.text = ">"
            stimulus.position = (0,-0.5)
    
        stimulus.draw()
        my_clock.reset()
        win.flip()
        event.waitKeys(keyList = ["<",">"])
        my_clock.getTime()
        trial = trial +1
    
    #tweede soort blok
    instructies.text = "Het is de bedoeling dat je u focust op de positie van de stimulus. Reageer met de pijltjestoesten of de stimulus zich links, rechts of in het midden van het scherm staat. \n\nPress <space> to continue"
    instructies.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    for trial in range (ntrials):
        
        if trial%2:
            stimulus.text = "<"
            stimulus.position = (0,0.5)
        else :
            stimulus.text = ">"
            stimulus.position = (0,-0.5)
    
        stimulus.draw()
        my_clock.reset()
        win.flip()
        event.waitKeys(keyList = ["<",">"])
        my_clock.getTime() 
        trial = trial +1
    
    #derde soort blok
    instructies.text = "Het is de bedoeling dat je u focust op de richting van de stimulus. Reageer met de pijltjestoetsen of de stimulus naar links of naar rechts wijst. \n\nPress <space> to continue"
    instructies.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    for trial in range (ntrials):
        
        if trial%2:
            stimulus.text = "<"
            stimulus.position = (0,0)
        else :
            stimulus.text = ">"
            stimulus.position = (0,0.5)
    
        stimulus.draw()
        my_clock.reset()
        win.flip()
        event.waitKeys(keyList = ["<",">"])
        my_clock.getTime()
        trial = trial +1
        
    block = block + 1

#goodbye
goodbye.draw()
win.flip()
event.waitKeys(keyList ="space")
core.quit()