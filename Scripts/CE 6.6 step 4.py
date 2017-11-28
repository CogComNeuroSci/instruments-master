# Importing modules
## Below we first import the numpy module for sampling the normal distribution,
## the time module for timing the updating of the display
## and the visual module for drawing stimuli on the screen.
import numpy, time
from psychopy import visual, event

# Global variables
## There are number of variables that stay the same across the entire assignment.
## These are initialized here as integers, which is logical because we don't want them to be mutable.
start_value = 1
end_value = 100
value = [start_value,start_value,start_value,start_value]
mean = 0.10
sd = 0.025

# Initialise list to track value over time
value_list = [[start_value,start_value,start_value,start_value]]

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(fullscr = True, color = (-1,-1,-1), units="norm")

# Increase the value to 100
while (True not in [x > end_value for x in value]):

    temp = [0,0,0,0]
    for f in range(len(value)):
        ## we sample from the normal distribution with mean 0.10 and sd 0.025
        adjustment = numpy.random.normal(loc=mean, scale=sd, size=1)

        ## update the current value
        value[f] = value[f] + adjustment*value[f]
        
        ## update the temporary storage
        temp[f] = value[f]

    ## append the current value to the list
    value_list.append(temp)
    del temp

    ## display the message with the current value
    disp_text = "Current bitcoin value: \n {0:.1f} euro, \t {1:.1f} euro \n {2:.1f} euro, \t {3:.1f} euro".format(int(value[0]),int(value[1]),int(value[2]),int(value[3]))
    stim = visual.TextStim(win,text=disp_text,pos=(0.0,0.5))
    stim.draw()

    ## draw evolving value
    for f in range(len(value)):
        for i in range(1,len(value_list)):
            start = ((value_list[i-1][f])/100) - 0.8
            stop = ((value_list[i][f])/100) - 0.8
            curve = visual.Line(win, start=(-0.52 + 0.02*i,start), end=(-0.50 + 0.02*i,stop))

            ## Adjust the red, green and blue rgb values (for a nice color gradient in the curve)
            if f == 0:
                red = 1
                green = -((round(value_list[i][f])/50)-1)
                blue = -((round(value_list[i][f])/50)-1)
            elif f == 1:
                red = -((round(value_list[i][f])/50)-1)
                green = 1
                blue = -((round(value_list[i][f])/50)-1)
            elif f == 2:
                red = -((round(value_list[i][f])/50)-1)
                green = -((round(value_list[i][f])/50)-1)
                blue = 1
            elif f == 3:
                red = ((round(value_list[i][f])/50)-1)
                green = ((round(value_list[i][f])/50)-1)
                blue = ((round(value_list[i][f])/50)-1)

            if red < -1:
                red = -1
            if green < -1:
                green = -1
            if blue < -1:
                blue = -1

            curve.lineColorSpace = "rgb"
            curve.lineColor = (red,green,blue)
            curve.lineWidth = 2
            curve.draw()

    win.flip()
    time.sleep(0.1)
    
    if event.getKeys():
        break

# Close the window at the end of the presentation
while not event.getKeys():
    pass
win.close()