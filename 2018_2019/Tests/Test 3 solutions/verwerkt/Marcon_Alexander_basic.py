##Test 3: Gabor stimulus taak_________________________________________________________

#implementeren modules________________________________________________________________
from psychopy import visual, gui, core, event
import time, numpy

#Forced Stop__________________________________________________________________________
for key in ["escape"]:
    event.globalKeys.add(key, func=core.quit)

#wat variabelen_______________________________________________________________________
nBlokken = 3
nTrials = 8

#mijn klokken_________________________________________________________________________
StimulusTijd = core.Clock()
RTklok       = core.Clock()

#initiatie window_____________________________________________________________________
GTwin = visual.Window([600, 500], units = "norm", color = (-1,-1,-1))

#aanmaken dialogbox___________________________________________________________________
info = {"naam": "", "nummer": "", "leeftijd": "", "gender":["man", "vrouw", "x"], 
        "handvoorkeur": ["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary = info, title = "Gabor Taak", order = ["naam", "leeftijd", "gender", "nummer", "handvoorkeur"])

if infoDlg.OK:
    print(info)
else:
    print('User cancelled')

    ## variabelen opslaan:____________________________________________________________
PPnaam   = info["naam"]

#Aanmaken stimuli_____________________________________________________________________
welkom      = visual.TextStim(GTwin, text = "Welkom {0}! Druk op de spatie om verder te gaan.".format(PPnaam), color =(1,1,1))
instructies = visual.TextStim(GTwin, text = "In deze taak zal je moeten reageren op de oriëntatie van een Gabor stimulus. Deze stimulus zal voorafgegaan en gevolgd worden door een andere Gabor stimulus, maar die zal je moeten negeren. Als de middelste Gabor stimulus naar links (de lijnen lopen van linksboven naar rechtsonder) is georiënteerd zal je op 'f' moeten drukken, als deze naar rechts (de lijnen lopen van rechtsboven naar linksonder) is georiënteerd zal je op 'j' moeten drukken. Als je nog vragen hebt kan je deze nu aan de experimentleider stellen. Druk op de spatie om verder te gaan.", height = 0.05, color = (1,1,1))
blok        = visual.TextStim(GTwin, text = "xxx", color = (1,1,1))
afscheid    = visual.TextStim(GTwin, text = "Bedankt om deel te nemen aan dit experiment! Wij wensen u nog een prettige dag!", color = (1,1,1))
Feedback    = visual.TextStim(GTwin, text = "OK", color = (1,1,1))
Gabor2      = visual.GratingStim(GTwin, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=[2], ori = -45, name='gabor2')
Gabor1_3    = visual.GratingStim(GTwin, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')



#nodige lijsten aanmaken______________________________________________________________
Oriëntatie   = numpy.array(3*[45, -45, 45, -45, 45, -45, 45, -45])
CorResp      = numpy.array(3*["j", "f","j", "f","j", "f","j", "f"])
Frequentie   = numpy.array(3*[2, 2, 2, 2, 20, 20, 20, 20])
Aanbieding   = numpy.array([0.016, 0.016, 0.016, 0.016, 0.016, 0.016, 0.016, 0.016, 0.033, 0.033, 0.033, 0.033, 0.033, 0.033, 0.033, 0.033, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])
ResponseKey  = numpy.repeat(-99.9, len(CorResp))
ReactieTijd  = numpy.repeat(-99.9, len(CorResp))
Accuraatheid = numpy.repeat(-99.9, len(CorResp))

MyArray = numpy.column_stack([Oriëntatie, Frequentie, Aanbieding, CorResp, ResponseKey, ReactieTijd, Accuraatheid])

#Welkom, instructies__________________________________________________________________
welkom.draw()
GTwin.flip()
k = event.waitKeys(keyList = "space")

instructies.draw()
GTwin.flip()
k = event.waitKeys(keyList = "space")

#De taak______________________________________________________________________________
for b in range(nBlokken):
    
    # welke blok gaat er beginnen?____________________________________________________
    blok.text = "Blok " + str(b+1) + " gaat nu beginnen. Druk op de spatiebalk om van start te gaan"
    blok.draw()
    GTwin.flip()
    event.waitKeys(keyList = "space")
    
    # 8 trials________________________________________________________________________
    for t in range(nTrials):
        #frequentie en oriëntatie:____________________________________________________
        ##Gabor2.ori = MyArray[t,0] --> TypeError: can't multiply sequence by non-int of type 'float' --> niet gevonden wat ik hiermee moest doen, wou met mijn mijst met oriëntaties de oriëntatie van mijn stimulus doen wisselen, maar dan kreeg ik deze foutmelding
        Gabor2.sf  = MyArray[t,1] ##wou hiermee mijn kolom met frequenties mijn frequentie doen afwisselen, maar dat doet het precies niet
        
        #stimulus op scherm zetten____________________________________________________
        Gabor1_3.draw()
        GTwin.flip()
        core.wait(1)
        
        Gabor2.draw()
        
        ##RTklok en StimulusTijd resetten_____________________________________________
        ReactieTijd = RTklok.getTime()
        RTklok.reset()
        StimulusTijd.reset() ## geen idee hoe ik de duur van mijn stimulus kan bepalen hiermee
        
        GTwin.flip()
        core.wait(0.016) ##heb niet gevonden hoe ik mijn lijst met aanbiedingstijden moest implementeren
        
        Gabor1_3.draw()
        GTwin.flip()
        RK = event.waitKeys(keyList = ("f", "j"))
        
        #registreren van antwoord______________________________________________________
        MyArray[t,4] = RK[-1]
        MyArray[t,5] = ReactieTijd
        
        #Accuraatheid__________________________________________________________________
        MyArray[t,6] = int(MyArray[t,3] == RK[-1])
        
        # Bepaal welke feedback er gegeven moet worden_________________________________
        if int(MyArray[t,6]) == 1:
            Feedback.text = "Correct!"
        else:
            Feedback.text = "Verkeerd antwoord!"
        
        #Feedback weergeven____________________________________________________________
        Feedback.draw()
        GTwin.flip()
        core.wait(1)

#Afscheid nemen________________________________________________________________________
afscheid.draw()
GTwin.flip()
event.waitKeys(keyList = "space")

#Scherm sluiten
win.close()

print(MyArray)