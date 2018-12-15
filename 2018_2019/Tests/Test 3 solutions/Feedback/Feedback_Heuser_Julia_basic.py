# import modules
from psychopy import visual, event, core, gui
import time, numpy

#opbouw van het experiment is heel chaotisch, heelas heb ik niet meer genoeg tijd om het anders op te bouwen.
# create a DlgFromDict
### Esther: het is nog beter om de numerische waarden ook de initializeren als numerische waarden
info = {'Name':'','Gender':['male', 'female', 'third gender'], 'Age':'', 'Participant Number': 0, 'handedness':['left', 'right', 'ambidexter']}
infoDlg = gui.DlgFromDict(dictionary=info, title='TestExperiment')
if infoDlg.OK:  
    print(info)
else:
    print('User Cancelled')


# initialize the window
### Esther: waarom niet gewoon de size=[600,500] in het window plaatsen?
win = visual.Window(fullscr = False, units= "norm")    #size=[600,500]

# initialize the variables

nblocks     = 3
ntrials     = 8
### Esther: pas op, deze stimulus aanbiedingstijdens zijn 10 keer te lang
duration = 0.16, 0.33, 0.5

#Welcome
### Esther:vergeet hier ook niet om aan te geven hoe de proefpersoon kan verdergaan
HelloText=visual.TextStim(win, text = "Welkom {0}!".format(info['Name']))
HelloText.draw()
win.flip()
### Esther: het is niet nodig om "space" in een lijst te steken
event.waitKeys(keyList=["space"])

#instructies
### Esther: zorg ervoor dat de proefpersoon altijd weet op welke toets ze moeten drukken om verdere te gaan.
InstructionText=visual.TextStim(win, text= "Druk de f toets al de Gabor naar links gedraaid is, druk de j toets als de Gabor naar rechts gedraaid is")
InstructionText.draw()
win.flip()
event.waitKeys(keyList=["space"])

# initialize graphical elements
Block_start     = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)
gaborMask = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[5, 0], ori = 90, name='gabor1')
#gabor met sf van 20 en orientatie 30, veranderd in loop
gabor1= visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[20, 0], ori = 30, name='gabor1')


#om de respons en de reactietijd op te slagen
lijst=[]
tijd=[]

#startblock
for b in range(nblocks):
    
    #hier veranderd elker blok de nummer
    Block_start.text = "Block " + str(b+1) + " gaat beginnen als je op space klikt"
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    
    
    for i in range(b*ntrials,(b+1)*ntrials):
        #ik weet dat ik hier ook de core.wait moet kunnen veranderen in de drie verschillende tijden, maar ik weet niet goed wie, dus heb ik nu alleen maar een trial met .16
        gaborMask.draw()
        win.flip()
        core.wait(1)
#door if te gebruiken heb ik hier de 8 verschillende trials 
### Esther: je hebt jezelf inderdaad uit de slag kunnen trekken, dus ik heb je de punten kunnen geven
### Esther: na de volgende twee chapters zullen we echter vergen dat dit gebeurt via de array
### Esther: je had wel de .draw, .flip en .wait uit de if-structuur kunnen nemen
        if i<=2:
            gabor1.sf=[20,0]
            gabor1.ori=30
            gabor1.draw()
            
            ### Esther: dit is het moment om het keyboard te clearen
            
            win.flip()
            
            ### Esther: dit is het moment om het scherm te flippen
            
            ### Esther: pas op, de aanbieding is niet aangepast aan het blok en 10 keer te lang
            core.wait(.16)
            
        elif i>2 and i<=4:
            gabor1.sf=[2,0]
            gabor1.ori=30
            gabor1.draw()
            win.flip()
            core.wait(.16)
 
            
        elif i>4 and i<=6:
        
            gabor1.sf=[20,0]
            gabor1.ori=-30
            gabor1.draw()
            win.flip()
            core.wait(.16)
         
        else:
            gabor1.sf=[2,0]
            gabor1.ori=-30
            gabor1.draw()
            win.flip()
            core.wait(.16)
            
        gaborMask.draw()
        win.flip()
        ### Esther: dit lijkt me niet de meest optimale strategie gezien je hier telkens opnieuw een timer dient aan te maken
        trial_timer = core.MonotonicClock()
        event.clearEvents(eventType = "keyboard")
        k = event.waitKeys(keyList=["f","j","escape"])
        
        ### Esther: hier zou ik meteen de RT meten
        
        if k == None:
            k=[""]
        if k[0] == "escape":
            break
        key = event.getKeys(timeStamped = trial_timer)
        lijst.append(k[0])
        tijd.append("{0:.2f}".format(trial_timer.getTime()))
    
    ### Esther: hier dien je ook nog uit de blokloop te breaken
 
#verzoek om defintie voor feedback aan te maken, maar omdat de opbouw van mijn experiment helaas echt niet goed gelukt is, kan ik deze niet echt gebruiken
#
#definitie voor feedback geven
#def feedback_message(correct = -99):
#    if correct == 1:
#        message(message_text = "Correct!", duration = 1)
#    else:
#        message(message_text = "Verkeerd antwoord!", duration = 1)

# make a function to deduce the correct response
#def determine_CorResp(target = "orientatien"):
#    if target == "-30":
#        CorResp = "f"
#    elif target == "30":
#        CorResp = "j"




tijdENantwoord = numpy.column_stack([lijst,tijd])
print(tijdENantwoord)
# display the goodbye message
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()