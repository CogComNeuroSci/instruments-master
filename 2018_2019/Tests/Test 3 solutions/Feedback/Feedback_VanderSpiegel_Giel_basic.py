#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import modules

### Esther: importeren van functies voor de sound stimuli zijn niet nodig

#from psychopy import prefs
#prefs.general['audioLib'] = ['pyo']
from psychopy import visual, event, core, gui
import time, numpy

#initialise the dialogue box

# create a dialog box
### Esther: waarom dit in een functie plaatsen? Op die manier weet je enkel de info over de naam van de participant maar niets anders
def dialoguebox():
    ### Esther: kies misschien een niet-gebruikt proefpersoon nummer als de default
    info = {"Participant number":20, "Participant name":"Unknown", "Gender":["male", "female","third gender"], "Age":0, 'hand preference':['left','right','ambiodextrous']}
    infoDlg = gui.DlgFromDict(dictionary=info, title="Stroop Experiment")
    if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
        print(info)
    else:
        print("User Cancelled")
        exit()
    participant = info ["Participant name"]
    return participant

# create a window to draw in
### Esther: deze allowGUI=False komt waarschijnlijk ook uit de gabor.py demo
win = visual.Window(units = 'norm', size = [600, 500], allowGUI=False)

#some variables for the text
duration = 0
participant = dialoguebox()
nblocks = 3
ntrials = 8
durationgabor = numpy.array ([0.016,0.033,0.050])
orientatiegabor = numpy.array ([90, 45, 135])

#dit is wat ik zou gebruiken om de antwoorden en reactietijden op te slaan
lijst=[]
tijd=[]

#
#Welcome         = visual.TextStim(win, text = "Welcome"+participant)
#Welcome.draw()
#win.flip()
#event.waitKeys(keyList=["space"])

#Instructions    = visual.TextStim(win, text = "you will receive some gabor stimuli to which you have to react."
#                    "\nIf the stimulus is oriented to the left (the lines go from the upper left to the lower right) you will need to press the f key."
#                    "\nif the stimulus is oriented to the right (the lines go from the upper right to the lower left) you will need to press the j key"
#                    "\n\npress space to continue")
#instructions.draw()
#win.(flip)
#event.waitKeys(keyList=["space"])
#Block_start     = visual.TextStim(win, text = "OK")
#Block_start.draw()
#win.flip()
#event.waitKeys(keyList=["space"])
#Feedback        = visual.TextStim(win, text = "OK")
#feedback.draw()
#win.flip()
#event.waitKeys(keyList=["space"])
#Goodbye         = visual.TextStim(win, text = "Goodbye + participant + !", pos = (0,0.75), height = 0.2)
#Goodbye.draw()
#win.flip()
#event.waitKeys(keyList=["space"])


# initialize graphical elements
MessageOnSCreen = visual.TextStim(win, text = "OK")
Instructions_text = ("you will receive some gabor stimuli to which you have to react."
                    "\nIf the stimulus is oriented to the left (the lines go from the upper left to the lower right) you will need to press the f key."
                    "\nif the stimulus is oriented to the right (the lines go from the upper right to the lower left) you will need to press the j key"
                    "\n\npress space to continue")

# make a function for presenting messages on screen
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    MessageOnSCreen.color   = color
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

# display the welcome message
message(message_text = "Welcome " + participant + "!\n\nPress the space bar to continue.", response_key = "space")

# display the instructions
message(message_text = Instructions_text, response_key = "space",)

# announce that the practice phase is about to start
message(message_text = "a new block will start. This is block {0}".format(1), response_key = "space")



#
##ongeveer deze structuur gebruiken voor de gabor stimuli blocken maar natuurlijk wel aangepast voor deze taak en niet voor de strooptaak
#for b in range(nblocks):
#    
#    # announce what block is about to start
#    Block_start.text = "Block " + str(b+1) + " will start now"
#    Block_start.draw()
#    win.flip()
#    time.sleep(1)
#    
#    # in 8 trials
#    for i in range(b*ntrials,(b+1)*ntrials):
#dit is sowieso de functie die ik wil gebruiken voor het escapen aan de trial
### Esther: niet zo'n goed idee, je wil niet gewoon alles quiten, gewoon ontsnappen aan de trials en de participant vaarwel zeggen
#       if event.getKeys(keyList=['escape']):
#            win.close()
#            core.quit()
#
# wanneer de proefpersoon geen jusit antwoord geeft zullen we gewoon 
#if k == None:
#        k=[""]

#voor de reactietijden te meten zou ik opteren voor de core.MonotonicClock functie
### Esther: deze klok kan je niet herzetten wanneer je wil, dus alles hangt af van de rest van je code
trial_timer = core.MonotonicClock()

##dit zou ik gebruiken voor de verticale gabor stimulus een seconde lang te tonen.
timer = core.CountdownTimer(1)
### Esther: niet fout, maar time.sleep(1) volstaat ook

def verticalegabor():
# INITIALISE SOME STIMULI
    gabor = visual.GratingStim(win, tex="sin", mask="circle", texRes=256, 
               size=[1.0, 1.0], sf=[4, 0], ori = 90, name='gabor1')
    ### Esther: je hebt zeker geen autoDraw nodig in dit experiment, let op met wat je overneemt uit andere scripts
    gabor.autoDraw = True
    message = visual.TextStim(win, units = 'norm', pos=(0.0, -0.9), text='Hit Q to quit')
    trialClock = core.Clock()
    
    # repeat drawing for each frame
    while timer.getTime() > 0: 
        gabor.phase += 0.01
        message.draw()
        # handle key presses each frame
        if event.getKeys(keyList=['escape', 'q']):
            win.close()
            core.quit()
        win.flip()

verticalegabor()
win.close()
core.quit()

#dit is hoe ik ongeveer de minder lange gabor stimuli zou willen tonen
#def gaborkleinestimuli():
#    timer = core.CountdownTimer(i)
#    
#    gabor = visual.GratingStim(win, tex="sin", mask="circle", texRes=256, 
#               size=[1.0, 1.0], sf=[4, 0], ori = orientatiegabor, name='gabor1')
#    gabor.autoDraw = True
#    message = visual.TextStim(win, units = 'norm', pos=(0.0, -0.9), text='Hit Q to quit')
#    trialClock = core.Clock()
#    
#    # repeat drawing for each frame
#    while timer.getTime() > 0: 
#        gabor.phase += 0.01
#        message.draw()
#        # handle key presses each frame
#        if event.getKeys(keyList=['escape', 'q']):
#            win.close()
#            core.quit()
#        win.flip()
#
#for i in range(durationgabor):
#    gaborkleinestimuli()
# The contents of this file are in the public domain.

#waarschijnlijk zou ik het wel vinden maar jammer genoeg niet in 3 uur de tijd, waarschijnlijk over een paar dagen wel.