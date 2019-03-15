# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy, time
from numpy import random
import os
import platform
import pandas

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height], units = "norm")

#initializing
my_clock = core.Clock()
info = {"Name": "", "Participant Number" : str(0), "age": str(0), "gender":["male","female", "x"], "Handedness": ["left", "right", "ambidexter"]} 
nTrials = 12#60
nBlocks = 12
stimulus        = visual.TextStim(win,text="", pos = (0.0 , 0.0))


#stimuli
#def stimuli():
    #stimuli1 = visual.TextStim(win, text = "<", pos = (-0.5,0))
    #stimuli2 = visual.TextStim(win, text = "<", pos = (0,0))
    #stimuli3 = visual.TextStim(win, text = "<", pos = (0.5,0))
    #stimuli4 = visual.TextStim(win, text = ">", pos = (-0.5,0))
    #stimuli5 = visual.TextStim(win, text = ">", pos = (0,0))
    #stimuli6 = visual.TextStim(win, text = ">", pos = (0.5,0))

# Esther: hieronder is de correcte response altijd gebaseerd op de stimulus text en niet op de positievan de stimulus
# Esther: eigenlijk was het niet nog niet mogelijk om de correcte response te bepalen, maar wel de congruentie van de stimulus

Design = [{"Stimulus": "<", "CorResp": "f", "pos": (-0.5,0)}, {"Stimulus": "<", "CorResp": "f", "pos": (0,0)},{"Stimulus": "<", "CorResp": "f", "pos": (0.5,0)}, 
          {"Stimulus": ">", "CorResp": "j", "pos": (-0.5,0)}, {"Stimulus": ">", "CorResp": "j", "pos" : (0,0)}, {"Stimulus": ">", "CorResp": "j", "pos" : (0.5,0)}]

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test4")
    directory_to_write_to = my_directory + "/data"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4" + "_subject_" + str(info["Participant Number"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, let's get started!")

# ESther: pas op, je moet eerst nog de info over de naam van de proefpersoon verwijderen uit de dialog box info zodat die niet in de data file terecht komt
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


#Welcome
def welkom():
    participant_name = info["Name"]
    Welcome = visual.TextStim(win, text = "Hallo " + participant_name + ", welkom op het experiment. Druk spatie om verder te gaan")
    Welcome.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    
#goodbye
def goodbye():
    goodbye = visual.TextStim(win, text = "Dankuwel voor deelname, het experiment zit erop. Druk spatie om het scherm te sluiten.")
    goodbye.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#instruction voor 2/3 van de blokken op richting pijltje
def instruction1():
    instruction = visual.TextStim(win, text = "U dient te reageren op de richting van het pijltje. Wijst het naar links, dan antwoordt u met het linkse pijltje(f) op het toetsenbord. Wijst het naar rechts, dan antwoordt u met het rechtse pijltje(j) op het toetsenbord. Druk spatie om voort te gaan")
    instruction.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#instruction voor 1/3 van de blokken op positie
def instruction2():
    instruction2 = visual.TextStim(win, text = "U dient te reageren op de positie van het pijltje. Staat het links, dan antwoordt u met het linkse pijltje(f) op het toetsenbord. Staat het rechts, dan antwoordt u met het rechtse pijltje(j) op het toetsenbord. Als het in het midden staat, dan antwoordt u met het onderste pijltje(b). Druk spatie om voort te gaan")
    instruction2.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#experiment

welkom()

blocki = 0
while blocki < nBlocks:

#dit was mijn eerste probeersel van het experiment:
    
    # Esther: er zijn 10 herhalingen van het design nodig, niet 1
    # Esther: verder zou fullRandom ook een betere optie geweest zijn dan random
    
    trials = data.TrialHandler(trialList = Design, nReps = 1 , method = "random")  
    thisExp.addLoop(trials)
    if blocki == 0:
        
        instruction2()
    else:
        instruction1()
    acc_block = 0
    
    for trial in trials:
        #stimulus moet komen
        stimulus.text = trial["Stimulus"]
        stimulus.pos = trial ["pos"]
        stimulus.draw()
        win.flip()
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["f","j","b"])  ##### ik wist niet hoe de pijltjes hier te zetten
        RT = my_clock.getTime()
        ## store the block number etc.
        trials.addData("Block", blocki+1)
        #trials.addData("trialnumber", trial+1)
        trials.addData("RT", RT)
        accuracy = 1*(keys[0]==trial["CorResp"])
        trials.addData("ACC", accuracy)
        acc_block += accuracy
        #trials.addData("CorResp", CorResp)
        
        
        thisExp.nextEntry()
#info.addData("Participant Number", Participant Number)
#info.addData("Handedness", handedness)
#info.addData("gender", gender)
#info.addData("age", age)

#dit het tweede maar werkte minder goed
# if blocki == [0,3]:
#        trials = data.TrialHandler(trialList = Design, nReps = 1 , method = "random")  
#        thisExp.addLoop(trials)
#        instruction2()
#        for trial in trials:
#            #stimulus moet komen
#            stimulus.text = trial["Stimulus"]
#            stimulus.pos = trial ["pos"]
#            stimulus.draw()
#            win.flip()
#            event.clearEvents(eventType="keyboard")
#            my_clock.reset()
#            keys = event.waitKeys(keyList = ["f","j","b"])  ##### ik wist niet hoe de pijltjes hier te zetten
#            RT = my_clock.getTime()
#            ## store the block number etc.
#            trials.addData("Block", blocki+1)
#            #trials.addData("trialnumber", trial+1)
#            trials.addData("RT", RT)
#            accuracy = 1*(keys[0]==trial["CorResp"])
#            trials.addData("ACC", accuracy)
#            acc_block += accuracy
#            #trials.addData("CorResp", CorResp)
#            
#            
#            thisExp.nextEntry()
#    
#    if blocki == [4,11]:
#        trials = data.TrialHandler(trialList = Design, nReps = 1 , method = "random")  
#        thisExp.addLoop(trials)
#        instruction1()
#        for trial in trials:
#            #stimulus moet komen
#            stimulus.text = trial["Stimulus"]
#            stimulus.pos = trial ["pos"]
#            stimulus.draw()
#            win.flip()
#            event.clearEvents(eventType="keyboard")
#            my_clock.reset()
#            keys = event.waitKeys(keyList = ["f","j","b"])  ##### ik wist niet hoe de pijltjes hier te zetten
#            RT = my_clock.getTime()
#            ## store the block number etc.
#            trials.addData("Block", blocki+1)
#            #trials.addData("trialnumber", trial+1)
#            trials.addData("RT", RT)
#            accuracy = 1*(keys[0]==trial["CorResp"])
#            trials.addData("ACC", accuracy)
#            acc_block += accuracy
#            #trials.addData("CorResp", CorResp)
#            
#            
#            thisExp.nextEntry()
#        
#
goodbye()