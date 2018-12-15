#modules importeren
from psychopy import visual, event, core, gui
import time, numpy

#window maken
win= visual.Window(size= [600,500], units='norm')

#dialoog venster maken
info = {"Naam":"", "Proefpersoonnummer":"", "Leeftijd": "", "Gender":["man", "vrouw", "derde gender"], "Handvoorkeur": ["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title='TestExperiment')
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print('User Cancelled')

#aantal blokken
n_blokken=3

#aantal trails
n_trails=8

#variabele kenmerken in een array stoppen
aanbiedingsTijd= numpy.array([0.16, 0.33, 0.50])
spatiale_frequentie= numpy.array([2,20,20,2,2,20,20,2])
orientatie= numpy.array([-30,30, -30,30,-30,30,-30,30])
corResp= numpy.array(["f", "j", "f", "j", "f", "j", "f", "j"])

#uitleg exp opstellen voor instructies
uitleg_exp= "Tijdens dit experiment zal je kort enkele figuren aangeboden krijgen. Deze figuren kunnen naar links gedraaid zijn of naar rechts, het is de bedoeling dat u detecteert wat de orientatie is van het object. Als de orientatie links is, druk f. Is de orientatie rechts, druk dan j. \n Druk spatie om verder te gaan."


#stimuli invoegen
welkom= visual.TextStim(win, text= "Welkom {0}, \ndruk spatie om verder te gaan.".format(info["Naam"]))
instructies= visual.TextStim(win, text= uitleg_exp)
gabor= visual.GratingStim(win, ori=0, mask= "circle")
gedraaide_gabor= visual.GratingStim(win,mask="circle")
blok_info= visual.TextStim(win)
feedback= visual.TextStim(win)
einde= visual.TextStim(win, text= "Bedankt voor je deelname!")


#ppn verwelkomen
welkom.draw()
win.flip()
event.waitKeys(keyList=["space"])

#instructies
instructies.draw()
win.flip()
event.waitKeys(keyList=["space"])

#functie om feedback te bepalen
def feedback_message():
    #correcte respons bepalen
    if orientatie[trail]==-30:
        corResp="f"
    else:
        corResp="j"
        
    #feedback geven
    if respons[0]==corResp:
        feedback.text= "Correct!"
    else:
        feedback.text="Verkeerd antwoord!"
    feedback.draw()
    win.flip()
    time.sleep(1)
    

#trailmatrix maken
orien=numpy.repeat(-99.99, len(orientatie))
spafreq=numpy.repeat(-99.99, len(orientatie))
RT= numpy.repeat(-99, len(orientatie))
respons= numpy.repeat(99, len(orientatie))
aanbieding=numpy.repeat(-99, len(orientatie))

trails= numpy.column_stack([info["Proefpersoonnummer"], info["Leeftijd"], info["Gender"], info["Handvoorkeur"], orien, spafreq, corResp, RT, respons, feedback.text, aanbieding, aanbiedingsTijd])

print(trails)

#kolk invoegen
klok= core.Clock()

#eerst een blokloop maken
for blok in range(n_blokken):
    #ppn melden dat eerste blok begint
    blok_info.text= "Blok {0}, druk op spatie om te beginnen aan het experiment".format(blok+1)
    blok_info.draw()
    win.flip()
    event.waitKeys(keyList=["space"])
    
    #trails maken
    for trail in range (n_trails):
        #normale gabor laten zien
        gabor.draw()
        win.flip()
        time.sleep(1)
        
        #klok installeren om na te gaan of de stimulus echt voor die bep tijd werd getoond
        start= time.clock()
        
        #gedraaide gabor laten zien
        gedraaide_gabor.sf=spatiale_frequentie[trail]
        gedraaide_gabor.ori=orientatie[trail]
        gedraaide_gabor.draw()
        win.flip()
        core.wait(aanbiedingsTijd[blok])
        
        #klok installeren om na te geen hoelang stim getoond werd
        stop=time.clock()
        
        #stop min start om te weten hoelang stim werd getoond
        aanbieding= stop-start
        print(aanbieding)
        
        #er worden geen responsen  van vorige trails overgedragen
        event.clearEvents(eventType= "keyboard")
        
        #normale gabor laten zien als mask
        gabor.draw()
        win.flip()
        
        #klok resetten
        klok.reset()
        
        #ppn laten antwoorden
        respons= event.waitKeys(keyList=["f", "j","escape" ])
        print(respons)
        
        #RT meten
        RT= klok.getTime()
        print(RT)
        
        ### Esther: pas op, de trails zijn zelfde in elke trial loop, dus je zal de data overschrijven
        #alles in trailmatrix stoppen
        trails[trail,4]=orientatie[trail]
        trails[trail,5]=spatiale_frequentie[trail]
        trails[trail,6]= corResp[trail]
        trails[trail,7]= RT[trail]
        trails[trail,8]= respons[trail]
        trails[trail,10]= aanbieding[trail]
        trails[trail, 11]= aanbiedingsTijd[blok] 
        
        feedback_message()
        
        if respons[0]=="escape":
            break
    if respons[0]=="escape":
        break

print(trails)

einde.draw()
win.flip()
time.sleep(1)
win.close()