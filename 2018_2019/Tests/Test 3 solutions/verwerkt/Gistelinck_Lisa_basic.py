#Het experiment kan runnen, maar bepaalde elementen moet ik nog aanpassen aan de criteria (deze staan met # genoteerd)
# modules importeren
from psychopy import visual, event, core, gui
import time, numpy,random

# dialoog box aanmaken
info = {"Participant nummer":0, "Participant naam":"Onbekend", "Geslacht":["man", "vrouw","neutraal"], "leeftijd":0,"handvoorkeur":["links","rechts","ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Stroop Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

#window aanmaken
win=visual.Window(size=[600,500],units='norm')

#variabelen aanmaken en definiëren
nblocks          =3
my_clock         =core.Clock()
gabor            =visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')
gabor1           =visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')
ntrials          =8
display_tijd     =numpy.array([16,33,50])
oriëntatie       =numpy.array([-30,30])
spatiale_frequ   =numpy.array([2,20])

# maak er arrays van
Trialnummer       = numpy.repeat("-99", ntrials)
Accuraatheid      = numpy.repeat(0, ntrials)
CorResp           = numpy.repeat("0", ntrials)
Resp              = numpy.repeat("0", ntrials)
Reactietijd       = numpy.repeat(-99, ntrials)
oriëntatie_1      = numpy.repeat('0',ntrials)
spatiale_frequ_1  = numpy.repeat(0,ntrials)

#samen stockeren
trials = numpy.column_stack([Trialnummer, CorResp, Resp, Accuraatheid,Reactietijd,oriëntatie_1,spatiale_frequ_1])
trials = numpy.tile(trials, (nblocks,1))

#functies gaan definiëren
MessageOnSCreen = visual.TextStim(win, text = "OK")
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
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
        
def correcte_respons():
    if oriëntatie=='-30':
        CorResp='f'
    elif oriëntatie=='30':
        CorResp='j'
    return CorResp
    
def feedback_message():
    if keys[0] != 0:  
        if trials[i, 1] == trials[i, 2]: ##als resp = corresp
            message(message_text = "Goed!", duration = 0.5)
            trials[i, 3] = 1
        else:
            message(message_text = "Fout!", duration = 0.5)
            trials[i, 3] = 0


#de persoon welkom heten
message(message_text = "Welkom " + info["Participant naam"] + "!\n\nDruk op de spatie om door te gaan.", response_key = "space")

#instructies
message(message_text = "Druk op de f-toets als de Gabor naar links gedraaid is, hier zullen de lijnen van linksboven naar rechtsonder lope; \nals het naar rechts gedraaid is, met de lijnen van rechtsboven naar linksonder, druk de j-toets in. Druk op spatie om verder te gaan", response_key = "space")

#de blockloop starten
for b in range(nblocks):
    
    # zeggen welk block er zal starten
    message(message_text = "Block " + str(b+1) + " zal starten wanneer je op spatie drukt.", response_key = "space")
    
    # in 3 trials
    for i in range(b*ntrials,(b+1)*ntrials):
        
        ##eerst trialnummer noteren
        trials[i,0] = i
        
        ##elke trial laat je starten met een Gabor stimulus-verticale orientatie
        gabor1.draw()
        win.flip()
        time.sleep(1)
        
        ##hier moet de gabor gepresenteerd worden met variabele oriëntatie en spatiale_freque MAAR per blok staat de core.wait() gelijk aan een vaste variabele die hij uit een array moet halen
        oriëntatie_1= random.choice(oriëntatie)
        gabor.ori = oriëntatie_1
        trials[i, 5] = oriëntatie_1
        
        ##hier wou ik een random choice geven voor de spatiale frequentie
        ##zet ik achter een comment omdat deze ook foutmelding gaf
        #spatiale_frequ_1 = (random.choice([spatiale_frequ, 0]))
        #gabor.sf = spatiale_frequ_1
        #trials[i, 6] = spatiale_frequ_1
        
        gabor.draw()
        win.flip()
        core.wait(0.55)#hier zou ik 'display_tijd[i]' zetten, maar er is foutmelding
        
        ##keyboard cleanen
        event.clearEvents(eventType='keyboard')
        
        ##terug de verticale gabor tonen
        gabor1.draw()
        win.flip()
        
        ##de klok aanzetten
        my_clock.reset()
        
        ##wachten op het antwoord
        keys=event.waitKeys(keyList = ["j", "f"])
        
        ##escapen uit de trial loop
        if keys[0] == "escape":
            break
            
        ##RT opslaan
        RT=my_clock.getTime()
        
        ##opslaan van de antwoorden
        trials[i,2] = keys[0]
        trials[i,4] = round(RT, 3)
        
        ##feeback geven
        feedback_message()
    
    # als je uit de block wilt escapen
    if keys[0] == "escape":
        break


# salut zeggen tegen de persoon (deze moet uit de loop)
message(message_text = "Bedankt en tot ziens!", duration = 1, pos = (0,0.50), height = 0.1)

# experiment volledig sluiten
win.close()