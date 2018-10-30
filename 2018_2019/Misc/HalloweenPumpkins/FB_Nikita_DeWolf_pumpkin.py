from psychopy import core, visual, event
import time

win = visual.Window(
    size=[400, 400],
    fullscr=True,
    color=[-1, -1, -1]
)

# Esther: ziet er goed uit, in Chapter 3 zal je zien dat je bv. de fillColor gewoon één keer op voorhand kan aanmaken en daar in de lijnen hieronder naar verwijzen.
# Esther: bijvoorbeeld:
# ColorNikita = [0.976,-0.027,-0.937]
#circle= visual.Circle(
#    win,
#    radius=0.5,
#    fillColor=ColorNikita,
#    lineColor=ColorNikita,
#    edges=50,
#    pos=(-0.1,0)
#)
#circle2= visual.Circle(
#    win,
#    radius=0.5,
#    fillColor=ColorNikita,
#    lineColor=ColorNikita,
#    edges=50,
#    pos=(0.05,0)
#)
# Esther: het voordeel is dat je slechts één keer de waarde hoeft aan te passen in plaats van voor elke cirkel apart ;)
# Esther: je kan dit idee ook doortrekken bij de andere vormen die hieronder aangemaakt worden.

circle= visual.Circle(
    win,
    radius=0.5,
    fillColor=[0.976,-0.027,-0.937],
    lineColor=[0.976,-0.027,-0.937],
    edges=50,
    pos=(-0.1,0)
)

circle2= visual.Circle(
    win,
    radius=0.5,
    fillColor=[0.976,-0.027,-0.937],
    lineColor=[0.976,-0.027,-0.937],
    edges=50,
    pos=(0.05,0)
)

oog1= visual.Polygon(
   win, 
   edges=3, 
   radius=0.5, 
   size=0.2, 
   pos=(-0.25,0.2),
   fillColor="brown", 
   lineColor="brown",
   ori=0
)

oog2= visual.Polygon(
   win, 
   edges=3, 
   radius=0.5, 
   size=0.2, 
   pos=(0.2,0.2),
   fillColor="brown", 
   lineColor="brown",
   ori=0
)


neus= visual.Polygon(
   win, 
   edges=3, 
   radius=0.5, 
   size=0.2,
   pos=(-0.02,0),
   fillColor="brown",
   lineColor="brown",
   ori=0
)

circle3= visual.Circle(
    win,
    radius=0.15,
    fillColor="brown",
    lineColor="brown",
    edges=50,
    pos=(-0.02,-0.3),
    ori=90
)

rect1= visual.Rect(
   win, 
   width=0.35,
   height=0.15,
   fillColor=[0.976,-0.027,-0.937],
   lineColor=[0.976,-0.027,-0.937],
   ori=0,
   pos=(-0.04, -0.2)
)

rect2= visual.Rect(
   win, 
   width=0.05,
   height=0.05,
   fillColor=[0.976,-0.027,-0.937],
   lineColor=[0.976,-0.027,-0.937],
   ori=90,
   pos=(-0.08, -0.3)
)

rect3= visual.Rect(
   win, 
   width=0.05,
   height=0.05,
   fillColor=[0.976,-0.027,-0.937],
   lineColor=[0.976,-0.027,-0.937],
   ori=90,
   pos=(0.04, -0.3)
)

steel= visual.Rect(
   win, 
   width=0.25, 
   height=0.1, 
   fillColor="green", 
   lineColor="green", 
   ori=90, 
   pos=(-0.02,0.62)
)

Text = visual.TextStim(win, text=u"Happy Halloween!", pos=(-0.01, -0.7), color="brown", font="trattatello")

circle.draw()
circle2.draw()
oog1.draw()
oog2.draw()
neus.draw()
circle3.draw()
rect1.draw()
rect2.draw()
rect3.draw()
steel.draw()
Text.draw()


win.flip()
time.sleep(3)

# Esther: hier krijg je een foutmelding, maar deze code zien we pas in chapter 5, dus dat is niet erg ;)
psychopy.event.waitKeys()

win.close()