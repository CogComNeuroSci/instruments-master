# This is an example of a Halloween pumpkin written using PsychoPy code
# By Tom Verguts, October 2017, by way of illustration for the Instruments in Psychology course
import time
from psychopy import visual,event

# definitions start here
win = visual.Window(size=[600,400],units="norm")
pumpkinVert = [(-0.2,0.0),(-0.4,0.1),(-.4,0.4),(-0.2,0.6),(0.2,0.6),(.4,0.4),(.4,0.1),(0.2,0)]
pumpkin = visual.ShapeStim(win, vertices=pumpkinVert, fillColor='orange', size=1, lineColor='black')
mouth = visual.Line(win, start=(-0.2,0.1), end=(0.2,0.1),lineColor="black")
eyeLeft = visual.Circle(win, radius=0.01, pos=(-0.2,0.4),lineColor="black",fillColor="black")
eyeRight = visual.Circle(win, radius=0.01, pos=(0.2,0.4),lineColor="black",fillColor="black")
pumpkin_top = visual.Rect(win,pos=(0,0.7),fillColor="green",width=0.1,height=0.2,lineColor="black")
tekst = visual.TextStim(win,text="Happy halloween!",height=0.3,pos=(0,-0.5),font='Monotype Corsiva',wrapWidth=3)
tekst.italic = False

# drawing starts here; with text...
pumpkin.draw()
pumpkin_top.draw()
eyeLeft.draw()
eyeRight.draw()
mouth.draw()
tekst.draw()
win.flip()
time.sleep(0.5)

# and without text
pumpkin.draw()
pumpkin_top.draw()
eyeLeft.draw()
eyeRight.draw()
mouth.draw()
win.flip()
time.sleep(1)

# and again with text
# for more flashes, you can copy-paste these two code blocks a number of times.
# a more efficient way to do this, will be discussed in Lesson 6
pumpkin.draw()
pumpkin_top.draw()
eyeLeft.draw()
eyeRight.draw()
mouth.draw()
tekst.draw()
win.flip()

# keep the final screen active until a key is pressed
while not event.getKeys():
    pass
win.close()