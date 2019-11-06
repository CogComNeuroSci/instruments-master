from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time

win = visual.Window(fullscr = True, color = 'black')

# afbeelding van pompoen afdrukken, vorm weergeven door middel van punten en lijnen, vorm omzetten naar coördinaten

pompoenVorm = [(-0.75,-0.02),(-0.73,0.13),(-0.66,0.26),(-0.57,0.38),(-0.45,0.45),(-0.33,0.5),(-0.21,0.51),(-0.21,0.44),(-0.13,0.5),(-0.04,0.52),(0.05,0.52),(0.17,0.48),(0.15,0.54),(0.26,0.54),(0.36,0.53),(0.46,0.5),(0.54,0.45),(0.6,0.4),(0.66,0.32),(0.71,0.22),(0.75,0.11),(0.76,-0.01),(0.76,-0.14),(0.74,-0.26),(0.71,-0.39),(0.67,-0.47),(0.6,-0.6),(0.53,-0.69),(0.44,-0.75),(0.33,-0.77),(0.2,-0.8),(0.06,-0.8),(-0.1,-0.79),(-0.23,-0.8),(-0.35,-0.76),(-0.47,-0.67),(-0.56,-0.59),(-0.64,-0.5),(-0.7,-0.39),(-0.74,-0.27),(-0.75,-0.14)]
pompoen = ShapeStim(win, vertices=pompoenVorm, fillColor='maroon', lineColor='black', size=1)
pompoen.draw()

oogRechtsBuiten = [(0.1,0.24),(0.2,0.3),(0.33,0.38),(0.43,0.4),(0.5,0.3),(0.49,0.26),(0.47,0.24),(0.43,0.22),(0.39,0.22),(0.29,0.23),(0.21,0.23)]
oogRechtsBu = ShapeStim(win, vertices=oogRechtsBuiten, fillColor='chocolate', lineColor='black', size=1)
oogRechtsBu.draw()

oogRechtsBinnen = [(0.21,0.23),(0.39,0.3),(0.39,0.22),(0.29,0.23)]
oogRechtsBi = ShapeStim(win, vertices=oogRechtsBinnen, fillColor='GoldenRod', lineColor='black', size=1)
oogRechtsBi.draw()

oogLinksBuiten = [(-0.45,0.36),(-0.36,0.34),(-0.23,0.28),(-0.1,0.24),(-0.16,0.2),(-0.24,0.17),(-0.32,0.14),(-0.38,0.13),(-0.49,0.16),(-0.5,0.24),(-0.48,0.3)]
oogLinksBu = ShapeStim(win, vertices=oogLinksBuiten, fillColor='chocolate', lineColor='black', size=1)
oogLinksBu.draw()

oogLinksBinnen = [(-0.38,0.13),(-0.38,0.21),(-0.35,0.24),(-0.24,0.23),(-0.2,0.23),(-0.16,0.2),(-0.24,0.17),(-0.32,0.14)]
oogLinksBi = ShapeStim(win, vertices=oogLinksBinnen, fillColor='GoldenRod', lineColor='black', size=1)
oogLinksBi.draw()

mondVorm = [(-0.61, 0.22),(-0.59,0.14),(-0.56, 0.07),(-0.5, 0),(-0.39, -0.02),(-0.25, -0.06),(0.01, -0.03),(0.26, 0.04),(0.47, 0.08),(0.57, 0.17),(0.59, 0.26),(0.64,0.16),(0.66, 0.08),(0.67, -0.06),(0.58, -0.26),(0.47, -0.42),(0.28, -0.49),(0.17, -0.48),(-0.12, -0.49),(-0.26, -0.42),(-0.39, -0.32),(-0.53, -0.16),(-0.62, 0.05),(-0.63, 0.14)]
mond = ShapeStim(win, vertices=mondVorm, fillColor='GoldenRod', lineColor='black', size=1)
mond.draw()

takVorm = [(-0.1, 0.506),(-0.09, 0.67),(-0.06, 0.87),(0.02, 0.97),(0.08,1),(0.14, 0.97),(0.2, 0.9),(0.23, 0.84),(0.15, 0.81),(0.12, 0.88),(0.08, 0.91),(0.05, 0.89),(0.04, 0.87),(0.01, 0.68),(0, 0.52)]
tak = ShapeStim(win, vertices=takVorm, fillColor='DarkOliveGreen', lineColor='black', size=1)
tak.draw()

takUiteinde = [(0.15,0.81),(0.17, 0.84),(0.19, 0.85),(0.23, 0.84),(0.23, 0.82),(0.21, 0.81),(0.18, 0.8)]
takU = ShapeStim(win, vertices=takUiteinde, fillColor='Olive',lineColor='black', size=1)
takU.draw()

tand1 = [(-0.5, 0),(-0.39, -0.02),(-0.5, -0.07)]
t1 = ShapeStim(win, vertices=tand1, fillColor='chocolate', lineColor='black', size=1)
t1.draw()

tand2 = [(-0.39, -0.02),(-0.25, -0.06),(-0.34, -0.19)]
t2 = ShapeStim(win, vertices=tand2, fillColor='chocolate', lineColor='black', size=1)
t2.draw()

tand3 = [(-0.25, -0.06),(0.01, -0.03),(-0.09, -0.25)]
t3 = ShapeStim(win, vertices=tand3, fillColor='chocolate', lineColor='black', size=1)
t3.draw()

tand4 = [(0.01, -0.03),(0.26, 0.04),(0.2, -0.25)]
t4 = ShapeStim(win, vertices=tand4, fillColor='chocolate', lineColor='black', size=1)
t4.draw()

tand5 = [(0.26, 0.04),(0.47, 0.08),(0.44, -0.1)]
t5 = ShapeStim(win, vertices=tand5, fillColor='chocolate', lineColor='black', size=1)
t5.draw()

tand6 = [(0.47, 0.08),(0.57, 0.17),(0.57, 0.04)]
t6 = ShapeStim(win, vertices=tand6, fillColor='chocolate', lineColor='black', size=1)
t6.draw()

tand7 = [(-0.53, 0.02),(-0.53, -0.16),(-0.62, 0.05)]
t7 = ShapeStim(win, vertices=tand7, fillColor='chocolate', lineColor='black', size=1)
t7.draw()

tand8 = [(-0.42, -0.09),(-0.39, -0.32),(-0.53, -0.16)]
t8 = ShapeStim(win, vertices=tand8, fillColor='chocolate', lineColor='black', size=1)
t8.draw()

tand9 = [(-0.39,-0.32),(-0.25,-0.23),(-0.12,-0.49),(-0.26,-0.42)]
t9 = ShapeStim(win, vertices=tand9, fillColor='chocolate', lineColor='black', size=1)
t9.draw()

tand10 = [(0.02, -0.28),(0.17, -0.48),(-0.12, -0.49)]
t10 = ShapeStim(win, vertices=tand10, fillColor='chocolate', lineColor='black', size=1)
t10.draw()

tand11 = [(0.33, -0.22),(0.52, -0.35),(0.47,-0.42),(0.28,-0.49),(0.17,-0.48)]
t11 = ShapeStim(win, vertices=tand11, fillColor='chocolate', lineColor='black', size=1)
t11.draw()

tand12 = [(0.67, -0.06),(0.55, -0.08),(0.52, -0.35),(0.58, -0.26)]
t12 = ShapeStim(win, vertices=tand12, fillColor='chocolate', lineColor='black', size=1)
t12.draw()

tand13 = [(0.64, 0.16),(0.66, 0.08),(0.67, -0.06),(0.62, 0.12)]
t13 = ShapeStim(win, vertices=tand13, fillColor='chocolate', lineColor='black', size=1)
t13.draw()

Htext = visual.TextStim(win, text = "Happy Halloween!", color = 'firebrick', pos=(0,-0.9))
Htext.draw()

#Volgens de opdracht dient de pompoen slechts gedurende één seconde op het scherm te verschijnen.
#Varieer onderstaande tijd om de pompoen langer in beeld te brengen.

win.flip()
time.sleep(1)

Htext.draw()
win.flip()
time.sleep(0.5)

win.flip()
time.sleep(0.5)

Htext.draw()
win.flip()
time.sleep(0.5)

win.flip()
time.sleep(0.5)

Htext.draw()
win.flip()
time.sleep(0.5)

win.flip()
time.sleep(0.5)

Htext.draw()
win.flip()
time.sleep(0.5)

win.flip()
time.sleep(0.5)

Htext.draw()
win.flip()
time.sleep(0.5)

win.flip()
time.sleep(0.5)

Htext.draw()
win.flip()
time.sleep(0.5)

win.flip()
time.sleep(0.5)

Htext.draw()
win.flip()
time.sleep(0.5)

win.flip()
time.sleep(0.5)

Htext.draw()
win.flip()
time.sleep(0.5)

win.close()
