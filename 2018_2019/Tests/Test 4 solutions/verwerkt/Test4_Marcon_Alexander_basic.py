## Test 4: Pijltjes

# Importeren van nodige modules________________________________________________________
from psychopy import visual, event, core, gui, data
import os, platform, math

# Initiatie window_____________________________________________________________________
T4win = visual.Window([1000, 700], units = "norm", color = (-1,-1,-1))

# Mijn directory_______________________________________________________________________
my_directory = os.getcwd()

os.chdir(my_directory) 

# Aanmaken dialogbox___________________________________________________________________
info = {"naam": "", "nummer": "0", "leeftijd": "0", "gender":["man", "vrouw", "x"], 
        "handvoorkeur": ["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary = info, title = "Test4", order = ["naam", "leeftijd", "gender", "nummer", "handvoorkeur"])

if infoDlg.OK:
    print(info)
else:
    print('User cancelled')

## Naam opslaan voor welkomstbericht___________________________________________________
PPnaam = info["naam"]

# Opslaan data proefpersonen___________________________________________________________
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Pijltjes")
    Data = my_directory + "/Test4_subject_" + info["nummer"]
    if not os.path.isfile(Data+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Dit nummer is reeds in gebruik. Gelieve een uniek nummer in te geven.")
        myDlg2.show()
print("OK, let's get started!")

Exp4 = data.ExperimentHandler(dataFileName = Data)

# Initialiseren________________________________________________________________________
n_Blokken  = 12
My_Clock_RT = core.Clock()

# Importeren trials____________________________________________________________________
T4_Exp_Design = "ExperimentalDesign.xlsx"
T4_Trial_List = data.importConditions(T4_Exp_Design)

# Aanmaken stimuli_____________________________________________________________________
Welkom        = visual.TextStim(T4win, text = "Welkom {0}! Moest je vragen hebben tijdens het experiment, spreek dan zeker de begeleider aan. Druk op de spatie om verder te gaan.".format(PPnaam))
Instructies_O = visual.TextStim(T4win, text = "In dit blok zal je moeten reageren op de oriëntatie van het pijltje (>/<), onafhankelijk van de positie ervan. "+
                                               "Je zal moeten reageren aan de hand van de pijltjestoetsen op het toetsenbord. Druk op het rechter pijltje als "+
                                               "het pijltje op het scherm naar rechts is georiënteerd. Druk op het linker pijltje als het pijltje op het scherm "+
                                               "naar links is georiënteerd. Als je alles hebt begrepen, druk dan op de spatiebalk om te beginnen.")
Instructies_P = visual.TextStim(T4win, text = "In dit blok zal je moeten reageren op de positie van het pijltje (>/<) op het scherm. Druk op het rechter pijltje "+
                                               "als het pijltje op het scherm rechts staat, druk links als deze links op het scherm staat en druk naar beneden "+
                                               "als het pijltje in het midden van het scherm staat. Als je alles hebt begrepen, druk dan op de spatie om te beginnen.")
Afscheid      = visual.TextStim(T4win, text = "Bedankt {0} om deel te nemen aan dit experiment! Wij wensen u nog een prettige dag! Druk spatie om het experiment af te sluiten.".format(PPnaam))
Stimulus      = visual.TextStim(T4win, text = "<", pos = (0,0))


# Welkom________________________________________________________________________________
Welkom.draw()
T4win.flip()
event.waitKeys(keyList = "space")

# Instructies_O___________________________________________________________________________
Instructies_O.draw ()
T4win.flip()
event.waitKeys(keyList = "space")

# Pijltjes taak_________________________________________________________________________
event.clearEvents(eventType = "keyboard")

My_Clock_RT.reset()

Stimulus.draw()
T4win.flip()
k = event.waitKeys(keyList = ["right", "left"])
print(k)

RT = My_Clock_RT.getTime()
print(RT)

# Instructies_O___________________________________________________________________________
Instructies_O.draw ()
T4win.flip()
event.waitKeys(keyList = "space")

# Pijltjes taak_________________________________________________________________________
event.clearEvents(eventType = "keyboard")

My_Clock_RT.reset()

Stimulus.draw()
T4win.flip()
k = event.waitKeys(keyList = ["right", "left"])
print(k)

RT = My_Clock_RT.getTime()
print(RT)

# Instructies_P_________________________________________________________________________
Instructies_P.draw()
T4win.flip()
event.waitKeys(keyList = "space")

#Positie taak___________________________________________________________________________
event.clearEvents(eventType = "keyboard")

My_Clock_RT.reset()

Stimulus.draw()
T4win.flip()
k = event.waitKeys(keyList = ["right", "left", "down"])
print(k)

RT = My_Clock_RT.getTime()
print(RT)

# Afscheid nemen________________________________________________________________________
Afscheid.draw()
T4win.flip()
event.waitKeys(keyList = "space")

# Scherm afsluiten______________________________________________________________________
T4win.close()

##De 12 blokken en 60 trials ben ik niet aan geraakt, puur door het feit dta ik te weinig geoefend heb en dus heel traag heb gewerkt omdat ik het niet meer gewoon ben.
##Ik heb wel nog een ExperimentalDesign.xlsx aangemaakt die ik (als ik wat sneller kon werken) had gebruikt om alles rond mijn Trialhandler te programmeren. Ik stuur dat bestand gewoon mee.

























