

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demo of psychopy.visual.ShapeStim: lines and arbitrary fillable shapes

See shapeContains.py for dynamic interaction of ShapeStim and Mouse.
"""

from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time

win = visual.Window(units='height', color = 'black', pos = [1100, 0], fullscr = True)

#PumpieThePumpkin shape
Pumpkin = [ (-0.6,0),(-0.575,0.1),(-0.55,0.2),(-0.5,0.3),(-0.4,0.375),(-0.3,0.425),(-0.2,0.45), (-0.1, 0.47),(0,0.47), (0.1, 0.47),(0.2,0.45), (0.3,0.425),(0.4,0.375), (0.5,0.3), (0.55,0.2),(0.575,0.1), (0.6,0),(0.575,-0.1),(0.55,-0.2),(0.5,-0.3),(0.4,-0.375),(0.3,-0.425),(0.2,-0.45),(0,-0.45),(-0.2,-0.45), (-0.3,-0.425),(-0.4,-0.375), (-0.5,-0.3), (-0.55,-0.2),(-0.575,-0.1), (-0.6,0)]
Pumpie = ShapeStim(win, vertices=Pumpkin, fillColor='#ff4500', size=.5, lineColor='#ff4500', interpolate = True)
schaduwboven = [(0,0.3), (-0.1,0.35),(-0.15,0.4), (-0.1,0.45), (0,0.47), (0.1,0.45), (0.15,0.4),(0.1,0.35)]
schaduw = ShapeStim(win, vertices=schaduwboven, fillColor='#992900', size=.5, lineColor='#ff4500', interpolate = True, opacity = 0.5)
stokje = [(0,0.35),(-0.05,0.37),(-0.07,0.4),(-0.05,0.45),(0,0.55),(0.05,0.6),(0.1,0.65),(0.15,0.67),(0.17,0.62),(0.1,0.55),(0.05,0.5),(0.07,0.45),(0.1,0.4),(0.05,0.35)]
stickie = ShapeStim(win, vertices=stokje, fillColor='#003300', size=.5, lineColor='#003300', interpolate = True)

#Pumpies' Lines

lineBackL = [(-0.07,0.4),(-0.1,0.43),(-0.2,0.45)]
LBL = ShapeStim(win, vertices= lineBackL, lineWidth=5, lineColor='#cc2900', closeShape = False, size = 0.5)
lineBackR = [(0.08,0.4),(0.1,0.43),(0.2,0.45)]
LBR = ShapeStim(win, vertices= lineBackR, lineWidth=5, lineColor='#cc2900', closeShape = False, size = 0.5)

linefrontL = [(-0.04,0.36), (-0.1,0.37),(-0.2,0.32),(-0.27,0.25),(-0.33, 0.2),(-0.35,0.15),(-0.4, 0),(-0.38, -0.15),(-0.34,-0.25),(-0.3,-0.35),(-0.2,-0.45)]
LFL = ShapeStim(win, vertices= linefrontL, lineWidth=5, lineColor='#cc2900', closeShape = False, size = 0.5)

linefrontR = [(0.05,0.35), (0.1, 0.36) ,(0.2,0.32),(0.27,0.25),(0.33, 0.2),(0.35,0.15),(0.4, 0),(0.38, -0.15),(0.34,-0.25),(0.3,-0.35),(0.2,-0.45)]
LFR = ShapeStim(win, vertices= linefrontR, lineWidth=5, lineColor='#cc2900', closeShape = False, size = 0.5)

linefrontF = [(0.01,0.35), (-0.03,0.3), (-0.05, 0.17), (-0.06, 0.1), (-0.07, 0), (-0.06, -0.1), (-0.05, -0.17), (-0.04,-0.3),(0, -0.45)]
LFF = ShapeStim(win, vertices= linefrontF, lineWidth=5, lineColor='#cc2900', closeShape = False, size = 0.5)

#Pumpies' eyes and mouth

eye1 = visual.Polygon(win, edges = 100, size= [0.08,0.13] ,pos = (0.1,0.03), fillColor = '#4d1400', lineColor = '#cc3600', lineWidth = 5, opacity = 1)
eye2 = visual.Polygon(win, edges = 100, size= [0.08,0.13] ,pos = (-0.1,0.03), fillColor = '#4d1400', lineColor = '#cc3600', lineWidth = 5, opacity = 1)
MTH = [(-0.35,-0.1),(-0.15,-0.17),(0,-0.2), (0.15, -0.17), (0.35,-0.1), (0.15, -0.3), (0, -0.35), (-0.15, -0.3)]
mouth = ShapeStim(win, vertices= MTH, lineWidth=4, lineColor='#cc3600', fillColor = '#4d1400', size = 0.5)


#ribbon
selfxVert = [(0,0.05), (0.05, 0),(0.15,0.1),(0.15,-0.1),(0.05,0),(0,-0.05),(-0.05,0),(-0.15,-0.1),(-0.15,0.1),(-0.05,0)]
ribbon = ShapeStim(win, vertices=selfxVert, fillColor='#ffe0b3', lineColor='#ffe0b3', size=0.6, pos = [0.022, 0.26], ori = 17)


#Sorry, I did not use Happy Halloween

Text = visual.TextStim(win, text = "HAPPY PUMPKIN SEASON", bold = True, font = 'calibri', color ='#ff6600', height = (0.15), pos = (0,-0.7), alignHoriz = 'center',units = 'norm')
##Text = visual.TextStim(win, text = "Happy Halloween", bold = True, font = 'calibri', color ='#ff6600', height = (0.17), pos = (0,-0.7), alignHoriz = 'center',units = 'norm')


#PumpieComesAlive

Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()

Text.draw()
win.flip()
time.sleep(1)

#Geen tekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
win.flip()
time.sleep(0.5)

#tekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
Text.draw()
win.flip()
time.sleep(1)

#geentekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
win.flip()
time.sleep(0.5)

#tekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
Text.draw()
win.flip()
time.sleep(1)

#geentekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
win.flip()
time.sleep(0.5)

#tekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
Text.draw()
win.flip()
time.sleep(1)

#geentekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
win.flip()
time.sleep(0.5)


#tekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
Text.draw()
win.flip()
time.sleep(1)

#geentekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
win.flip()
time.sleep(0.5)

#tekst
Pumpie.draw()
schaduw.draw()
LBL.draw()
LBR.draw()
LFL.draw()
LFR.draw()
LFF.draw()
stickie.draw()
eye2.draw()
eye1.draw()
mouth.draw()
ribbon.draw()
Text.draw()
win.flip()
time.sleep(1)

win.close()