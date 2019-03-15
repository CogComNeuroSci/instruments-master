##ENKEL DE CORRECTE RESPONSEN ZIJN NIET GELUKT, EN OOK DE NUMMERS VAN HET BLOK EN TRIALS

from __future__ import division
import numpy
from numpy import random
from psychopy import visual, event, core, gui, data
import os, platform, math

#ik wil een klokje
my_clock= core.Clock()

#directory
my_directory=os.getcwd()

#dialoogvenster
info = {"Participant name":"unknown", "Participant number":str(0), "Gender":["male", "female","third gender"], "Age":0, "Hand preference":["left","right","ambidexter"]}

already_exists=True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Pijltjestaak")
    file_name =my_directory + "/Test4_subject_" + str(info["Participant number"])
    
    number=info["Participant number"]
    gender=info["Gender"]
    age=info["Age"]
    hand=info["Hand preference"]
    
    extra={"number","gender","age","hand"} ##hier zorg ik ervoor dat alle ANONIEME data opgeslaan wordt in de experimenthandler later (zonder naam dus)
    
    if not os.path.isfile(file_name+ ".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

#experimment handler
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = extra)
print(file_name)

#functie aanmaken voor teksten
win = visual.Window(size=[1000,700])
MessageOnScreen = visual.TextStim(win, text = "OK")

def message(message_text = "", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    MessageOnScreen.text    = message_text
    MessageOnScreen.height  = height
    MessageOnScreen.pos     = pos
    MessageOnScreen.color   = color
    
    MessageOnScreen.draw()
    win.flip()
    if duration == 0:
        x=event.waitKeys(keyList =["space","escape"])
        if x[0] in ['escape', 'esc']:##dit is nergens gevraagd, maar steek ik er tussen voor mijn gemak. Ik gebruik ook win.close omdat dit vlotter is dan break
            win.close()
    else:
        core.wait(duration)

#welkom
message(message_text="Welkom {0}! \n\nDruk op spatie om verder te gaan.".format(info["Participant name"]))
#eerste instructies
message(message_text="In dit experiment zul je reageren op pijltjes; < of > .\n\nDeze pijltjes kunnen links op het scherm, rechts of centraal voorkomen. \n\nIn sommige blokken zul je reageren op de richting van het pijltje zelf, links of rechts, met uw pijltjes op het klavier.\n\nIn andere blokken zul je reageren op de plaats van de pijltjes; als de pijltjes links op het scherm staan, druk je op het linkerpijltje op het klavier, als ze rechts staan, druk je op het rechterpijltje op het klavier. Indien het pijltje gewoon centraal staat, druk je op het pijltje naar beneden.\n\nVoor aanvang van elk blok wordt aangegeven of u dient te reageren op de richting van het pijltje, of op de positie. \n\nIndien u geen vragen meer heeft, mag u op de spatiebalk duwen om verder te gaan.", height=0.07)


#instructies voor in de blockloop
Instructions1=("In dit blok dien je te reageren op de richting van het pijltje zelf\n\n" +
                            "Indien het pijltje naar rechts wijst, reageert u met uw rechter pijltje op het klavier\n\n" +
                            "Indien het pijltje naar links wijst, reageert u met uw linker pijltje op het klavier\n\n" +
                            "Druk op spatie om te starten")

Instructions2=("In dit blok dien je te reageren op de positie van het pijltje op het scherm\n\n" +
                            "Indien het pijltje rechts staant, reageert u met uw rechter pijltje op het klavier\n\n" +
                            "Indien het pijltje links staat, reageert u met uw linker pijltje op het klavier\n\n" +
                            "Als het gewoon centraal staat, reageert u met het pijltje naar onder op het klavier\n\n"+
                            "Druk op spatie om te starten")
which_type=["Instructions1","Instructions1","Instructions2","Instructions1","Instructions1","Instructions2","Instructions1","Instructions1","Instructions2","Instructions1","Instructions1","Instructions2"]

#design
Design = [{"Pijltje": "<", "Positie": (-0.5,0.0)}, {"Pijltje": "<", "Positie": (0.5,0.0)}, {"Pijltje": "<", "Positie": (0.0,0.0)},\
          {"Pijltje": ">", "Positie": (-0.5,0.0)}, {"Pijltje": ">", "Positie": (0.5,0.0)}, {"Pijltje": ">", "Positie": (0.0,0.0)}]


#trials lopen
for blok in range(12):
    message(message_text="Dit is blok {0} van 12.\n\nDe instructies voor het komende blok zullen verschijnen als u op de spatiebalk drukt".format(blok+1))
    
    #INSTRUCTIES
    InstrType = "None"
    InstrType = which_type[blok]
    
    if InstrType == "Instructions1":
        message(message_text=Instructions1, height=0.10)
    elif InstrType == "Instructions2":
        message(message_text=Instructions2, height=0.10)
    #trialhandler
    trials = data.TrialHandler(trialList = Design, nReps = 10, name = "Exp", method = "random")
    
    
    #experimenthandler aan trialhandler koppelen
    thisExp.addLoop(trials)
    for trial in trials:
        stimulus=visual.TextStim(win, text="")
        stimulus.text=trial["Pijltje"]
        stimulus.pos=trial["Positie"]
        
        if ((trial["Pijltje"]=="<") and trial["Positie"]==(-0.5,0.0)) or ((trial["Pijltje"]==">") and trial["Positie"]==(0.5,0.0)):
            trials.addData("Congruency", "congruent")
        elif ((trial["Pijltje"]=="<") and trial["Positie"]==(0.0,0.0)) or ((trial["Pijltje"]==">") and trial["Positie"]==(0.0,0.0)):
            trials.addData("Congruency", "neutral")
        else:
            trials.addData("Congruency", "incongruent")
        
        stimulus.draw()
        win.flip()
        
        
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        
        keys = event.waitKeys(keyList = ["left","right","down","escape"])
        if keys[0] in ['escape', 'esc']:##Opnieuw, dit is nergens gevraagd, enkel voor mijn gemak. En ik vind win.close() vlotter
            win.close()
        
        trials.addData("response", keys[0])
        trials.addData("RT", my_clock.getTime())
        
        thisExp.nextEntry()
        #einde trialloop
    #einde blokloop

message(message_text="Bedankt voor uw deelname!")


