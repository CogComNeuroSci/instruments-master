# importeren modules
from psychopy import visual, event, core, gui
import time, numpy

# dialoog box aanmaken
info = {"Naam participant": "Unknown", "Nummer participant":0, "Leeftijd":0, "Gender": ["man", "vrouw", "derde gender"], "Handvoorkeur": ["rechts", "links", "ambidexter"]}
box = gui.DlgFromDict(info)
if box.OK:
    print(info)

# window aanmaken
win = visual.Window(size = [600,500], units = "norm")

# klok maken
klok = core.Clock()

# de variabelen
nblocks        = 3
ntrials        = 8
orientatielist = (33, 330)
participant    = info["Nummer participant"]

# oriëntatie en Hz 
### Esther: waarom alles in 1 string steken? Idem voor de Hz?
Oriëntatie = numpy.array([ "30, 30, 30, 30, 330, 330, 330, 330"])
### ESther: je had hier een typo: een o versus een 0
Hz         = numpy.array([ "2, 20, 2, 20, 2, 2O, 2, 20"])

# arrays aanmaken
Trialnummer    = numpy.repeat("-99", ntrials)
Accuraatheid   = numpy.repeat(0, ntrials)
CorResp        = numpy.repeat("0", ntrials)
Resp           = numpy.repeat("0", ntrials)
Reactietijd    = numpy.repeat(-99, ntrials)
Oriëntatie     = numpy.repeat("-99", ntrials)

trials = numpy.column_stack([Trialnummer, CorResp, Resp, Accuraatheid, Reactietijd, Oriëntatie])
trials = numpy.tile(trials, (nblocks,1))

# de teksten aanmaken
Welkom = visual.TextStim(win, text = "Welkom " + info["Naam participant"] + "!\n\nDruk op de spatiebalk om verder te gaan")
Instructies = visual.TextStim(win, text = "Dit experiment bestaat uit 3 blokken waarin u telkens een stimulus aangeboden gaat krijgen. Het is uw taak om aan te geven of deze naar links of rechts gedraaid is. \n\nAls deze naar links gedraaid is, drukt u op f. Als deze naar rechts gedraaid is, drukt u op j \n\nDruk op de spatiebalk om verder te gaan.")
Aankondiging1 = visual.TextStim(win, text = "Druk op de spatiebalk om aan het eerste blok te beginnen")
Aankondiging2 = visual.TextStim(win, text = "Druk op de spatiebalk om aan het tweede blok te beginnen")
Aankondiging3 = visual.TextStim(win, text = "Druk op de spatiebalk om aan het derde blok te beginnen")
Afscheid = visual.TextStim(win, text = "Bedankt! \n\nDruk op de spatiebalk om het experiment af te sluiten")
Block_start = visual.TextStim(win, text = 'ok')

# stimuli aanmaken
### Esther : dit is wel een grating, maar nog niet helemaal een Gabor
Gabor1 = visual.GratingStim(win)
GaborRechts = visual.GratingStim(win, ori = 30)
GaborLinks = visual.GratingStim(win, ori = 330)

# Gabors aanmaken
GaborOnScreen = visual.GratingStim(win)
def gabor(response_key = "space", duration = 0, ori = 0, sf = 0):
    
    GaborOnScreen.ori      = ori 
    
    ### Esther: .duration bestaat niet bij een GratingStim
    GaborOnScreen.duration = duration
    
    GaborOnScreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        ### Esther: core.wait!
        time.sleep(duration)

# een functie maken van een trail ook al is dit waarschijnlijk tijdverspilling
def performtrail():
    
    # beginnen met de verticale gabor die 1 seconde moet blijven
    gabor(duration = 1, ori = 0)
    
    
## ik heb gebprobeerd maar zit hier vast

# welkom tonen
Welkom.draw()
win.flip()
### Esther: "space" hoeft niet tot een lijst omgevormd te worden 
event.waitKeys(keyList = ["space"])

# instructies tonen
Instructies.draw()
win.flip()
event.waitKeys(keyList = ["space"])

# stimuli tonen
for b in range(nblocks):
    
    # aankondiging van de blokken
    Block_start.text = "Blok " + str(b+1) + " zal beginnen wanneer u op de spatiebalk drukt"
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    for i in range(b*ntrials, (b+1)*ntrials):
        
        gabor(duration = 1, ori = 0)
        
        
        keys = event.waitKeys(keyList = ["f","j","escape"])
        
        # escape 
        if keys[0] == "escape":
            break
    
    if keys [0] == "escape":
        break 
## Ik heb weer geprobeerd maar zat weer vast, het lukt me maar niet om de stimulus te doen stoppen na 1 seconde, de enige manier dat die weggaat is door escape

# afscheid tonen
Afscheid.draw()
win.flip()
event.waitKeys(keyList = ["space"])