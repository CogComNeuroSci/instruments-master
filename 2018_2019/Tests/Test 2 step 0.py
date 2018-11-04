# Importing modules
import numpy, time
from psychopy import visual

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(size = [600, 600], color = (-1,-1,-1), units = "norm")

# stationary solar sytem: celectial bodies positions
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!

# Prepare the graphical elements
sun     = visual.Circle(win, radius=0.15, color = "yellow")
planet  = visual.Circle(win, radius=0.07, color = "blue", pos = [Planetx,Planety])
moon    = visual.Circle(win, radius=0.02, color = "white", pos = [Planetx+Moonx,Planety+Moony])

# display the celestial bodies
sun.draw()
planet.draw()
moon.draw()
win.flip()
time.sleep(1)

# the end!
win.close()