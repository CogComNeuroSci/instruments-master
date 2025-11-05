# This is an example of a Halloween pumpkin written using PsychoPy code
# By Tom Verguts, October 2017, updated in September 2018, by way of illustration for the Instruments in Psychology course
import time
from psychopy import visual

# definitions start here
win = visual.Window(fullscr = True, units = "norm")

rect            = visual.ImageStim(win, image = "HalloweenPumpkin.jpg") #You can download an image from here: https://pp02bevragingen.ugent.be/HalloweenPumpkin.jpg
pumpkinVert     = [(-0.2,0.0),(-0.4,0.1),(-.4,0.4),(-0.2,0.6),(0.2,0.6),(.4,0.4),(.4,0.1),(0.2,0)]
pumpkin         = visual.ShapeStim( win, lineColor = "black", fillColor = "orange", vertices = pumpkinVert, size = 1)
mouth           = visual.Line(      win, lineColor = "black", start = (-0.2,0.1), end = (0.2,0.1))
eyeLeft         = visual.Circle(    win, lineColor = "black", fillColor = "black", pos = (-0.2,0.4), radius = 0.01)
eyeRight        = visual.Circle(    win, lineColor = "black", fillColor = "black", pos = (0.2,0.4), radius = 0.01)
pumpkin_top     = visual.rect.Rect(      win, lineColor = "black", fillColor = "green", pos = (0,0.7), width = 0.1, height = 0.2)
tekst           = visual.TextStim(  win, text = "Happy halloween!", height = 0.3, pos = (0,-0.5), font = "Monotype Corsiva", wrapWidth = 3)
tekst.italic    = False

# drawing starts here; first the image
rect.draw()
win.flip()
time.sleep(2)

# Now our drawing; with text...
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
# a more efficient way to do this, will be discussed in Chapter 4
pumpkin.draw()
pumpkin_top.draw()
eyeLeft.draw()
eyeRight.draw()
mouth.draw()
tekst.draw()
win.flip()
time.sleep(1)
win.close()