# Importing modules
## Below we first import the numpy module for sampling the normal distribution,
## the time module for timing the updating of the display
## and the visual module for drawing stimuli on the screen.
import numpy, time
from psychopy import visual

# Global variables
## There are number of variables that stay the same across the entire assignment.
## These are initialized here as integers, which is logical because we don't want them to be mutable.
start_value = 1
end_value = 100
value = start_value
mean = 0.10
sd = 0.025

# Initialise list to track value over time
value_list = [value]

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(fullscr = True, color = (-1,-1,-1), units="norm")

# Increase the value to 100
while value < end_value:
    ## we sample from the normal distribution with mean 0.10 and sd 0.025
    adjustment = numpy.random.normal(loc = mean, scale = sd, size = 1)

    ## update the current value
    value = value + adjustment*value

    ## append the current value to the list
    value_list.append(value)

    ## Adjust the green and blue rgb values (you can do this in one line, but I tried to make it understandable)
    blue_green = -((numpy.ndarray.round(value)/50)-1)
    if blue_green < -1:
        blue_green = -1

    ## display the message with the current value
    disp_text = "Current bitcoin value: {:.1f} euro".format(int(value))
    stim = visual.TextStim(win,text=disp_text,color=(1,blue_green,blue_green),pos=(0.0,0.5))
    stim.draw()

    ## draw evolving value
    for i in range(1,len(value_list)):
        start = (value_list[i-1]/100) - 0.8
        stop = (value_list[i]/100) - 0.8
        curve = visual.Line(win, start=(-0.52 + 0.02*i,start), end=(-0.50 + 0.02*i,stop))
        curve.draw()

    win.flip()
    time.sleep(0.1)

# Close the window at the end of the presentation
time.sleep(1)
win.close()