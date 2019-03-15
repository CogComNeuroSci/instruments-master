# import modules
from psychopy import visual, event, core, gui, data
import os
import platform

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height], units = "norm")

# initializing
nBlocks = 12
info        = {"Participantnummer": str(0), "Naam": "", "Leeftijd": "", "Gender":["man", "vrouw", "derde gender"], "handvoorkeur":["links", "rechts", "ambidexter"]}
my_clock    = core.Clock()

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Experiment test 4")
    directory_to_write_to = my_directory + "/data"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participantnummer"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Probeer een ander participantnummer in te geven.")
        myDlg2.show()

# naam bewaren voor begroeting
Naam_pp = info["Naam"]

# anonimiteit
info.pop("Naam")

thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# Design
Design = [{"Richting": "<", "Plaats": (-0.5,0), "Congruentie": "Congruent"}, {"Richting": "<", "Plaats": (0,0), "Congruentie": "Neutraal"}, {"Richting": "<", "Plaats": (0.5,0), "Congruentie": "Incongruent"},
            {"Richting": ">", "Plaats": (-0.5,0), "Congruentie": "Incongruent"}, {"Richting": ">", "Plaats": (0,0), "Congruentie": "Neutraal"}, {"Richting": ">", "Plaats": (0.5,0), "Congruentie": "Congruent"}]

# graphical elements
stimulus        = visual.TextStim(win,text="")
welkom         = visual.TextStim(win,text = "Welkom, {}!\nDruk op de spatiebalk om verder te gaan.".format(Naam_pp))
instruct        = visual.TextStim(win, text = "Instructions")
blocktext       = visual.TextStim(win, text = "")
goodbye         = visual.TextStim(win,text=( "Bedankt voor uw deelname!\nDruk op de spatiebalk om het experiment af te sluiten."))

# Begroeting
welkom.draw()
win.flip()
event.waitKeys(keyList = "space")

# blockloop + trials
for block in range(nBlocks):
    
    trials = data.TrialHandler(trialList = Design, nReps = 10, method = "random")  
    thisExp.addLoop(trials)
    
    # Instructies, CorResp en response mapping bepalen
    if (block+1)%3 == 0:
        instruct.text = ("Reageer op de positie van het pijltje.\n"+
                         "Staat het pijltje links op het scherm,\ndruk dan op de linker pijltjestoets.\n"+
                         "Staat het pijltje in het midden van het scherm,\ndruk dan op de onderste pijltjestoets."+
                         "Staat het pijltje rechts op het scherm,\ndruk dan op de rechter pijltjestoets."+
                         "\nDruk om de spatiebalk om te starten.")
        CorResp = ["left", "down", "right"]*2
        mapping = "positie"
    else:
        instruct.text = ("Reageer op de richting van het pijltje.\n"+
                         "Wijst het pijltje naar links,\ndruk dan op de linker pijltjestoets.\n"+
                         "Wijst het pijltje naar rechts,\ndruk dan op de rechter pijltjestoets."+
                         "\nDruk om de spatiebalk om te starten.")
        CorResp = ["left"]*3+["right"]*3
        mapping = "richting"
    instruct.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    TrialNrBlok = 0
    
    for trial in trials:
        ## Trialnummer in blok
        TrialNrBlok += 1
        ## Tekenen en tonen stimulus
        stimulus.text = trial["Richting"]
        stimulus.pos = trial["Plaats"]
        stimulus.draw()
        event.clearEvents(eventType="keyboard")
        win.flip()
        my_clock.reset()
        
        ## wachten op respons
        if (block+1)%3 == 0:
            keys = event.waitKeys(keyList = ["left","right", "down"])
        else:
            keys = event.waitKeys(keyList = ["left","right"])
        RT = my_clock.getTime()
        
        ## aanvullen output file
        trials.addData("Response Mapping", mapping)
        trials.addData("CorResp", CorResp[trials.thisIndex])
        trials.addData("response", keys[0])
        trials.addData("RT", RT)
        accuracy = 1*(keys[0]==CorResp[trials.thisIndex])
        trials.addData("ACC", accuracy)
        trials.addData("Bloknummer", block+1)
        trials.addData("Trialnr in blok", TrialNrBlok)
        trials.addData("Trialnr in exp", (block*60)+TrialNrBlok)
        
        thisExp.nextEntry()
    
# Afscheid
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()