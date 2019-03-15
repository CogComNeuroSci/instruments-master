from psychopy import visual, event, core, gui, data
import os
import platform

my_directory = os.getcwd()
my_clock = core.Clock()

## make the window
win = visual.Window(size = (1000,700))

## info for dialog box
info        = {"Naam":"", "Nummer": str(0), "Leeftijd": str(0), "Gender":["man", "vrouw", "derde gender"], "Handvoorkeur" : ["links", "rechts", "ambidexter"]}

## make the data storeable
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Info proefpersoon")
    directory_to_write_to = my_directory + "/data"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Nummer"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg()
        myDlg2.addText("Dit nummer bestaat al. \nVoer een ander nummer in.")
        myDlg2.addField("Nummer:")
        myDlg2.show()
Naam = info["Naam"]
info.pop("Naam")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

## Tekst
intro       = visual.TextStim(win, text = ("Goedendaag {},\nWelkom bij dit experiment!\nDruk op spatiebalk om verder te gaan").format(Naam))
instructies = visual.TextStim(win, height = 0.075, text = ("Gebruik de toetsen 'H', 'J' en 'K' om te reageren op de stimuli\nDruk op 'H' als het gepresenteerde pîjltje naar links staat en druk op 'K' als het pijltje naar rechts staat\nIn de laatste opgaven moet je reageren op de positie van het pijltje.\nDruk op 'H' als de pijl aan de linkerkant staat, op 'J' als de pijl in het midden staat en 'K' als de pijl aan de rechterkant staat, ongeacht van de richting van de pijl.\nDruk op spatiebalk als je klaar bent om met het experiment te beginnen.\nVeel succes!"))
outro       = visual.TextStim(win, text = ("Dit was het einde van het experiment!\nBedankt voor u deelname"))

## Stimuli
stimulus = visual.TextStim(win,text="", pos=(0.0, 0.0))
Design = [{"pijl": ">", "pos":(0.0, 0.0)}, {"pijl": ">", "pos":(0.5, 0.0)}, {"pijl": ">", "pos":(-0.5, 0.0)}, {"pijl": "<", "pos":(0.0, 0.0)}, {"pijl": "<", "pos":(0.5, 0.0)}, {"pijl": "<", "pos":(-0.5, 0.0)}]

intro.draw()
win.flip()
event.waitKeys(keyList = "space")

instructies.draw()
win.flip()
event.waitKeys(keyList = "space")

for block in range(12):
    
    trials = data.TrialHandler(trialList = Design, nReps = 10, method = "random")
    thisExp.addLoop(trials)
    
    for trial in trials:
        stimulus.pos = trial["pos"]
        stimulus.text = trial["pijl"]
        stimulus.draw()
        win.flip()
        
        event.clearEvents(eventType="keyboard")
        my_clock.reset()

#       if (block) >= 4:
#           instructies.text = ("Nu volgen de laatste opgaven\nDruk op 'H' als de pijl aan de linkerkant staat, op 'J' als de pijl in het midden staat en 'K' als de pijl aan de rechterkant staat. Probeer de richting van het pijltje te negeren\nDruk op spatiebalk om verder te doen.\nVeel succes!")
#           instructies.draw()
#           win.flip()
#           event.waitKeys(keyList = "space")
        
        if (block) >= 7:
           keys = event.waitKeys(keyList = ["h","j","k"])
        else:
           keys = event.waitKeys(keyList = ["h","k"])
        
        trials.addData("respons", keys[0])
        trials.addData("Reactietijd", my_clock.getTime())
        trials.addData("Block", block+1)
#        trials.addData("Trial", trial+1)
#        trials.addData("BlockTrial", (trial+1)/(block+1))
        
        thisExp.nextEntry()

outro.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()