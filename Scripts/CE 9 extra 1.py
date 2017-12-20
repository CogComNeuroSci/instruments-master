"""
CE 9: additional explanation on adjusting properties in loops

Some of you have encountered problems when trying to adjust 
an object (such as a text object) inside of a loop.

Below we demonstrate a few of the common mistakes and
provide a bit of explanation and a solution.

"""

from psychopy import visual, event, core, gui

# initialize the window
win = visual.Window([500,400])

# Make the text object and insert a string
TextString      = "Just a bit of text"
TextObject      = visual.TextStim(win, text = TextString)
FixationCross   = visual.TextStim(win, text = "+")

# Now we will try to update the string in a loop structure.
## In this first attempt we adjust TextString, try it out!
for i in range(3):
    
    FixationCross.draw()
    win.flip()
    core.wait(1)
    
    TextString = str(i)
    
    TextObject.draw()
    win.flip()
    core.wait(1)
## Clearly this doesn't work. Why not? Because indeed in line 19 you 
## assign the string information from TextString to the text property
## of the TextStim function.
## However, this doesn't mean that there is a continuous connection between
## the information stored in TextString and the text displayed by TextObject.
## Changing the content of TextString doesn't influence TextObject!

## Second attempt.
for i in range(3):
    
    FixationCross.draw()
    win.flip()
    core.wait(1)
    
    TextObject = visual.TextStim(win, text = str(i))
    
    TextObject.draw()
    win.flip()
    core.wait(1)
## This solution solves the problem because you immediately insert
## the new value i in the function that constructs the TextObject.
## However, also this solution is suboptimal as you have to make the
## TextObject all over again each time you execute the loop.

## Third attempt.
for i in range(3):
    
    FixationCross.draw()
    win.flip()
    core.wait(1)
    
    TextObject.text = str(i)
    
    TextObject.draw()
    win.flip()
    core.wait(1)
## This is the winning solution. You now recycle the TextObject that you
## made at the start of the script and just update the text property.