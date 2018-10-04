# Importing modules
## Below we first import the numpy module for sampling the normal distribution,
## the time module for timing the updating of the display
## and the visual module for drawing stimuli on the screen.
import numpy, time
from psychopy import visual

# Global variables
## There are a number of variables that stay the same across the entire assignment.
## These are initialized here as integers, which is logical because we don't want them to be mutable.
start_value = 1
end_value = 100
value = start_value
mean = 0.10
sd = 0.025

# Increase the value to 100
while value < end_value:
    ## we sample from the normal distribution with mean 0.10 and sd 0.025
    adjustment = numpy.random.normal(loc = mean, scale = sd, size = 1)

    ## update the current value
    value = value + adjustment*value

    ## printing the result for debugging purposses
    print(numpy.ndarray.round(value))