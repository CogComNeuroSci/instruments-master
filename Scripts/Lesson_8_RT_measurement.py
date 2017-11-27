# some I/O testing in a basic "experiment"
# import stuff
from psychopy import visual, event, core
import numpy as np
from numpy import random
import time

# initialize stuff
win = visual.Window(size=[500,400])
tekst1 = visual.TextStim(win,text="are you ready...? ")
tekst2 = visual.TextStim(win,text="Go!")
tekst_juist=visual.TextStim(win,text="correct :-)")
tekst_fout=visual.TextStim(win,text="wrong :-(")
klok=core.Clock()
tijd=[] # empty list
n_trial=3
key_list=["f","j"]
correct_list=["f","f","j"]

# start the process
for loop in range(n_trial):
    n = random.randint(1,5) # wait a sec (or two)
    tekst1.draw()
    win.flip()
    time.sleep(n)
    tekst2.draw()
    win.flip()
    klok.reset() 
    keys=event.waitKeys(key_list)
    tijd.append(klok.getTime())
    if keys[-1] in correct_list[loop]:
        tekst_juist.draw()
    else:
        tekst_fout.draw()
    win.flip()
    time.sleep(1)

# wrap it up
meantime=np.mean(tijd)
tekst3 = visual.TextStim(win,text="mean RT = {0:.1f} sec".format(meantime),pos=[0,0.5])
tekst3.draw()
win.flip()
time.sleep(1)
win.close()