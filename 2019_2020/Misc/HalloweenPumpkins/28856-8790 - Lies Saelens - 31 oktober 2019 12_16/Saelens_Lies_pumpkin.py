from __future__ import division 

from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time

win = visual.Window(size=(800, 600), units='height')

pumpkinVert = [(-0.3,0),(-0.4,0.1),(-0.4,0.3),(-0.3,0.4),(-0.2,0.3),(-0.1,0.4),(0,0.3),(0.1,0.4),(0.2,0.3),(0.3,0.4),(0.4,0.3),(0.4,0.1),(0.3,0),(0.2,0.1),(0.1,0),(0,0.1),(-0.1,0),(-0.2,0.1)]
pumpkin = visual.ShapeStim( win, lineColor = "black", fillColor = "orange", vertices = pumpkinVert, size = 1)

steelVert = [(0, 0.3), (-0.05,0.45), (0.05, 0.45)]
steel = visual.ShapeStim(win, lineColor = "black", fillColor = "darkgreen", vertices = steelVert, size = 1)

oogrechtsVert = [(0.12,0.25), (0.14,0.28), (0.16,0.25)]
oogrechts = visual.ShapeStim(win, lineColor = "black", fillColor = "black", vertices = oogrechtsVert, size = 1)

ooglinksVert = [(-0.12,0.25), (-0.14,0.28), (-0.16,0.25)]
ooglinks = visual.ShapeStim(win, lineColor = "black", fillColor = "black", vertices = ooglinksVert, size = 1)

neusVert = [(-0.02,0.20), (0,0.23), (0.02,0.20)]
neus = visual.ShapeStim(win, lineColor = "black", fillColor= "black", vertices = neusVert, size = 1)

mondVert = [(-0.2,0.15),(-0.15,0.18),(-0.10,0.15),(-0.05,0.18),(0,0.15),(0.05,0.18),(0.10,0.15),(0.15,0.18),(0.20,0.15),(0.15,0.12),(0.10,0.15),(0.05,0.12),(0,0.15),(-0.05,0.12),(-0.10,0.15),(-0.15,0.12),(-0.20,0.15)]
mond = visual.ShapeStim(win, lineColor = "black", fillColor = "black", vertices = mondVert, size = 1)

message = visual.TextStim(win, text = "Happy Halloween!", color = "black", pos = (0,-0.2), height = 0.1)

pumpkin.autoDraw = True
steel.autoDraw = True
oogrechts.autoDraw = True
ooglinks.autoDraw = True
neus.autoDraw = True
mond.autoDraw = True
message.draw()

win.flip()

time.sleep(7)
win.close()