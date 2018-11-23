from psychopy import visual
import time, numpy

Planetx = 0.705
print(Planetx)
Planety = 0.236
Moonx = 0.002 + Planetx
Moony = 0.12 + Planety
## Esther: let op, de waarden in het rgb systeem lopen van -1 tot 1, dus de waarde voor blauw mocht eigenlijk op -1 staan
zon_color = (1, 1, 0)
radius = 0.075

#window
win = visual.Window(size = (600,600), Color = 'black')

#hemellichamen
## Esther: de radii zijn op z'n minst de helft te klein
zon     = visual.Circle(win, radius = radius, edges = 128, lineColor = zon_color, fillColor = zon_color)
aarde   = visual.Circle(win, radius = 0.035, edges = 128, lineColor = 'blue' , fillColor = 'blue', pos = (Planetx, Planety))
maan    = visual.Circle(win, radius = 0.001, edges = 128, lineColor = 'white', fillColor = 'white', pos = (Moonx, Moony))

#zon laten groeien
for i in range(80):
    ## Esther: dit is niet de berekening die we gevraagd hadden
    zon.radius = radius + i*0.01
    zon.draw()
    aarde.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)

win.close()
