#importeren van modules
from psychopy import visual
import time,numpy

#window aanmaken
win=visual.Window([600,600],color=(-1,-1,-1), units="norm")


#hemellichamen aanmaken
## Esther: let op, gezien je in het norm coordinatenstelsel werkt, zijn je cirkels nu de helft te klein
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
zon=visual.Circle(win, radius=0.075, edges=32, fillColor="yellow", lineColor="yellow", pos=(0,0))

planeet=visual.Circle(win, radius=0.035, edges=32, fillColor="blue", lineColor="blue", pos=(0.705,0.236))

maan=visual.Circle(win, radius= 0.01, edges=32, fillColor="white", lineColor="white",pos=(0.707,0.346))

#drawing

planeet.draw()
maan.draw()

#vaste waarden
beginstraal_zon=0.075
straal_zon=beginstraal_zon

zon.ColorSpace="rgb"

#array voor opslag voorgaande zongrootte
zon_radius_array=numpy.array([straal_zon])


#hier laat de zon groeien, dit is echter niet zichtbaar op het scherm. 
#de straal van de zon wordt wel groter, 
#dit is te zien in de output van de shelf.
#Ik kan jammer genoeg niet vinden hoe ik de units moet aanpassen, 
#dus sla ik deze stap over
for i in range (60):
    ## Esther: dit is niet exact de berekening die we gevraagd hadden (*1.03)
    zon.radius=straal_zon+straal_zon*i*0.03
    zon_radius_array=numpy.append(zon_radius_array,straal_zon)
    print(zon.radius)

## Esther: de indexering faalt hier (straal_zon is geen integer)
#kleurverandering
#   geel_rood=-((numpy.ndarray(straal_zon)/30)-1)
#   if geel_rood<-1:
#      geel_rood=-1
    ## Esther: dit is niet exact de manier om van geel naar rood te gaan (enkel groen moet verminderen, de blauwe moet op -1 blijven)
#   zon.lineColor=(1,geel_rood,geel_rood)
#   zon.fillColor=(1,geel_rood,geel_rood)
    zon.draw()
    ## Esther: je was heel dicht bij de oplossing, maar je bent vergeten je window flippen!
    ##win.flip()





win.flip()
time.sleep(1)