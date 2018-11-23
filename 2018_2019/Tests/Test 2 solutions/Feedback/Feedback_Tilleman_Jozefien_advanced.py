from psychopy import visual
import time
import numpy as np
import math

win=visual.Window(size=(600,600),color=[-1,-1,-1],units="norm")

#creating planets
sun=visual.Circle(win, pos=(0,0), radius= 0.075)
planet=visual.Circle(win,fillColor="blue",lineColor="blue", radius= 0.045)
moon=visual.Circle(win,fillColor="white", radius= 0.001)

#position of planets


#creating variables for planet
Planetx=[0]
Planety=[0.5]

## Esther: je was heel dicht bij de oplossing maar moest de hoek nog omzetten van graden naar radialen
for t in range(360):
    Planetx.append(0.8*math.cos(t))
    Planety.append(0.5*math.sin(t))

print(Planetx)
print(Planety)

#creating variables for moon

Moonx=[0]
Moony=[0.012]

for t in range(360):
    Moonx.append(0.012*math.cos(t))
    Moony.append(0.012*math.sin(t))

print(Moonx)
print(Moony)


#putting planets on screen

G=1
i=1
Sun_planet=1
Sun_moon=1
while Sun_planet>0 and Sun_moon>0:

    #making sun bigger en darker
    sun.radius+=0.00225
    G-=0.01
    sun.fillColor=[1,G,-1]
    sun.lineColor=[1,G,-1]
    sun.draw()
    
    #moving planets and moon
    planet.pos=(Planetx[i],Planety[i])
    planet.draw()
    moon.pos=((Planetx[i]+Moonx[i]),(Planety[i]+Moony[i]))
    moon.draw()
    
    #calculating euclidian distance
    Sun_planet=math.sqrt((-Planetx[i])**2+(-Planety[i])**2)-sun.radius-planet.radius
    Sun_moon=math.sqrt((-(Planetx[i]+Moonx[i]))**2+(-(Planety[i]+Moony[i]))**2)-sun.radius-moon.radius
    print(i)
    if i==359:
        i=1
    else:
        i+=1
    win.flip()
    time.sleep(0.1)



#creating final screen


Message=visual.TextStim(win, color="white")
if Sun_planet<0 and Sun_moon<0:
    Message.text="De planeet en de maan hebben tegelijk de rode reus geraakt"
elif Sun_planet<0 and Sun_moon>=0:
    Message.text="De planeet  heeft de rode reus geraakt"
elif Sun_planet>=0 and Sun_moon<0:
    Message.text="De maan heeft de rode reus geraakt"
else:
    Message.text="Geen enkele van de hemellichamen heeft de rode reus geraakt"

Message.draw()
win.flip()
time.sleep(4)


#close window
win.close()