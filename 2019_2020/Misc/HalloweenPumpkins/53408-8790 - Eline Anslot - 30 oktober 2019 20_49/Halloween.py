import time
from psychopy import visual

win = visual.Window(fullscr = True, unit = 'deg', monitor = 'testMonitor')

#Real Halloween Pumpkin
Picture = "Halloween.jpg"
Halloween_Image = visual.ImageStim(win, image = Picture)
Halloween_Image.draw()
win.flip()
time.sleep(1)

#Halloween_Text alleen
Halloween_Text = visual.TextStim(win, text = "Happy Halloween!", color = "red", pos = (0, 0.8), bold = True)
Halloween_Text.draw()
win.flip()
time.sleep(0.5)

#My Halloween Pumpkin
Halloween_Text = visual.TextStim(win, text = "Happy Halloween!", color = "red", pos = (0, 0.9), bold = True)
Halloween_Text.draw()

Light_white = visual.ElementArrayStim(win, fieldShape = "circle", nElements = 1, fieldPos=(-0.8, 0.5))
Light_white.draw()

Light_black = visual.ElementArrayStim(win, fieldShape = "circle", nElements = 4, fieldPos=(0.8, -0.5), colors = "black")
Light_black.draw()

Branch = visual.ShapeStim(win, fillColor = "brown", lineColor = "black", vertices = [(0, 0), (0, 0.2), (0.1, 0.3),(0.1, 0)], pos = (-0.05, 0.49))
Branch.draw()

Pumpkin_shape_background = visual.GratingStim(win, tex = 'saw', mask = "circle", color = "black", size = 0.999)
Pumpkin_shape_background.draw()

Pumpkin_shape = visual.Polygon(win, edges = 30, radius = 0.5, fillColor = "orange", lineColor = 'black', opacity = 0.75)
Pumpkin_shape.draw()

Vertices_Point = [(0.1, 0.8), (0.3, -0.4), (0.4, -0.2), (0.6, -0.2), (0.6, -0.8), (0.8, -0.8), (0.8, -0.2), (1, -0.2), (1, -0.7), (1.1, -0.7), (1.3, -0.2), (1.5, -0.4), (1.7, 0.8)]
Smile = visual.ShapeStim(win, fillColor = "black", lineColor= "black", lineWidth= 3, vertices = Vertices_Point, size = (0.3, 0.2), units = 'norm', pos = (-0.3, -0.2), opacity = 0.8)
Smile.draw()

Eye = visual.ShapeStim(win, fillColor = "black", lineColor = "black", vertices = [(0, 0.3), (0.1, 0), (0.5, -0.3), (-0.2, -0.2)], units = 'norm', size = (0.2, 0.3), pos = (-0.3, 0.2))
Eye.draw()

Eye_flip = visual.ShapeStim(win, fillColor = "black", lineColor = "black", vertices = [(0.8, 0.3), (0.7, 0), (0.3, -0.3), (1, -0.2)], units = 'norm', size = (0.2, 0.3), pos = (0, 0.2))
Eye_flip.draw()

win.flip()
time.sleep(1)

#Zonder Halloween_Text

Light_white = visual.ElementArrayStim(win, fieldShape = "circle", nElements = 1, fieldPos=(-0.8, 0.5))
Light_white.draw()

Light_black = visual.ElementArrayStim(win, fieldShape = "circle", nElements = 4, fieldPos=(0.8, -0.5), colors = "black")
Light_black.draw()

Branch = visual.ShapeStim(win, fillColor = "brown", lineColor = "black", vertices = [(0, 0), (0, 0.2), (0.1, 0.3),(0.1, 0)], pos = (-0.05, 0.49))
Branch.draw()

Pumpkin_shape_background = visual.GratingStim(win, tex = 'saw', mask = "circle", color = "black", size = 0.999)
Pumpkin_shape_background.draw()

Pumpkin_shape = visual.Polygon(win, edges = 30, radius = 0.5, fillColor = "orange", lineColor = 'black', opacity = 0.75)
Pumpkin_shape.draw()

Vertices_Point = [(0.1, 0.8), (0.3, -0.4), (0.4, -0.2), (0.6, -0.2), (0.6, -0.8), (0.8, -0.8), (0.8, -0.2), (1, -0.2), (1, -0.7), (1.1, -0.7), (1.3, -0.2), (1.5, -0.4), (1.7, 0.8)]
Smile = visual.ShapeStim(win, fillColor = "black", lineColor= "black", lineWidth= 3, vertices = Vertices_Point, size = (0.3, 0.2), units = 'norm', pos = (-0.3, -0.2), opacity = 0.8)
Smile.draw()

Eye = visual.ShapeStim(win, fillColor = "black", lineColor = "black", vertices = [(0, 0.3), (0.1, 0), (0.5, -0.3), (-0.2, -0.2)], units = 'norm', size = (0.2, 0.3), pos = (-0.3, 0.2))
Eye.draw()

Eye_flip = visual.ShapeStim(win, fillColor = "black", lineColor = "black", vertices = [(0.8, 0.3), (0.7, 0), (0.3, -0.3), (1, -0.2)], units = 'norm', size = (0.2, 0.3), pos = (0, 0.2))
Eye_flip.draw()

win.flip()
time.sleep(1)

#My Halloween Pumpkin
Halloween_Text = visual.TextStim(win, text = "Happy Halloween!", color = "red", pos = (0, 0.9), bold = True)
Halloween_Text.draw()

Light_white = visual.ElementArrayStim(win, fieldShape = "circle", nElements = 1, fieldPos=(-0.8, 0.5))
Light_white.draw()

Light_black = visual.ElementArrayStim(win, fieldShape = "circle", nElements = 4, fieldPos=(0.8, -0.5), colors = "black")
Light_black.draw()

Branch = visual.ShapeStim(win, fillColor = "brown", lineColor = "black", vertices = [(0, 0), (0, 0.2), (0.1, 0.3),(0.1, 0)], pos = (-0.05, 0.49))
Branch.draw()

Pumpkin_shape_background = visual.GratingStim(win, tex = 'saw', mask = "circle", color = "black", size = 0.999)
Pumpkin_shape_background.draw()

Pumpkin_shape = visual.Polygon(win, edges = 30, radius = 0.5, fillColor = "orange", lineColor = 'black', opacity = 0.75)
Pumpkin_shape.draw()

Vertices_Point = [(0.1, 0.8), (0.3, -0.4), (0.4, -0.2), (0.6, -0.2), (0.6, -0.8), (0.8, -0.8), (0.8, -0.2), (1, -0.2), (1, -0.7), (1.1, -0.7), (1.3, -0.2), (1.5, -0.4), (1.7, 0.8)]
Smile = visual.ShapeStim(win, fillColor = "black", lineColor= "black", lineWidth= 3, vertices = Vertices_Point, size = (0.3, 0.2), units = 'norm', pos = (-0.3, -0.2), opacity = 0.8)
Smile.draw()

Eye = visual.ShapeStim(win, fillColor = "black", lineColor = "black", vertices = [(0, 0.3), (0.1, 0), (0.5, -0.3), (-0.2, -0.2)], units = 'norm', size = (0.2, 0.3), pos = (-0.3, 0.2))
Eye.draw()

Eye_flip = visual.ShapeStim(win, fillColor = "black", lineColor = "black", vertices = [(0.8, 0.3), (0.7, 0), (0.3, -0.3), (1, -0.2)], units = 'norm', size = (0.2, 0.3), pos = (0, 0.2))
Eye_flip.draw()

win.flip()
time.sleep(1)