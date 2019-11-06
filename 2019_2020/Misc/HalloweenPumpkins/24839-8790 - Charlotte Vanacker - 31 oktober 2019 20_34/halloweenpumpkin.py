import time
from psychopy import visual
from psychopy.visual import ShapeStim

#step1: put picture on the screen
win = visual.Window(fullscr=True)
##picture=visual.ImageStim(win, image="pumpkin")
##picture.draw()

#step 2: orange pumpkin shape
ellips= visual.Polygon(win, edges = 200, radius = 0.4, pos=(0,-0.2), lineColor="orange", fillColor="orange")
ellips.draw()

#step 3: face of the pumpkin
#eyes
triangle=visual.Polygon(win, edges=3, radius=0.1, ori=110, pos=(-0.2,-0.1), lineColor="black", fillColor="black")
triangle.draw()
triangletwo=visual.Polygon(win, edges=3, radius=0.1, ori=-110, pos=(0.2,-0.1), lineColor="black", fillColor="black")
triangletwo.draw()
#nose
trianglethree=visual.Polygon(win, edges=3, radius=0.05, pos=(0,-0.175), lineColor="black", fillColor="black")
trianglethree.draw()

#mouth
mouthVert=[(-0.3,-0.25), (-0.15,-0.5),(0,-0.35),(0.15,-0.5),(0.3,-0.25), (0.15,-0.35),(0,-0.25),(-0.15,-0.35)]
mouth=ShapeStim(win, vertices=mouthVert, fillColor='black', lineWidth=2, lineColor='black')
mouth.draw()

#groene stengel
pointVert=[(0,0.4),(0,0.3),(-0.05,0.2),(0.1,0.2)]
point=ShapeStim(win, vertices=pointVert, fillColor='green', lineWidth=1, lineColor='green')
point.draw()

#HappyHalloween
Text=visual.TextStim(win, text=u"Happy Halloween!", color = "orange", pos=(0, 0.7), height=0.2)
Text.draw()
win.flip()
time.sleep(1)

###TIMEFRAME2###

#step 2: orange pumpkin shape
ellips= visual.Polygon(win, edges = 200, radius = 0.4, pos=(0,-0.2), lineColor="orange", fillColor="orange")
ellips.draw()

#step 3: face of the pumpkin
#eyes
triangle=visual.Polygon(win, edges=3, radius=0.1, ori=110, pos=(-0.2,-0.1), lineColor="black", fillColor="black")
triangle.draw()
triangletwo=visual.Polygon(win, edges=3, radius=0.1, ori=-110, pos=(0.2,-0.1), lineColor="black", fillColor="black")
triangletwo.draw()
#nose
trianglethree=visual.Polygon(win, edges=3, radius=0.05, pos=(0,-0.175), lineColor="black", fillColor="black")
trianglethree.draw()

#mouth
mouthVert=[(-0.3,-0.25), (-0.15,-0.5),(0,-0.35),(0.15,-0.5),(0.3,-0.25), (0.15,-0.35),(0,-0.25),(-0.15,-0.35)]
mouth=ShapeStim(win, vertices=mouthVert, fillColor='black', lineWidth=2, lineColor='black')
mouth.draw()

#groene stengel
pointVert=[(0,0.4),(0,0.3),(-0.05,0.2),(0.1,0.2)]
point=ShapeStim(win, vertices=pointVert, fillColor='green', lineWidth=1, lineColor='green')
point.draw()

win.flip()
time.sleep(0.5)

###TIMEFRAME3###

#step 2: orange pumpkin shape
ellips= visual.Polygon(win, edges = 200, radius = 0.4, pos=(0,-0.2), lineColor="orange", fillColor="orange")
ellips.draw()

#step 3: face of the pumpkin
#eyes
triangle=visual.Polygon(win, edges=3, radius=0.1, ori=110, pos=(-0.2,-0.1), lineColor="black", fillColor="black")
triangle.draw()
triangletwo=visual.Polygon(win, edges=3, radius=0.1, ori=-110, pos=(0.2,-0.1), lineColor="black", fillColor="black")
triangletwo.draw()
#nose
trianglethree=visual.Polygon(win, edges=3, radius=0.05, pos=(0,-0.175), lineColor="black", fillColor="black")
trianglethree.draw()

#mouth
mouthVert=[(-0.3,-0.25), (-0.15,-0.5),(0,-0.35),(0.15,-0.5),(0.3,-0.25), (0.15,-0.35),(0,-0.25),(-0.15,-0.35)]
mouth=ShapeStim(win, vertices=mouthVert, fillColor='black', lineWidth=2, lineColor='black')
mouth.draw()

#groene stengel
pointVert=[(0,0.4),(0,0.3),(-0.05,0.2),(0.1,0.2)]
point=ShapeStim(win, vertices=pointVert, fillColor='green', lineWidth=1, lineColor='green')
point.draw()

#HappyHalloween
Text=visual.TextStim(win, text=u"Happy Halloween!", color = "orange", pos=(0, 0.7), height=0.2)
Text.draw()
win.flip()
time.sleep(1)

###TIMEFRAME4###

#step 2: orange pumpkin shape
ellips= visual.Polygon(win, edges = 200, radius = 0.4, pos=(0,-0.2), lineColor="orange", fillColor="orange")
ellips.draw()

#step 3: face of the pumpkin
#eyes
triangle=visual.Polygon(win, edges=3, radius=0.1, ori=110, pos=(-0.2,-0.1), lineColor="black", fillColor="black")
triangle.draw()
triangletwo=visual.Polygon(win, edges=3, radius=0.1, ori=-110, pos=(0.2,-0.1), lineColor="black", fillColor="black")
triangletwo.draw()
#nose
trianglethree=visual.Polygon(win, edges=3, radius=0.05, pos=(0,-0.175), lineColor="black", fillColor="black")
trianglethree.draw()

#mouth
mouthVert=[(-0.3,-0.25), (-0.15,-0.5),(0,-0.35),(0.15,-0.5),(0.3,-0.25), (0.15,-0.35),(0,-0.25),(-0.15,-0.35)]
mouth=ShapeStim(win, vertices=mouthVert, fillColor='black', lineWidth=2, lineColor='black')
mouth.draw()

#groene stengel
pointVert=[(0,0.4),(0,0.3),(-0.05,0.2),(0.1,0.2)]
point=ShapeStim(win, vertices=pointVert, fillColor='green', lineWidth=1, lineColor='green')
point.draw()

win.flip()
time.sleep(0.5)

###TIMEFRAME5###

#step 2: orange pumpkin shape
ellips= visual.Polygon(win, edges = 200, radius = 0.4, pos=(0,-0.2), lineColor="orange", fillColor="orange")
ellips.draw()

#step 3: face of the pumpkin
#eyes
triangle=visual.Polygon(win, edges=3, radius=0.1, ori=110, pos=(-0.2,-0.1), lineColor="black", fillColor="black")
triangle.draw()
triangletwo=visual.Polygon(win, edges=3, radius=0.1, ori=-110, pos=(0.2,-0.1), lineColor="black", fillColor="black")
triangletwo.draw()
#nose
trianglethree=visual.Polygon(win, edges=3, radius=0.05, pos=(0,-0.175), lineColor="black", fillColor="black")
trianglethree.draw()

#mouth
mouthVert=[(-0.3,-0.25), (-0.15,-0.5),(0,-0.35),(0.15,-0.5),(0.3,-0.25), (0.15,-0.35),(0,-0.25),(-0.15,-0.35)]
mouth=ShapeStim(win, vertices=mouthVert, fillColor='black', lineWidth=2, lineColor='black')
mouth.draw()

#groene stengel
pointVert=[(0,0.4),(0,0.3),(-0.05,0.2),(0.1,0.2)]
point=ShapeStim(win, vertices=pointVert, fillColor='green', lineWidth=1, lineColor='green')
point.draw()

#HappyHalloween
Text=visual.TextStim(win, text=u"Happy Halloween!", color = "orange", pos=(0, 0.7), height=0.2)
Text.draw()
win.flip()
time.sleep(1)



win.close()