# goal of this code: make a window, draw a window, and close it finally.

from psychopy import visual
# visual is a module from psychopy containing several visual methods

import time 
# time is a module from python containing several time-related methods
# Hence, the window will be shown for 3 seconds exactly

win = visual.Window([600,400])
stim = visual.TextStim(win, text = "hello world!", color = (0,1,0))
rect = visual.Rect(win, width = 2, height = 2, lineColor = (1,0,0))

stim.draw()
rect.draw()

win.flip()
time.sleep(3)
win.close()