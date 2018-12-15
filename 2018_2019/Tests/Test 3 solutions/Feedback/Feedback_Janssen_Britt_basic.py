# importeren van  modules
from psychopy import visual, event, core, gui
import time, numpy


# een window maken
win = visual.Window(size=[600,500], units = 'norm')


# een toets om uit het volledige experiment te geraken
for key in ['q']:
    event.globalKeys.add(key, func=core.quit)
    ##in case something somewhere goes wrong



nblocks = 3
ntrials = 8

## een klok installeren
my_clock = core.Clock()
my_clock2 = core.Clock()


# definities

## een dialogbox
def dialog_box():
    info = {"Participant naam":"", "Participant nummer":0, "Leeftijd":0, "Geslacht":["male", "female"], "Handvoorkeur":["Links", "Rechts", "Ambidexter"]}
    infoDlg = gui.DlgFromDict(dictionary=info, title="Simon taak")
    if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
        print(info)
    else:
        print("User Cancelled")
    
    participant_naam = info["Participant naam"]
    participant_nummer = info["Participant nummer"]
    participant_leeftijd = info["Leeftijd"]
    participant_geslacht = info["Geslacht"]
    participant_handvoorkeur = info["Handvoorkeur"]
    return participant_naam, participant_nummer, participant_leeftijd, participant_geslacht, participant_handvoorkeur


## een text definitie
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    MessageOnSCreen = visual.TextStim(win, text = "OK")
    
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    MessageOnSCreen.color   = color
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

def feedback_message(correct = -99):
    if correct == 1:
        message(message_text = "Correct!", duration = 1)
    else:
        message(message_text = "Verkeerd antwoord!", duration = 1)


# veranderbare waarden

## een array maken die de tijden van de target gabor weergeeft
tijd_gabor = numpy.array([0.016, 0.033, 0.050])

## een array maken die de oriëntatie van de target gabor weergeeft
ori_gabor = numpy.array([30.0, 30.0, 30.0, 30.0, -30.0, -30.0, -30.0, -30.0])

## een array maken die de spatiale frequentie van de target gabor weergeeft
sf_gabor = numpy.array([2, 2, 20, 20, 2, 2, 20, 20])

ori = numpy.repeat(-99.9, ntrials)
Sf = numpy.repeat(-44.4, ntrials)
tijd = numpy.repeat(-88.8, ntrials)
CorResp = numpy.repeat("", ntrials)
Resp = numpy.repeat("", ntrials)
RT = numpy.repeat(-55.5, ntrials)
Accuracy = numpy.repeat(-33.3, ntrials)
tijd_echt = numpy.repeat(-22.2, ntrials)

# onvernderbare waarden

instructies = "In dit experiment heb je de uitdaging om de oriëntatie van een Gabor te schatten: \n\nDeze is lichtjes naar links of lichtjes naar rechts gedraaid.\n\nHet zal echter moeilijk te onderscheiden zijn, want \n\n(1) hij wordt maar kort aangeboden en \n\n(2) hij wort voorafgegaan door een maskerende Gabor met een verticale oriëntatie. \n\nDruk op spatie om verder te gaan"
instructies2 = "Als de Gabor naar links georiënteerd is (de lijnen lopen van linksboven naar rechtsonder), druk dan op de f-toets. \n\nAls de Gabor naar rechts georiënteerd is (de lijnen lopen van rechtsboven naar linksonder), druk dan op de j-toets.\n\nDruk op spatie om verder te gaan."

## sf geeft het aantal lijntjes weer! 
gabor_mask = visual.GratingStim(win, tex='sin', ori=0.0, phase=(0.0, 0.0),  mask='gauss', sf = 5)
gabor_target = visual.GratingStim(win, tex='sin', ori=2.0, phase=(0.0, 0.0),  mask='gauss', sf = 5)



## een array maken van alles wat we willen opslaan
trials = numpy.column_stack([ori, Sf, tijd, CorResp, Resp, RT, Accuracy, tijd_echt])

## omdat er 3 blokken zijn
trials = numpy.tile(trials, (nblocks, 1))

# uitvoeren experiment

## de dialog box tonen
participant_naam, participant_nummer, participant_leeftijd, participant_geslacht, participant_handvoorkeur = dialog_box()

## de welcom-tekst tonen
message(message_text = "Welkom " + participant_naam + "!\n\nDruk op spatie om verder te gaan.", response_key  = "space")

## de instructies tonen
message(message_text = instructies, response_key  = "space", height = 0.07)
message(message_text = instructies2, response_key  = "space", height = 0.07)



## de loops
for i in range(nblocks):
    ## aankondiging van bloknummer
    
    ### Esther: zorg ervoor dat de proefpersonen altijd weten op welke toets ze moeten drukken om verder te gaan
    message(message_text = "Blok " + str(i+1) + " gaat nu beginnen", response_key  = "space")

    for n in range(i*ntrials,(i+1)*ntrials):
        p = 0
        

        ## de maskerende gabor tekenen
        gabor_mask.draw()
        win.flip()
        core.wait(1)
        
        ## werkt nog niet, hij blijft bij dezelfde orientatie en dezelfde Sf :((((
        gabor_target.ori = ori_gabor[p]
        gabor_target.sf = Sf[p]
        
        ## de target gabor tekenen
        gabor_target.draw()
        
        ### Esther: dit is het beste moment om het keyboard te resetten
        
        win.flip()
        
        my_clock2.reset()
        ## i want we willen de tijd doen variëren per blok en niet per trial (n)
        core.wait(tijd_gabor[i])
        
        tijd_stim_echt = my_clock2.getTime()
        

        ## de maskerende gabor tekenen
        gabor_mask.draw()
        
        event.clearEvents(eventType = "keyboard")
        
        win.flip()
        
        ### Esther: dit is een beter moment om de presentatietijd te meten
        
        ### Esther: dit is niet het goede moment om de RT klok te resetten
        my_clock.reset()

        keys = event.waitKeys(keyList = ["f","j", "escape"])
        
        if keys[0] == "escape":
            break

        ## als er niet wordt geantwoord komt er een N te staan in de tabel
        if keys == None:
            keys = 'N'
        print(keys)
        
        RT = my_clock.getTime()
        
        ## bepalen van de juiste respons
        if ori_gabor[p] == 30.0:
            CorResp = "j"
        else:
            CorResp = "f"
    
        
        trials[n,5] = round(RT,4)
        trials[n,0] = round(ori_gabor[p],2)
        trials[n,2] = round(tijd_gabor[i],4)
        trials[n,3] = CorResp
        trials[n,1] = sf_gabor[p]
        
        if keys == 'N':
            ## als je niet reageert, wordt er bij de Resp een N gezet
            trials[n,4] = 'N'
        else:
            trials[n,4] = keys[0]
        
        if trials[n,3] == trials[n,4]:
            ## Accuracy wordt 1
            trials[n,6] = 1
        else:
            ## Accuracy wordt 0
            trials[n,6] = 0
        
        feedback_message(correct = int(trials[n,6]))
        
        ## verifiëren of de stim inderdaad de gewenste periode op het scherm stond
        print(tijd_stim_echt)
        trial[n,7] = tijd_stim_echt]
        p = p+1

    ### Esther: vergeet ook niet hier uit de blok loop te breaken




## Afscheid nemen na laatste trial
message(message_text = "Dit was de laatste trial, hartelijk dank voor uw medewerking.", response_key  = "space")


# Aflsuiten programma
print(trials)

win.close()