
#Esther: het lijntje code hieronder is niet langer nodig nu we in Python3 werken in plaats van Python2 ;)
#from __future__ import division

from psychopy import core, visual, event
from numpy import sin, pi

import time


win = visual.Window(color="black", fullscr=True)


body1=visual.Circle(win, radius=0.5, edges=50, pos=(-0.1,0),fillColor="orange", lineColor="orange")
body2=visual.Circle(win, radius=0.5, edges=50, pos=(0.1,0),fillColor="orange", lineColor="orange")

hoofdline1=visual.Polygon(win, edges=128, pos=(0,0.49), fillColor="black", lineColor="black", opacity=0.3, size=0.4)
hoofdline1.vertices = hoofdline1.vertices[32:96]
hoofdline1.needVertexUpdate = True
hoofdline2=visual.Polygon(win, edges=128, pos=(0,0.5), fillColor="orange", lineColor="orange", size=0.4, ori=1)
hoofdline2.vertices = hoofdline2.vertices[32:96]
hoofdline2.needVertexUpdate = True

oog1=visual.Polygon(win, edges=3, pos=(0.19,0.25), fillColor="black", lineColor="black", opacity=0.3,size=0.2)
oog2=visual.Polygon(win, edges=3, pos=(-0.19,0.25), fillColor="black", lineColor="black", opacity=0.3,size=0.2)
nose=visual.Polygon(win, edges=3, pos=(0,0), fillColor="black",lineColor="black", opacity=0.3,size=0.2, ori=180)
oor1=visual.Polygon(win, edges=3, pos=(-0.44,0.42), fillColor="orange",lineColor="orange",size=0.2, ori=-40)
oor2=visual.Polygon(win, edges=3, pos=(0.44,0.42), fillColor="orange", lineColor="orange",size=0.2, ori=40)

mond=visual.Polygon(win, edges=128, pos=(0,-0.25), fillColor="black", lineColor="black", opacity=0.3, size=0.3)
mond.vertices = mond.vertices[32:96]
mond.needVertexUpdate = True
mondline=visual.Line(win, start=(0, -0.1), end=(0, -0.26), lineColor="black", opacity=0.4)
tooth=visual.Rect(win, width=0.05, height=0.1, pos=(0.05,-0.25), lineColor="orange", fillColor="orange")

strunk=visual.Rect(win, width=0.1, height=0.4, pos=(0,0.6), lineColor="green", fillColor="green")

fancy=['Times', 'Times New Roman']
HapHal=visual.TextStim(win, text="Happy Halloween!", pos=(0,-0.8), color="white", font=fancy)

trialClock = core.Clock()
t = 0

# Esther: prachtig! Een while loop en een sinusfunctie voor de tekst, impressive!
while not event.getKeys() and t <30:
    t = trialClock.getTime()
    HapHal.contrast = sin(t * pi * 2)
    HapHal.draw()
    strunk.draw()
    body1.draw()
    body2.draw()
    hoofdline1.draw()
    hoofdline2.draw()
    mondline.draw()
    mond.draw()
    tooth.draw()
    oor1.draw()
    oor2.draw()
    nose.draw()
    oog1.draw()
    oog2.draw()
    
    win.flip()

win.close()
