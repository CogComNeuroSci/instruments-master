#Project: Test 3
#Date: 12/12/2018
#Author: Geysen Steven (01611639)
#Ik zit vast bij de Gabor stimuli. Alles daarna is snel gemaakt en zit nog vol fouten


#Basics

from psychopy import visual, monitors, core, event, gui
import numpy as np
import time


##Window
mon = monitors.Monitor('my laptop screen')
mon.setDistance(40)              ##how many cm is your pp from the screen
mon.setWidth (38)                ##how wide is the screen in cm
mon.setSizePix((1536,864))       ##size in pixels


##GUI
info = {'Naam participant':'Unknown', 'Nummer participant':0, 'Leeftijd':0, 'Geslacht':['man', 'vrouw', 'derde gender'], 'Handvoorkeur':['links', 'rechts', 'ambidexter']}
infoDlg = gui.DlgFromDict(dictionary = info, title = 'Test 3')

win = visual.Window(size = (600,500), units = 'norm', monitor = mon)


##Clock for RT
my_clock = core.Clock()


#Variables

nblocks = 3
ntrials = 8
Duration = np.array([0.016, 0.033, 0.05])


#Gabor

Orientation = np.array([30, 330, 30, 330, 30, 330, 30, 330])
gabor1 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 0, name='Mask')

gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 10, name='Target')


#Respons
##Duration


##Correct response
CorResp = np.repeat('', len(Orientation))

##Response
Resp = np.repeat(0,len(CorResp))

##Accuracy
Accuracy = np.repeat(-99.9, len(CorResp))

##Reaction time
RT = np.repeat(-99.9, len(CorResp))

##Trials
### Esther: pas op, Duration heeft slechts 3 waarden en kan dus niet gecombineerd worden met de andere eigenschappen
#trials = np.column_stack([Orientation, Duration, CorResp, Resp, Accuracy, RT])
trials = np.column_stack([Orientation, Resp, CorResp, Resp, Accuracy, RT])

### Esther: hier moet de trial matrix ook verdriedubbeld worden voor de drie blokken

#Text

MessageOnSCreen = visual.TextStim(win, text = 'Hallo')
Welkom = visual.TextStim(win, text ='Welkome {} \n\nDruk spatie om verder te gaan'.format(info['Naam participant']))
Instructies = visual.TextStim(win, text = ('Duid zo juist en zo snel mogelijk aan welke oriëntatie de stimulus op het scherm heeft.\n'+
                'Gebruik hiervoor "f" wanneer de stimulus naar links gedraaid is (de lijnen lopen van linksboven naar rechtsonder), '+
                'gebruik "j" wanneer de stimulus naar rechts gedraaid is (de lijnen lopen van rechtsboven naar linksonder).\n'+
                'Druk spatie om verder te gaan'))
Block_text = visual.TextStim(win, text = 'hey')
Feedback = visual.TextStim(win, text = 'Oei')
Einde = visual.TextStim(win, text = 'Bedankt voor je deelname')


#Functies

##Text with infinite wait.Keys
def text_IWKeys(win, text, key_list):
    '''display text, key to continue.
    waits forever'''
    text.draw()
    win.flip()
    event.waitKeys(keyList = key_list)


##Text without space (time.sleep())
def text_sleep(win, text, duration):
    '''Display text, wait duration to continue.
    uses time.sleep'''
    text.draw()
    win.flip()
    time.sleep(duration)


##Feedback message
def feedback_message ():
    
    ### Esther: misschien wat raar om Resp terug om te zetten naar keys[0] hier
    keys[0] = Resp
    if keys[0] == CorResp:
        Feedback.text = 'Correct'
        Accuracy = 1
    else:
        Feedback.text = 'Fout'
        Accuracy = 0
    text.draw()
    win.flip()
    time.sleep(1)
    return Accuracy


#                        #
#          Core          #
#                        #


if infoDlg.OK:

    #Greeting
    text_IWKeys(win, Welkom, 'space')
    
    #Instructions
    text_IWKeys(win, Instructies, 'space')

    #Blocks
    for b in range(nblocks):
        
        #Block aankondigen
        Block_text.text = 'block {} gaat beginnen.\n Druk spatie om verder te gaan'.format(str(b+1))
        text_IWKeys(win, Block_text, 'space')
        
        ### Esther: pas op, je trialnummers worden hier niet aangepast aan de block-structuur
        ### Esther: daardoor zal je de antwoorden van het vorige blok overschrijven met antwoorden uit het huidige blok
        
        #Trials
        for t in range(ntrials):
            
            ### Esther: eerste perfecte uitvoering van de meting van de RT die ik zie (en ik zit halfweg in het verbeterwerk), proficiat!
            
            #Mask
            gabor1.draw()
            win.flip()
            time.sleep(1)
            
            #Target
            ### Esther: dit is niet de goede manier om de orientatie eigenschap aan te passen
            gabor.ori(Orientation[t])
            gabor.draw()
            event.clearEvents(eventType = 'keyboard')
            ### Esther: vergeet de () niet!
            win.flip
            my_clock.reset()
            core.wait(Duration[b])
            
            #Gabor die wacht op antwoord
            gabor1.draw()
            win.flip()
            
            ### Esther: pas op, gezien "escape" niet deel is van de opties
            keys = event.waitKeys(keyList = ['f', 'j'])
            
            #Escape uit block
            if keys[0] == 'escape':
                break
            
            #Reaction time
            RT = my_clock.getTime()
            
            ### Esther: de correcte antwoorden zijn hier nog niet ingegeven
            if keys[0] == trials[b,2]:
                Feedback.text = 'Correct'
                trials[b,4] = 1
            else:
                Feedback.text = 'Fout'
                trials[b,4] = 0
            
            trials[b,5] = RT
            trials[b,3] = keys[0]
            
            text_sleep(win, Feedback, 1)
            

        ### Esther: hier ook nog uit de block-loop breaken

    #End
    text_sleep(win, Einde, 1)

    win.close()

else:
    trials = 'user cancelled'

