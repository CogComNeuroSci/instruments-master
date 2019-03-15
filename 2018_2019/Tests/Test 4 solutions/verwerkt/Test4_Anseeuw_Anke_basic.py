# dingen importeren
from psychopy import visual, event, core, gui, data
import os, pandas

# dialoguebox
info= {"Participant nummer": 0, "Naam": "", "Leeftijd": 0, "Gender":["man", "vrouw", "derde gender"], "Handvoorkeur": ["links", "rechts", "ambidexter"]}

directory = os.getcwd()

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4_Anseeuw_Anke_basic")
    directory2= directory + "/data" 
    if not os.path.isdir(directory2):
        os.mkdir(directory2)
    filenaam = directory2 + "/Test4_" + "subject_" +str(info["Participant nummer"])+".csv" 
    if not os.path.isfile(filenaam+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Probeer een ander nummer")
        myDlg2.show()


thisExp = data.ExperimentHandler(dataFileName = filenaam, extraInfo = info)


# visualisatie
win= visual.Window([1000,700])
welkom=visual.TextStim(win, text= "Welkom "+info["Naam"]+"!\nDruk op de spatiebalk om verder te gaan.")
instructies= visual.TextStim(win, text= 'instructies')
stimulus= visual.TextStim(win, text= "")
goodbye= visual.TextStim(win, "Bedankt om deel te nemen aan dit experiment.\nDruk nog éénmaal op de spatiebalk om het experiment te beëindigen en geef een seintje aan de experimentor.")
klok=core.Clock()

#naam verwijderen uit gegevens
info.pop("Naam")

# trialmatrix maken en koppelen aan experimenthandler
positie= [(-0.5, 0), (0,0), (0.5, 0)]
pijl= ["<-", "->"]

triallist= data.createFactorialTrialList({"positie":positie, "pijl":pijl})
trials= data.TrialHandler(triallist, nReps= 10, method="random")
thisExp.addLoop(trials)

#congruentie
congruentie=[1, -1, 0]
##congruent=1
##incongruent=-1
##neutraal=0
if pijl=="->" and positie==(0.5, 0) ^ pijl=="<-" and positie==(-0.5, 0):
    congruentie=congruentie[0]
elif pijl=="<-" and positie==(0.5,0) ^ pijl=="->" and positie==(-0.5, 0):
    congruentie=congruentie[1]
else:
    congruentie=congruentie[2]
    


# initiëring van het experiment
welkom.draw()
win.flip()
event.waitKeys(keyList = ["space"] )

# blockloop
for block in range(12):
    blocktext= visual.TextStim(win, text="Dit is blok "+ str(block+1)+".\n"+"Druk op de spatie om door te gaan.")
    blocktext.draw()
    win.flip()
    event.waitKeys(keyList = ["space"] )
    
    ##instructies
    if block < 8:
        instructies.text= "Druk op het linkse pijltje op je toetsenbord als het pijltje naar links gericht staat (<),\nen druk op het rechtste pijltje als het pijltje naar rechts gericht staat (>)." +'Druk op de spatie om te beginnen.'
    else:
        instructies.text= "Druk op het linker pijltje als de figuur op de linkerkant van het scherm gepresenteerd wordt,\ndruk op het rechtse pijltje als de figuur rechts staat \nen druk op het pijltje naar boven als de figuur in het midden staat." 'Druk op de spatie om verder te beginnen.'
    instructies.draw()
    win.flip()
    event.waitKeys(keyList = ["space"] )
    
    #correcte respons
    ##corresp=[]
    ##if block <8:
        ##corresp[corresp==pijl[0]]="left"
        ##corresp[corresp==pijl[1]]="right"
    ##else:
        ##corresp[corresp==positie[0]]="left"
        ##corresp[corresp==positie[1]]="up"
        ##corresp[corresp==positie[2]]="right"
    
    
    
    #trialloop
    for trial in  trials:
        stimulus.text= trial["pijl"]
        stimulus.pos= trial["positie"]
        stimulus.draw()
        
        ##toetsenbord wissen en klok resetten
        event.clearEvents(eventType = "keyboard")
        klok.reset()
        
        win.flip()
        keys=event.waitKeys(keyList = ["left", "right", "up"] )
        
        ##respons opslaan
        trials.addData("response", keys[0])
        ##reactietijd opslaan
        trials.addData("RT",klok.getTime())
        ##congruentie opslaan
        trials.addData("congruentie", congruentie)
        ##correcte respons opslan
        ##trials.addData("correcte respons", corresp)
        
        
        ##naar volgende trial
        thisExp.nextEntry()
        
# Na 1 blok komen de trials niet meer aan bod. Wat doe ik hier verkeerd?
        
#validatie (advanced, maar aangezien ik van de basic nog niet alles vond, wist ik niet of ik dit in een aparte file moest steken)
## trialhandler omzetten naar dataframes
dataframe= pandas.DataFrame.from_dict(trials)
## titel geven aan de kolommen
dataframe.columns=["positie", "pijl"]
## tabel maken
print(pandas.crosstab(dataframe.positie, dataframe.pijl))


goodbye.draw()
win.flip()
event.waitKeys(keyList = ["space"] )
core.quit()
