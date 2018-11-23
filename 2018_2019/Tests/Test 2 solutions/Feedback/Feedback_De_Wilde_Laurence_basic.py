 #uploaden modules
from psychopy import visual
import time


 #maken van window en zonnenstelsel
win = visual.Window(size = [600,600] ,color = "black" , units = "norm")

## Esther: pas op, de hemellichamen zijn half zo groot als we gevraagd hadden!
zon = visual.Circle(win, lineColor = "yellow", fillColor="yellow", pos = (0,0), radius= 0.075)
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
planeet = visual.Circle(win, lineColor = "blue", fillColor="blue", pos = (0.705,0.236), radius = 0.035)
maan = visual.Circle(win, lineColor = "white", fillColor="white", pos = (0.707,0.356), radius = 0.01)

zon.draw()
planeet.draw()
maan.draw()

win.flip()
time.sleep(1)
win.close()
