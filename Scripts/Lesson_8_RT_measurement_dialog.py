# some I/O testing in a basic "experiment", with an initial dialog box
# import stuff
from psychopy import visual, event, core, gui
import numpy as np
from numpy import random
import time

# initialize stuff
win = visual.Window(size=[500,400])
text1 = visual.TextStim(win,text="are you ready...? ")
text2 = visual.TextStim(win,text="Go!")
text_correct=visual.TextStim(win,text="correct :-)")
text_wrong=visual.TextStim(win,text="wrong :-(")
clock=core.Clock()
info={"name": "name", "subject nr": 1}
my_dialog=gui.DlgFromDict(dictionary=info,title="Give your data")
times=[] # empty list
n_trial=3
key_list=["f","j"]
correct_list=["f","f","j"]

# get prelim info
print(info)
# start the process
for loop in range(n_trial):
    n = random.randint(1,3) # wait a sec (or two)
    text1.draw()
    win.flip()
    time.sleep(n)
    text2.draw()
    win.flip()
    clock.reset() 
    keys=event.waitKeys(key_list)
    times.append(clock.getTime())
    if "escape" in keys:
        core.quit()
    if keys[-1] in correct_list[loop]:
        text_correct.draw()
    else:
        text_wrong.draw()
    win.flip()
    time.sleep(1)

# calculate stats
meantime=np.mean(times)
text3 = visual.TextStim(win,text="mean RT = {0:.1f} sec".format(meantime),pos=[0,0.5])
text3.draw()
win.flip()
while not event.getKeys():
    pass
win.close()