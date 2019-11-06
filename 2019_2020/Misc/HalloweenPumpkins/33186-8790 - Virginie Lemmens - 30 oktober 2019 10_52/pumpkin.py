from psychopy import visual
import time
from psychopy.visual import ShapeStim
win = visual.Window(size=[600,400], color='black')
win.flip()
# ovaal maken
vert = ([-0.7,0], [-0.6,0.3], [0,0.5], [0.6,0.3], [0.7,0], [0.6,-0.3], [0,-0.6], [-0.6, -0.3])
bol = ShapeStim(win, vertices= vert, fillColor= 'orange', size= 0.8, pos= (0,0))
bol.draw()
# steel maken
vert2= ([-0.15,0.5], [-0.1,0.7], [0.05,0.8], [0.1,0.7], [0,0.5])
steel= ShapeStim(win, vertices=vert2, fillColor= 'green', size= 0.8, pos= (0,0))
steel.draw()
# ogen
Oog1Vert = ([-0.4,0.1], [-0.1,0.1], [-0.25,0.4])
oog1 = ShapeStim(win, vertices= Oog1Vert, fillColor= 'black', size=0.8, pos=(0,0))
oog1.draw()
oog2Vert= ([0.4,0.1], [0.1, 0.1], [0.25, 0.4])
oog2 = ShapeStim(win, vertices= oog2Vert, fillColor='black', size=0.8, pos= (0,0))
oog2.draw()
# mond 
mondVert = ([-0.4, -0.1], [0, -0.15], [0.4, -0.1], [0, -0.4])
mond = ShapeStim(win, vertices= mondVert, fillColor='black', size= 0.8, pos=(0,0))
mond.draw()
tekst = visual.TextStim(win, text= 'Happy Halloween!', color='orange', pos=(0,-0.8))
tekst.draw()
win.flip()
time.sleep(8)
win.close()
