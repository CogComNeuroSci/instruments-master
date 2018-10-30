from psychopy import visual
import time
from psychopy import core

win = visual.Window ( fullscr = True, color = ("black"))

ellips1 = visual.Circle(win, fillColor = [1,0.35,0], ori = 0, lineColor = [1,0.2,0], radius = 0.5, pos = (-0.2,0), size = [0.5,0.9])
ellips2 = visual.Circle(win, fillColor = [1,0.4,0], ori = 0, lineColor = [1,0.2,0], radius = 0.5, pos = (-0.1,0), size = [0.5,0.96])
ellips3 = visual.Circle(win, fillColor = [1,0.42,0], ori = 0, lineColor = [1,0.2,0], radius = 0.5, pos = (0,0), size = [0.4,1])
ellips4 = visual.Circle(win, fillColor = [1,0.4,0], ori = 0, lineColor = [1,0.2,0], radius = 0.5, pos = (0.1,0), size = [0.5,0.96])
ellips5 = visual.Circle(win, fillColor = [1,0.35,0], ori = 0, lineColor = [1,0.2,0], radius = 0.5, pos = (0.2,0), size = [0.5,0.9])


verts1 = [(-0.05, 0.01), (-0.15, 0.20), (-0.3, 0.3), (-0.25,0.1)]
lefteye = visual.ShapeStim(win, fillColor='black', vertices=verts1, lineColor='black', opacity=1, pos = (-0.005,0.002))

verts2 = [(0.05, 0.01), (0.15, 0.20), (0.3, 0.3), (0.25,0.1)]
righteye = visual.ShapeStim(win, fillColor='black', vertices=verts2, lineColor='black', opacity=1, pos = (-0.005,0.002))

verts3 = [(-0.3, -0.05), (-0.27, -0.15), (-0.23,-0.07), (-0.19,-0.11), (-0.16,-0.04), (-0.12,-0.09), (-0.09,-0.07), (-0.04,-0.15),(-0.01,-0.09),
          (0.01,-0.11), (0.04,-0.07), (0.07,-0.06), (0.09,-0.11), (0.12,-0.09), (0.16,-0.04), (0.19,-0.11),(0.23,-0.07),(0.27, -0.15),(0.3, -0.09),
          (0.35, -0.20), (0.3,-0.17), (0.25,-0.23), (0.21,-0.19), (0.19,-0.24), (0.14,-0.20), (0.11,-0.25), (0.06,-0.19), (0.03,-0.22), (0,-0.18), (-0.02,-0.24), 
          (-0.07,-0.21), (-0.10,-0.22), (-0.14,-0.18), (-0.21,-0.23), (-0.26,-0.17), (-0.28,-0.20), (-0.33,-0.14)]
mouth = visual.ShapeStim(win, fillColor='black', vertices=verts3, lineColor='black', opacity=1, pos = (-0.005,0.002))


eye1 = visual.Circle(win, fillColor = ("red"), ori = -45, lineColor = ("red"), radius = 0.5, opacity=1, pos = (-0.2,0.15), size = [0.05,0.06])
eye2 = visual.Circle(win, fillColor = ("red"), ori = 45, lineColor = ("red"), radius = 0.5, opacity=1, pos = (0.2,0.15), size = [0.05,0.06])

stim = visual.TextStim(win,text = "Happy Halloween!", color = ("red"),pos = (0,-0.7))


ellips1.draw()
ellips5.draw()
ellips2.draw()
ellips4.draw()
ellips3.draw()
lefteye.draw()
righteye.draw()
mouth.draw()
eye1.draw()
eye2.draw()
stim.draw()
#
win.flip()
core.wait(1)

ellips1.draw()
ellips5.draw()
ellips2.draw()
ellips4.draw()
ellips3.draw()
lefteye.draw()
righteye.draw()
mouth.draw()
eye1.draw()
eye2.draw()
#
win.flip()
core.wait(0.5)
ellips1.draw()
ellips5.draw()
ellips2.draw()
ellips4.draw()
ellips3.draw()
lefteye.draw()
righteye.draw()
mouth.draw()
eye1.draw()
eye2.draw()
stim.draw()
#
win.flip()
core.wait(0.5)

ellips1.draw()
ellips5.draw()
ellips2.draw()
ellips4.draw()
ellips3.draw()
lefteye.draw()
righteye.draw()
mouth.draw()
eye1.draw()
eye2.draw()
stim.draw()
#
win.flip()
core.wait(1)

ellips1.draw()
ellips5.draw()
ellips2.draw()
ellips4.draw()
ellips3.draw()
lefteye.draw()
righteye.draw()
mouth.draw()
eye1.draw()
eye2.draw()
#
win.flip()
core.wait(0.5)
ellips1.draw()
ellips5.draw()
ellips2.draw()
ellips4.draw()
ellips3.draw()
lefteye.draw()
righteye.draw()
mouth.draw()
eye1.draw()
eye2.draw()
stim.draw()

win.flip()
time.sleep(5)
win.close()
