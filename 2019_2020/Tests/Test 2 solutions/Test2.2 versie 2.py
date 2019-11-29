# Importing modules
import time, numpy
from psychopy import visual

# Display preparation
win = visual.Window(size = [800, 800], color = (-1,-1,-1), units = "norm")

# Prepare the graphical elements
message = visual.TextStim(win, text = "test")
dot     = visual.Circle(win, radius = 0.03)

# Determine the number of dots
ndots = 1

## Sample from the normal distribution for the color
hue = numpy.random.normal(loc = 0, scale = 0.5, size = ndots)
hue2 = hue * 2
R = numpy.repeat(-1.,ndots)
G = numpy.repeat(1.,ndots)
B = numpy.repeat(-1.,ndots)
R[hue < 0] = -1
G[hue < 0] = hue2[hue < 0]+1
B[hue < 0] = -(hue2[hue < 0]+1)
R[hue > 0] = hue2[hue > 0]-1
G[hue > 0] = 1
B[hue > 0] = -1

R[R < -1] = -1
R[R >  1] =  1
G[G < -1] = -1
G[G >  1] =  1
B[B < -1] = -1
B[B >  1] =  1

# Display the welcome message
message.text = "Welcome!"
message.draw()
win.flip()
time.sleep(1)

# Display the dot
dot.color = [R[0],G[0],B[0]]
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
