
from psychopy import visual,core

win = visual.Window([700,500], units="pix",color=(-1,-1,-1))

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(1)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)
circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

text = visual.TextStim(
    win,
    text = "Happy Halloween",
    font ='Chiller',
    opacity = 0.5,
    height = 80,
    pos= (0,-180)
)

text.draw()

text.pos = [3,-177]
text.color = [1,1,1]

text.draw()

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Tekst voor een halve seconde tonen
core.wait(0.5)

stem = visual.Polygon(
    win,
    edges=3,
    radius= 40,
    lineColor='green',
    fillColor='green',
    pos=(0,150),
    ori=180
)

stem.draw()

stem.pos = [5,155]
stem.opacity = 0.5
stem.draw()


circle = visual.Circle(
    win,
    radius=150,
    edges=100,
    fillColor='orange',
    lineColor='orange'
)

circle_offset = 65

for offset in [-1,1]:
    circle.pos =[offset*circle_offset,0]
    circle.draw()

circle.pos = [offset*circle_offset+5,5]
circle.opacity = 0.5
circle.draw()

eyes = visual.Polygon(
    win,
    edges=3,
    radius=40,
    fillColor='black',
    lineColor='black'
)

eyes_offset= 75

for offset in [-1,1]:
    eyes.pos=[offset*eyes_offset,50]
    eyes.draw()

nose = visual.Polygon(
    win,
    edges=3,
    radius=20,
    fillColor='black',
    lineColor='black'
)
nose.draw()

mouthVert=[(-100,-50),(100,-50),(100,-50),(75,-75),(60,-90),(30,-100),(0,-100),(-30,-100),(-60,-90),(-75,-75)]

mouthline=visual.ShapeStim(
    win,
    lineColor='black',
    fillColor='black',
    closeShape=True,
    vertices= mouthVert,
    lineWidth=5
)

mouthline.draw()

teeth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25
)

teeth_offset = 30

for offset in [-1,1]:
    teeth.pos=[offset*teeth_offset,-50]
    teeth.draw()

tooth = visual.Rect(
    win,
    lineColor='orange',
    fillColor='orange',
    width = 25,
    height = 25,
    pos= (0,-100)
)

tooth.draw()

win.flip()

#Enkel foto tonen
core.wait(0.5)

win.close()
