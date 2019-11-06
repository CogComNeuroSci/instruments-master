#pumpkin

from __future__ import division
from psychopy import visual, event, core, monitors
from psychopy.visual import ShapeStim
import time

#make a window on the correct monitor
win = visual.Window(size = [900,900], color = [0,0,1], monitor = 'Macbook Air')

#schaduw
circle_bottom = visual.Circle(win, pos = [-0.2,-0.75], size = [0.8,0.2], color = 'grey')
circle_bottom.draw()

#basic pumpkin shape (bottom)
circle_bottom = visual.Circle(win, pos = [0,-0.4], size = [0.8,0.8], color = 'orange')
circle_bottom.draw()


#basic pumpkin shape (upper)
circle_upper = visual.Circle(win, ori = 19, pos = [0.2,0.2], size = [0.87,1.27], color = 'orange')
circle_upper.draw()

#smooth circles rechts blok
smoothcircles = visual.Rect(win, height = 0.8, width = 0.2, ori = 16, pos = [-0.19, 0], fillColor = 'orange', lineColor = 'orange')
smoothcircles.draw()

#innercirkels
#circle_inner
circle_inner1 = visual.Circle(win, lineWidth = 35, ori = 19, pos = [0.09,0.026], size = [0.14,1.66], lineColor = 'darkorange')
circle_inner1.draw()

#circle_inner2
circle_inner2 = visual.Circle(win, lineWidth = 35, ori = 19, pos = [0.1,0.026], size = [0.34,1.66], lineColor = 'darkorange')
circle_inner2.draw()

#circle_inner4
circle_inner4 = visual.Circle(win, lineWidth = 35, ori = 19, pos = [0.1,0.02], size = [0.64,1.66], lineColor = 'darkorange')
circle_inner4.draw()

#circle_inner5
circle_inner5 = visual.Circle(win, lineWidth = 35, ori = 19, pos = [0.12,0.02], size = [0.80,1.66], lineColor = 'darkorange')
circle_inner5.draw()

#mouth_shape
circle_mouth = visual.Circle(win, pos = [0.25,-0.3], size = [0.6,0.9], ori = 20, color = 'brown')
circle_mouth.draw()

#Tandenboven
#Tand1
tand1 = visual.Polygon(win, pos = [0.1,-0.045], ori = 180, size= [0.1,0.3], fillColor = 'white')
tand1.draw()
#Tand2
tand2 = visual.Polygon(win, pos = [0.2,0.04], ori = 180, size= [0.1,0.3], fillColor = 'white')
tand2.draw()
#Tand3
tand3 = visual.Polygon(win, pos = [0.3,0.05], ori = 180, size= [0.1,0.3], fillColor = 'white')
tand3.draw()
#Tand4
tand4 = visual.Polygon(win, pos = [0.4,0.04], ori = 180, size= [0.1,0.3], fillColor = 'white')
tand4.draw()
#Tand5
tand5 = visual.Polygon(win, pos = [0.5,-0.045], ori = 180, size= [0.1,0.3], fillColor = 'white')
tand5.draw()

#Tandenbeneden
#Tand1
tand1 = visual.Polygon(win, pos = [0,-0.55], size= [0.1,0.3], fillColor = 'white')
tand1.draw()
#Tand2
tand2 = visual.Polygon(win, pos = [0.1,-0.6], size= [0.1,0.3], fillColor = 'white')
tand2.draw()
#Tand3
tand3 = visual.Polygon(win, pos = [0.2,-0.65], size= [0.1,0.3], fillColor = 'white')
tand3.draw()
#Tand4
tand4 = visual.Polygon(win, pos = [0.3,-0.6], size= [0.1,0.3], fillColor = 'white')
tand4.draw()
#Tand5
tand5 = visual.Polygon(win, pos = [0.4,-0.55], size= [0.1,0.3], fillColor = 'white')
tand5.draw()


#mondrand
circle_mouth = visual.Circle(win, lineWidth = 900000, pos = [0.25,-0.3], size = [0.6,0.9], ori = 20, lineColor = 'orange')
circle_mouth.draw()

circle_mouth = visual.Circle(win, lineWidth = 900000, pos = [0.25,-0.3], size = [0.625,0.925], ori = 20, lineColor = 'orange')
circle_mouth.draw()

circle_mouth = visual.Circle(win, lineWidth = 900000, pos = [0.25,-0.3], size = [0.65,0.95], ori = 20, lineColor = 'orange')
circle_mouth.draw()

circle_mouth = visual.Circle(win, lineWidth = 900000, pos = [0.25,-0.3], size = [0.6525,0.9525], ori = 20, lineColor = 'orange')
circle_mouth.draw()

circle_mouth = visual.Circle(win, lineWidth = 900000, pos = [0.25,-0.3], size = [0.655,0.955], ori = 20, lineColor = 'orange')
circle_mouth.draw()

circle_mouth = visual.Circle(win, lineWidth = 900000, pos = [0.25,-0.3], size = [0.66,0.96], ori = 20, lineColor = 'orange')
circle_mouth.draw()

circle_mouth = visual.Circle(win, lineWidth = 900000, pos = [0.25,-0.3], size = [0.67,0.97], ori = 20, lineColor = 'orange')
circle_mouth.draw()




#steeltje
driehoek = visual.Polygon(win, pos = [0.05, 0.84], ori = 160, size= [0.08,0.2], fillColor = 'green', lineColor = 'green')
driehoek.draw()


#brow1
brow1 = visual.Rect(win, height = 0.01, width = 0.2, ori = 200, fillColor = 'black', lineColor = 'black', pos = [0.25,0.62])
brow1.draw()

#brow2
brow2 = visual.Rect(win, height = 0.01, width = 0.2, ori = 340, fillColor = 'black', lineColor = 'black', pos = [0.5,0.62])
brow2.draw()

#oog1white
eye1white = visual.Circle(win, pos = (0.25,0.4), size =[0.2,0.4], color = 'white')
eye1white.draw()
#oog1black
eye1black = visual.Circle(win, pos = (0.28,0.3), size =[0.1,0.12], color = 'black')
eye1black.draw()
#driehoekinoog
driehoekoog = visual.Polygon(win, pos = (0.28,0.25), size= [0.05,0.1], fillColor = 'white', lineColor = 'white')
driehoekoog.draw()

#oog2white
eye2white = visual.Circle(win, pos = (0.50,0.4), size =[0.2,0.4], color = 'white')
eye2white.draw()
#oog2black
eye2black = visual.Circle(win, pos = (0.53,0.3), size =[0.1,0.12], color = 'black')
eye2black.draw()
#driehoekinoog
driehoekoog = visual.Polygon(win, pos = (0.53,0.25), size= [0.05,0.1], fillColor = 'white', lineColor = 'white')
driehoekoog.draw()

#Text1
halloween = visual.TextStim(win, text = 'HAPPY HALLOWEEN!', color = 'Crimson' , pos = [-0.5,0.74], bold = True)
halloween.draw()

#Text
halloween = visual.TextStim(win, text = 'HAPPY HALLOWEEN!', opacity = 0.4, color = 'Crimson', pos = [-0.52,0.72], bold = True)
halloween.draw()

#Text
halloween = visual.TextStim(win, text = 'HAPPY HALLOWEEN!', opacity = 0.2, color = 'Crimson', pos = [-0.54,0.7], bold = True)
halloween.draw()

#window einde
win.flip()
time.sleep (8)
win.close()
