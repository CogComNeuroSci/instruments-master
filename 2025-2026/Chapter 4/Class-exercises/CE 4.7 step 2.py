# Importing modules
## Below we first import the numpy module for sampling the normal distribution,
## the time module for timing the updating of the display
## and the visual module for drawing stimuli on the screen.
## this is an updated version because the combination of ints and numpy.arrays is treated subtly different
## in this version....
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
stim = visual.TextStim(win, text = "test", pos = (0.0,0.5))

# Increase the value to 100
while value < end_value:
    ## we sample from the normal distribution with mean 0.10 and sd 0.025
    adjustment = numpy.random.normal(loc = mean, scale = sd, size = 1)

    ## update the current value
    value = value + adjustment*value

    ## Adjust the green and blue rgb values (you can do this in one line, but I tried to make it understandable)
    # in general, we want the color (+1, blue_green, blue_green)    initial (+1, +1, +1)  -> (+1, -1, -1)
    # if value goes from 1 to 100..... then blue_green goes from +1 to -1
    # if value goes from 1 to 100. .... then (value/50 - 1) goes from -1 to +1
    # if value goes from 1 to 100. .... then -(value/50 - 1) goes from +1 to -1
    
    blue_green = -((value[0]/50)-1)
    # check the edge cases!!!
    if blue_green < -1: #    blue_green = -1.2   --> blue_green = -1
        blue_green = -1

    ## Adjust the text and the color of the message
    stim.text   = f"Current bitcoin value: {value[0]:.2f} euro"
    stim.color  = (1, blue_green, blue_green)

    ## Display the message with the current value
    ## Flip the screen and hold for a bit
    stim.draw()
    win.flip()
    time.sleep(0.1)

# Close the window at the end of the presentation.
time.sleep(1)
win.close()

#The Bitcoin exercise is challenging. Uncomment the two lines below to see explanations of the code above
#import webbrowser
#webbrowser.open('https://pp02bevragingen.ugent.be/BitcoinHelp/step2.pptx')