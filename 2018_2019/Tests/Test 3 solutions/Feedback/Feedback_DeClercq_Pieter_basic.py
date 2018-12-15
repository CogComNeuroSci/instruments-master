#ik heb vanalles geprobeerd om de correcte responsen en respons van de participant in de matrix te stoppen. Dit is niet gelukt... Dus heb ik het maar zo gelaten.
#doordat ik correcte respons niet in matrix kon stoppen, is het ook niet gelukt feedback te geven voor 1 sec
#verder is het mij ook niet gelukt om het aantal seconden te variëren over de blokken

from psychopy import visual, event, core, gui
import time, numpy, random

#info participant
info = {"Participant nummer":0, "Participant naam":"Unknown", "Geslacht":["man", "vrouw", "derde gender"], "Leeftijd":0, "Handvoorkeur":["rechts","links","ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

participantnaam=info["Participant naam"]
participantnummer=info["Participant nummer"]

#orientation, seconds and sf bepalen:
orientation=numpy.array([-30,30,30,-30,30,-30,-30,30])
frequention=numpy.array([2,20,2,20,2,2,20,20])

#correcte respons:
CorResp=numpy.repeat(0, len(orientation))

#respons participant:
k=numpy.repeat(-99.9,len(orientation))


#window
win=visual.Window(size=[600,500], units="norm")
#clock aanmaken
myclock=core.Clock()

#gabor
gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, units='norm', ori = 0)

#RT:
RT=numpy.repeat(-99.9, len(CorResp))

#functie voor messages
MessageOnScreen = visual.TextStim(win, text = "OK")

#matrix
matrix=numpy.column_stack((orientation,frequention,CorResp,k,RT))
print(matrix)

def message(message_text = "", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    MessageOnScreen.text    = message_text
    MessageOnScreen.height  = height
    MessageOnScreen.pos     = pos
    MessageOnScreen.color   = color
    
    MessageOnScreen.draw()
    win.flip()
    if duration == 0:
        x=event.waitKeys(keyList = ["space"])
    else:
        core.wait(duration)

#functie voor de gabor
def gabor_functie():
    gabor1 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, units='norm', ori = 0)
    gabor1.draw()
    win.flip()
    core.wait(1)
    
    gabor.ori=matrix[i,0]
    gabor.sf=matrix[i,1]
    gabor.draw()
    win.flip()
    
    myclock.reset()
    
    core.wait(0.05)
    
    gabor1.draw()
    
    win.flip()
    k=event.waitKeys(keyList=["f","j","escape"])
    ## Esther: ik zou hier meteen de RT meten
    
    if k[0] in ["escape","esc"]:
        ### Esther: het is niet de bedoeling dat je meteen alles afsluit, enkel dat je uit de trial en blok loop kan ontsnappen
        win.close()
    
    #matrix[i,3]=k[0] 
    ##ik snap niet waarom dit bv niet lukte. Ik kreeg deze error: ValueError: could not convert string to float: 'f'
    
    RT=myclock.getTime() * 1000
    matrix[i,4]=RT
    
    message(message_text="feedback. Niet gelukt", duration=1)
    
    return k,RT
#functie CorResp:


#functie feedback:
def feedback_message(correct = -99):
    if matrix [i,0]==-30:
        CorResp="f"
    elif matrix [i,0]==30:
        CorResp="j"


message(message_text="Welkom {0}! \n\nDruk op de spatiebalk om verder te gaan.".format(participantnaam.capitalize()))
message(message_text="Neem onderstaande instructies grondig door \n\nU zal heel kort een Gabor stimulus op het scherm krijgen. Deze stimulus zal aanvankelijk enkel verticale lijnen bevatten. \n\n"+
                      "Na 1 seconde zal deze stimulus vervangen worden door een gelijkaardige Gabor stimulus, \n\n echter, ditmaal zal de stimulus lichtjes naar links of rechts gedraaid zijn \n\n"+
                      "Als u denkt dat de Gabor stimulus naar links gedraaid is, duwt u op de f-toets\n\n"+
                      "Als u denkt dat de Gabor stimulus naar rechts gedraaid is, duwt u op de j-toets\n\n"+
                      "Na zeer korte periode wordt de gedraaide stimulus vervangen door opnieuw een Gabor stimulus met verticale lijnen \n\n"+
                      "We gaan pas over naar de volgende trial indien u geduwd hebt op de j of f toets. Hierna krijgt u feedback over uw antwoord\n\n"+
                      "Het experiment bestaat uit 3 blokken met daarin telkens een korte pauze\n\n"+
                      "U kan verdergaan naar het eerste experimentblock door op de spatiebalk te duwen", height=0.05)

#de loop zelf
for j in range(3):
    message(message_text="Dit is blok {0} \n\nDruk op spatie om verder te gaan".format(j+1))
    
    for i in range(8):
        k, RT=gabor_functie()
    print(matrix)

message(message_text="Hartelijk dank voor uw deelname! \n\nDruk op spatie om het experiment af te sluiten")


win.close()