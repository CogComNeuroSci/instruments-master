#modules importeren
import time, numpy
from psychopy import visual, core, event, gui

#dialog box

info = {"Participant number":0, "Participant name":"Unknown", "Gender":["man", "vrouw", "derde gender"], "Leeftijd":0, "Handvoorkeur":["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="test 3")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

#window
win=visual.Window([600, 500], units = "norm")
welkom=visual.TextStim(win, text="Welkom "+info["Participant name"]+"!\n"+"Druk op de spatiebalk om verder te gaan")
instructies= visual.TextStim(win, text="Op het scherm zien jullie straks gabor stimuli.\n"+" Het is de bedoeling dat je op de f-toets drukt indien de lijnen in deze stimulus naar links gedraaid zijn, \n" +"en op de j toets als deze naar rechts gedraaid zijn. ")
goodbye=visual.TextStim(win, text="Bedankt "+info["Participant name"]+ "voor je deelname aan dit experiment, \n"+"druk op de spatiebalk om af te sluiten.")
feedback=visual.TextStim(win, text = "OK")

clock=core.Clock()

#aantallen
ntrial= 8
nblock= 3

#gabor stimuli
vert=visual.GratingStim(win, tex='sin', mask='gauss', sf= 20)
gedraaid= visual.GratingStim(win, tex= 'sin', mask='gauss', sf= 2, ori= 30)


#arrays
##gabor
ORI= numpy.array([30, 30, 30, 30, 330, 330, 330, 330])
SF=numpy.array([2, 20, 2, 20, 2, 20, 2, 20])

##corresp
corresp = numpy.copy(ORI)
corresp[corresp==30]="j"
corresp[corresp==330]="f"


##gegeven respons
resp= numpy.repeat("key", ntrial)

##accuracy
acc= numpy.repeat(0, ntrial)

##RT
RT= numpy.repeat(0, ntrial)

##info participant
subject = numpy.repeat(info["Participant number"],ntrial)
gender  = numpy.repeat("".join(info["Gender"]),ntrial)
leeftijd = numpy.repeat(info["Leeftijd"],ntrial)
handvoorkeur= numpy.repeat("".join(info["Handvoorkeur"]), ntrial)
##"".join om ervoor te zorgen dat je vb. niet "m""a""n" krijgt maar "man"

##alles samenvoegen
matrix= numpy.column_stack([ORI, SF, resp, corresp, acc, RT, subject, gender, leeftijd, handvoorkeur])
matrix = numpy.tile(matrix, (nblock, 1))

#array blockloop
atijd= numpy.array([0.016, 0.033, 0.05])

#feedback functie
def feedback_message(messagetext = ""):
    
    feedback.text= messagetext
    if matrix[trial, 2]==matrix[trial, 3]:
        feedback.text= "Correct!"
    else:
        feedback.text= "Verkeerd antwoord"
    feedback.draw()
    win.flip()
    core.wait(1)
    return feedback
    
    
#ik krijg telkens deze foutmelding: ValueError: invalid literal for int() with base 10: 'j'
#en af en toe als ik dingen aanpas krijg ik deze: TypeError: can't multiply sequence by non-int of type 'float'
#telkens als ik een string in mijn matrix wil plaatsen ( of het nu voor het experiment is, of tijdens het experiment) lukt dit dus niet
#ik heb al super veel geprobeerd maar blijf hierop vast zitten
#aangezien ik wel wou tonen hoe ik het experiment normaal zou opstellen, zette ik alles er toch in en werkt deze daarom niet.
#sorry hiervoor!

#experiment initiëren
welkom.draw()
win.flip()
event.waitKeys(keyList=['space'])

instructies.draw()
win.flip()
event.waitKeys(keyList=['space'])


#Blockloop
for block in range (nblock):
    blocktext= visual.TextStim(win, text="Dit is blok "+ str(block+1)+".\n"+"Druk op de spatie om door te gaan.")
    blocktext.draw()
    win.flip()
    event.waitKeys(keyList=['space'])
    
    #trialloop
    for trial in range (ntrial):
        ## masker
        vert.sf=matrix[trial,1]
        vert.draw()
        win.flip()
        core.wait(1)
        
        ## target
        gedraaid.ori= matrix[trial,0]
        gedraaid.sf= matrix[trial, 1]
        gedraaid.draw()
        win.flip()
        clock.reset()
        core.wait(atijd[block])
        
        ## opnieuw masker
        vert.draw()
        event.clearEvents(eventType = "keyboard")
        win.flip()
        core.wait(0.5)

        
        keys= event.waitKeys(keyList=["f", "j", "escape"])
        RT=clock.getTime()
        
        
        ## escape uit trial
        if keys[0] == "escape":
            break
        
        ## gegeven respons opslaan
        matrix[trial, 2]=keys[0]
       
        ## accuracy opslaan
        matrix[trial, 4]= matrix[trial, 2]==matrix[trial, 3]
        
        ## RT opslaan
        matrix[trial,5]=RT
        
        ##feedback
        feedback_message(feedback.text)
        print(matrix)
        
        ##indien feedbackfunctie niet zou werken
        ## if matrix[trial, 2]==matrix[trial, 3]
            ##feedback.text= "Correct"
        ## else:
            ##feedback.text= "Verkeerd antwoord!"
        ##feedback.draw()
        ##win.flip()
        ##core.wait(1)
    
    #om uit blockloop te escapen
    if keys[0] == "escape":
        break
        
print(matrix)
goodbye.draw()
win.flip()
event.waitKeys(keyList=['space'])
