"""
some I/O testing in a basic "experiment"

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
key_list = ["f","j"]
correct_list = ["f","f","j"]

## This code can be used if you have trouble with an azerty keyboard.
##key_qwerty=["a","z"] # incomplete list!
##key_azerty=["q","w"] # incomplete list!
##key_board_azerty = False # switch the lists above if you use AZERTY

# feedback sound elements
## checking the audio library just to be sure
print 'Using %s(with %s) for sounds' % (sound.audioLib, sound.audioDriver)
## make the sounds
sound_duration = 0.25
sound_to_play = sound.Sound("A",octave=1,secs=sound_duration,stereo=True)

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
        current_sound = 4
        sound_adjustment = 0.2
    else:
        text_error.draw()
        current_sound = 3
        sound_adjustment = -0.2
    win.flip()
    for soundi in range(5):
        current_sound = current_sound + sound_adjustment
        sound_to_play = sound.Sound("A",octave=current_sound,secs=sound_duration,stereo=True)
        sound_to_play.play()
        time.sleep(sound_duration)

# display the average RT for one second
meantime = np.mean(RT)
text_feedback = visual.TextStim(win,text="mean RT = {0:.1f} sec".format(meantime),pos=[0,0.5])
text_feedback.draw()
win.flip()
time.sleep(1)

# wrap it up
win.close()