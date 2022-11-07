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

# Initialize array to track the four values over time
value_array = numpy.array([value, value, value, value])

# Increase the value to 100
while numpy.any(value_array > 100) == False:
    
    ## adjust all four values
    ## we sample from the normal distribution with mean 0.10 and sd 0.025
    adjustment = numpy.random.normal(loc = mean, scale = sd, size = 4)

    ## update the current value
    value = value + adjustment*value

    ## append the current value to the list
    value_array = numpy.vstack([value_array, value])

# determine horizontal and vertical coordinates
nsteps = value_array.shape[0]
y_array = (value_array/100) - 0.8
x_array = -0.50 + (1/nsteps)*numpy.array(range(nsteps))

# determining the color gradient
adjusted_color_array = -((value_array/50)-1)

# Increase the value to 100
for step in range(value_array.shape[0]):

    ## Adjust the text and the color of the message
    stim.text   = "Current bitcoin value: \n {0} euro, \t {1} euro \n {2} euro, \t {3} euro".format(int(value_array[step,0]),int(value_array[step,1]),int(value_array[step,2]),int(value_array[step,3]))

    ## for each of the four values
    for f in range(value_array.shape[1]):
        
        ## draw evolving value
        for i in range(1,step):
            
            ## Adjust the red, green and blue rgb values (for a nice color gradient in the curve)
            adjusted_color = adjusted_color_array[i,f]
            
            if f == 0:
                curve.lineColor = (1,adjusted_color,adjusted_color)
            elif f == 1:
                curve.lineColor = (adjusted_color,1,adjusted_color)
            elif f == 2:
                curve.lineColor = (adjusted_color,adjusted_color,1)
            elif f == 3:
                curve.lineColor = (1,1,adjusted_color)
            
            ## draw this piece of the curve
            curve.start     = (x_array[i-1],  y_array[i-1,f])
            curve.end       = (x_array[i],    y_array[i,f])
            curve.draw()

    ## Display the message with the current value
    ## Flip the screen and hold for a bit
    stim.draw()
    win.flip()
    time.sleep(0.1)

# Close the window at the end of the presentation
time.sleep(1)
win.close()