#het lukt me niet om alles gelijktijdig te presenteren, maar bauwe cirkel langs een elips laten bewegen lukt wel (om dit te zien, uncomment
#de commando's in de while loop)
#verder had ik geen tijd meer om de maan handmatig aan te passen


##An ellipse in canonical position (center at origin, major axis along the X-axis) 
##with semi-axes a and b can be represented parametrically as##x = a*cos(⁡t)
##y = b*sin⁡(t). 
##x,y are the coordinates of any point on the ellipse, ##a, b are the radius on the x and y axes respectively, ( * See radii notes below ) ##t is the parameter, which ranges from 0 to 2π radians.

import math
import time
from psychopy import visual

win = visual.Window(size = [600,600],color = (-1,-1,-1), units = "norm")

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


zonnestraal      = 0.15
i                = 0 
planeet_counter  = 0
maan_counter     = 0


##laat de zon groeien en van kleur veranderen in 60 stappen
for i in range(60):
    
    ##straal op de x-as is de helft van 80% van de breedte vh scherm --> (0.8*2)/2
    a = 1.6 / 2
    b = 1 / 2
    t = 0
    startx = 0.014
    starty = 0.5
    ##t ranget van 0 to 2*pi (ongeveer 6) in 300 stappen dus telkens met 0.02 verhogen
    while t < 6:
        planeet = visual.Circle(win,lineColor = "blue", fillColor = "blue", radius = 0.07, pos = (startx,starty) )
        startx = 0.8 * math.cos(t)
        starty = 0.5 * math.sin(t)
        t = t + 0.02
        #planeet.draw()
        #win.flip()
        #time.sleep(0.1)

    zon         = visual.Circle(win, lineColor=(1, 1 - i*0.03, 0 - i*0.016),fillColor = (1, 1 - i*0.03, 0 - i*0.016), radius = zonnestraal )  
    zonnestraal = zonnestraal + zonnestraal*0.03
    maan        = visual.Circle(win,lineColor = "white",  fillColor = "white",  radius = 0.02, pos = (Planetx[i]+Moonx[i], Planety[i]+Moony[i]) )
    
    ##60 loops in stappen van 1
    i = i + 1

    planeet.draw()
    zon.draw()
    maan.draw()    
    win.flip()
    time.sleep(0.1)
    
    ##zorg ervoor dat de loop stopt bij een botsing en registreer welke botsing er voorviel door een variabele, gedefinieerd als counter, 
        ##met 1 te laten vermeerderen. Indien er geen botsing is blijft de counter op 0 staan. 
    if zon.overlaps(planeet) == True:
        planeet_counter += 1
        break
    elif zon.overlaps(maan) == True:
        maan_counter += 1
        break

##Presenteer de tekst op het einde adhv waar de maan tegen gebotst is. Presenteer dit voor 1 seconde.
if planeet_counter == 0 and maan_counter == 0:
    boodschap = "Geen enkele van de hemellichamen heeft de rode reus geraakt."
elif planeet_counter == maan_counter:
    boodschap = "De planeet en de maan hebben tegelijk de rode reus geraakt."
elif planeet_counter  > maan_counter:
    boodschap = "De planeet heeft de rode reus geraakt. "
else:
    boodschap = "De maan heeft de rode reus geraakt."

eindscherm = visual.TextStim(win,text = boodschap)
eindscherm.draw()
win.flip()
time.sleep(1)

##sluit alles af
win.close()
