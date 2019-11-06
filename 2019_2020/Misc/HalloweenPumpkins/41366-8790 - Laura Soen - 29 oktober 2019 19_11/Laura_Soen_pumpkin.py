from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)



win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)


win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

#tekst
stim = visual.TextStim(win, font= 'ObelixProBroken', text="Happy Halloween!", color= 'darkred', pos=(0,-0.8))
stim.draw()

win.flip()
time.sleep(1)

win = visual.Window(fullscr=True)


oval = visual.Circle(
    win=win,
    radius= [260, 220],
    units="pix",
    fillColor= ('darkorange'), lineColor= ('brown'), lineWidth= 8)
oval.draw()

oval1 = visual.Circle(
    win=win,
    radius= [40, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), size= 1.22)
oval1.draw()

oval2 = visual.Circle(
    win=win,
    radius= [80, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 2, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [120, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 3, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [130, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 4, size= 1.22)
oval2.draw()

oval2 = visual.Circle(
    win=win,
    radius= [160, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 5, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [170, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 6, size= 1.22)
oval2.draw

oval2 = visual.Circle(
    win=win,
    radius= [180, 180],
    units="pix",
    fillColor= None, lineColor= ('brown'), lineWidth= 7, size= 1.22)
oval2.draw()
#mond

vierkant= visual.Rect(win, width = 0.37, height = 0.19, color = 'yellow', pos=(0.01, -0.35))
vierkant.draw()

vierkant2= visual.Rect(win, width = 0.35, height = 0.17, color = 'brown', pos=(0.01, -0.35))
vierkant2.draw()


selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0, -.25), size=0.3)
selfx.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx2 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.1, -.25), size=0.3)
selfx2.draw()

selfxVert = [(0.1, 0),(0.2, -.3), (.3, 0)]
selfx3 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.2, -.25), size=0.3)
selfx3.draw()

selfxVert = [(0.12, 0),(0.22, -.3), (.32, 0)]
selfx4 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.1, -.25), size=0.3)
selfx4.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx5 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.02, -.45), size=0.3)
selfx5.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx6 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.08, -.45), size=0.3)
selfx6.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx7 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(-0.17, -.45), size=0.3)
selfx7.draw()

selfxVert = [(0.12, 0),(0.22, .3), (.32, 0)]
selfx8 = ShapeStim(win, vertices=selfxVert, fillColor='darkorange', lineColor='darkorange', pos=(0.12, -.45), size=0.3)
selfx8.draw()

#ogen


driehoek = ShapeStim(win, vertices=((0.1, 0),(0.1, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.31, .1), size=0.8)
driehoek.draw()

driehoek1 = ShapeStim(win, vertices=((0.1, 0),(0.3, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(0, .1), size=0.8)
driehoek1.draw()

driehoek2 = ShapeStim(win, vertices=((0.1, 0.0),(0.1, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.27, .11), size=0.7)
driehoek2.draw()

driehoek3 = ShapeStim(win, vertices=((0.1, 0.0),(0.3, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(0, .11), size=0.7)
driehoek3.draw()

#neus

driehoek4 = ShapeStim(win, vertices=((0.1, 0),(0.2, .2), (.3, 0)), fillColor='brown', lineColor='brown', pos=(-0.08, -0.10), size=0.4)
driehoek4.draw()
driehoek5 = ShapeStim(win, vertices=((0.1, 0.0),(0.2, .17), (.3, 0.0)), fillColor='yellow', lineColor='yellow', pos=(-0.07, -0.09), size=0.3)
driehoek5.draw()

#steel


driehoek5 = visual.Rect(win, width = 0.05, height = 0.12, fillColor='green', lineColor='green', pos=(0.01, 0.68), size=1)
driehoek5.draw()

win.flip()
time.sleep(0.5)
win.close()
