#importeren van modules
from psychopy import visual
import time,numpy

#window aanmaken
win=visual.Window([600,600],color=(-1,-1,-1), units="norm")


#hemellichamen aanmaken
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
    zon.radius=straal_zon+straal_zon*i*0.03
    zon_radius_array=numpy.append(zon_radius_array,straal_zon)
    print(zon.radius)

#kleurverandering
#   geel_rood=-((numpy.ndarray(straal_zon)/30)-1)
#   if geel_rood<-1:
#      geel_rood=-1
#   zon.lineColor=(1,geel_rood,geel_rood)
#   zon.fillColor=(1,geel_rood,geel_rood)
    zon.draw()





win.flip()
time.sleep(1)