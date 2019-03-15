# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy
from numpy import random
import os
import platform
import pandas
import numpy

my_directory = os.getcwd()
info = {"Participant number": str(0), "Name": "", "Gender":['male','female','other'],"age":0, "Hand preference":["left","right","ambidexter"]}

#Dialog box + folder
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "data")
    directory_to_write_to = my_directory + "/data"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"])+"_data"
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


#info taak + Design maken
nblocks = 12

posL = (-0.5,0)
posR = (0.5, 0)
posM = (0,0)
my_clock    = core.Clock()

DesignDirection = [{"Direction":"<-","Position": posL,"Correct":"left"},{"Direction":"<-","Position": posR,"Correct":"left"},{"Direction":"<-","Position": posM,"Correct":"left"},{"Direction":"->","Position": posL,"Correct":"right"},{"Direction":"->","Position": posR,"Correct":"right"},{"Direction":"->","Position": posM,"Correct":"right"}]
DesignPosition = [{"Direction":"<-","Position": posL,"Correct":"left"},{"Direction":"<-","Position": posR,"Correct":"right"},{"Direction":"<-","Position": posM,"Correct":"up"},{"Direction":"->","Position": posL,"Correct":"left"},{"Direction":"->","Position": posR,"Correct":"right"},{"Direction":"->","Position": posM,"Correct":"up"}]

#Grafische elementen
win_width = 1000
win_height = 700
win                  = visual.Window([win_width,win_height], units = 'norm')
stimulus             = visual.TextStim(win, text = "<-", pos=(0,0))
welcome              = visual.TextStim(win, text = ("Welkom {}!").format(subject_name))
instructionDirection = visual.TextStim(win, text = ("Reageer op de richting waarin de pijltjes wijzen. \n"
                                                      "Druk op de linker pijltjestoets voor links,\n"
                                                      "Rechter pijltjestoets voor rechts\n"
                                                      "Druk op spatie om verder te gaan"))
instructionPosition  = visual.TextStim(win, text = ("Reageer op de positie van de pijltjes.\n"
                                                      "Druk op linker pijltjestoets voor links,\n"
                                                      "rechter pijltjestoets voor rechts\n"
                                                      "en pijltje omhoog voor midden.\n"
                                                       "Druk op spatie om verder te gaan."))
goodbye              = visual.TextStim(win, text = ("Bedankt voor je deelname!\n"
                                                     "Druk op spatie om af te sluiten."))

#Bepalen welke instructies getoond zullen worden
def choose_instruction(blocknr):
    if blocknr%3 ==0: 
        instructionPosition.draw()
        win.flip()
        event.waitKeys(keyList = "space")
    else:
        instructionDirection.draw()
        win.flip()
        event.waitKeys(keyList = "space")

#Bepalen welke trials getoond zullen worden
def choose_trials(blocknr):
    if blocknr%3 == 0:
        Design = DesignPosition
    else:
        Design = DesignDirection
        
    trials = data.TrialHandler(trialList = Design, nReps = 10, method = "fullrandom")
    thisExp.addLoop(trials)
    return trials

#Bepalen welke toetsen gebruikt mogen worden 
def choose_keyoptions(blocknr):
    if blocknr%3 == 0:
        keys = event.waitKeys(keyList = ["right","left","up"])  
    else:
        keys = event.waitKeys(keyList = ["left","right"])
    return keys

##Define congruency: geeft error: list indices must be integers or slices, not str
#def congruency(trial):
#    if trial["Direction"] == "<-" and trial["Position"] == posL:
#        congr = "congruent"
#    elif trial["Direction"] == "->" and trial["Position"] == posR:
#        congr = "congruent"
#    else:
#        congr = "incongruent"
#    return congr


#Verwelkoming
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

#tonen instructies + starten trials
for block in range(nblocks):
    
    blok = block + 1
    choose_instruction(blok)
    trials = choose_trials(blok)
    
    
    for trial in trials:
        #stimulus.pos = trial["Position"]   ##Geeft error: "list indices must be integers or slices, not str"
        #stimulus.text = trial["Direction"] ##Geeft error: "list indices must be integers or slices, not str"
        stimulus.draw()
        win.flip()
        
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        keys = choose_keyoptions(block)
        
        #congr = congruency(trial)
        congr = "congruent"
        ##Trialnummer binnen blok bepalen: geeft error: "can only concatenate list (not "int") to list
        #trialditblok = trial + 1
        
        ##Trialnummer binnen experiment bepalen, geeft error: 'can only concatenate list (not "int") to list'
        #trialalleblokken = trial + (blok*60)
        ##Dit geprobeerd, maar geeft rare uitkomsten in excelfile
        trialalleblokken = str(trial) + (str(blok)*60)
        
        #acc = 1*(keys[0]==trial["Correct"]) ##Geeft error: list indices must be integers or slices, not str
        acc = 1
        
        
        trials.addData("Blok", blok)
        trials.addData("Congruency", congr)
        
        #trials.addData("Positie", trial["Position"])
        trials.addData("Positie", posM)
        
        #trials.addData("Direction", trial["Direction"])
        trials.addData("Direction", "<-")
        
        #trials.addData("Trialnummer dit blok", trialditblok)
        trials.addData("Trialnummer dit blok", trial)
        
        #trials.addData("Trialnummer totaal", trialalleblokken)
        trials.addData("Trialnummer totaal", 5)
        
        #trials.addData("Correct", trial[Correct])
        trials.addData("Correct", "<-")
        
        trials.addData("RT",my_clock.getTime())
        trials.addData("Response", keys[0])
        trials.addData("Accuracy", acc)
        
        thisExp.nextEntry()

# Afscheid nemen 
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

