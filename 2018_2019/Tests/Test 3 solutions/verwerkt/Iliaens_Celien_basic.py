#import modules
from psychopy import visual, event, core, gui
import time, numpy, random

#Registratie gegevens proefpersoon 
info = {"Participant number":0, "Participant name":"Unknown", "Age":0,"Gender":["Male","Female","Other"],"Hand preference":["Left","Right","Ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Stroop Experiment")
if infoDlg.OK:
    print(info)
else:
    print("User Cancelled")


#Window aanmaken 
win = visual.Window(size=(600,500), fullscr = False, units = 'norm')

#Teksten aanmaken
welkomtekst = visual.TextStim(win, text=    "Welkom {0}! \n\n"
                                            "Druk op de spatiebalk om verder te gaan".format(info["Participant name"]))
instructietekst = visual.TextStim(win, text = "Tijdens dit experiment zal je moeten bepalen of een Gabor naar links of naar rechts gedraaid is. \n"
                                                "Wanneer de Gabor naar links gedraaid is (lijnen lopen van linksboven naar rechtsonder), druk dan 'f'.\n"
                                                "Wanneer de Gabor naar rechts gedraaid is (lijnen lopen van rechtsboven naar linksonder), druk dan 'j'.\n\n"
                                                "Druk op de spatiebalk om verder te gaan")

Eindtekst = visual.TextStim(win, text = "Dit is het einde van het experiment.\n\n"
                                        "Druk op de spatiebalk om af te sluiten.")


#Stimuli aanmaken

gabormask = visual.GratingStim(win, mask = "circle", ori = 180, sf =2)

ntrials = 8
nblocks = 3
klok = core.Clock()
klok2 = core.Clock()

orientation =   numpy.array([30,30,30,30,-30,-30,-30,-30])
frequency =     numpy.array([2,2,20,20,2,2,20,20])
aanbiedingT =   numpy.array([0.0016, 0.0033, 0.0050])
corResp =       numpy.repeat("x", ntrials)
Resp =          numpy.repeat("x", ntrials)
trialnumber =   numpy.repeat("x", ntrials)
RT =            numpy.repeat("-99", ntrials)
Accuracy=       numpy.repeat('-99', ntrials)
aanbieding =    numpy.repeat('-99', ntrials)
controle_aanb=  numpy.repeat('-99', ntrials)

trials = numpy.column_stack([trialnumber, orientation, aanbieding, frequency, corResp, Resp, RT, Accuracy, controle_aanb])

#Enkele functies definiëren 
def tekstpresentatie(tekst):
    tekst.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])

def gmask():
    gabormask.draw()
    win.flip()
    core.wait(1)

def gaborwait():
    gabormask.draw()
    event.clearEvents(eventType = "keyboard")
    win.flip()

def correctresp(number = 30):
    if number == 30:
        corresp = 'j'
    else:
        corresp = 'f'
    return corresp 

def acc():
    if trials[i,4] == trials[i,5]:
        trials[i,7] = 1
    else:
        trials[i,7] =0

def feedback_message():
    if trials[i,4] == trials[i,5]:
        fbtext = "Correct!"
    else:
        fbtext = "Verkeerde antwoord!"
    
    message = visual.TextStim(win, text = fbtext)
    message.draw()
    win.flip()
    time.sleep(1)

#Begin experiment
tekstpresentatie(welkomtekst)
tekstpresentatie(instructietekst)

#trials
for b in range(nblocks):
    #Weergeven in welk blok we zitten
    bloktekst = visual.TextStim(win, text = "Blok {} zal nu starten.\n\n"
                                        "Druk op de spatiebalk om verder te gaan.".format(b+1))
    tekstpresentatie(bloktekst)
    
    for i in range(ntrials):
        
        #orientatie en frequency van Gabor bepalen
        g_ori = trials[i,1]
        g_sf = trials[i,3]
        gabor = visual.GratingStim(win, mask ="circle", ori = g_ori, sf = g_sf)
        
        #Gabor met verticale oriëntatie
        gmask()
        
        #Gabor stimulus met aangepaste aanbiedingstijd
        gabor.draw()
        win.flip()
        klok2.reset()
        core.wait(aanbiedingT[b])
        trials[i,8] = klok2.getTime()  #registreren van effectieve aanbiedingstijd
        
        #nieuwe verticale gabor aanbieden + keyboard clearen
        gaborwait()
        
        #klok resetten + wachten op respons
        klok.reset()
        keys = event.waitKeys(keyList = ['f','j','escape'])
        
        #mogelijkheid tot ontsnappen uit trials
        if keys[0] == "escape":
            break
        
        #trials informatie aanvullen
        trials[i,0] = i+1               #trialnummer
        trials[i, 2] = aanbiedingT[b]   #aanbiedingstijd
        trials[i,5] = keys[0]           #gegeven antwoord
        trials[i,6] = klok.getTime()    #reactietijd 
        
        #correct response bepalen en opslaan
        ##Ik weet niet waarom, maar mijn correcte respons wordt niet juist opgeslagen ('f' wordt altijd als juiste antwoord aangeduid)
        ##Hierdoor klopt ook mijn accuracy en feedback niet altijd
        trials[i,4] = correctresp(number = g_ori)
        
        #accuracy bepalen en opslaan
        acc()
        
        #feedback geven 
        feedback_message()
        
    if keys[0] == 'escape':
        break 
            
    print(trials)

tekstpresentatie(Eindtekst)




