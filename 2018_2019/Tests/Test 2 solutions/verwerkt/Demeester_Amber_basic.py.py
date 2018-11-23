# Test 2 - Amber Demeester
# Importeren van alles die nodig is 
import time, numpy
from psychopy import visual, event

#aanmaken van vanalles
grootte_zon = 0.15*2
grootte_maan =0.02*2
grootte_planeet = 0.07*2

win = visual.Window(size=[600,600], color = (-1,-1,-1))
zon = visual.Circle(win,lineColor="yellow",fillColor="yellow",size= 0.15)
planeet = visual.Circle (win, lineColor = "blue", fillColor = "blue", size = 0.02, pos = (0.705,0.236))
maan = visual.Circle(win,lineColor = "white", fillColor = "white", size = 0.07, pos = (0.707,0.356 )) 
tekst = visual.TextStim( win, text= "De rest van de punten zullen hopelijk voor de volgende test zijn.")

#drawen enzo 
zon.draw()
planeet.draw()
maan.draw()
win.flip()
time.sleep(3)

tekst.draw()
win.flip()
time.sleep (2)

win.close()