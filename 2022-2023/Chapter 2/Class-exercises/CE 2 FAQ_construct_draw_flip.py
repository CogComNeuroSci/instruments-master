# load the necessary modules
import time
from psychopy import visual

# open an experiment window
win = visual.Window(fullscr = True)

# step 1: construct
pumpkin = visual.Circle(win, color = 'orange', size = [1.5,1])
eyeR    = visual.Circle(win, color = 'black', size = [0.2,0.1], pos = ( 0.3,0.2))
eyeL    = visual.Circle(win, color = 'black', size = [0.2,0.1], pos = (-0.3,0.2))

# step 2: draw
pumpkin.draw()
eyeR.draw()
eyeL.draw()

# step 3: flip
win.flip()

# step 4: sleep/wait
time.sleep(1)

# the end!
win.close()