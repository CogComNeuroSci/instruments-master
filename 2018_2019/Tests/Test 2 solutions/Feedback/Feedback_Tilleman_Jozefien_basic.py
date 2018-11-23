from psychopy import visual
import time
import numpy as np
import math

win=visual.Window(size=(600,600),color=[-1,-1,-1],units="norm")

#creating planets
## Esther: de radii zijn ongeveer de helft zo groot als we gevraagd hadden
sun=visual.Circle(win, pos=(0,0), radius= 0.075)
planet=visual.Circle(win,fillColor="blue",lineColor="blue", radius= 0.045)
moon=visual.Circle(win,fillColor="white", radius= 0.01)

#position of planets

Planetx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
Planety = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
Moonx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
Moony = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]


#putting planets on screen

G=1
i=1
Sun_planet=1
Sun_moon=1
while Sun_planet>0 and Sun_moon>0:

    #making sun bigger en darker
    ## Esther: dit is niet de stijging tot 103% van de vorige waarde als gevraagd
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
    
    ## Esther: je hebt hier inderdaad een reset moeten doen gezien de zon niet groeide op de voorziene manier en omdat de radii van de cirkels te klein waren
    if i==59:
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