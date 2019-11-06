from psychopy import visual
from psychopy.visual import ShapeStim
import time

win = visual.Window(fullscr = True, units = 'height', color = (-1,-1,-1))

#pumpkinShape
Circle1 = visual.Polygon (win, edges = 100, size = [0.5,0.5], fillColor = (0.72,-0.07,-0.87), lineColor = (0.46,-0.16,-0.8), lineWidth = 4, pos = (-0.20,0))
Circle2 = visual.Polygon (win, edges = 100, size = [0.5,0.5], fillColor = (0.72,-0.07,-0.87), lineColor = (0.46,-0.16,-0.8), lineWidth = 4, pos = (-0.10,0))
Circle3 = visual.Polygon (win, edges = 100, size = [0.5,0.5], fillColor = (0.72,-0.07,-0.87), lineColor = (0.46,-0.16,-0.8), lineWidth = 4, pos = (0,0))
Circle4 = visual.Polygon (win, edges = 100, size = [0.2, 0.5], fillColor = (0.72,-0.07,-0.87), lineColor = (0.46,-0.16,-0.8), lineWidth = 4, pos = (0,0))
Circle5 = visual.Polygon (win, edges = 100, size = [0.5,0.5], fillColor = (0.72,-0.07,-0.87), lineColor = (0.46,-0.16,-0.8), lineWidth = 4, pos = (0.10, 0))
Circle6 = visual.Polygon (win, edges = 100, size = [0.5,0.5], fillColor = (0.72,-0.07,-0.87), lineColor = (0.46,-0.16,-0.8), lineWidth = 4, pos = (0.20,0))
PumpkinLight = visual.GratingStim (win, mask = 'gauss', pos = (0,-0.02), size = (2.3, 1), opacity = 0.5)

#pumpkinStem
StemVert = [(-0.27,0.3), (-0.2,0.5), (-0.1,0.55), (-0.05,0.575), (0,0.6), (0.1, 0.7), (0.15,0.65), (0, 0.3)]
Stem = ShapeStim (win, vertices = StemVert, fillColor = (-0.47,0.19,-0.8), lineColor = (-0.63,-0.19,-0.85), lineWidth = 4, size = (0.5,0.5), opacity = 0.9)
StemLight = visual.GratingStim (win, mask = 'gauss', pos = (0, 0.25), size = (0.17,0.1))

#pumpkinFace
EyeLeft = visual.Polygon (win, edges = 3, size = [0.15,0.125], fillColor = (0.82,0.85,-1), lineColor = (0.46, -0.16, -0.8), lineWidth = 4, opacity = 0.7, pos = (-0.125, 0.1), ori = -110)
EyeLeftLight = visual.GratingStim(win, mask = 'gauss', pos = (-0.125,0.1), size = (0.14,0.11))
EyeRight = visual.Polygon (win, edges = 3, size = [0.15, 0.125], fillColor = (0.82,0.85,-1), lineColor = (0.46, -0.16, -0.8), lineWidth = 4, opacity = 0.7, pos = (0.125, 0.1), ori = 110)
EyeRightLight = visual.GratingStim(win, mask = 'gauss', pos = (0.125,0.1), size = (0.14,0.11))

MouthVert = [(-0.5,-0.1), (-0.38,-0.32), (-0.2,-0.47), (-0.05,-0.36), (0.1, -0.41), (0.25,-0.35), (0.4,-0.4), (0.5,-0.12), (0.3, -0.2), (0.1,-0.17), (0,-0.1), (-0.2,-0.2), (-0.34,-0.1)]
Mouth = ShapeStim (win, vertices = MouthVert, fillColor = (0.82,0.85,-1), lineColor = (0.46, -0.16, -0.8), lineWidth = 4, opacity = 0.7, size = (0.5,0.5))
MouthLight = visual.GratingStim(win, mask = 'gauss', pos = (0,-0.135), size = (0.75,0.15))

#text
Text = visual.TextStim (win, text = 'HAPPY HALLOWEEN!', color = [1,1,1], font = 'Chiller', bold = True, height = 0.13, pos = (0, -0.37))

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#tekstDraw
Text.draw()

#show Pumpkin + Text For 1sec
win.flip()
time.sleep(1)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#show Pumpkin for 0.5sec
win.flip()
time.sleep(0.5)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#tekstDraw
Text.draw()

#show Pumpkin + Text For 1sec
win.flip()
time.sleep(1)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#show Pumpkin for 0.5sec
win.flip()
time.sleep(0.5)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#tekstDraw
Text.draw()

#show Pumpkin + Text For 1sec
win.flip()
time.sleep(1)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#show Pumpkin for 0.5sec
win.flip()
time.sleep(0.5)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#tekstDraw
Text.draw()

#show Pumpkin + Text For 1sec
win.flip()
time.sleep(1)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#show Pumpkin for 0.5sec
win.flip()
time.sleep(0.5)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#tekstDraw
Text.draw()

#show Pumpkin + Text For 1sec
win.flip()
time.sleep(1)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#show Pumpkin for 0.5sec
win.flip()
time.sleep(0.5)

#pumkinDraw
StemLight.draw()
Stem.draw()

PumpkinLight.draw()
Circle1.draw()
Circle6.draw()
Circle2.draw()
Circle5.draw()
Circle3.draw()
Circle4.draw()

EyeLeftLight.draw()
EyeLeft.draw()
EyeRightLight.draw()
EyeRight.draw()

MouthLight.draw()
Mouth.draw()

#tekstDraw
Text.draw()

#show Pumpkin + Text For 1sec
win.flip()
time.sleep(1)

win.close()