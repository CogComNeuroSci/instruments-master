"""
some I/O testing in a basic "experiment"

"""

# import modules
import time
from psychopy import visual, event, core
import numpy as np
from numpy import random

# initializing
my_clock = core.Clock()
time_list = [] ## empty list
n_trials = 3
key_list = ["f","j"]
correct_list = ["f","f","j"]

# graphical elements
win = visual.Window(size=[500,400])
text1 = visual.TextStim(win,text="are you ready...?")
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

    ## wait for the key press and register it
    keys = event.waitKeys(key_list)

    ## register the time
    time_list.append(my_clock.getTime())

    ## display the accuracy feedback (predetermined)
    if keys[-1] in correct_list[loop]:
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