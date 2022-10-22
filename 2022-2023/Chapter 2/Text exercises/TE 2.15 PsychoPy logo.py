# goal of this code: make a window, draw a window, and close it finally.

from psychopy import visual
# visual is a module from psychopy containing several visual methods

import time 
# time is a module from python containing several time-related methods
# Hence, the window will be shown for 3 seconds exactly

win = visual.Window([400,400])

grating = visual.GratingStim(win, mask = "circle", ori = 30, sf = 4)

grating.draw()

win.flip()
time.sleep(3)
win.close()