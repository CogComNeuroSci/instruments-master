#importing modules from psychopy
from psychopy import visual, event, core
#creating a window
win = visual.Window ( color = "white", fullscr = True )
#first, create the vertices of your shape
pumpkinvert = [(0.2, 0.35), (0.1, 0.35), (0, 0.23), (-0.1, 0.35), (-0.2, 0.35), (-0.25, 0.3), (-0.3, 0.2), (-0.32, 0), (-0.3, -0.2), (-0.25, -0.3), (-0.2, -0.35),
(-0.1, -0.35), (0, -0.33), (0.1, -0.35), (0.2, -0.35), (0.25, -0.3), (0.3, -0.2), (0.32, 0), (0.3, 0.2),(0.25, 0.3)]
#then, create the shape
pumpkin = visual.ShapeStim (win, vertices = pumpkinvert, fillColor = 'orange', lineColor = (0.820,-0.090,-1.000), lineWidth = 5)
#..and draw it
pumpkin.draw()
#do the same for the leaves
leafvert = [(0, 0.23), (-0.05, 0.265), (-0.07, 0.35), (0.01, 0.3)]
leaf = visual.ShapeStim (win, vertices = leafvert, fillColor = "green", lineColor = (-0.294,0.576,-0.655), lineWidth = 4)
leaf.draw()
leafvert2 = [(0, 0.23), (0.03, 0.24), (0.04, 0.3), (0.01, 0.3)]
leaf2 = visual.ShapeStim (win, vertices = leafvert2, fillColor = (-0.294,0.576,-0.655), lineColor = "green", lineWidth = 4)
leaf2.draw()
#... the stem
stemvert = [(0, 0.23), (-0.03, 0.38), (0.03, 0.4)]
stem = visual.ShapeStim (win, vertices = stemvert, fillColor = (0.004,-0.498,-1.000), lineWidth = 4, lineColor = "black")
stem.draw()
#Text "Happy Halloween!"
text11 = visual.TextStim(win, text = "Happy", color = "black", pos= (0, 0.6), bold = True, ori = -15)
text11.draw()
text12 = visual.TextStim(win, text = "Halloween!", color = "black", pos= (0, -0.6), bold = True, ori = 15)
text12.draw()
text21 = visual.TextStim(win, text = "Happy", color = "black", pos= (0.035, 0.55), bold = True, ori = -15, opacity = 0.25)
text22 = visual.TextStim(win, text = "Halloween!", color = "black", pos= (0.035, -0.55), bold = True, ori = 15, opacity = 0.25)

text21.draw()
text22.draw()
#the eyes
eyevert = [(-0.05, 0.05), (-0.15, 0.05), (-0.2, 0.20)]
eye = visual.ShapeStim (win, vertices = eyevert, fillColor = "black")
eye.draw()
eyevert2 = [(0.05, 0.05), (0.15, 0.05), (0.2, 0.20)]
eye2 = visual.ShapeStim (win, vertices = eyevert2, fillColor = "black")
eye2.draw()
#the nose
nosevert = [(0, 0.08), (-0.02, 0), (0.02, 0)]
nose = visual. ShapeStim (win, vertices = nosevert, fillColor = "black")
nose.draw()
#and the mouth
mouth_vert = [(0, -0.15),(-0.05, -0.2), (-0.1, -0.15), (-0.15, -0.2), (-0.25, 0.05), (-0.10, -0.10), (-0.05, -0.05), (0, -0.10), (0.05, -0.05), (0.10, -0.10), 
(0.25, 0.05), (0.15, -0.2), (0.1, -0.15), (0.05, -0.2)]
mouth = visual.ShapeStim (win, vertices = mouth_vert, fillColor = "black")
mouth.draw()
#show window where all the stimuli will appear
win.flip()
#... for 5 seconds
core.wait(5)
#close the window after that
win.close()