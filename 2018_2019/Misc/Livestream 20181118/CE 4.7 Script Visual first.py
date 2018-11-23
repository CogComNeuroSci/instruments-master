from psychopy import visual
import time

win = visual.Window(color = "black")
#poging 2
##hoe gaat Bitcoin evolueren
a= visual.Line(win,start=(-0.7, -0.6), end=(-0.6,-0.6),lineColor="white")
b= visual.Line(win,start=(-0.6,-0.6), end=(-0.50,-0.59),lineColor="white")
c= visual.Line(win,start=(-0.50,-0.59), end=(-0.40,-0.57),lineColor="white")
d= visual.Line(win,start=(-0.40,-0.57), end=(-0.30,-0.53),lineColor="white")
b.draw()
c.draw()
d.draw()


mogelijkewaarden = (-0.01,0.02,0.06,0.09)
for i in mogelijkewaarden:
    e= visual.Line(win,start=(-0.30,-0.53), end=(-0.10,-0.45+i),lineColor=(0.35,0,0))
    f= visual.Line(win,start=(-0.1, -0.45+i), end=(0,-0.35+i),lineColor=(0.65,0,0))
    g= visual.Line(win,start=(0,-0.35+i), end=(0.1,-0.2+i),lineColor=(0.85,0,0))
    h= visual.Line(win,start=(0.1,-0.20+i), end=(0.2,0.10+i),lineColor="red")
    if i == 0.02:
        e= visual.Line(win,start=(-0.30,-0.53), end=(-0.10,-0.45+i),lineColor=(0,0.35,0))
        f= visual.Line(win,start=(-0.1, -0.45+i), end=(0,-0.35+i),lineColor=(0,0.65,0))
        g= visual.Line(win,start=(0,-0.35+i), end=(0.1,-0.2+i),lineColor=(0,0.85,0))
        h= visual.Line(win,start=(0.1,-0.20+i), end=(0.2,0.10+i),lineColor="green")
    if i ==0.06:
        e= visual.Line(win,start=(-0.30,-0.53), end=(-0.10,-0.45+i),lineColor=(0,0,0.35))
        f= visual.Line(win,start=(-0.1, -0.45+i), end=(0,-0.35+i),lineColor=(0,0,0.65))
        g= visual.Line(win,start=(0,-0.35+i), end=(0.1,-0.2+i),lineColor=(0,0,0.85))
        h= visual.Line(win,start=(0.1,-0.20+i), end=(0.2,0.10+i),lineColor="blue")
    if i ==0.09:
        e= visual.Line(win,start=(-0.30,-0.53), end=(-0.10,-0.45+i),lineColor="yellow")
        f= visual.Line(win,start=(-0.1, -0.45+i), end=(0,-0.35+i),lineColor="yellow")
        g= visual.Line(win,start=(0,-0.35+i), end=(0.1,-0.2+i),lineColor="yellow")
        h= visual.Line(win,start=(0.1,-0.20+i), end=(0.2,0.10+i),lineColor="yellow")
    e.draw()
    f.draw()
    g.draw()
    h.draw()

win.flip()
time.sleep(1)
win.close()