# Importing modules
## Below we first import the numpy module for sampling the normal distribution,
## the time module for timing the updating of the display
## and the visual module for drawing stimuli on the screen.
import numpy, time
from psychopy import visual

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(fullscr = True, color = (-1,-1,-1), units = "norm")

# Initialize variables
## There are number of variables that stay the same across the entire assignment.
start_value     = 1
end_value       = 100
value           = start_value
mean            = 0.10
sd              = 0.025

# Initialize the graphical elements
stim    = visual.TextStim(win, text = "test", pos = (0.0,0.5))
curve   = visual.Line(win, start = (0,0), end = (0,0))
curve.lineColorSpace = "rgb"
curve.lineWidth = 2

# Initialize array to track value over time
value_array = numpy.array([value])

# Increase the value to 100
while value < end_value:
    ## we sample from the normal distribution with mean 0.10 and sd 0.025
    adjustment = numpy.random.normal(loc = mean, scale = sd, size = 1)

    ## update the current value
    value = value + adjustment*value

    ## append the current value to the list
    value_array = numpy.append(value_array, value)

    ## Adjust the green and blue rgb values (you can do this in one line, but I tried to make it understandable)
    blue_green = -((numpy.ndarray.round(value)/50)-1)
    if blue_green < -1:
        blue_green = -1

    ## Adjust the text and the color of the message
    stim.text   = "Current bitcoin value: {} euro".format(int(value))
    stim.color  = (1, blue_green, blue_green)

    ## draw evolving value
    for i in range(1,value_array.size):
        
        ## Adjust the green and blue rgb values (for a nice color gradient in the curve)
        blue_green = -((round(value_array[i])/50)-1)
        if blue_green < -1:
            blue_green = -1
        curve.lineColor = (1, blue_green, blue_green)
        
        ## determine the start and stop value of all the lines that make up the curve
        start_y         = (value_array[i-1]/100) - 0.8
        end_y           = (value_array[i]/100) - 0.8
        
        ## draw this piece of the curve
        curve.start     = (-0.52 + 0.02*i, start_y)
        curve.end       = (-0.50 + 0.02*i, end_y)
        curve.draw()

    ## Display the message with the current value
    ## Flip the screen and hold for a bit
    stim.draw()
    win.flip()
    time.sleep(0.1)

# Close the window at the end of the presentation
time.sleep(1)
win.close()