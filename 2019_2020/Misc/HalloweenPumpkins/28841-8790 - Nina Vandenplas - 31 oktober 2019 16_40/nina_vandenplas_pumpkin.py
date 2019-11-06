from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time

win = visual.Window(size=(500, 400), units='height')

#pompoen
pompoenVert = [(0,-0.5),(0.15,-0.38),(0.35,-0.35),(0.53,-0.18),(0.7,0),(0.53,0.18),(0.35,0.35),(0.15,0.38),(0,0.5),(-0.15,0.38),(-0.35,0.35),(-0.53,0.18),(-0.7,0),(-0.53,-0.18),(-0.35,-0.35),(-0.15,-0.38)]
pompoen = ShapeStim(win, vertices=pompoenVert, fillColor='orange', size=.8)

#oogjes
oogVert = [(-0.3,0.3),(-0.4,0.1),(-0.2,0.1)]
oog = ShapeStim(win, vertices=oogVert, fillColor='black', size=0.8)

oogVert2 = [(0.3,0.3),(0.4,0.1),(0.2,0.1)]
oog2=ShapeStim(win, vertices=oogVert2, fillColor='black', size=0.8)

#mondje
mondjeVert = [(-0.5,-0.05),(0,-0.2),(0.5,-0.05),(0,-0.4)]
mondje = ShapeStim(win, vertices=mondjeVert, fillColor='black', size=0.8)

#neusje
neusjeVert = [(0,0.1),(-0.1,-0.1),(0.1,-0.1)]
neusje = ShapeStim(win,vertices=neusjeVert, fillColor='black',size=0.8)

#steeltje
steeltjeVert = [(-0.15,0.4),(0.15,0.6),(0.3,0.5),(0.1,0.4)]
steeltje = ShapeStim(win, vertices=steeltjeVert, fillColor='green',size=0.8)

#tekst
stim = visual.TextStim(win, text = "Happy Halloween!", color ='red',pos=(-0.1,-0.4),height=0.1)


pompoen.draw()
oog.draw()
oog2.draw()
mondje.draw()
neusje.draw()
steeltje.draw()
stim.draw()
win.flip()
time.sleep(5)