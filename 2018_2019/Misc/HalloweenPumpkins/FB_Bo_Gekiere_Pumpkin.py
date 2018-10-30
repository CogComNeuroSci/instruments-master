from psychopy import visual,event,core
import time
win = visual.Window(monitor="testMonitor",size =[600,400], color= "black",units="norm")
pumpkinOrange = [(-.2,-.1),(-.4,-.3),(-.4,-.6),(-.2,-.8),(.2,-.8),(.4,-.6),(.4,-.3),(.2,-.1)]
Loog1 = [(-.2,-.3),(-.3,-.4),(-.1,-.4)]
Roog1 = [(.2,-.3),(.3,-.4),(.1,-.4)]
Mond = [(.2,-.6),(-.1,-.7),(-.2,-.6),(.1,-.7)]pumpkin = visual.ShapeStim(win, vertices = pumpkinOrange, fillColor = 'orange', lineWidth = 0, size = .75, pos = (0,0))
Loog = visual.ShapeStim(win, vertices = Loog1, fillColor = 'black', lineWidth = 0, size = .75, pos = (0,0))
Roog = visual.ShapeStim(win, vertices = Roog1, fillColor = 'black', lineWidth = 0, size = .75, pos = (0,0))
Mond = visual.ShapeStim(win, vertices = Mond, fillColor = 'black', lineWidth = 0, size = .75, pos = (0,0))
pumpkin.draw()
Loog.draw()
Roog.draw()
Mond.draw()win.flip()time.sleep(2) win.close()