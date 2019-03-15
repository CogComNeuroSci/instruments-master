from psychopy import visual, event, core, gui, data
import time, numpy, os

my_home_directory = os.getcwd()

win = visual.Window(size = [1000,700], units = 'norm')
my_clock    = core.Clock()

#Testafhankelijke informatie

nblocks = 12
blockTrials = 60

Stimuli = ["<",">"]
Posities = [(-0.50,0),(0,0),(0.50,0)]
NUnique = len(Stimuli) * len(Posities)
nReps = blockTrials / NUnique

#GUI & data file management

info = {"Naam": "Unknown", "Proefpersoonnummer": str(0), "Leeftijd": str(0), "Gender": ["Man", "Vrouw", "Ander"], "Handvoorkeur": ["Links", "Rechts", "Ambidexter"]}

already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    directory_to_write_to = my_home_directory + "/data"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Proefpersoonnummer"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        albestaand = visual.TextStim(win, text = "Dit proefpersoonnummer bestaat al, geef een ander proefpersoonnummer in. \n\nDuw op spatie om verder te gaan.")
        albestaand.draw()
        win.flip()
        event.waitKeys(keyList = ["space"])

subject_name = info["Naam"]
info.pop("Naam")

#Trials

# Esther: het is misschien handiger om je tekst op te splitsen over verschillende lijnen zodat je script eenvoudiger leesbaar is

#graphic elements
stimulus = visual.TextStim(win, text = "")
Instructie1 = visual.TextStim(win,  text = ("In deze volgende trials is het de bedoeling dat u let op de positie van het pijltje. \n Indien het pijltje zich aan de linkerkant van het scherm bevindt, duwt u op de linkse pijltjestoets. \n Indien het pijltje zich rechts bevindt, duwt u rechts. \n Indien het pijltje zich in het midden bevindt, duwt u op het pijltje naar beneden.\n U hoeft geen rekening te houden met de oriëntatie van het pijltje. \n\n Duw op spatie om te beginnen."))
Instructie2 = visual.TextStim(win,  text = ("In deze volgende trials is het de bedoeling dat u let op de oriëntatie van het pijltje. \n Indien het pijltje naar links wijst, duwt u op de linkse pijltjestoets. \n Indien het pijltje naar rechts wijst, duwt u rechts. \n U hoeft geen rekening te houden met de oriëntatie van het pijltje. \n\n Duw op spatie om te beginnen."))
welcome = visual.TextStim(win, text = "Welkom {0}. \n\nDuw op spatie om verder te gaan.".format(subject_name.split() [0]))


#randomisatie

Design = data.createFactorialTrialList({"Stimulus": Stimuli, "Positie": Posities})

thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

#welkom

welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

#«trials

for blocki in range(nblocks):
    #instructies
    
    if (blocki+1) <= nblocks/3:
        
        Instructie1.draw()
        win.flip()
        event.waitKeys(keyList = "space")
    else:
        Instructie2.draw()
        win.flip()
        event.waitKeys(keyList = "space")
    
    # Esther: fullRandom is hier nog een betere optie dan random
    
    blockTrials = data.TrialHandler(trialList = Design, nReps = nReps, method = "random")
    thisExp.addLoop(blockTrials)
    
    
    for trial in blockTrials:

            
            stimulus.text = trial["Stimulus"]
            stimulus.pos = trial["Positie"]
            stimulus.draw()
            win.flip()
            
            event.clearEvents(eventType="keyboard")
            my_clock.reset()
            keys = event.waitKeys(keyList = ["left","down", "right"])
            
            # Esther: de info over stimulus en positie heb je al toegevoegd via de trialHandler, dus die hoef je hier niet nog eens op te slaan
            
            blockTrials.addData("Stimulus", stimulus.text)
            blockTrials.addData("Positie", stimulus.pos)
            blockTrials.addData("response", keys[0])
            blockTrials.addData("RT", my_clock.getTime())
            
            if trial["Stimulus"] == "<" and trial["Positie"] == (-0.50,0):
                Congruence = "Congruent"
            elif trial["Stimulus"] == ">" and trial["Positie"] == (0.50,0):
                Congruence = "Congruent"
            elif trial["Positie"] == (0,0):
                Congruence = "Neutral"
            else:
                Congruence = "Incongruent"
                
            blockTrials.addData("Congruence", Congruence)
            
            thisExp.nextEntry()


goodbye = visual.TextStim(win, text = "Goodbye, {0}! \n\nDuw spatie om af te ronden.".format(subject_name.split() [0]))
goodbye.draw()
win.flip()
event.waitKeys(keyList = ["space"])

