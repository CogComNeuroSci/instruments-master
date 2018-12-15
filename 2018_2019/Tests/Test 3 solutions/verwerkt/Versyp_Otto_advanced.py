#Importeren van de nodige modules
from psychopy import visual,event,core,gui, logging
import time, numpy

#Maken van de GUI
info = {'Name':'', 'Participant':'2','Gender':['male', 'female','other'], 'Handedness':['left','right','ambidextrous']}
infoDlg = gui.DlgFromDict(dictionary=info, title='TEST 3')

#initialiseren van de nodige zaken en nagaan of er framedrops waren, 1/60 omdat mijn monitor 60 Hz is en +0.001 omdat er een tolerantie is voor 1 ms, in de trial functie heb ik een print() gebruikt die het totale aantal gedropte frames weergeeft
win=visual.Window(size=[600,500],units='norm')
win.recordFrameIntervals = True
win.refreshThreshold = 1/60 + 0.001
logging.console.setLevel(logging.WARNING)

#initialiseren twee verschillende gabor stimuli (een masking verticale en nadien de experimentele)
messageonscreen=visual.TextStim(win,text='')
normalestimulus=visual.GratingStim(win,tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=2, ori = 0)
anderestimulus=visual.GratingStim(win,tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=2, ori = 0)

instructie='Wanneer de "gabor" stimulus naar links is gedraaid dient u op de "f" toets te drukken. \n Wanneer deze naar rechts is gedraaid dient u de "j" toets in te drukken. \n Klik op de spatiebalk om verder te gaan.'
ntrials=8
nblocks=3

#info uit de GUI halen
naam=info['Name']
ppnummer=info['Participant']
geslacht="".join(info["Gender"])
hand="".join(info["Handedness"])

#arrays voor de variatie van de gabor stimulus, 24elk (8 per blok) en elke combinatie komt evenveel voor, voor de advanced versie heb ik ervoor gezorgd dat de grootte van de array afhankelijk is van de hoeveelheid trials en blocks
frequentie=numpy.repeat((2,20,2,20,2,20,2,20),(ntrials/8)*nblocks)
orientatie=numpy.repeat((30,-30,30,-30,30,-30,30,-30),(ntrials/8)*nblocks)
CorResp=numpy.repeat(("30","-30","30","-30","30","-30","30","-30"),(ntrials/8)*nblocks)

#aanmaken van arrays die later aangepast worden per trial
tijd=numpy.copy(frequentie)
reactietijd=numpy.repeat(-99.9,(nblocks*ntrials))
antwoord=numpy.repeat('x',(nblocks*ntrials))
accuracy=numpy.repeat(-1,(nblocks*ntrials))
#initialiseren van klok
clockie=core.Clock()

#omvormen naar array voor juiste responsen
CorResp[CorResp=="30"]="j"
CorResp[CorResp=="-30"]="f"

#informatie van pp
nummer=numpy.repeat(ppnummer,len(frequentie))
sex=numpy.repeat(geslacht,len(frequentie))
handig=numpy.repeat(hand,len(frequentie))

trials=numpy.column_stack([nummer,sex,handig,frequentie,orientatie,CorResp,tijd,reactietijd,antwoord,accuracy])


#functie voor het presenteren van berichten
def message(tekst='',duration=0,response_key='space'):
    messageonscreen.text=tekst
    
    messageonscreen.draw()
    win.flip()
    
    if duration==0:
        event.waitKeys(keyList=[response_key])
    else:
        time.sleep(duration)

#wist niet zeker of dit moest/mocht aangezien er ook geen practice trials waren maar ik dacht waarom niet
def stimulus_and_response(sf=frequentie,ori=orientatie):
    #spatiale frequente is gelijk bij standaard en experimentele stimulus
    normalestimulus.sf=sf[i]
    
    #orientatie verschilt tussen de stimuli
    anderestimulus.sf=sf[i]
    anderestimulus.ori=ori[i]
    #tekenen van de standaardstimulus
    normalestimulus.draw()
    win.flip()
    core.wait(1)
    
    #clearen van eventuele input in queue
    event.clearEvents(eventType = "keyboard")
    #bepalen van de tijd afhankelijk van het blok
    if (b+1)==1:
        tijd[i]=0.016
    elif (b+1)==2:
        tijd[i]=0.033
    elif (b+1)==3:
        tijd[i]=0.050
    
    #tekenen stimulus en resetten van klok nadat de stimulus op het scherm is verschenen
    anderestimulus.draw()
    win.flip()
    clockie.reset()
    #tijd is afhankelijk van blok, flippen zodat pp nog kan reageren nadat de stimulus is verdwenen
    core.wait(tijd[i])
    print('Overall, %i frames were dropped.' % win.nDroppedFrames)
    win.flip()
    
    keys = event.waitKeys(keyList = ["f","j","escape"])
    
    RT = clockie.getTime()
    #zorgen dat deze waardes terug bij het main script geraken
    return keys, RT

def feedback_message():
    #juiste antwoord & accuraatheid bepalen
    if antwoord[i]==CorResp[i]:
        message(tekst='Correct!', duration=1)
        trials[i,9]=1
    elif antwoord[i]!=CorResp[i]:
        message(tekst='Verkeerd antwoord!', duration=1)
        trials[i,9]=0


message(tekst='Welkom {0}. Druk op de spatiebalk om verder te gaan.'.format(naam))

message(tekst=instructie)

for b in range(nblocks):
    
    message(tekst='Welkom in blok {0}. \n Druk op de spatiebalk om te beginnen met het experiment.'.format(b+1))
    
    for i in range(b*ntrials,(b+1)*ntrials):
        #opvangen van de waardes uit de functie
        keys,RT=stimulus_and_response()
        
        #opslaan van de bekomen waardes en exit mogelijkheid
        if keys[0]=="escape":
            break
        
        trials[i,8]=keys[0]
        trials[i,7]=RT
        #functie voor feedback
        feedback_message()
    #afscheid mededeling en exit mogelijkheid
    if keys[0]=='escape':
        break
    if b==2:
        message(tekst="Dat was de laatste trial, bedankt voor je medewerking!")


print(trials)
