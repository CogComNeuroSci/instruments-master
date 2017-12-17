"""
some I/O testing in a basic "experiment"

"""

# import modules
import time
from psychopy import visual, event, core, sound
import numpy as np
from numpy import random
from psychopy import gui

# initialize the window
win = visual.Window(size=[500,400])

# initializing
my_clock = core.Clock()
RT = [] ## empty list
n_trials = 3
key_list = ["f","j"]
correct_list = ["f","f","j"]

## This code can be used if you have trouble with an azerty keyboard.
##key_qwerty=["a","z"] # incomplete list!
##key_azerty=["q","w"] # incomplete list!
##key_board_azerty = False # switch the lists above if you use AZERTY

# create a DlgFromDict
info = {    "Participant":  "", 
            "Number":       0,
            "Gender":       ["female", "male"],
            "Age":          0,
            "ExpNr":        2017.6}
infoDlg = gui.DlgFromDict(  dictionary  =info, 
                            title       ="Class Exercise 8.4",
                            order       =["Participant", "Number", "Gender", "Age"],
                            fixed       =["ExpNr"])  ## this attribute can't be changed by the user

print("Participant {0}, Number {1}, Gender {2}, Age {3}".format(info["Participant"], info["Number"], info["Gender"], info["Age"]))

# welcome the participant
text_welcome = visual.TextStim(win,text="Welcome to the experiment {0}!".format(info["Participant"]))
text_welcome.draw()
win.flip()
time.sleep(3)

# graphical elements
text_ready = visual.TextStim(win,text="are you ready...?")
text_go = visual.TextStim(win,text="Go!")
text_correct = visual.TextStim(win,text="correct :-)")
text_error = visual.TextStim(win,text="wrong :-(")

# response registration
for loop in range(n_trials):

    ## display the first message and wait a second (or two)
    n = random.randint(1,6)
    text_ready.draw()
    win.flip()
    time.sleep(n)

    ## display the second message
    text_go.draw()
    win.flip()

    ## reset the clock to measure the RT
    my_clock.reset() 

## This code can be used if you have trouble with an azerty keyboard.
##    keys=[""]
##    while not keys[0] in key_list:
##        keys=event.waitKeys()
##        if key_board_azerty==True and keys[0] in key_azerty:
##            keys[0] = key_qwerty[key_azerty.index(keys[0])]

    ## wait for the key press and register it
    keys = event.waitKeys(keyList = ["f","j"])

    ## register the time
    RT.append(my_clock.getTime())

    ## display the accuracy feedback (predetermined)
    if keys[-1] in correct_list[loop]:
        text_correct.draw()
    else:
        text_error.draw()
    win.flip()
    time.sleep(1)

# display the average RT for one second
meantime = np.mean(RT)
text_feedback = visual.TextStim(win,text="mean RT = {0:.1f} sec".format(meantime),pos=[0,0.5])
text_feedback.draw()
win.flip()
time.sleep(1)

# wrap it up
win.close()