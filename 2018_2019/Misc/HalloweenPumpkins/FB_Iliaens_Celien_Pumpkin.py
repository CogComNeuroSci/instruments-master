from psychopy import visual
import time

#scherm
win=visual.Window(monitor="testMonitor",color=(-1,-1,-1), units='norm')
stim=visual.Polygon(win, radius=[200,170],units="pix", edges=60,color=(1.000,-0.231,-1.000),pos=(0,0))
stim.draw()


# Esther: ziet er goed uit, in Chapter 3 zal je zien dat je bv. de fillColor gewoon één keer op voorhand kan aanmaken en daar in de lijnen hieronder naar verwijzen.
# Esther: bijvoorbeeld:
# ColorCelien = [0.867,0.333,-0.914]
# ooglinks = visual.ShapeStim(win, vertices=oogVert, lineColor='black', lineWidth=2.0, size=.10,pos=(0,0),units='norm',fillColor=ColorCelien)
# oogrechts= visual.ShapeStim(win, vertices=oog2Vert, lineColor='black', lineWidth=2.0, size=0.10, pos=(0,0),units='norm',fillColor=ColorCelien)
# neus=visual.ShapeStim(win, vertices=neusvert, lineColor='black', lineWidth=2.0, size=0.10, pos=(0,0), units='norm',fillColor=ColorCelien)
# mond=visual.ShapeStim(win, vertices=mondvert, lineColor='black', lineWidth=2.0, size=0.10, pos=(0,0), units='norm',fillColor=ColorCelien)
# Esther: het voordeel is dat je slechts één keer de waarde hoeft aan te passen in plaats van voor elke cirkel apart ;)
# Esther: je kan zelfs nog een stap verder gaan en 1 shapestim maken waarvan je enkel de vertices hoeft aan te passen (alle andere features blijven toch gelijk)

# Esther: en om het nog een tikje eleganter te maken, kan je gewoon eerst alle grafische elementen maken en dan pas beginnen met drawen en flippen. You see?


#linkeroog
oogVert = [(0.7,1.0),(0.7,1.2),(1.7,2.0),(1.9,1.5),(1.9,1.0),(1.7,1.0)]
ooglinks = visual.ShapeStim(win, vertices=oogVert, lineColor='black', lineWidth=2.0, size=.10,pos=(0,0),units='norm',fillColor=[0.867,0.333,-0.914])
ooglinks.draw()

#rechteroog
oog2Vert=[(-0.7,1),(-0.7,1.2),(-1.7,2),(-1.9,1.5),(-1.9,1.0),(-1.7,1)]
oogrechts= visual.ShapeStim(win, vertices=oog2Vert, lineColor='black', lineWidth=2.0, size=0.10, pos=(0,0),units='norm',fillColor=[0.867,0.333,-0.914])
oogrechts.draw()

#neus
neusvert=[(-0.25,0.7),(0.25,0.7),(0,0.2)]
neus=visual.ShapeStim(win, vertices=neusvert, lineColor='black', lineWidth=2.0, size=0.10, pos=(0,0), units='norm',fillColor=[0.867,0.333,-0.914])
neus.draw()

#mond
mondvert=[(0,-1.75),(0.50,-2),(0.75,-1.5),(1,-1.75),(1.25,-1.25),(1.50,-1.50),(2,0),(1.5,-2.75),(1.25,-2.60),(1,-2.85),(0.5,-2.60),(0,-3),(-0.5,-2.75),(-0.75,-2.85),(-1,-2.60),(-1.5,-2.75),(-2,0),(-1.5,-1.5),(-1.25,-1.25),(-1,-1.75),(-0.75,-1.5),(-0.5,-2)]
mond=visual.ShapeStim(win, vertices=mondvert, lineColor='black', lineWidth=2.0, size=0.10, pos=(0,0), units='norm',fillColor=[0.867,0.333,-0.914])
mond.draw()

#tekst
tekst=visual.TextStim(win, text="Happy Halloween!",color=[1.000,-0.231,-1.000],pos=(0,0.8))
tekst.draw()

win.flip()
time.sleep(1)

#flikkeren zonder tekst
stim.draw()
ooglinks.draw()
oogrechts.draw()
neus.draw()
mond.draw()

win.flip()
time.sleep(0.5)

#flikkeren met tekst
stim.draw()
ooglinks.draw()
oogrechts.draw()
neus.draw()
mond.draw()
tekst.draw()

win.flip()
time.sleep(0.5)

#flikkeren zonder tekst
stim.draw()
ooglinks.draw()
oogrechts.draw()
neus.draw()
mond.draw()

win.flip()
time.sleep(0.5)

#flikkeren met tekst
stim.draw()
ooglinks.draw()
oogrechts.draw()
neus.draw()
mond.draw()
tekst.draw()

win.flip()
time.sleep(0.5)

#flikkeren zonder tekst
stim.draw()
ooglinks.draw()
oogrechts.draw()
neus.draw()
mond.draw()

win.flip()
time.sleep(0.5)

#flikkeren met tekst
stim.draw()
ooglinks.draw()
oogrechts.draw()
neus.draw()
mond.draw()
tekst.draw()

win.flip()
time.sleep(0.5)


win.close()