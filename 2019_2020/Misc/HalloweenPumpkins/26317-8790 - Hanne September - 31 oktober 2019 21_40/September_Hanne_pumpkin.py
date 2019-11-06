from __future__ import division
from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time
import psychopy.visual
import psychopy.event

win = psychopy.visual.Window(
    size=[1440, 900],
    units="height",
    fullscr=False,
    color=[-1, -1, -1]
)

circle = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=150,
    fillColor='orange',
    lineColor='orange'
)
circle.draw()

circle2 = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=150,
    fillColor='orange',
    lineColor='orange'
)
circle2.pos=(-100,0)
circle2.draw()

circle3 = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=150,
    fillColor='orange',
    lineColor='orange'
)
circle3.pos=(100,0)
circle3.draw()

Vert1 = [(0.06,0.04),(0.12,0.12),(0.12,0.08)]
Triangle1 = visual.ShapeStim( win, lineColor = "black", fillColor = "black", vertices = Vert1, units="height")
Triangle1.draw()

Vert2 = [(-0.06,0.04),(-0.12,0.12),(-0.12,0.08)]
Triangle2 = visual.ShapeStim( win, lineColor = "black", fillColor = "black", vertices = Vert2, units="height")
Triangle2.draw()

Vert3=[(-0.05,-0.05),(0.05,-0.05),(-0.05,-0.04),(0.05,-0.04)]
Line = visual.ShapeStim( win, lineColor = "black", fillColor = "black", vertices = Vert3, units="height")
Line.draw()

Vert4=[(-0.06,0.24),(0.06,0.24),(-0.04,0.22),(0.04,0.22),(-0.06,0.2),(0.06,0.2)]
Line2 = visual.ShapeStim( win, lineColor = "green", fillColor = "green", vertices = Vert4, units="height")
Line2.draw()

stim = visual.TextStim(win, text = "HAPPY HALLOWEEN", color = 'orange',pos=(0,-0.2))
stim.draw()

win.flip()

psychopy.event.waitKeys()

win.close()
