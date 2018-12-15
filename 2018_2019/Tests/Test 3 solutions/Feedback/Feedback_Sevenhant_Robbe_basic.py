# import modules
from psychopy import prefs
from psychopy import visual, event, core, sound, gui
import time, numpy

#maak window
win = visual.Window(size=[600,500], units = "norm")

# create a dialog box
info = {"Participant number":0, "Participant name":"Unknown", "Gender":["male", "female", "derde gender"], "handvoorkeur": ["links", "rechts", "ambidexter"], "Age":0}
### Esther: dit is niet het Stroop experiment ;)
infoDlg = gui.DlgFromDict(dictionary=info, title="Stroop Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

#maak variabelen aan
nblocks = 3
gaborwait      = numpy.array ([0.016, 0.033,0.050])
ori_verandering = numpy.array([30,30,30,30,330,330,330,330])
sf_verandering  = numpy.array([2,20,2,20,2,20,2,20])

#zorg dat de responsetabel groeit en rt
resp = numpy.repeat(0,len(sf_verandering))
RT = numpy.repeat(0,len(sf_verandering))

matrix = numpy.column_stack([ori_verandering,sf_verandering,resp, RT])

### Esther: hier zal je ook nog de matrix moeten verdrievoudigen zodat je voldoende trials hebt voor de drie blokken

# initialize graphical elements
MessageOnSCreen = visual.TextStim(win, text = "OK")
myGabor = visual.GratingStim(win, tex='sin', mask='gauss',ori= 0, sf= 2)
myGabor_zonderdraai = visual.GratingStim(win, tex='sin', mask='gauss',ori= 0, sf=2)


#maak tekst voor instructies en einde experiment
### Esther: vergeet niet aan de proefpersoon te vertellen op welke toets ze dienen te drukken om verder te gaan
instructies_tekst = "Druk op de 'f'-toets wanneer de figuur naar links draait, druk op de 'j'-toets wanneer de figuur naar rechts draait."
einde_tekst       = "Dit is het einde van het experiment, bedankt voor u deelname!"

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

#maak een klok
my_clock= core.Clock()

#verwelkom participant
message(message_text= "Welkom " + info["Participant name"] + ".\n\nDruk op de spatiebalk om verder te gaan.", response_key = "space") 

#geef instructies op scherm
message(message_text= instructies_tekst, response_key ="space")

#start het experiment
for blocks in range(nblocks):
    #zet de corewait voor deze trail
    wachttijd = gaborwait[blocks]
    #zegt in welk blok ze zitten
    message(message_text = "Blok " + str(blocks+1) +" begint nadat u op de spatiebalk drukt.", response_key="space")
    
    ### Esther: let op, op deze manier 
    for trials in range(8):
        #bepaal de waarden van ori en sf
        myGabor_zonderdraai.sf = sf_verandering[trials]
        myGabor.sf = sf_verandering[trials]
        myGabor.ori= ori_verandering[trials]
        
        #eerst voor 1sec niet gedraaid
        myGabor_zonderdraai.draw()
        win.flip()
        time.sleep(1)
        #teken de gedraaide simulus
        myGabor.draw()
        
        ### Esther: dit is nog een beter moment om het keyboard te clearen
        
        win.flip()
        my_clock.reset()
        core.wait(wachttijd)
        
        #terug niet gedraaid en wachten op response
        myGabor_zonderdraai.draw()
        event.clearEvents(eventType = "keyboard")
        
        win.flip()
        
        keys = event.waitKeys(keyList = ["f","j", "escape"])
        RT=my_clock.getTime()
        
        #ontsnap uit trial door esc
        if keys[0] == "escape":
            break
        
        #registreer het antwoord en RT
        resp = keys[0]
        #matrix[trials,2] = resp -> zorgt voor crash geen tijd meer om op te lossen
        matrix[trials,3] = RT
    
    ### Esther: hier dien je ook nog te ontsnappen aan de blokloop

#corresp zou zijn: if myGabor.ori = 30 and resp = 'j': corresp=1 
#                                               else corresp=0, maar tijd is op

#afscheid nemen van proefpersoon
message(message_text = einde_tekst)


#sluit scherm
win.close()

print(matrix)












