from psychopy import data, visual, event, core, gui
import os
import numpy

win              = visual.Window([1000, 700],units = "norm")
experiment_timer = core.Clock()


##GUI__________________________________________________________________________________________________________________________________________

info    = {"Naam?": "", 
           "Proefpersoonnummer?": "", 
           "Leeftijd?":"",
           "Gender?" : "man, vrouw, derde gender",
           "Handvoorkeur?" : "links, rechts, ambidexter"}


##DATA_________________________________________________________________________________________________________________________________________

directory_to_write = os.getcwd()

## keep asking for a new name when the data file already exists 
already_exists = True
while already_exists:
    
    infoDlg = gui.DlgFromDict(dictionary=info, title="Demo") ##display GUI and get pp number from it
    nummer = info["Proefpersoonnummer?"]
    
    # Esther: pas op, er zal hier nog een / moeten staan voor je test4 en niet voor subject
    # Esther: hier .csv toevoegen zorgt ervoor dat de ExperimentHandler nog een tweede keer .csv zal toevoegen waardoor je nooit dubbele files zal kunnen detecteren
    
    file_name = directory_to_write + "test 4" + "/subject_" + nummer + ".csv" 
    print(file_name)
    
    if not os.path.isfile(file_name):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This name was already used. Please ask the experimenter to help you to enter a unique name.")
        myDlg2.show()

thisExp = data.ExperimentHandler(dataFileName = file_name)


##WELCOME______________________________________________________________________________________________________________________________________

welcome       = visual.TextStim(win,text = "Welkom {0}! Druk op de spatie om verder te gaan.".format(info["Naam?"]))
instructions  = visual.TextStim(win,text = "In dit experiment verschijnt op elke trial een pijltje. \n\n" + 
                                            "Dit pijltje kan naar verschillende kanten wijzen en op verschillende plaatsen staan.\n\n" + 
                                            "Per blok zal je op een ander kenmerk moeten reageren, lees dus goed de instructies.\n\n" +
                                            "Als je klaar bent, druk op spatie om verder te gaan" )


welcome.draw()
win.flip()
k = event.waitKeys(keyList = "space")
instructions.draw()
win.flip()
k = event.waitKeys(keyList = "space")


##STIMULI_____________________________________________________________________________________________________________________________________

input_file_name = "EXcelData.xlsx"
## Import the trial list from the Excel file
trial_list = data.importConditions(input_file_name) 
print(trial_list)

# Esther: fullRandom was een betere optie dan random

trials = data.TrialHandler(trial_list, nReps = 10, method = "random")

## Define the name of the output file 
output_file_name = "file_name"

## Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = output_file_name)

## Couple the TrialHandler to the ExperimentHandler 
thisExp.addLoop(trials)


##STIMULI_____________________________________________________________________________________________________________________________________

reageeroprichting = visual.TextStim(win,text = "Reageer op de richting van de pijl.\n\n" + 
                                                "Als het pijltje naar links staat (<), druk op de linkse toetsenbordpijl.\n\n" + 
                                                "Als het pijltje naar rechts staat (>), druk op de rechtse toetsenbordpijl.\n\n" + 
                                                "Als je klaar bent, druk op spatie om verder te gaan")
reageeroppositie = visual.TextStim(win,text = "Reageer op de positie van de pijl.\n\n" + 
                                                "Als het pijltje links op het scherm staat, druk op de linkse toetsenbordpijl.\n\n" + 
                                                "Als het pijltje rechts op het scherm staat, druk op de rechtse toetsenbordpijl.\n\n" + 
                                                "Als je klaar bent, druk op spatie om verder te gaan")

##LOOP_____________________________________________________________________________________________________________________________________

for block in range(12):

    
    if block < 7:
        reageeroprichting.draw()
        win.flip()
        k = event.waitKeys(keyList = "space")
    else:
        reageeroppositie.draw()
        win.flip()
        k = event.waitKeys(keyList = "space")

    # Esther: hier had je eigenlijk de trialHandler en addloop() moeten gebruiken 

    for trial in trials:
        
        stimulus = visual.TextStim(win, text = trial["Pijl"] )
        stimulus.pos = (trial["Positie"],0)
        stimulus.draw()
        win.flip()
        
        experiment_timer.reset()
        response = event.waitKeys(keyList = ["right","left"])   # Esther: de down optie niet vergeten hier!
        rt       = experiment_timer.getTime()
        
        trials.addData('stimulus', stimulus)
        trials.addData('positie', trial["Positie"])
        trials.addData('RT',rt)
        
        thisExp.nextEntry()


##afsluit_____________________________________________________________________________________________________________________________________

afsluit = visual.TextStim(win, text = "Het experiment is gedaan! Bedankt voor uw deelname.\n\n" + 
                                      "Gelieve de proefleider bij u te roepen.")
afsluit.draw()
win.flip()
k = event.waitKeys(keyList = "space")
win.close()
