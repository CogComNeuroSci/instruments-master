### Esther: hier ben je vergeten om de library van de gui in te laden
from psychopy import visual, event, core
import time 


win = visual.Window([600,500], units = 'norm')

# Gegevens

expName = 'participant'
### Esther: het is nog beter om numerische eigenschappen ook te initializeren als nummers
### Esther: het is beter om de response opties voor gender en handvoorkeur ook echt te presenteren als respons opties in plaats van enkel een suggestie
expInfo = {'voornaam': '', 'achternaam': '', 'proefpersoonnummer': '','leeftijd': '', 'gender': 'man, vrouw, derde gender', 'handvoorkeur': 'links, rechts of ambidexter'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName



# Groeten

verwelkoming = "Welkom {0}".format(voornaam)
Groet = visual.TextStim(win, text = verwelkoming, color = (1,0,0))

# Instructies

Instructies = visual.TextStim(win, text = "Je krijgt telkens een Gabor te zien. Als de Gabor naar links gedraaid is druk je de f toets, als de Gabor naar rechts gedraaid is druk je de j toets.", color = (1,0,0))


# Gabors

gabor1 = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.0, 1.0], sf = [4, 0], ori = 0)

gabor2 = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.0, 1.0], sf = [4, 0], ori = 30)

gabor3 = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.0, 1.0], sf = [4, 0], ori = -30)

# Afscheid

Salut = visual.TextStim(win, text = "Bedankt voor je deelname!", color = (1,0,0))


# Toetsen

TekstSpatie = visual.TextStim(win, text = "Druk spatie om verder te gaan.", pos = (0.0, -0.9), color = (1,0,0))

StimuliResp = event.getKeys("f", "j")

thisExp.addData('StimuliResp.RT in ms', StimuliResp.rt * 1000)

# Tijden

Tijden = [16, 33, 50]





# Response tijd nakijken


my_clock1 = core.Clock()
my_clock2 = core.Clock()
my_clock3 = core.Clock()


for trial in range(3):
    
    my_clock1.reset()
    
    gabor2.draw()
    
    event.clearEvents(eventType = "f","j")
    
    my_clock2.reset()
    
    win.flip()
    
    my_clock3.reset()
    
    keys = event.waitKeys()
    RT1 = my_clock1.getTime() * 1000
    RT2 = my_clock2.getTime() * 1000
    RT3 = my_clock3.getTime() * 1000
    
    print("Your RT is not {0} ms, nor {1} ms; it's {2} ms"  
              .format(round(RT1,1),round(RT2,1),round(RT3,1)))
    print("The measurement error is either {0} ms, or {1} ms" 
              .format(round(RT1-RT3,1),round(RT2-RT3,1)))


# Correct response

feedback_message = 

if not key_resp.keys :
    msg="Verkeerd antwoord!"
else:
    msg="Correct!"



# Draws

win.flip()
while win.flip():
    Groet.draw() 
    TekstSpatie.draw()
    if event.getKeys(keyList = 'space'):
        win.close()


win.flip()
while win.flip():
    Instructies.draw()
    TekstSpatie.draw()
    if event.getKeys(keyList = 'space'):
        win.close()
        core.quit()


Draw.gabor1()
win.flip()
core.wait(1)

win.flip()
while win.flip():
    gabor2.draw()
    TekstSpatie.draw()
    core.wait(Tijden)
    if event.getKeys(keyList = 'f,j'):
        feedback_message()
        core.wait(1)
        win.close()
        core.quit()

win.flip()
while win.flip():
    gabor3.draw()
    TekstSpatie.draw()
    core.wait(Tijden)
    if event.getKeys(keyList = 'f,j'):
        feedback_message()
        core.wait(1)
        win.close()
        core.quit()




win.flip()
while win.flip():
    Salut.draw()
    TekstSpatie.draw()
    if event.getKeys(keyList = 'space'):
        win.close()
        core.quit()







win.flip()

win.close()
core.quit()
