####################################
## Test program for Python timing ##
####################################

############
## import ##
############

from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim

import time
from time import sleep

## Draw fixations
## The circles will appear here
    ## When the key is pressed, the circle appear on screen with a delay of two seconds
## Press any key to escape

###############
## Fixations ##
###############

win = visual.Window(fullscr = True, units='height', color = 'grey')
win = visual.Window(fullscr = True, units='height', color = 'grey')

fixation1 = visual.Circle(win, radius = .005, pos=(-0.6667,0.3), fillColor = '#e6e6fa')
fixation2 = visual.Circle(win, radius = .005, pos=(0,0), fillColor = '#e6e6fa')
fixation3 = visual.Circle(win, radius = .005, pos=(0.6667,-0.3), fillColor = '#e6e6fa')

while not event.getKeys():
    fixation1.draw()
    fixation2.draw()
    fixation3.draw()
    win.flip()
    
###########
## Delay ##
###########

win.flip(clearBuffer=True)
time.sleep(2)

#######################
## Circles appearing ##
#######################

circle1 = visual.Circle(win, radius = .10, pos=(-0.6667,0.3), fillColor = 'black')
circle2 = visual.Circle(win, radius = .10, pos=(0,0), fillColor = 'black')
circle3 = visual.Circle(win, radius = .10, pos=(0.6667,-0.3), fillColor = 'black')

circle4 = visual.Circle(win, radius = .10, pos=(-0.6667,0.3), fillColor = 'white')
circle5 = visual.Circle(win, radius = .10, pos=(0,0), fillColor = 'white')
circle6 = visual.Circle(win, radius = .10, pos=(0.6667,-0.3), fillColor = 'white')

while not event.getKeys():
    circle1.draw()
    circle2.draw()
    circle3.draw()
    
    win.flip()
    time.sleep(1)
    win.flip(clearBuffer=True)

    circle4.draw()
    circle5.draw()
    circle6.draw()

    win.flip()
    time.sleep(1)
    win.flip(clearBuffer=True)
