from psychopy import visual
import time
from psychopy.visual import ShapeStim

# Esther: let er op dat de optie fullscreen de meer specifieke omschrijving van de grootte van het scherm zal overschrijven, just so you know.
win=visual.Window([600,400], fullscr=True, color='black')

steel = visual.Rect(win, width=0.05, height=0.3, pos=(0,0.4), fillColor='green', lineColor='green')
steel.draw()

pompoenbasis=visual.Circle(win, radius=0.4, edges=32, color='orange')
pompoenbasis.draw()

oogrechtsVert = [(0.2,0.2), (0.3,0.3), (0.4,0.2)]
oogrechts = ShapeStim(win, vertices=oogrechtsVert, fillColor='black', size=.5, lineColor='black')
oogrechts.draw()

ooglinksVert = [(-0.2,0.2), (-0.3,0.3), (-0.4,0.2)]
ooglinks = ShapeStim(win, vertices=ooglinksVert, fillColor='black', size=.5, lineColor='black')
ooglinks.draw()

mondVert = [(-0.15,-0.2), (0,-0.4), (0.15,-0.2)]
mond = ShapeStim(win, vertices=mondVert, fillColor='black', size=.5, lineColor='black')
mond.draw()

tekst=visual.TextStim(win, text="Happy Halloween!", pos= (0, -0.8), color=[1,0,0])
tekst.draw()

# ESther: win.flip en time.sleep staan in de verkeerde volgorde!
# Esther: dit blijft het geval doorheen heel de code!

time.sleep(1)

#alles laten verdwijnen voor volgende weergave plus de codes nodig voor de volgende weergaves. Elk blokje is een weergave
win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
time.sleep(0.5)

win.flip()
steel.draw()
pompoenbasis.draw()
oogrechts.draw()
ooglinks.draw()
mond.draw()
tekst.draw()
time.sleep(0.5)


win.close()







