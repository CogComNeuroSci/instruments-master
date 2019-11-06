import time
from psychopy import visual
win = visual.Window()


#POMPOEN MET tekst


#steel

steelVertices = [(0.1,0.65),(-0.1,0.65),(-0.05,0.8),(-0.15,0.85),(-0.05,0.9),(0.05,0.8)]
steel = visual.ShapeStim(win, vertices = steelVertices , fillColor = 'brown', lineColor = 'brown')
steel.draw()

#pompoenachtergrond

ovaal1= visual.Polygon(win, edges = 100, radius = (0.9,0.7), pos = (0,0), lineColor = 'yellow' , fillColor = 'orange')
ovaal1.draw()
ovaal2= visual.Polygon(win, edges = 100, radius = (0.75,0.7), pos = (0,0), lineColor = 'yellow')
ovaal2.draw()
ovaal3= visual.Polygon(win, edges = 100, radius = (0.6,0.7), pos = (0,0), lineColor = 'yellow')
ovaal3.draw()
ovaal4= visual.Polygon(win, edges = 100, radius = (0.45,0.7), pos = (0,0), lineColor = 'yellow')
ovaal4.draw()
ovaal5= visual.Polygon(win, edges = 100, radius = (0.3,0.7), pos = (0,0), lineColor = 'yellow')
ovaal5.draw()
ovaal6= visual.Polygon(win, edges = 100, radius = (0.15,0.7), pos = (0,0), lineColor = 'yellow')
ovaal6.draw()

middellijn= visual.Line(win, start=(0, 0.7), end=(0,-0.7), lineColor = 'yellow')
middellijn.draw()

#ogen

LoogVertices = [(-0.4,0.3),(-0.15,0.1),(-0.4,0.1)]
Loog = visual.ShapeStim(win, vertices = LoogVertices , fillColor = 'black', lineColor = 'black')
Loog.draw()

RoogVertices = [(0.4,0.3),(0.15,0.1),(0.4,0.1)]
Roog = visual.ShapeStim(win, vertices = RoogVertices , fillColor = 'black', lineColor = 'black')
Roog.draw()

#mond

mondVertices = [(-0.45,-0.35),(-0.3,-0.25),(-0.2,-0.3),(-0.1,-0.25),(0,-0.3),(0.1,-0.25),(0.2,-0.3),(0.3,-0.25),(0.45,-0.35),(0.3,-0.35),(0.2,-0.4),(0.1,-0.35),(0,-0.4),(-0.1,-0.35),(-0.2,-0.4),(-0.3,-0.35)]
mond = visual.ShapeStim(win, vertices = mondVertices , fillColor = 'black', lineColor = 'black')
mond.draw()

#tekst

tekst = visual.TextStim(win, text= "Happy Halloween!", color='white', pos = (0,-0.80))
tekst.draw()

win.flip()
time.sleep(1)






#ENKEL POMPOEN



#steel

steelVertices = [(0.1,0.65),(-0.1,0.65),(-0.05,0.8),(-0.15,0.85),(-0.05,0.9),(0.05,0.8)]
steel = visual.ShapeStim(win, vertices = steelVertices , fillColor = 'brown', lineColor = 'brown')
steel.draw()

#pompoenachtergrond

ovaal1= visual.Polygon(win, edges = 100, radius = (0.9,0.7), pos = (0,0), lineColor = 'yellow' , fillColor = 'orange')
ovaal1.draw()
ovaal2= visual.Polygon(win, edges = 100, radius = (0.75,0.7), pos = (0,0), lineColor = 'yellow')
ovaal2.draw()
ovaal3= visual.Polygon(win, edges = 100, radius = (0.6,0.7), pos = (0,0), lineColor = 'yellow')
ovaal3.draw()
ovaal4= visual.Polygon(win, edges = 100, radius = (0.45,0.7), pos = (0,0), lineColor = 'yellow')
ovaal4.draw()
ovaal5= visual.Polygon(win, edges = 100, radius = (0.3,0.7), pos = (0,0), lineColor = 'yellow')
ovaal5.draw()
ovaal6= visual.Polygon(win, edges = 100, radius = (0.15,0.7), pos = (0,0), lineColor = 'yellow')
ovaal6.draw()

middellijn= visual.Line(win, start=(0, 0.7), end=(0,-0.7), lineColor = 'yellow')
middellijn.draw()

#ogen

LoogVertices = [(-0.4,0.3),(-0.15,0.1),(-0.4,0.1)]
Loog = visual.ShapeStim(win, vertices = LoogVertices , fillColor = 'black', lineColor = 'black')
Loog.draw()

RoogVertices = [(0.4,0.3),(0.15,0.1),(0.4,0.1)]
Roog = visual.ShapeStim(win, vertices = RoogVertices , fillColor = 'black', lineColor = 'black')
Roog.draw()

#mond

mondVertices = [(-0.45,-0.35),(-0.3,-0.25),(-0.2,-0.3),(-0.1,-0.25),(0,-0.3),(0.1,-0.25),(0.2,-0.3),(0.3,-0.25),(0.45,-0.35),(0.3,-0.35),(0.2,-0.4),(0.1,-0.35),(0,-0.4),(-0.1,-0.35),(-0.2,-0.4),(-0.3,-0.35)]
mond = visual.ShapeStim(win, vertices = mondVertices , fillColor = 'black', lineColor = 'black')
mond.draw()


win.flip()
time.sleep(1.5)





#POMPOEN MET tekst



#steel

steelVertices = [(0.1,0.65),(-0.1,0.65),(-0.05,0.8),(-0.15,0.85),(-0.05,0.9),(0.05,0.8)]
steel = visual.ShapeStim(win, vertices = steelVertices , fillColor = 'brown', lineColor = 'brown')
steel.draw()

#pompoenachtergrond

ovaal1= visual.Polygon(win, edges = 100, radius = (0.9,0.7), pos = (0,0), lineColor = 'yellow' , fillColor = 'orange')
ovaal1.draw()
ovaal2= visual.Polygon(win, edges = 100, radius = (0.75,0.7), pos = (0,0), lineColor = 'yellow')
ovaal2.draw()
ovaal3= visual.Polygon(win, edges = 100, radius = (0.6,0.7), pos = (0,0), lineColor = 'yellow')
ovaal3.draw()
ovaal4= visual.Polygon(win, edges = 100, radius = (0.45,0.7), pos = (0,0), lineColor = 'yellow')
ovaal4.draw()
ovaal5= visual.Polygon(win, edges = 100, radius = (0.3,0.7), pos = (0,0), lineColor = 'yellow')
ovaal5.draw()
ovaal6= visual.Polygon(win, edges = 100, radius = (0.15,0.7), pos = (0,0), lineColor = 'yellow')
ovaal6.draw()

middellijn= visual.Line(win, start=(0, 0.7), end=(0,-0.7), lineColor = 'yellow')
middellijn.draw()

#ogen

LoogVertices = [(-0.4,0.3),(-0.15,0.1),(-0.4,0.1)]
Loog = visual.ShapeStim(win, vertices = LoogVertices , fillColor = 'black', lineColor = 'black')
Loog.draw()

RoogVertices = [(0.4,0.3),(0.15,0.1),(0.4,0.1)]
Roog = visual.ShapeStim(win, vertices = RoogVertices , fillColor = 'black', lineColor = 'black')
Roog.draw()

#mond

mondVertices = [(-0.45,-0.35),(-0.3,-0.25),(-0.2,-0.3),(-0.1,-0.25),(0,-0.3),(0.1,-0.25),(0.2,-0.3),(0.3,-0.25),(0.45,-0.35),(0.3,-0.35),(0.2,-0.4),(0.1,-0.35),(0,-0.4),(-0.1,-0.35),(-0.2,-0.4),(-0.3,-0.35)]
mond = visual.ShapeStim(win, vertices = mondVertices , fillColor = 'black', lineColor = 'black')
mond.draw()

#tekst

tekst = visual.TextStim(win, text= "Happy Halloween!", color='white', pos = (0,-0.80))
tekst.draw()

win.flip()
time.sleep(1)



#ENKEL POMPOEN



#steel

steelVertices = [(0.1,0.65),(-0.1,0.65),(-0.05,0.8),(-0.15,0.85),(-0.05,0.9),(0.05,0.8)]
steel = visual.ShapeStim(win, vertices = steelVertices , fillColor = 'brown', lineColor = 'brown')
steel.draw()

#pompoenachtergrond

ovaal1= visual.Polygon(win, edges = 100, radius = (0.9,0.7), pos = (0,0), lineColor = 'yellow' , fillColor = 'orange')
ovaal1.draw()
ovaal2= visual.Polygon(win, edges = 100, radius = (0.75,0.7), pos = (0,0), lineColor = 'yellow')
ovaal2.draw()
ovaal3= visual.Polygon(win, edges = 100, radius = (0.6,0.7), pos = (0,0), lineColor = 'yellow')
ovaal3.draw()
ovaal4= visual.Polygon(win, edges = 100, radius = (0.45,0.7), pos = (0,0), lineColor = 'yellow')
ovaal4.draw()
ovaal5= visual.Polygon(win, edges = 100, radius = (0.3,0.7), pos = (0,0), lineColor = 'yellow')
ovaal5.draw()
ovaal6= visual.Polygon(win, edges = 100, radius = (0.15,0.7), pos = (0,0), lineColor = 'yellow')
ovaal6.draw()

middellijn= visual.Line(win, start=(0, 0.7), end=(0,-0.7), lineColor = 'yellow')
middellijn.draw()

#ogen

LoogVertices = [(-0.4,0.3),(-0.15,0.1),(-0.4,0.1)]
Loog = visual.ShapeStim(win, vertices = LoogVertices , fillColor = 'black', lineColor = 'black')
Loog.draw()

RoogVertices = [(0.4,0.3),(0.15,0.1),(0.4,0.1)]
Roog = visual.ShapeStim(win, vertices = RoogVertices , fillColor = 'black', lineColor = 'black')
Roog.draw()

#mond

mondVertices = [(-0.45,-0.35),(-0.3,-0.25),(-0.2,-0.3),(-0.1,-0.25),(0,-0.3),(0.1,-0.25),(0.2,-0.3),(0.3,-0.25),(0.45,-0.35),(0.3,-0.35),(0.2,-0.4),(0.1,-0.35),(0,-0.4),(-0.1,-0.35),(-0.2,-0.4),(-0.3,-0.35)]
mond = visual.ShapeStim(win, vertices = mondVertices , fillColor = 'black', lineColor = 'black')
mond.draw()


win.flip()
time.sleep(1.5)



#POMPOEN MET tekst



#steel

steelVertices = [(0.1,0.65),(-0.1,0.65),(-0.05,0.8),(-0.15,0.85),(-0.05,0.9),(0.05,0.8)]
steel = visual.ShapeStim(win, vertices = steelVertices , fillColor = 'brown', lineColor = 'brown')
steel.draw()

#pompoenachtergrond

ovaal1= visual.Polygon(win, edges = 100, radius = (0.9,0.7), pos = (0,0), lineColor = 'yellow' , fillColor = 'orange')
ovaal1.draw()
ovaal2= visual.Polygon(win, edges = 100, radius = (0.75,0.7), pos = (0,0), lineColor = 'yellow')
ovaal2.draw()
ovaal3= visual.Polygon(win, edges = 100, radius = (0.6,0.7), pos = (0,0), lineColor = 'yellow')
ovaal3.draw()
ovaal4= visual.Polygon(win, edges = 100, radius = (0.45,0.7), pos = (0,0), lineColor = 'yellow')
ovaal4.draw()
ovaal5= visual.Polygon(win, edges = 100, radius = (0.3,0.7), pos = (0,0), lineColor = 'yellow')
ovaal5.draw()
ovaal6= visual.Polygon(win, edges = 100, radius = (0.15,0.7), pos = (0,0), lineColor = 'yellow')
ovaal6.draw()

middellijn= visual.Line(win, start=(0, 0.7), end=(0,-0.7), lineColor = 'yellow')
middellijn.draw()

#ogen

LoogVertices = [(-0.4,0.3),(-0.15,0.1),(-0.4,0.1)]
Loog = visual.ShapeStim(win, vertices = LoogVertices , fillColor = 'black', lineColor = 'black')
Loog.draw()

RoogVertices = [(0.4,0.3),(0.15,0.1),(0.4,0.1)]
Roog = visual.ShapeStim(win, vertices = RoogVertices , fillColor = 'black', lineColor = 'black')
Roog.draw()

#mond

mondVertices = [(-0.45,-0.35),(-0.3,-0.25),(-0.2,-0.3),(-0.1,-0.25),(0,-0.3),(0.1,-0.25),(0.2,-0.3),(0.3,-0.25),(0.45,-0.35),(0.3,-0.35),(0.2,-0.4),(0.1,-0.35),(0,-0.4),(-0.1,-0.35),(-0.2,-0.4),(-0.3,-0.35)]
mond = visual.ShapeStim(win, vertices = mondVertices , fillColor = 'black', lineColor = 'black')
mond.draw()

#tekst

tekst = visual.TextStim(win, text= "Happy Halloween!", color='white', pos = (0,-0.80))
tekst.draw()

win.flip()
time.sleep(1)



win.close()

