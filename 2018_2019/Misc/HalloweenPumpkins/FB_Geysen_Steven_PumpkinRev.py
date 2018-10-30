from psychopy import visual, monitors
import time

mon = monitors.Monitor("my laptop screen")
mon.setDistance(40)
mon.setWidth (38)
mon.setSizePix((1536,864))

# Esther: prima, ik heb hem enkel niet op full screen gezet omdat ik anders niet het aantal pixel heb waar je op rekent om die tekst in de hoed te krijgen (vermoed ik)
#win = visual.Window(fullscr = True , color = 'green', monitor = mon)
win = visual.Window(size = (1536,864) , color = 'green', monitor = mon)

# Esther: zeer nice touch met de autoDraw! Eerste keer dat ik iemand dat zie gebruiken voor deze oefening!
circle = visual.Polygon(win, edges = 9999,  fillColor = 'orange')
circle.autoDraw = True
oog1 = visual.Polygon(win, edges = 3, radius=.08, fillColor = 'black', pos = (-0.15,0.2))
oog1.autoDraw = True
oog2 = visual.Polygon(win, edges = 3, radius = .08, fillColor = 'black', pos = (0.15,0.2))
oog2.autoDraw = True
mond = visual.Polygon(win, edges = 9999,  fillColor = 'black', radius=0.15, pos = (0,-0.15))
mond.autoDraw = True
tand1 = visual.Polygon(win, edges = 3,  fillColor = 'white', radius=0.05, pos= (-0.08,-0.07), ori=30)
tand1.autoDraw = True
tand2 = visual.Polygon(win, edges = 3,  fillColor = 'white', radius=0.05, pos= (0.08,-0.07), ori=90)
tand2.autoDraw = True
tand3 = visual.Polygon(win, edges = 3,  fillColor = 'white', radius=0.05, pos= (0,-0.043), ori=180)
tand3.autoDraw = True
tand4 = visual.Polygon(win, edges = 3,  fillColor = 'white', radius=0.05, pos= (0,-0.27))
tand4.autoDraw = True
hoed = visual.Rect(win, width = 8, height = 8, pos= (0,10), fillColor = 'black', units ='deg')
hoed.autoDraw = True
bandhoed = visual.Rect(win, width = 20, height = 4, pos= (0,8), fillColor = 'black', units ='deg')
bandhoed.autoDraw = True

woorden = visual.TextStim(win, text = "Happy Halloween",  pos=(0,0.58))
woorden.autoDraw = True

win.flip()
time.sleep(1)
woorden.autoDraw = False
win.flip()
time.sleep(0.5)
woorden.autoDraw = True
win.flip ()
time.sleep(0.5)
woorden.autoDraw = False
win.flip()
time.sleep(0.5)
woorden.autoDraw = True
win.flip ()
time.sleep(0.5)
woorden.autoDraw = False
win.flip()
time.sleep(0.5)
woorden.autoDraw = True
win.flip ()
time.sleep(0.5)
woorden.autoDraw = False
win.flip()
time.sleep(0.5)
woorden.autoDraw = True
win.flip ()
time.sleep(0.5)
woorden.autoDraw = False
win.flip()
time.sleep(0.5)
woorden.autoDraw = True
win.flip ()
time.sleep(0.5)
woorden.autoDraw = False
win.flip()
time.sleep(0.5)
woorden.autoDraw = True
win.flip ()
time.sleep(0.5)
win.close()