# Test 2 - Amber Demeester
# Importeren van alles die nodig is 
import time, numpy
from psychopy import visual, event

#aanmaken van vanalles
## Esther: je hebt gelijk dat je hier eerst de reflex hebt om maal 2 te doen, maar goed dat het dat niet hebt gedaan bij het effectief tekenen van de cirkels!
grootte_zon = 0.15*2
grootte_maan =0.02*2
grootte_planeet = 0.07*2

win = visual.Window(size=[600,600], color = (-1,-1,-1))

## Esther: hier heb je size gebruikt als variabele om de grootte van de cirkel te bepalen, maar hierdoor zijn je cirkels de helft te klein.
zon = visual.Circle(win,lineColor="yellow",fillColor="yellow",size= 0.15)
## Esther: de grootte van de maan en planeet zijn gewisseld
planeet = visual.Circle (win, lineColor = "blue", fillColor = "blue", size = 0.02, pos = (0.705,0.236))
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
maan = visual.Circle(win,lineColor = "white", fillColor = "white", size = 0.07, pos = (0.707,0.356 )) 


tekst = visual.TextStim( win, text= "De rest van de punten zullen hopelijk voor de volgende test zijn.")
## Esther: test3, test4 en de eindtest zijn als het ware allemaal herkansingen op test2.
## Esther: het moeilijkste heb je nu al gezien, nu is het nog een kwestie van niet opgeven en veel oefenen tot je de klik maakt!

## Esther: OK, goed dat je al comments hebt geplaatst, maar maak ze misschien nog iets informatiever de volgende keer, alles is punten waard! ;)
#drawen enzo 
zon.draw()
planeet.draw()
maan.draw()
win.flip()
time.sleep(3)

tekst.draw()
win.flip()
time.sleep (2)

win.close()