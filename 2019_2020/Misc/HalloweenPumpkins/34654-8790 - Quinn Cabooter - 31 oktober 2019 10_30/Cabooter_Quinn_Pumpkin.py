from psychopy import visual
import time
from psychopy.visual import ShapeStim

win = visual.Window(fullscr = True, units = 'norm', color = (-0.3,-1.000,-1.000))

#pumpkin shape
pumpkinVert = [(0,0.552), (2.1/14.85, 0.552),(4.2/14.85, 0.504),(5.1/14.85, 0.428), 
(6.3/14.85, 0.314), (6.8/14.85, 0.2), (7/14.85, 0.085), (7/14.85, 0),
(0,-0.552), (2.1/14.85, -0.552),(4.2/14.85, -0.504),(5.1/14.85, -0.428), 
(6.3/14.85, -0.314), (6.8/14.85, -0.2), (7/14.85, -0.085), (7/14.85, 0),
(0,-0.552), (-2.1/14.85, -0.552),(-4.2/14.85, -0.504),(-5.1/14.85, -0.428), 
(-6.3/14.85, -0.314), (-6.8/14.85, -0.2), (-7/14.85, -0.085), (-7/14.85, 0),
(0,0.552), (-2.1/14.85, 0.552),(-4.2/14.85, 0.504),(-5.1/14.85, 0.428), 
(-6.3/14.85, 0.314), (-6.8/14.85, 0.2), (-7/14.85, 0.085), (-7/14.85, 0)]

pumpkin = ShapeStim(win, vertices = pumpkinVert,lineColor = 'orange', fillColor = 'orange')

# Pumpkin Stem

stemVert = [(-4, 44.61),(4, 44.61), (4, 56), (10, 66), (6, 71), (-2, 60)]
stem = ShapeStim(win, size = 1/100, vertices = stemVert, lineColor = 'green', fillColor = 'green')

#Pumpkin eyes
eyesVert = [[(13.46, 26.92), (21.54, 12.46), (6, 12.46)],[(-13.46, 26.92), (-21.54, 12.46), (-6, 12.46)]]
eyes = ShapeStim(win, size = 0.01, vertices = eyesVert, lineColor = 'black', fillColor = 'black')

#Pumkin mouth

mouthVert = [[(0, -13.33), (8.39, -13.33),(8.39, -25.55), (16.08, -25.55), (16.08, -13.33),(26.57, -13.33),
(25.17, -21.11), (22.37, -28.88), (16.08, -35.55), (8.39, -37.77),(4, -38.88),(4,-26.5),(0, -26.5)],[(0, -13.30), (-8.39, -13.33),(-8.39, -25.55), (-16.08, -25.55), (-16.08, -13.33),(-26.57, -13.33),
(-25.17, -21.11), (-22.37, -28.88), (-16.08, -35.55), (-8.39, -37.77),(-4, -38.88),(-4,-26.5),(0, -26.5)]]
mouth= ShapeStim(win, size = 0.01, vertices = mouthVert, lineColor = 'black', fillColor =  'black')


# Nose
noseVert= [(0, 13.33), (5.59, 0), (-5.59,0)]
nose = ShapeStim(win, size = 0.01, vertices = noseVert, lineColor = 'black', fillColor = 'black')

# Happy halloween
txt = visual.TextStim(win, text= 'Happy halloween!', color = 'orange',font = 'Bradley Hand', pos = (0, -0.75))


pumpkin.draw()
stem.draw()
eyes.draw()
mouth.draw()
nose.draw()
txt.draw()

win.flip()


time.sleep(7)
win.close()