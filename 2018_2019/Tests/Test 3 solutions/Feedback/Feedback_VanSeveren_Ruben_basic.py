#alle benodigdheden importeren

from psychopy import visual, event, core, gui
import numpy, time

#window aanmaken

win = visual.Window(size = [600,500], units = "norm")

#dialog box aanmaken

info = {"Naam": "voornaam", "Nummer":0, "Leeftijd":0, "gender": ["man","vrouw","derde gender"], "handvoorkeur": ["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Experiment")
if infoDlg.OK:
    print(info)
else:
    print("User Cancelled")

#Welcome
welcome = visual.TextStim(win,text="Welkom {0}! Druk op de spatie toets om verder te gaan!".format(info["Naam"]))
Instructies = visual.TextStim(win, text = "Als de stimulus naar links gedraaid is (de lijnen lopen van linksboven naar rechtsonder), druk 'f'. Als de stimulus naar rechts gedraaid is (de lijnen lopen van rechtsboven naar linksonder), druk 'j'. Druk op de spatie toets om verder te gaan!")

welcome.draw()
win.flip()
### Esther: je hoeft "space" niet in een lijst te steken
event.waitKeys(keyList = ["space"]) 

Instructies.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#functies definiëren



#stimuli definiëren
Gabor_stimulus_vertical = visual.GratingStim(win, mask = "gauss",units = "deg", ori = 180, sf = 20)
#Orientation = [("180","210")]
#SF = [("2","20")]
#Gabor_stimuli = visual.GratingStim(win, mask = "gauss", units = "deg", ori = Orientation, sf = SF)

#loop
for j in range(1):
    
    Block1 = visual.TextStim(win, text = "Blok 1 gaat dadelijk beginnen, druk op spatie om verder te gaan!")
    Block1.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    for i in range (8):
        Gabor_stimulus_vertical.draw()
        win.flip()
        core.wait(1)
        #Gabor_stimuli.draw()
        #win.flip()
        ### Esther: deze durations zouden 10 keer te groot zijn
        #core.wait(0.16)
        
        
        #reactietijd meten
 

    Block2 = visual.TextStim(win, text = "Blok 2 gaat dadelijk beginnen, druk op spatie om verder te gaan!")
    Block2.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    for i in range(8):
        Gabor_stimulus_vertical.draw()
        win.flip()
        core.wait(1)
        #Gabor_stimuli.draw()
        #win.flip()
        #core.wait(0.33)
    Block2 = visual.TextStim(win, text = "Blok 3 gaat dadelijk beginnen, druk op spatie om verder te gaan!")
    Block2.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    for i in range(8):
        Gabor_stimulus_vertical.draw()
        win.flip()
        core.wait(1)
        #Gabor_stimuli.draw()
        #win.flip()
        #core.wait(0.50)





#afscheid 

afsluit = visual.TextStim(win, text = "Het experiment is gedaan, gelieve de proefleider te roepen.")
afsluit.draw()
win.flip()
k = event.waitKeys(keyList = "space")
win.close()

