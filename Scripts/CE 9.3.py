"""
some I/O testing in a basic "experiment"
modularized version for the practice of functions (Lesson 9)

"""

# import modules
import time
from psychopy import visual, event, core, sound
import numpy as np
from numpy import random

# initialize the window
win = visual.Window(size=[500,400])

# initializing
my_clock = core.Clock()
RT = [] ## empty list
n_trials = 3
correct_list = ["left","left","right"] ## right-click means double-click on a Mac
my_mouse = event.Mouse()

# graphical elements
text_ready = visual.TextStim(win,text="are you ready...?")
text_go = visual.TextStim(win,text="Go!")
text_correct = visual.TextStim(win,text="correct :-)")
text_error = visual.TextStim(win,text="wrong :-(")

# get-ready function; it doesn't return anything, but it does something on the screen
def get_ready(max_wait = 5):
    n = random.randint(1,max_wait+1) ## wait a sec (or two); note that n is a local variable
    text_ready.draw()
    win.flip()
    time.sleep(n)
    text_go.draw()
    win.flip()

def readout_mouse():
    my_clock.reset()
    event.clearEvents(eventType="mouse")
    my_mouse.clickReset()
    while np.sum(my_mouse.getPressed())==0:
        pass
    keys = my_mouse.getPressed()
    return keys

# check what type of feedback must be given
def feedback(response):
    if (response[0]==1 and correct_list[loop]=="left") or (response[2]==1 and correct_list[loop]=="right"):
        text_correct.draw()
    else:
        text_error.draw()
    win.flip()
    time.sleep(1)

# start the process
for loop in range(n_trials):
    ## get them ready; they wait for maximally 5 seconds in the line below
    get_ready(5)
    ## start actual trial
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