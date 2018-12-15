# import modules
from psychopy import prefs
from psychopy import visual, event, core, sound, gui
import time, numpy, random

info = {"Participant number":0, "Participant name":"Unknown", "age":0, "gender": ["male", "female", "x"], "hand": ["right", "left","ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor experiment")

participantnr = info["Participant number"]
participant_name = info["Participant name"]
print(participantnr)
print(participant_name)

#Window

win = visual.Window(size=[600,500], units = "norm")

#Initializing
nblocks = 3
ntrials = 2            #########moet nog naar 8 gezet worden
key_list = ["f","j"]
spfr = ([2, 20])
orientatie  = ([30, -30])
my_clock = core.Clock()



#tijden Gabor Stimuli
gabortime = numpy.array([0.016, 0.033, 0.05])

#Welkom
def welkom():
    Welcome = visual.TextStim(win, text = "Hallo " + participant_name + ", welkom op het experiment. Druk spatie om verder te gaan")
    Welcome.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#Instructie
def instructie():
    instruction = visual.TextStim(win, text = "U dient op de f toets te drukken wanneer de Gabor naar links gedraaid is (de lijnen lopen van linksboven naar rechtsonder) en op de j toets wanneer de Gabor naar rechts gedraaid is (de lijnen lopen van rechtsboven naar linksonder). Druk spatie om door te gaan.")
    instruction.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    
#escape from experiment
#for key in ["escape"]:
#    event.globalKeys.add(key=key, func= core.quit)

#trialstart
def StartGabor():
    Gabor_stimulus1 = visual.GratingStim(win, tex = "sin", mask = "gauss", ori = 0)
    Gabor_stimulus1.draw()
    win.flip()
    core.wait(1)
    
#Gaborwacht
def Gaborwacht():
    Gabor_stimulus1 = visual.GratingStim(win, tex = "sin", mask = "gauss", ori = 0)
    Gabor_stimulus1.draw()
    win.flip()
    
    

#block
def block(): 
    ### Esther: zorg ervoor dat de proefpersoon altijd weet op welke knop te moeten drukken om verder te gaan
    blocknummer = visual.TextStim(win, text = "Je begint nu aan blok {0}".format(i+1))
    blocknummer.draw()
    win.flip()
    time.sleep(1)

#matrix
#correctresp= numpy.repeat(-99.99, ntrials)
#accuracy= numpy.repeat(-99.99, ntrials)
#resp = numpy.repeat(-99.99, ntrials)
#RT= numpy.repeat(-99.99, ntrials)

#matrix= numpy.column_stack([correctresp, accuracy, resp, RT])

#correcte respons
def correctresp(target = orientatie):
    if target == 30:
        correctresp = "j"
    else: 
        correctresp = "f"
    return correctresp
    
#feedback
def feedback_message():
    ### Esther: pas op, hier zal je moeten verwijzen naar k[0] in plaats van k
    if k == "j" and orientatie == 30:
        feedback = "Correct!"
        AC= 1
    else:
        feedback = "Verkeerd!"
        AC= 0
    ### Esther: pas op, deze tweede if...else zal de output van de eerste overschrijven
    if k == "f" and orientatie == -30:
        feedback = "Correct!"
        AC = 1
    else:
        feedback = "Verkeerd!"
        AC = 0
    feedback_text = visual.TextStim(win, text= feedback)
    feedback_text.draw()
    win.flip()
    core.wait(1)
    return AC 

#goodbye
def goodbye():
    dagtekst = visual.TextStim(win, text = "salukes")
    dagtekst.draw()
    win.flip()
    time.sleep(2)
    win.close()


RTlist = []
accuraatheid = []

#experiment
welkom()
instructie()

#blockdesign
for i in range(nblocks):
    block()
    for trial in range(ntrials):
        StartGabor()
        ### Esther: dit is niet het goede moment om de klok te resetten
        my_clock.reset()
        
        ### esther: door de random choice kan je niet garanderen dat elk trial type even frequent voorkomt
        spfr = random.choice([2, 20])
        orientatie = random.choice([30, -30])
        Gabor_stimulus2 = visual.GratingStim(win, tex = "sin", mask = "gauss", ori = orientatie, sf = spfr)
        Gabor_stimulus2.draw()
        win.flip()
        core.wait(gabortime[i])
        
        Gaborwacht()
        k = event.waitKeys(keyList = ["f","j"])
        
        RT = my_clock.getTime()
        #RT opslaan
        RTlist.append(RT)
        correctresp()
        feedback_message()
        #accuraatheid opslaan
        #accuraatheid.append(AC)
        print(RTlist)
        print(k)
goodbye()
## ik wil een matrix maken van de RT en de k maar de k lukte niet. de RT wel: matrix[trial, (kolom)] = RT





