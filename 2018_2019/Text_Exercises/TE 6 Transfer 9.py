# import the necessary modules
from my_functions import fixationCross
from psychopy import visual
 
# define a window
win = visual.Window(size = [500, 400])
 
# display the fixation cross
fixationCross(win, 2)
 
# close the window
win.close()
