#pumpkin

from __future__ import division
from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time

#make a window
win = visual.Window(size = [900,900], color = (0,0,1))

#radius is de straal
#onderste oranje cirkel
circle_bottom = visual.Circle(win, size = [0.1,0.1], radius = 2, color = 'Orange')
circle_bottom.draw()
time.sleep(2)

#bovenste oranje cirkel
circle_upper = visual.Circle(win, pos = (0.03,0.07), size = [0.1,0.12], radius = 2, color = 'Orange')
circle_upper.draw()
time.sleep(2)

#mond
circle_mouth = visual.Circle(win, pos = (0.03,0.03), size = [0.06,0.08], radius = 2, color = 'Brown')
circle_mouth.draw()
time.sleep(2)

#dekselvorm
deksel= visual.Circle(win, pos = (-0.02,0.30), size = [0.07,0.02], radius = 2, color = 'Orange')
deksel.draw()
time.sleep(2)

#steeltje
steeltje = visual.Rect(win, width = 0.02, height = 0.05, lineColor = 'green', fillColor = 'Green', pos = (0,0.37))
steeltje.draw()
time.sleep(2)

#Tandenboven
#links
Tand = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (-0.06,0.12))
Tand.draw()
time.sleep(2)
#middenlinks
Tand = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (0,0.15))
Tand.draw()
time.sleep(2)
#middenrechts
Tand1 = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (0.06,0.15))
Tand1.draw()
time.sleep(2)
#rechts
Tand1 = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (0.12,0.12))
Tand1.draw()
time.sleep(2)

#Tandenonder
#links
Tand = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (-0.06,-0.07))
Tand.draw()
time.sleep(2)
#middenlinks
Tand = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (0,-0.08))
Tand.draw()
time.sleep(2)
#middenrechts
Tand1 = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (0.06,-0.08))
Tand1.draw()
time.sleep(2)
#rechts
Tand1 = visual.Rect(win, width = 0.02, height = 0.07, lineColor = 'White', fillColor = 'White', pos = (0.12,-0.07))
Tand1.draw()
time.sleep(2)


#Oog 1: 
#cirkel
eye1 = visual.Circle(win, pos = (0.02,0.25), size = [0.01,0.01], radius = 2, color = 'Black')
eye1.draw()
time.sleep(2)
#oogwit
eyewhite1 = visual.Circle(win, pos = (0.02,0.25), size = [0.002,0.003], radius = 2, color = 'White')
eyewhite1.draw()
time.sleep(2)

#Oog 2: 
#cirkel
eye2 = visual.Circle(win, pos = (0.08,0.25), size = [0.01,0.01], radius = 2, color = 'Black')
eye2.draw()
time.sleep(2)
#oogwit
eyewhite2 = visual.Circle(win, pos = (0.08,0.25), size = [0.002,0.003], radius = 2, color = 'White')
eyewhite2.draw()
time.sleep(2)

#window einde
win.flip()
time.sleep(2)
win.close()