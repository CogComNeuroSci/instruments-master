from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim

import time

win = visual.Window(fullscr = True, units='height')

pumpkinVert = [(-0.3,-0.3),(-0.5,-0.25),(-0.5,0.25),(-0.3,0.3),(-0.2,0.25),(-0.1,0.3),(0,0.25),(0.1,0.3),(0.2,0.25),(0.3,0.3),(0.5,0.25),(0.5,-0.25),(0.3,-0.3),(0.2,-0.25),(0.1,-0.3),(0,-0.25),(-0.1,-0.3),(-0.2,-0.25),(-0.3,-0.3)]
pumpkin = visual.ShapeStim( win, lineColor = "gold", fillColor = "orange", vertices = pumpkinVert, size = 1)

steeltjeVert = [(0,0.25),(0.10,0.45),(0.15,0.38),(0,0.25)]
steeltje = visual.ShapeStim(win, lineColor = "darkgreen", fillColor = "green", vertices = steeltjeVert)

oogLinksVert = [(-0.25,0.05),(-0.35,0.17),(-0.25,0.25),(-0.15,0.17)]
oogLinks = visual.ShapeStim(win, lineColor = "gold", fillColor = "black", vertices = oogLinksVert)
oogRechtsVert = [(0.25,0.05),(0.35,0.17),(0.25,0.25),(0.15,0.17)]
oogRechts = visual.ShapeStim(win, lineColor = "gold", fillColor = "black", vertices = oogRechtsVert)

oogLinksBinnenVert = [(-0.25,0.08),(-0.30,0.17),(-0.25,0.20),(-0.20,0.17)]
oogLinksBinnen = visual.ShapeStim(win, lineColor = "black", fillColor = "orange", vertices = oogLinksBinnenVert)
oogRechtsBinnenVert = [(0.25,0.08),(0.30,0.17),(0.25,0.20),(0.20,0.17)]
oogRechtsBinnen = visual.ShapeStim(win, lineColor = "black", fillColor = "orange", vertices = oogRechtsBinnenVert)

mondVert = [(-0.25,-0.2),(-0.25,0),(0.2,-0.2),(-0.25,-0.2)]
mond = visual.ShapeStim(win, lineColor = "black", fillColor = "black", vertices = mondVert)

tandenVert = [(-0.25,-0.2),(-0.2,-0.15),(-0.15,-0.2),(-0.1,-0.15),(-0.05,-0.2),(0,-0.15),(0.05,-0.2),(0.1,-0.16),(0.15,-0.2)]
tanden = visual.ShapeStim(win, lineColor = "grey", fillColor = "white", vertices = tandenVert)

tekst = visual.TextStim(win, text = "Happy Halloween!", height = 0.2, pos = (0,-0.37), font = "Berlin Sans FB", wrapWidth = 3, color = "gold")
tekst.italic = False

pumpkin.draw()
steeltje.draw()
oogLinks.draw()
oogRechts.draw()
oogLinksBinnen.draw()
oogRechtsBinnen.draw()
mond.draw()
tanden.draw()
tekst.draw()
win.flip()
time.sleep(0.5)

pumpkin.draw()
steeltje.draw()
oogLinks.draw()
oogRechts.draw()
oogLinksBinnen.draw()
oogRechtsBinnen.draw()
mond.draw()
tanden.draw()
win.flip()
time.sleep(1)

pumpkin.draw()
steeltje.draw()
oogLinks.draw()
oogRechts.draw()
oogLinksBinnen.draw()
oogRechtsBinnen.draw()
mond.draw()
tanden.draw()
tekst.draw()
win.flip()
time.sleep(0.5)

pumpkin.draw()
steeltje.draw()
oogLinks.draw()
oogRechts.draw()
oogLinksBinnen.draw()
oogRechtsBinnen.draw()
mond.draw()
tanden.draw()
tekst.draw()
win.flip()
time.sleep(0.5)

pumpkin.draw()
steeltje.draw()
oogLinks.draw()
oogRechts.draw()
oogLinksBinnen.draw()
oogRechtsBinnen.draw()
mond.draw()
tanden.draw()
win.flip()
time.sleep(1)

pumpkin.draw()
steeltje.draw()
oogLinks.draw()
oogRechts.draw()
oogLinksBinnen.draw()
oogRechtsBinnen.draw()
mond.draw()
tanden.draw()
tekst.draw()
win.flip()
time.sleep(0.5)
win.close()