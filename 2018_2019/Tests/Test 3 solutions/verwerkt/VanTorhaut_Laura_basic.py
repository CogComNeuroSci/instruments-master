# importeren van de modules
from psychopy import visual, event, core, gui
import time, numpy

# verschillende variablen
n_blokken = 3
n_trials= 8

# aanmaken van de stimuli
## in totaal zijn 4 stimuli mogelijk: 30° naar links (ori = 330) + 2Hz, 30° naar links (ori = 330+ 20Hz, 30° naar rechts (ori = 30) en 2 Hz + 30° naar rechts (ori = 30) en 20 Hz
oriëntatie = numpy.array ([30, 30, 330, 330, 30, 30, 330, 330])
spat_frequentie = numpy.array ([2, 2, 20, 20, 2, 2, 20, 20])
## de aanbiedtijd per blok
###aanbiedtijd = numpy.array([0.16, 0.33,0.5])

# correct antwoord bepalen
##cor_resp = numpy.copy (oriëntatie)
##cor_resp [cor_resp == 30] = "j"
##cor_resp [cor_resp == 330] = "f"

# feedback definiëren
##def feedback_message ():
    ##if keys == cor_resp:
        ##feedbackcorrect = visual.TextStim (win, text = "Correct!")
        ##feedbackcorrect.draw ()
        ##win.flip ()
        ##time.sleep (1)
    ##else:
        ##feedbackfout = visual.TextStim (win, text = "Verkeerd antwoord!")
        ##feedbackfout.draw ()
        ##win.flip ()
        ##time.sleep (1)

# aanmaken van een dialoogvenster
info = {"Naam proefpersoon": " ", "Proefpersoonnummer": 0, "Leeftijd": 0, "Gender": [ "man", "vrouw", "derde gender"], "Handvoorkeur": [ "links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabortaak")
if infoDlg.OK:
    print(info)
else:
    print("User Cancelled")

# aanmaken van een window
win = visual.Window (size =(600, 500), units = 'norm')

# welkom proefpersonen
welkom = visual.TextStim (win, text = "Welkom " + info["Naam proefpersoon"] + "!\nDruk op spatie om verder te gaan.")
welkom.draw ()
win.flip ()
event.waitKeys(keyList = ["space"])

# instructies
instructietekst = ("In het volgende experiment worden er Gabor stimuli gebruikt.\nHet is de bedoeling dat je de oriëntatie van de stimulus bepaald\n" +
                    "Je dient op de f-toets te drukken wanneer de Gabor naar links gedraaid is\n(de lijnen lopen van linksboven naar rechtsonder)\n"+
                    "en je drukt op de j-toets wanneer de Gabor naar rechts gedraaid is\n(de lijnen lopen van rechtsboven naar linksonder).\n"+
                    "Druk op spatie om verder te gaan.")
Instructie = visual.TextStim (win, text = instructietekst, height = 0.05)
Instructie.draw ()
win.flip ()
event.waitKeys(keyList = ["space"])

# klok aanmaken
mijn_klok = core.Clock()

# blockloop: 3 blokken met afwisselende aanbiedtijd
#for aanbiedtijd in range (n_blokken):
    #Startblok = "Blok " + str(b+1) + " start als je op spatie duwt."
    #Startblok.draw()
    #win.flip()
    #event.waitKeys(keyList = ["space"])

# trailloop deze loop moet je in de blokloop zetten en dan moet je core.wait () aanpassen
for i in range (n_trials):
    ## gemaskeerde gabor voor 1 seconde tonen, maar blijft op het scherm staan, maar je kan wel antwoorden geven.
    gabor1 = visual.GratingStim (win, mask = "circle", ori = 0)
    gabor1.draw ()
    win.flip ()
    time.sleep (1)
    ## doelstimulus 16 ms tonen. Deze is niet zichtbaar op het scherm.
    stimulus = visual.GratingStim (win, mask = "circle", ori = oriëntatie [i], sf = spat_frequentie [i])
    stimulus.draw ()
    mijn_klok.reset()
    win.flip
    core.wait (0.16)
    ## 2de gemaskeerde gabor tonen totdat antwoord is gegeven
    gabor2 = visual.GratingStim (win, mask = "circle", ori = 0)
    gabor2.draw ()
    keys = event.waitKeys (keyList = ["f", "j", "escape"])
    RT = mijn_klok.getTime()
    print (keys)
    print (RT)
    if keys[0] == "escape": ## om uit de trailloop te gaan
        break
    win.flip ()
    # feedback geven door eerder gedefinïeerde feedback_message ()
    ##feedback_message ()

# aan elkaar plakken van de trails
trials = numpy.column_stack([oriëntatie, spat_frequentie]) ## hier kan je cor_resp, RT en keys nog aan toevoegen om het juiste antwoord, de reactietijd en het gegeven antwoord in de matrix te krijgen
print (trials)

# einde
einde = visual.TextStim (win, text = "Bedankt voor je deelname!")
einde.draw ()
win.flip ()
time.sleep (1)