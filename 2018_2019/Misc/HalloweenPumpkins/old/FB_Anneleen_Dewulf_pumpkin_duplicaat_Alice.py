import time
from psychopy import visual

win=visual.Window(size=[500,400],color='green')


circle=visual.Circle(win,radius=.5,pos=(0,0),fillColor='orange',lineColor='orange')
circle.draw()

Polygon2 =visual.Polygon(win, edges=10, radius=0.5, pos=(-0.10,0),fillColor='orange', lineColor='orange')
Polygon2.draw()

Polygon3 =visual.Polygon(win, edges=10, radius=0.5, pos=(0.10,0),fillColor='orange', lineColor='orange')
Polygon3.draw()

triangle= visual.Polygon(win,edges=3,radius=.07,pos=(-0.20,0.15),fillColor='black',lineColor='black')
triangle.draw()

triangle2= visual.Polygon(win,edges=3,radius=.07,pos=(0.20,0.15),fillColor='black',lineColor='black')
triangle2.draw()

rectangle=visual.Rect(win,width=.40,height=.05,pos=(0,-0.2),fillColor='black',lineColor='black')
rectangle.draw()

rectangle2=visual.Rect(win,width=.05,height=.1,pos=(0,0.55),fillColor='black',lineColor='black')
rectangle2.draw()

tekst=visual.TextStim(win,text="Happy Halloween", color='black')
tekst.draw()

win.flip()
time.sleep(5)
win.close()