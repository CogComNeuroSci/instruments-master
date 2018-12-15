#TEST3
#Implementing a Gabor task

#import
from psychopy import event,core,gui
import random
from time import sleep as sl
import numpy as np
from psychopy import visual as vis

#make a clock
core.wait(0.5)
clock=core.Clock()

#make a window
win=vis.Window(size=(600,500))

#Make a dialog box
info={'Naam':'','Proefpersoonnummer':'','leeftijd':'','Gender':['man','vrouw','derde gender'],'handvoorkeur':['links','rechts']}
infoDLG=gui.DlgFromDict(dictionary=info)

Name= info.get('Naam')
Proefpersoon= info.get('Proefpersoonnummer')

#initialization
n_blocks= 3
n_trials= 8
##List of answers
Response = []
##List of Reaction times
Reaction_time=[]
##Orientations and frequency
frequency_gabor1   =[[2,0],[20,0]]
frequency_gabor2   =[[2,0],[20,0]]
orientations_gabor2=[120,30]
CorResponse        = ['f','j']
Times              =[0.16,0.33,0.50]

##trial number
trial_nb = 0
T_trials= n_blocks*n_trials

#make arrays
##PFFN
Ppn = np.repeat(Proefpersoon,len(frequency_gabor1)*4*n_blocks)
##orientatie en sf
Orientation= np.array(orientations_gabor2*4*n_blocks)
SF1        = np.array(frequency_gabor1*4*n_blocks)
SF2        = np.array(frequency_gabor2*4*n_blocks)
print(Orientation)
##CorResp
CorResp         = np.array(CorResponse*4*n_blocks)
##Reactietijd
Reactie_tijd = np.repeat(-99.,T_trials)
##Answer
Antwoord     = np.repeat(['a'],T_trials)
##Accuracy
Acc          = np.repeat(-1,T_trials)
##Presentation
GP            = np.array(Times*n_trials)
Geplande_tijd = np.sort(GP)
print(Geplande_tijd)
effectieve_tijd = np.repeat(0,T_trials)

##Put it into a matrix 
trials= np.column_stack([Ppn,SF1,SF2,CorResp,Reactie_tijd,Antwoord,Acc,Geplande_tijd,effectieve_tijd])

print(trials)

#visual features
Welkom       = vis.TextStim(win,text='Welkom {0}\n [Druk op spatie om verder te gaan]'.format(Name))
Instructions = vis.TextStim(win,text='Je gaat telkens een gabor stimulus te zien krijgen. \n Jouw taak zit erin te detecteren of deze naar links (lijnen lopen van links boven naar rechts onder)' 
                                      + 'of naar rechts gedraaid is (lijnen lopen van rechts boven naar links onder). \n Indien je denkt deze naar links is gedraaid, druk dan op f.'
                                      + '\n Indien je denkt deze naar rechts is gedraaid, druk dan op j.\n [Druk op spatie om verder te gaan]',height=0.08)
Block_text   = vis.TextStim(win)
Goodbye      = vis.TextStim(win,text='Hartelijk dank voor jouw deelname!\n [Druk op spatie om het experiment te stoppen]')

##Feedback
FB = vis.TextStim(win)

##GABOR STIMULI
gabor_vert     = vis.GratingStim(win, tex="sin", mask="gauss", texRes=256, units='norm',
                 size=[1.0, 1.0], ori = 0, name='gabor1')

gabor_oriented = vis.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
                 size=[1.0, 1.0], sf=[2, 0],ori = 30, name='gabor1')  ##Hier de orientatie van wijzigen

#functions
def ACC():
    if ORI==120 :
        if k==['f']:
            CorResp=1
        else:
            CorResp=0
    elif ORI==30:
        if k==['j']:
            CorResp=1
        else:
            CorResp=0
    return CorResp

def feedback_message():
    if CorResp==1:
        FB.text='Correct!'
    else:
        FB.text='Verkeerd antwoord!'
    FB.draw()
    win.flip()
    sl(1)

#Start the experiment
##Proefpersoon verwelkomen
Welkom.draw()
win.flip()
event.waitKeys(keyList=['space'])
##Presenteer de instructies
Instructions.draw()
win.flip()
event.waitKeys(keyList=['space'])

##Start met het experiment
for block in range (n_blocks):
    Block_text.text='Dit is block {0}. \n [Druk op spatie om verder te gaan]'.format(block+1)
    Block_text.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    ##Start trials
    for i in range(n_trials):
        #assigning the different times
        if block==0:
            time=0.16
        elif block==1:
            time=0.33
        else:
            time=0.50
        #Assigning ori and frequency
        ORI=random.choice (orientations_gabor2)
        gabor_vert.sf     = random.choice (SF1) ## Ik weet dat ik het hier moet wijzigen, maar heb de tijd niet gehad om een de variabele toe te wijzen aan de trial matrix
        gabor_oriented.sf = random.choice (SF2) ## De corResp matchen nu niet meer... :(
        gabor_oriented.ori= ORI
        ##for the later function
        
        
        #Toon verticale Gabor voor 1 sec
        gabor_vert.draw()
        win.flip()
        sl(1)
        clock.reset()
        
        #Toon andere gabor
        while clock.getTime()<time:
            gabor_oriented.draw()
            win.flip()
        
        #meet effectieve_tijd
        trials[trial_nb,10]= clock.getTime()
        
        #Toon terug verticale gabor
        gabor_vert.draw()
        win.flip()
        k=event.waitKeys(keyList=['j','f','escape','esc'])
        RT= clock.getTime()
        trials[trial_nb,6]=RT
        trials[trial_nb,7]=k[0]
        
        ##escape functie
        if k[0] in ['escape','esc']:
            break
        
        #show feedback
        CorResp=ACC()
        trials[trial_nb,8]=CorResp
        feedback_message()
        
        #Manage trial number (from 0 to 8*3)
        trial_nb=trial_nb+1

#Print
print(trials)

core.quit()
#Einde
Goodbye.draw()
win.flip()
event.waitKeys(['space']
win.close()
