from psychopy import visual, core, event
import time
import numpy 

win = visual.Window((600,600), color = "black",units = "norm")

Planetx = 0.705
Planety = 0.236
Moonx = 0.002
Moony = 0.12 
color = [0, 0, 0] # geel is [1, 1, -1], maar veranderd niet van kleur
colorChange = 0.05
mouse = event.Mouse()
msg = visual.TextStim(win, text=' ', pos=(0, -.4))

i = 0.15
while i < 60: #kleiner dan 60 want 60 stappen is van 0 tem 59.
    i = i + 0.002575
    zon = visual.Circle(win, radius = i, pos = (0,0), fillColor = color)
    planeet = visual.Circle(win, radius = 0.07, pos = (Planetx,Planety), fillColor = "blue")
    maan = visual.Circle(win, radius = 0.02, pos = (Moonx,Moony), fillColor = "white")
    
    while (color[0] + colorChange) < 1: # kleur veranderd steeds als ik de waarde 1 aanpas, Bij 1 blijft hij wit, als ik hem op 60 zet is hij blauw?
        color = [channel+colorChange for channel in color]
        zon.setFillColor(color)

    zon.draw()
    maan.draw()
    planeet.draw()
    
    win.flip()
    time.sleep(1)

win.close()

#Hier lukt overgang van kleur van grijs naar wit wel
#from psychopy import visual, core, event
#import time
#
#win = visual.Window((600,600), color = "black",units = "norm")
#
#Planetx = 0.705
#Planety = 0.236
#Moonx = 0.002
#Moony = 0.12
#
#i = 0.15
#color = [0, 0, 0]
#colorChange = 0.05
#Zon = visual.Circle(win, radius = i, pos = (0,0), fillColor = color)
#while (color[0] + colorChange) < 60:
#    color = [channel+colorChange for channel in color]
#    Zon.setFillColor(color)
#    core.wait(0.1)
#    if event.getKeys():
#        break
#    Zon.draw()
#    win.flip()
#
#win.close()
#core.quit()

#######2 manieren om de botsing te doen beiden lukt niet om te runnen
### Deze tekst zou moeten helpen voor de botsing
#        while not mouse.isPressedIn(Maan):
#            if Maan.contains(Zon):
#                msg.text = 'botsing'
#            elif Maan.overlaps(Zon):
#                msg.text = 'botsing'
#            else:
#                msg.text = 'veilig'
#    msg.draw()


### in een andere figuur (op een andere manier) lukt dit wel
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#"""
#Demo for psychopy.visual.ShapeStim.contains() and .overlaps()
#
#Also inherited by various other stimulus types.
#"""
#
#from __future__ import division
#from psychopy import visual, event, core
#
#win = visual.Window(size=(500, 500), monitor='testMonitor', units='norm')
#mouse = event.Mouse()
#txt = 'click the shape to quit\nscroll to adjust circle'
#instr = visual.TextStim(win, text=txt, pos=(0, -.7), opacity=0.5)
#msg = visual.TextStim(win, text=' ', pos=(0, -.4))
#
# a target polygon (strange shape):
#shape = visual.ShapeStim(win, fillColor='darkblue', lineColor=None,
#    vertices=[(-0.02, -0.0), (-.8, .2), (0, .6), (.1, 0.06), (.8, .3), (.6, -.4)])
#
# define a buffer zone around the mouse for proximity detection:
# use pix units just to show that it works to mix (shape and mouse use norm units)
#bufzone = visual.Circle(win, radius=30, edges=13, units='pix')
#
# loop until detect a click inside the shape:
#while not mouse.isPressedIn(shape):
#    instr.draw()
#    # dynamic buffer zone around mouse pointer:
#    bufzone.pos = mouse.getPos() * win.size / 2  # follow the mouse
#    bufzone.size += mouse.getWheelRel()[1] / 20.0  # vert scroll adjusts radius
#    # is the mouse inside the shape (hovering over it)?
#    if shape.contains(mouse):
#        msg.text = 'botsing'
#        shape.opacity = bufzone.opacity = 1
#    elif shape.overlaps(bufzone):
#        msg.text = 'botsing'
#        shape.opacity = bufzone.opacity = 0.6
#    else:
#        msg.text = 'veilig'
#        shape.opacity = bufzone.opacity = 0.2
#    bufzone.draw()  # drawing helps visualize the mechanics
#    msg.draw()
#    shape.draw()
#    win.flip()
#win.close()
#core.quit()

###dit is ook een manier maar lukt ook niet om te runnen
#planeetx = [0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661, 0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715, 0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035, -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681, -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699, -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
#        zon.fillColor=(1,1-(zon.radius*1.90),-1)
#        if numpy.absolute(planeet.pos[0])<zon.radius and numpy.absolute(planeet.pos[1])<zon.radius: