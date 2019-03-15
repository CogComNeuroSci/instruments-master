## Test 4; Yana ibens

# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy 
from numpy import random
import os
import platform

# set directory
my_directory = os.getcwd()

# window aanmaken
win = visual.Window(size = [1000,700], units = "norm")

# variabelen
nblocks     = 12
ntrials     = 60
info        = {"Naam participant": "Unknown", "Nummer participant":0, "Leeftijd":0, "Gender": ["man", "vrouw", "derde gender"], "Handvoorkeur": ["rechts", "links", "ambidexter"]}
clock       = core.Clock()
RespOptions = ['right', 'left', 'up']
Stimuli     = numpy.array(["<", ">"])
Positie     = [-0.75,0], [0,0], [0.75,0]

# data file
already_exists = True 
while already_exists: 
    
    myDlg = gui.DlgFromDict(dictionary = info, title = "data") 
    
    directory_to_write_to = my_directory + "/data"
    
    if not os.path.isdir(directory_to_write_to): 
        os.mkdir(directory_to_write_to)
        
    file_name = directory_to_write_to + "/Test4" + "_subject_"+str(info["Nummer participant"])
    if not os.path.isfile(file_name+".csv"): 
        already_exists = False 
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
 
print("OK, let's get started!")
subject_name = info["Naam participant"]
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# de teksten aanmaken
stimulus        = visual.TextStim(win,text="")
blockstart = visual.TextStim(win,text="")
Welkom = visual.TextStim(win, text = "Welkom " + info["Naam participant"] + "!\n\nDruk op de spatiebalk om verder te gaan")
Instructies = visual.TextStim(win, text = "In dit experiment verschijnt er op elke trial een pijltje. Ofwel wijst dit pijltje naar links ofwel naar rechts. \n\nHet pijltje verschijnt ofwel aan de linker kant van het scherm, het midden van het scherm of de rechter kant van het scherm. \n\nIn sommige blokken zal u moeten reageren op de positie van het pijltje en in andere blokken op de richting van het pijltje. Hiervoor gebruikt u de pijltjes op het klavier.\n\nDruk op spatie om aan het experiment te beginnen")
Afscheid = visual.TextStim(win, text = "Bedankt! \n\nDruk op de spatiebalk om het experiment af te sluiten")
info.pop("Naam participant")

# 3-by-2 factorial design

##DesignPositie = [{"Positie" : "-0.75,0", "Stimuli" : ">" , "Congruency" : "incongruent", "CorrectRespone" : "left"}, {"Positie" : "-0.75,0", "Stimuli" : "<" , "Congruency" : "congruent" , "CorrectRespone" : "left"}, {"Positie" : "0,0", "Stimuli": ">" "Congruency" : "incongruent" , "CorrectResponse" : "up"}, {"Positie" : "0,0", "Stimuli": "<" "Congruency" : "incongruent" , "CorrectResponse" : "up"}, {"Positie" : "0,0.75", "Stimuli" : "<", "Congruency": "incongruent", "CorrectResponse" : "right"}, {"Positie" : "0,0.75", "Stimuli" : ">", "Congruency": "congruent", "CorrectResponse" : "right"}]
##DesignStimuli = [{"Stimuli" : "<", "Positie" : "-0.75,0" , "Congruency" = "congruent" ,"CorrectResponse" : "left"},  {"Stimuli" : "<", "Positie" : "0,0" , "Congruency" = "incongruent", "CorrectResponse" : "left"}, {"Stimuli" : "<", "Positie" : "0,0.75" , "Congruency" = "incongruent" , "CorrectResponse" : "left"}, {"Stimuli" : ">", "Positie": "-0.75,0" , "Congruency" : "incongruent" , "CorrectResponse" : "right"}, {"Stimuli" : ">", "Positie": "-0,0" , "Congruency" : "incongruent" , "CorrectResponse" : "right"}, {"Stimuli" : ">", "Positie": "0,0.75" , "Congruency" : "congruent" , "CorrectResponse" : "right"}]
## Ik krijg een error en ik weet niet waarom 

# trails definen
def announce_blockstart(blocknr):
    if blocknr == 0:
        blockstart.text = ( "In deze blok moet je op de positie van de pijl reageren. \nAls hij rechts staat, druk je op de rechter pijl, staat hij rechts, druk je op de rechter pijl, en wanneer hij in het midden staat druk je op de pijl naar boven. \n\nDruk op spatie om te beginnen")
    if blocknr==1:
        blockstart.text = ( "In deze blok moet je op de richting van de pijl reageren. \nAls hij naar rechts wijst, druk je op de rechter pijl, wijst hij naar links, druk je op de linker pijl./n/nDruk op spatie om te beginnen")
    if blocknr==2:
        blockstart.text = ( "In deze blok moet je op de richting van de pijl reageren. \nAls hij naar rechts wijst, druk je op de rechter pijl, wijst hij naar links, druk je op de linker pijl./n/nDruk op spatie om te beginnen")
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")



#def choose_trials(bloknr):
#if bloknr == 0:
#        Design_block = DesignPositie
#    trials = data.TrialHandler(trialList = Design_block, nReps = 10 method = "random") 
#thisExp.addLoop(trials)
#else:
#        Design_block = DesignStimuli
#trials = data.TrialHandler(trialList = Design_block, nReps = 10, method = "random")  
#    thisExp.addLoop(trials)
#return trials
## Ik krijg een error maar weet niet waarom


# welkom tonen
Welkom.draw()
win.flip()
event.waitKeys(keyList = "space")

# instructies tonen
Instructies.draw()
win.flip()
event.waitKeys(keyList = "space")

# trial starten
#block = 0
#while block < 3:
#    announce_blockstart(block)
#    
#    trials = choose_trials(block)
#    acc_block = 0
#    for trial in trials:
#        stimulus.text=trial["Stimuli"]
#        stimulus.draw()
#        win.flip()
#        
#        event.clearEvents(eventType="keyboard")
#        clock.reset()
#        keys = event.waitKeys(keyList = ["right","left", "up"])
#    
#        trials.addData("response", keys[0])
#        accuracy = 1*(keys[0]==trial["Correct"])
#        acc_block += accuracy
#        
#        trials.addData("RT",clock.getTime())
#        trials.addData("Response",keys[0])
#        trials.addData("CorrectResponse",trial["Correct"])
#        trials.addData("accuracy",accuracy)
#        
#        thisExp.nextEntry() 
#    # end of the trial loop
#    if (block == 1) or (block==2) or (acc_block == 4):
#        block += 1
## Hier wilde ik nog verder van af werken

# afscheid tonen
Afscheid.draw()
win.flip()
event.waitKeys(keyList = "space")

## trials_addData voor de rest van de data in de datafile te stoppen