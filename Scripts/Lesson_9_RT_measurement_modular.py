# some I/O testing in a basic "experiment"
# modularized version for the practice of functions (Lesson 9)
# import stuff
from psychopy import visual, event, core, sound, gui
import numpy as np
from numpy import random
import time

# initialize global variables
win = visual.Window(size=[500,400])
text1 = visual.TextStim(win,text="are you ready...? ")
text2 = visual.TextStim(win,text="Go!")
text_correct=visual.TextStim(win,text="correct :-)")
text_wrong=visual.TextStim(win,text="wrong :-(")
clock=core.Clock()
muis = event.Mouse()
response_time=[] ## empty list for response time
n_trial=3
key_list=["f","j"]
correct_list=["f","f","j"]
sound_duration=1.5
right_sound=sound.Sound("A",octave=5,secs=sound_duration,stereo=True)
wrong_sound=sound.Sound("A",octave=3,secs=sound_duration,stereo=True)

def check_input_device():
    info={"input device":"keyboard"}
    deviceDlg = gui.DlgFromDict(dictionary=info,title="Input device")
    if info["input device"]=="keyboard":
        return "keyboard"
    else:
        return "mouse"

# get-ready function; it doesn't return anything, but it does something on the screen
def get_ready(max_wait = 3):
    n = random.randint(1,max_wait) ## wait a sec (or two); note that n is a local variable
    text1.draw()
    win.flip()
    time.sleep(n)
    text2.draw()
    win.flip()

def readout_keys():
    clock.reset()
    keys=[""]
    while not keys[-1] in key_list:
        keys=event.waitKeys()
    return keys[-1]

def readout_mouse():
    event.clearEvents(eventType="mouse")
    muis.clickReset()
    clock.reset()
    while np.sum(muis.getPressed())==0:
        pass
    keys = muis.getPressed()
    if keys[0]==1:
        return key_list[0]
    else:
        return key_list[1]

# check what type of feedback must be given
def feedback(response):
    if response[-1] in correct_list[loop]:
        text_to_write = text_correct
        sound_to_play = right_sound
    else:
        text_to_write = text_wrong
        sound_to_play= wrong_sound
    return text_to_write, sound_to_play

# start the process
input = check_input_device()
for loop in range(n_trial):
    ## get them ready; they wait for maximally 3 seconds in the line below
    get_ready(3)
    ## start actual trial
    if input=="keyboard":
        response = readout_keys()
    else:
        response = readout_mouse()
    ## they have pressed something
    response_time.append(clock.getTime())
    ## check what feedback must be given to this response
    text_to_write, sound_to_play = feedback(response)
    text_to_write.draw()
    win.flip()
    sound_to_play.play()
    core.wait(sound_duration)

# wrap it up
meantime=np.mean(response_time)
text3 = visual.TextStim(win,text="mean RT = {0:.1f} sec".format(meantime),pos=[0,0.5])
text3.draw()
win.flip()
time.sleep(1)
win.close()
core.quit()