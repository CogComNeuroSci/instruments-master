'''basic test 3 IEP, Remy Verdin'''
#import modules
from psychopy import visual, event, core, gui
import time, numpy, random

# initialize the window
win = visual.Window([600, 500], units = "norm")

#initialize the gui box
info = {'Participant nummer': 0, 'Naam': 'unknown', 'Leeftijd': 0, 'Gender': ["male", "female", "non binary"], 'Handvoorkeur': ["rechts", "links", "ambidexter"] }
dlg = gui.DlgFromDict(dictionary= info,title="Participant info", pos=(200, 400))
thisInfo = dlg
naam = info['Naam']

#initialize some stimuli
say_hello =  visual.TextStim(win, text='Welkom {0}! :-) Druk op spatie om door te gaan,'.format(naam.capitalize()))
instr_text = visual.TextStim(win, text='Het is de bedoeling dat je links (op f) drukt als de Gabor naar links gedraaid is.Wanneer de gabor naar rechts gedraaid is druk je rechts (op j). Het experiment bestaat uit 3 blokken.Druk weer op spatie om verder te gaan' )
byebye = visual.TextStim(win, text='Bedankt voor je deelname. Roep de proefleider!')


#functie voor gui box
def gui_box():
    if dlg.OK:
        printstatement = print(info)
    else:
        printstatement = print('User Cancelled')
    return printstatement

#functie voor startscherm
def begroeting():
    say_hello.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#functie voor instructies
def instr():
    instr_text.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#functie voor start van blok
def start_blok():
    blokn_text = visual.TextStim(win, text='Blok {0} begint. Druk op spatie om verder te gaan'.format(bloknummer+1))
    blokn_text.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

#functie om links of rechts georienteerde gabor te kiezen
def kiesLofR():
    Gabor = random.choice([LeftGabor],[RightGabor])
    return Gabor

#functie voor afscheidsscherm
def afscheid():
    byebye.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    win.close()

#functie voor accuraatheid te berekenen
def AccuracyCheck():
    if (orientatie == 30 and k[0] == 'j') or (orientatie == -30 and k[0] == 'f'):
        AC= 1
    elif (orientatie == 30 and k[0] == 'f') or (orientatie == -30 and k[0] == 'j'):
        AC= 0
    return AC

#functie voor feedback
def feedback_message(Accuracy):
    if Accuracy == 1:
        feedback = 'Correct!'
    else:
        feedback= 'Verkeerd antwoord!'
    feedback_text = visual.TextStim(win, text= feedback)
    feedback_text.draw()
    win.flip()
    core.wait(1)


#
blokken = 3
trials = 8
aanbieding = [0.016, 0.033, 0.05]
Lorientatie= [30,-30,30,-30,30,-30,30,-30]
Lspfr=[(20,0),(20,0),(2,0),(2,0),(20,0),(20,0),(2,0),(2,0)]
RTList = [ ]
RespList = [ ]
checkList = [ ]

#initialize clock
my_clock = core.Clock()

#structuur van het experiment zelf
gui_box()
begroeting()
for bloknummer in range(blokken):
    start_blok()
    for trialnummer in range(trials):
        spfr = Lspfr[trialnummer]
        VertGabor = visual.GratingStim(win,tex='sin', mask='gauss',size=(1.0, 1.0), sf= spfr, ori = 0)
        VertGabor.draw()
        win.flip()
        core.wait(1)
        orientatie = Lorientatie[trialnummer]
        AGabor = visual.GratingStim(win,tex='sin', mask='gauss',size=(1.0, 1.0), sf=spfr, ori= orientatie )
        AGabor.draw()
        win.flip()
        my_clock.reset()
        core.wait(aanbieding[bloknummer])
        check = my_clock.getTime()
        VertGabor.draw()
        win.flip()
        ### ESther: dit is het moment om de check te meten
        
        ### ESther: het is geen goed idee om hier de klok te resetten
        my_clock.reset()
        k = event.waitKeys(keyList=['f','j','escape'])
        
        ### Esther: dit is het goede moment om al uit je trial loop te ontsnappen
        
        RT = my_clock.getTime()
        
        RTList.append(RT)
        RespList.append(k[0])
        checkList.append(check)
        
        Accuracy = AccuracyCheck()
        feedback_message(Accuracy)
    if k[0] == "escape":
        break
afscheid()
print(RTList)
print(RespList)
print(checkList)