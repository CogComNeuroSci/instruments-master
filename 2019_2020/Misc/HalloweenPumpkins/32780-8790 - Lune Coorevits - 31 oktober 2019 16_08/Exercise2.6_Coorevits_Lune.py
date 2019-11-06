from __future__ import division
from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time
win = visual.Window(fullscr = True)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
Htext = visual.TextStim(win, text = "Happy Halloween!", color = 'OrangeRed', pos = (0, -0.72), font = 'Lucida Calligraphy', height = 0.1)
Htext.draw()
#
win.flip()
time.sleep(1)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
win.flip()
time.sleep(0.5)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
Htext = visual.TextStim(win, text = "Happy Halloween!", color = 'OrangeRed', pos = (0, -0.72), font = 'Lucida Calligraphy', height = 0.1)
Htext.draw()
#
win.flip()
time.sleep(1)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
win.flip()
time.sleep(0.5)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
Htext = visual.TextStim(win, text = "Happy Halloween!", color = 'OrangeRed', pos = (0, -0.72), font = 'Lucida Calligraphy', height = 0.1)
Htext.draw()
#
win.flip()
time.sleep(1)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
win.flip()
time.sleep(0.5)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
Htext = visual.TextStim(win, text = "Happy Halloween!", color = 'OrangeRed', pos = (0, -0.72), font = 'Lucida Calligraphy', height = 0.1)
Htext.draw()
#
win.flip()
time.sleep(1)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
win.flip()
time.sleep(0.5)
######STIMULUS HAPPY######
#
Hbackground1 = visual.Rect(win, width = 2, height = 2, fillColor = 'White', lineColor = 'White')
Hbackground1.draw()
#
Hshadow = gabor = visual.GratingStim(win, tex = "sin", mask = "gauss", texRes = 256, size = [1.5, 1.2], sf = 0, ori = 0, color = 'Black', pos = (0, -0.3))
Hshadow.draw()
#
#Hpumpkin = visual.Circle(win, radius = 0.4, fillColor = 'DarkOrange', lineColor = 'OrangeRed', edges = 500)
#Hpumpkin.draw()
#
Hpumpkin1 = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, 0))
Hpumpkin1.draw()
#
Hpumpkin2L = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.15, 0))
Hpumpkin2L.draw()
#
Hpumpkin2R = visual.Polygon (win, edges = 200, size = (0.4, 0.8), fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.15, 0))
Hpumpkin2R.draw()
#
Hhoedbodem = visual.Polygon (win, edges = 200, size = (0.8, 0.25), fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedbodem.draw()
#
HhoedVert = ((0.2, 0.05), (-0.2, 0.05), (0, 0.6))
Hhoedtop = visual.ShapeStim (win, vertices = HhoedVert, fillColor = 'Black', lineColor = 'Black', pos = (0, 0.3))
Hhoedtop.draw()
#
Hhoedriem = visual.Line(win, start = (-0.185, 0.42), end = (0.185, 0.42), lineColor = 'DarkGoldenRod', lineWidth = 10)
Hhoedriem.draw()
#
#HeyeL = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
#HeyeL.draw()
#
#HeyeR = visual.Polygon (win, edges = 3, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
#HeyeR.draw()
#
HeyeL1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (-0.15, 0.1))
HeyeL1.draw()
HeyeLShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.12, 0.1))
HeyeLShadow.draw()
#
HeyeR1 = visual.Circle(win, radius = 0.05, fillColor = 'Black', lineColor = 'Black', pos = (0.15, 0.1))
HeyeR1.draw()
HeyeRShadow = visual.Circle(win, radius = 0.025, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.18, 0.1))
HeyeRShadow.draw()
#
#Hmouth1 = visual.Line(win, start = (-0.15, -0.17), end = (0.15, -0.17), lineColor = 'Black')
#Hmouth1.draw()
#
Hmouth2 = visual.Circle(win, radius = 0.15, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.17))
Hmouth2.draw()
#
Hmouth3 = visual.Rect(win, width = 0.35, height = 0.18, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0, -0.095))
Hmouth3.draw()
#
Htooth1= visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (-0.08, -0.19))
Htooth1.draw()
#
Htooth2 = visual.Rect(win, width = 0.03, height = 0.04, fillColor = 'DarkOrange', lineColor = 'DarkOrange', pos = (0.055, -0.30))
Htooth2.draw()
#
Hnose = visual.Polygon (win, edges = 3, radius = 0.035, fillColor = 'Black', lineColor = 'Black', pos = (0, -0.05))
Hnose.draw()
#
Htext = visual.TextStim(win, text = "Happy Halloween!", color = 'OrangeRed', pos = (0, -0.72), font = 'Lucida Calligraphy', height = 0.1)
Htext.draw()
#
win.flip()
time.sleep(1)
win.close()