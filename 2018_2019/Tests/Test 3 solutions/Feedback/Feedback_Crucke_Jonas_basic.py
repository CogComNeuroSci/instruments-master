#importeren

from psychopy import prefs, visual, event, core, gui
import time, numpy, random


#dialogbox
### Esther: het is beter om de response opties voor gender en handvoorkeur ook echt te presenteren als respons opties in plaats van enkel een suggestie
info= {"participant name": "Unknown","participant number":0, "participant age": 0, "gender":"male, female, third", "handpreference": "left, right, ambidextrous"}
infoDlg= gui.DlgFromDict (dictionary=info, title= "Gabortaak")
if infoDlg.OK: 
    print (info)
else:
    print ("User Cancelled")


#window

win=visual.Window (size=[600,500], units="norm")


#klok om reactietijd te meten

my_clock = core.Clock()


#variabelen initialiseren

nBlocks=3
nTrials=8
time_array=numpy.array([0.016, 0.033, 0.05])
sf_lijst=[2,20,2,20,2,20,2,20]
hoek_lijst=[330,30,330,30,30,330,30,330]

#boodschappen

##welkom
welkom=visual.TextStim(win, text="Welkom bij dit experiment, {0}.\nDruk op spatie om verder te gaan.".format(info["participant name"]))

##instructies
instructie=visual.TextStim(win, text="In dit experiment zal je een stimulus te zien krijgen voor een zeer korte tijd.\nJe dient op de f-toets te drukken wanneer de stimulus links georienteerd is (van linksboven naar rechtsonder).\nJe dient op de j-toets te drukken wanneer de stimulus naar rechts georienteerd is (van rechtsboven naar linksonder).\nDruk op spatie om verder te gaan.")

##start van het blok
blok_start=visual.TextStim(win, text="Het volgende blok zal nu van start gaan.\nDruk op spatie om verder te gaan.")

##feedback
feedback=visual.TextStim(win, text="feedback")

##afscheid
afscheid=visual.TextStim(win, text="Dit was het laatste blok.\nBedankt voor uw deelname, {0}!".format(info["participant name"]))


#Stimuli

verticale_grating=visual.GratingStim(win, mask='circle', ori=0)
grating=visual.GratingStim(win, mask='circle')




#matrix
Subject             = numpy.repeat(info["participant number"],nTrials)
Orientation         = numpy.repeat(" ",nTrials)
Correct_Response    = numpy.repeat("key", nTrials)
Response_Given      = numpy.repeat("key", nTrials)


Matrix = numpy.column_stack([Subject, Orientation, Correct_Response, Response_Given])
Matrix = numpy.tile(Matrix, (nBlocks, 1))


#response

#def det_CorResp(target=):
    #if target==30:
        #CorResp="j"
    #else:
        #CorResp="f"


#feedback, ik heb geprobeerd om een functie te schrijven, maar dit lukte mij niet. Ik heb het dus op de oude manier gedaan in de loop

#def feedback_message(target=Matrix[T,2]):
    #if target== Matrix[T,3] :
        #feedback.text="Goed!"
    #else:
        #feedback.text="Fout!"
    #return feedback.text


#welkom en instructies

welkom.draw()
win.flip()
event.waitKeys(keyList="space")

instructie.draw()
win.flip()
event.waitKeys(keyList="space")

#escape
stoploop=True

#blockloop
for B in range (nBlocks):
    if stoploop==True:
        blok_start.draw()
        win.flip()
        event.waitKeys(keyList="space")
        
        #trialloop
        for T in range (8):
            #maskeren
            verticale_grating.draw()
            win.flip()
            core.wait(1)
            
            #test-grating
            ##bepalen van de hoek 
            grating.ori=hoek_lijst[T]
            Matrix[T,1]=grating.ori
            ##juiste antwoord stockeren in matrix
            if grating.ori==30:
                Matrix[T,2]="j"
            else:
                Matrix[T,2]="f"
            ##bepalen van sf
            grating.sf=sf_lijst[T]
            ##tekenen van grating
            grating.draw()
            win.flip()
            ##tijd op het scherm aangeven
            core.wait(time_array[B])
            
            #maskeren
            verticale_grating.draw()
            win.flip()
            #event.waitKeys(keyList=["f","j", "escape"])
            
            #Response
            Response = event.waitKeys(keyList = ["f","j","escape"])
            if Response[0]=="escape":
                stoploop=False
                break
            else:
                Matrix[T,3]=Response[0]
            
            #feedback
            if Matrix [T,2]==Matrix[T,3]:
                feedback.text= "Correct!"
            else:
                feedback.text="Verkeerd antwoord!"
            feedback.draw()
            win.flip()
            time.sleep (1)


#matrix printen
print(Matrix)

#afscheid
afscheid.draw()
win.flip()
event.waitKeys(keyList="space")


#window sluiten
win.close()