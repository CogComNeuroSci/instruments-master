# Importing modules
import time, numpy
from psychopy import visual

# Display preparation
win = visual.Window(size = [800, 800], color = (-1,-1,-1), units = "norm")

# Prepare the graphical elements
message = visual.TextStim(win, text = "test")
dot     = visual.Circle(win, radius = 0.05)

# Determine the number of dots
ndots = 10

# Display the welcome message
message.text = "Welcome!"
message.draw()
win.flip()
time.sleep(1)

for trial in range(8):
    
    ## Sample from the normal distribution for the color
    red = numpy.random.normal(loc = 0, scale = 0.5, size = ndots)
    red[red < -1] = -1
    red[red >  1] =  1
    
    ## Sample from the normal distribution for the position
    pos_h = numpy.random.normal(loc = 0, scale = 0.5, size = ndots)
    pos_v = numpy.random.normal(loc = 0, scale = 0.5, size = ndots)
    pos_h[pos_h < -0.9] = -0.9
    pos_h[pos_h >  0.9] =  0.9
    pos_v[pos_v < -0.9] = -0.9
    pos_v[pos_v >  0.9] =  0.9
    
    # Display the dots
    for doti in range(ndots):
        dot.color = [red[doti],-1,-red[doti]]
        dot.pos = (pos_h[doti], pos_v[doti])
        dot.draw()
    win.flip()
    time.sleep(1)
    
    # Determine whether the dots are on average more red or more blue
    if numpy.mean(red) > 0.05:
        message.text = "More red"
        message.color = [1,-1,-1]
    elif numpy.mean(red) < -0.05:
        message.text = "More blue"
        message.color = [-1,-1,1]
    else:
        message.text = "Equal"
        message.color = [1,1,1]
    message.draw()
    win.flip()
    time.sleep(1)
    
    if trial == 3:
        # Display the break message
        message.text = "Take a break"
        message.color = [1,1,1]
        message.draw()
        win.flip()
        time.sleep(1)


# Display the goodbye message
message.text = "The end!"
message.color = [1,1,1]
message.draw()
win.flip()
time.sleep(1)

# Close the experiment window
win.close()
