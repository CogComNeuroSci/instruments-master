# import modules
from psychopy import core, visual, event, monitors
import time
import matplotlib.pyplot as plt
import numpy as np
#eerst doen: elk apart ordenen: wat zijn grafische elementen? wat zijn datastructuren? wat zijn de dingen die varieren over tijd?
# alle grafische code in script al zetten, window openen, objecten maken etc, scherm flippen enz
#dan aan datastructuren beginnen en loops
#dan pas datastructuren in grafische code zetten




# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
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


#initialize variables
win = visual.Window(size = [600,600],color = (-1,-1,-1)) 
kleur_zon=[1,1,-1]   ##rood is 1,-1,-1
# stationary solar sytem: celectial bodies positions
#Planetx = 0.705
#Planety = 0.236
#Moonx = 0.002   # this coordinate is relative to the position of the planet!
#Moony = 0.12    # this coordinate is relative to the position of the planet!
grootte_zon= (0.075*2) ##maal 2 want norm gaat van -1 tot 1
zon = visual.Circle(win, radius=grootte_zon, lineColor=kleur_zon,fillColor=kleur_zon, fillColorSpace='rgb',)
blauwe_planeet = visual.Circle(win, radius=(0.035*2), lineColor="blue",fillColor="blue", pos=(Planetx[0],Planety[0]))
witte_maan = visual.Circle(win, radius=(0.01*2), lineColor="white",fillColor="white", pos = (Planetx[0]+Moonx[0],Planety[0]+Moony[0]))
count=0
col=1
botsing = False
botsing_blauw = 0
botsing_wit =0

#stoppen met keypress
for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)


#zon groei lijst
grootte_zon_lijst= [grootte_zon]
for i in range(60):
    grootte_zon = (grootte_zon+ (grootte_zon*0.03))
    grootte_zon_lijst.append(grootte_zon)
print(grootte_zon_lijst)


#display stimuli
## Esther: het lijntje hieronder kon net iets eleganter geprogrammeerd worden, maar ok
while botsing == False and grootte_zon_lijst[count]<0.44:     #tot botsing of tot zon volgroeid is (0.44 is laatste waarde in grootte_zon_lijst)
    zon.radius=grootte_zon_lijst[count]
    blauwe_planeet.draw()
    witte_maan.draw()
    zon.draw()
    win.flip()
    time.sleep(0.1)

    blauwe_planeet.pos=(Planetx[count],Planety[count])
    witte_maan.pos=(Planetx[count]+Moonx[count],Planety[count]+Moony[count])
    count+=1
    col= col-(2/60) ##van 1 naar -1 in 60 stappen
    if col< -1: ##waarde limiteren
        col = -1
                
    zon.color=[1,col,-1]
    zon.lineColor=[1, col, -1]

    if zon.overlaps(blauwe_planeet):
        botsing = True
        botsing_blauw += 1
    if zon.overlaps(witte_maan):
        botsing=True
        botsing_wit += 1

# boodschap botsing
if botsing_blauw==0 and botsing_wit==0:
    boodschap = "Geen enkele van de hemellichamen heeft de rode reus geraakt"  
elif botsing_blauw==botsing_wit:
    boodschap = "De planeet en de maan hebben tegelijk de rode reus geraakt"
elif botsing_blauw>botsing_wit:
    boodschap = "De planeet heeft de rode reus geraakt"
else:
    boodschap = "De maan heeft de rode reus geraakt"
boodschap_tekst = visual.TextStim(win,text=boodschap, color=[1,1,1])
boodschap_tekst.draw()
win.flip()
time.sleep(1)
win.close()














