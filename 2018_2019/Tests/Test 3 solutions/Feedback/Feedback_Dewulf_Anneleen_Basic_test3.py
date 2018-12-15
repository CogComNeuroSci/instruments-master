#importing modules

import time,numpy,random
from psychopy import visual,event,core, gui

#gegeven
info={"proefpersoonnummer":0,"naam":"unknown","leeftijd":0,"gender":["man","vrouw","derde gender"],"handvoorkeur":["links","rechts","ambidexter"]}
box=gui.DlgFromDict(dictionary=info,title="stroopexperiment")
if box.OK:
    print(info)
else:
    print("participant cancelled")
mog_freq=(2,20)
mog_ori=(30,-30)
### Esther: pas op, als deze in milliseconden staan, zijn de stimuli 10 keer te lang
onsetdelay=(0.16,0.33,0.50) ##in milliseconden
nblocks=3
ntrials=8
naam=info["naam"]

#graphics
### Esther: pas op, dit zijn niet exact de dimensies die we gevraagd hadden!
win=visual.Window([600,400])
clock=core.Clock()
Grating = visual.GratingStim(win, mask = "circle", sf = 2,ori=0)
fixgrating=visual.GratingStim(win,mask="circle",ori=0)
Message=visual.TextStim(win,text="OK")

#intitializing variables die worden overgeschreven later in het experiment
### Esther: waarom deze initialiseren als een string?
frequenties=numpy.repeat("",ntrials)
orientaties=numpy.repeat("",ntrials)
RT=numpy.repeat(numpy.nan,ntrials)
CorResp=numpy.repeat(numpy.nan,ntrials)
Resp=numpy.repeat(numpy.nan,ntrials)
Accuracy=numpy.repeat(numpy.nan,ntrials)
    ##initializing participant variables --> 
    ##dit is een advanced opdracht, maar dit had ik te laat door.Ik heb dan ook geen apart advancedscript meer kunnen aanmaken
### Esther: de naam van de proefpersoon niet opslaan in de trial matrix!
naam= numpy.repeat(info["naam"],len(CorResp))
### ESther: pas op, hier sla je een tweede keer de naam op in plaats van het proefpersoonnummer
ppnummer = numpy.repeat(info["naam"],len(CorResp))
leeftijd = numpy.repeat(info["leeftijd"],len(CorResp))
gender=numpy.repeat("".join(info["gender"]),len(CorResp))
handvoorkeur=numpy.repeat("".join(info["handvoorkeur"]),len(CorResp))

#matrix vormen en zorgen dat deze herhaald wordt gedurende het aantal blokken
### Esther: de naam van de proefpersoon niet opslaan in de trial matrix!
trials=numpy.column_stack([frequenties,orientaties,Resp,CorResp,RT,Accuracy,naam,ppnummer,leeftijd,gender,handvoorkeur])
trials=numpy.tile(trials,(nblocks,1))

### Esther:
print(trials)

#defining

def message(text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    Message.text    = text
    Message.height  = height
    Message.pos     = pos
    Message.color   = color
    
    Message.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

def perform_trial():
    
    ### Esther: dit is een beter moment om het keyboard te clearen
    
    ##zorgen dat stimulus op scherm komt
    grating.draw()
    win.flip()
    
    ##clock resetten
    clock.reset()
    
    ### Esther: dit is niet het beste moment om het keyboard te clearen
    ##enkel keyboard instructies goedkeuren
    event.clearEvents(eventType="keyboard")
    
    ### Esther: dit is geen goede optie om de stimulus presentatietijd te regelen
    ##mogelijke keys aanduiden
    keys=event.waitKeys(keyList=["f","j","escape"],maxWait=onsetdelay[b])
    
    ### Esther: pas op, dit is niet de RT!
    ##tijd meten
    RT=clock.getTime()
    
    ### Esther: deze mask moet sowieso getoond worden, die is niet optioneel
    if keys==None:
        fixgrating.draw()
        win.flip()
        keys=event.waitKeys(keyList=["f","j","escape"])
    
    return keys,onsetdelay,RT

def correct_response(target="x"):
    if target==-30:
        CorResp="f"
    elif target==30:
        CorResp="j"
    return CorResp

def feedback_message(correct=99):
    if correct==1:
        message(text="Correct",duration=0.25)
    if correct==0:
        message(text="Verkeerd antwoord",duration=0.25)


#exeriment
##welcome
message(text="Welkom {0}! Druk op de spatiebalk om door te gaan".format(info["naam"]),response_key="space")

##instructies
message(text="Als de Gaborstimulus links gedraaid is, druk dan'F'; als de Gaborstimulus rechts gedraaid is, druk dan'J'. \n Druk nu spatiebalk om door te gaan naar het experiment")

##blockdesign
for b in range(nblocks):
    message(text="Dit is de start van blok" +str(b+1)+"Druk op spatiebalk om verder te gaan",response_key="space")
    
    for i in range(b*ntrials,(b+1)*ntrials):
        fixgrating.draw()
        win.flip()
        time.sleep(1)
        
        ### Esther: de bedoelding was hier om de eigenschappen te kruisen in plaats van at random bepalen
        frequentie=random.choice(mog_freq)
        orientatie=random.choice(mog_ori)
        
        
        grating=visual.GratingStim(win,mask="circle",ori=orientatie, sf= frequentie)
        trials[i,0]=frequentie
        trials[i,1]=orientatie
        
        
        keys,onsetdelay,RT=perform_trial()
        
        ### Esther: pas op, je slaat hier ook de data op wanneer er op escape wordt geduwd
        if keys[0]!=0:
            ##verschillende variabelen opslaan in matrix
            trials[i,2]=keys[0]
            trials[i,4]=RT
            trials[i,3]=correct_response(target=orientatie)
            trials[i,5]=int(trials[i,2]==trials[i,3])
            
            ##feedback presenteren
            feedback_message(correct=int(trials[i,5]))
        ## uit de trial loop ontsnappen
        if keys[0] == "escape":
            break
            
    ### Esther: hier moet je ook nog uit de block-loop breken
    
#Goodbye
message(text="Hartelijk bedankt! Druk op de spatiebalk op het experiment te verlaten",response_key="space")
print(trials)


