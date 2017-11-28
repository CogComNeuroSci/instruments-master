"""
some I/O testing in a basic "experiment"
now for a mouse button press readout

"""

# import modules
import time
from psychopy import visual, event, core
import numpy as np
from numpy import random

# initialize the window
win = visual.Window(size=[500,400])

# initializing
my_clock = core.Clock()
time_list = [] ## empty list
n_trials = 3
correct_list = ["left","left","right"] ## right-click means double-click on a Mac
my_mouse = event.Mouse()

# graphical elements
text1 = visual.TextStim(win,text="are you ready to push a mouse button...?")
text2 = visual.TextStim(win,text="Go!")
text_correct = visual.TextStim(win,text="correct :-)")
text_error = visual.TextStim(win,text="wrong :-(")

# response registration
for loop in range(n_trials):

    ## display the first message and wait a second (or two)
    n = random.randint(1,5)
    text1.draw()
    win.flip()
    time.sleep(n)

    ## display the second message
    text2.draw()
    win.flip()

    ## reset the clock to measure the RT
    my_clock.reset() 

    ## remove any remaining mouse events 
    event.clearEvents(eventType="mouse")
    
    ## wait for the mouse press and register it
    while np.sum(my_mouse.getPressed())==0:
        pass

    ## register the time
    time_list.append(my_clock.getTime())

    ## display the accuracy feedback (predetermined)
    if (my_mouse.getPressed()[0]==1 and correct_list[loop]=="left") or (my_mouse.getPressed()[2]==1 and correct_list[loop]=="right"):
        text_correct.draw()
    else:
        text_error.draw()
    win.flip()
    time.sleep(1)

# display the average RT for one second
meantime = np.mean(time_list)
text3 = visual.TextStim(win,text="mean RT = {0:.1f} sec".format(meantime),pos=[0,0.5])
text3.draw()
win.flip()
time.sleep(1)

# wrap it up
win.close()