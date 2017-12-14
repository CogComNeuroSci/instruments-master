"""
some I/O testing in a basic "experiment"
modularized version for the practice of functions (Lesson 9)

"""

# import modules
import time
from psychopy import visual, event, core, sound, gui
import numpy as np
from numpy import random

# initialize the window
win = visual.Window(size=[500,400])

# initializing
my_clock = core.Clock()
RT = [] ## empty list
n_trials = 3
key_list = ["f","j"]
correct_list = ["f","f","j"]
my_mouse = event.Mouse()

# graphical elements
text_ready = visual.TextStim(win,text="are you ready...?")
text_go = visual.TextStim(win,text="Go!")
text_correct = visual.TextStim(win,text="correct :-)")
text_error = visual.TextStim(win,text="wrong :-(")

def check_input_device():
    info={"input device":["keyboard","mouse"]}
    deviceDlg = gui.DlgFromDict(dictionary=info,title="Input device")
    if info["input device"]=="keyboard":
        return "keyboard"
    else:
        return "mouse"

# get-ready function; it doesn't return anything, but it does something on the screen
def get_ready(max_wait = 5):
    n = random.randint(1,max_wait+1) ## wait a sec (or two); note that n is a local variable
    text_ready.draw()
    win.flip()
    time.sleep(n)
    text_go.draw()
    win.flip()

def readout_keys():
    my_clock.reset()
    keys = event.waitKeys(keyList = ["f","j"])
    return keys

def readout_mouse():
    my_clock.reset()
    event.clearEvents(eventType="mouse")
    my_mouse.clickReset()
    while np.sum(my_mouse.getPressed())==0:
        pass
    keys = my_mouse.getPressed()
    if keys[0]==1:
        return key_list[0]
    else:
        return key_list[1]
    
# check what type of feedback must be given
def feedback(response):
    if response[-1] in correct_list[loop]:
        text_correct.draw()
    else:
        text_error.draw()
    win.flip()
    time.sleep(1)

# start the process
input = check_input_device()
for loop in range(n_trials):
    ## get them ready; they wait for maximally 5 seconds in the line below
    get_ready(5)
    ## start actual trial
    if input=="keyboard":
        response = readout_keys()
    else:
        response = readout_mouse()
    ## they have pressed something
    RT.append(my_clock.getTime())
    ## check what feedback must be given to this response
    feedback(response)

# display the average RT for one second
meantime = np.mean(RT)
text_feedback = visual.TextStim(win,text="mean RT = {0:.1f} sec".format(meantime),pos=[0,0.5])
text_feedback.draw()
win.flip()
time.sleep(1)

# wrap it up
win.close()