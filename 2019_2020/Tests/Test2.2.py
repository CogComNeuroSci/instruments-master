# Importing modules
import time, numpy
from psychopy import visual

# Display preparation
win = visual.Window(size = [800, 800], color = (-1,-1,-1), units = "norm")

# Prepare the graphical elements
message = visual.TextStim(win, text = "test")
dot     = visual.Circle(win, radius = 0.05)
   
## Sample from the normal distribution for the color
red = numpy.random.normal(loc = 0, scale = 0.5, size = 1)
red[red < -1] = -1
red[red >  1] =  1

# Display the welcome message
message.text = "Welcome!"
message.draw()
win.flip()
time.sleep(1)

# Display the dot
dot.color = [red,-1,-red]
dot.draw()
win.flip()
time.sleep(1)

# Display the goodbye message
message.text = "The end!"
message.draw()
win.flip()
time.sleep(1)

# Close the experiment window
win.close()
