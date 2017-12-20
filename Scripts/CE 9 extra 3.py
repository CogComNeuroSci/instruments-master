"""
CE 9: additional explanation on the use of break in functions

Some of you have tried to make a function in which a break command is issued.

This is not an option. Just try to comment out the break command in the code below.
You'll get an error message: break can't be used if it's not directly inside of a loop.

So if you want to break from a loop, you'll have to do it directly in the loop and 
not via a function that is used in the loop.

"""

from psychopy import visual, event, core, gui

# initialize the window
win = visual.Window([500,400])

# Make the text object and insert a string
TextObject      = visual.TextStim(win, text = "Time to escape!")
FixationCross   = visual.TextStim(win, text = "+")

# make the function
def myESCfunction():
    ## Escape function to get out of the trial loop
    if "f" in event.waitKeys():
        #break
        pass

# while-loop from which to escape with a break
while True:
    TextObject.draw()
    win.flip()
    ## Escape function to get out of the trial loop
    if "f" in event.waitKeys():
        break
