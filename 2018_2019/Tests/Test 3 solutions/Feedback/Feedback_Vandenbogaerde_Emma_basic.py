# modules importeren
from psychopy import gui, visual, core, event
import time

# Registreren van proefpersoon 

### Esther: het is nog beter om numerische eigenschappen ook te initializeren als nummers
info = {"Naam":"Unknown", "Proefpersoonnummer": "Unknown", "Leeftijd": "Unknown", "Gender": ["man", "vrouw", "derde gender"], "Handvoorkeur": ["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary = info, title = "Gabor Experiment")

naam = info["Naam"]
proefpersoonnummer = info["Proefpersoonnummer"]
leeftijd = info["Leeftijd"]
gender = "".join(info["Gender"])
handvoorkeur = "".join(info["Handvoorkeur"]

# window maken 
win = visual.Window([600,500], units = "norm")

#variabelen
nblocks = 3
ntrials = 8

# klok om reactietijd te meten 
clock = core.Clock()

#gabor stimuli
gabor_verticaal = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')

gabor_rechts = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 30, name='gabor1')

gabor_links = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 330, name='gabor1')

#instructies
instructies = visual.TextStim(win, text = "Als de lijnen naar rechts zijn gedraaid, druk 'j'. Als de lijnen naar links zijn gedraaid, druk'f'. \n Druk spatie om het experiment te starten.")

#welkom
name = info["Naam"]
def greeting(name):
    greeting_string = "Welkom " + name + "! " + "Druk spatie om het experiment te starten"
    return greeting_string

### Esther: misschien wat overkill om hier een functie voor te maken...
welkom = visual.TextStim( win, text = greeting(name))
welkom.draw() 
win.flip()
### Esther: "space" hoeft niet tot een lijst omgevormd te worden 
event.waitKeys(keylist = ["space"])

#blok 1: 16 miliseconden

#instructies
instructies.draw()
win.flip()
event.waitKeys(keylist = ["space"])
#stimuli

#block 2: 33 miliseconden

#instructies
instructies.draw()
win.flip()
event.waitKeys(keylist = ["space"])
#stimuli 

#block 3: 50 miliseconden 

#instucties
instructies.draw()
win.flip()
event.waitKeys(keylist = ["space"])
#stimuli

#afscheid
afscheid = visual.TextStim(win, text = "Bedankt voor jouw deelname! Druk spatie om het experiment te eindigen")
afscheid.draw()
win.flip()
event.waitKeys(keylist = ["space"])

