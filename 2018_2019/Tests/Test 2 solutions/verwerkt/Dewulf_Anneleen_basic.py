
#this is test 2 for the course IEP
#this test is made on 21/11/2018 by Anneleen Dewulf
# stationary solar sytem: celectial bodies positions

#importing modules
from psychopy import visual
import numpy
import time
import math
import random

Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!

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

#graphical elements
win=visual.Window([600,600],color="black")
diameterzon=0.15*2
diameterplaneet=0.07*2
diametermaan=0.02*2
sizeszon=[0.3,0.4,0.5]#zon zal gaan vergroten tot rode reus --> random gekozen waarden
colorzon=[(1,1,1),(1,-0.5,-0.5),(1,-1,-1)] #zon zal roder worden greenblue zal van 1 naar -1 gaan variëren

zon=visual.Circle(win,color="yellow",radius=math.sqrt(diameterzon))
maan=visual.Circle(win,radius=math.sqrt(diametermaan),pos=(0.002,0.12),fillColor="white",size=0.05)
planeet=visual.Circle(win,radius=math.sqrt(diameterplaneet),color="blue",pos=(0.705,0.236),size=0.1)
botsingtext=visual.TextStim(win,text="Botsing")

#aangepaste beginposities omdat we ze aan begin van rooster mogen laten starten
planeetposbeginx =0.014
planeetposbeginy=0.5
maanposbeginx=0.002
maanposbeginy=0.12

#testdraw
    #zon.draw()
    #maan.draw()
    #planeet.draw()
    #win.flip()
    #time.sleep(1)

#put sun on display and let is grow bigger in mean time will the moon and planet move around the sun in an ellips
for i in sizeszon:
    zon=visual.Circle(win,color="yellow",radius=math.sqrt(i),fillColor="yellow")
    for i in sizeszon:
        planeetposbeginx=planeet.pos[0]
        planeetposbeginy=planeet.pos[1]
        planeetposbeginx = planeetposbeginx + random.choice(Planetx) 
        planeetposbeginy = planeetposbeginy + random.choice(Planety)
        
        maanposbeginx=maan.pos[0]
        maanposbeginy=maan.pos[1]
        maanposbeginx=maanposbeginx+random.choice(Moonx)
        maanposbeginy=maanposbeginy+random.choice(Moony)
        
        #ik besefte net dat ik verkeerd bezig was om random.choice te implementeren. Beter had ik gebruik gemaakt van planeetposbeginx = planeetposbeginx + (Planetx)*planeetposbeginx zoals in de bitcoin
        #en daarna numpy.append.
        planeet.pos=(planeetposbeginx,planeetposbeginy)
        maan.pos=(maanposbeginx,maanposbeginy)
        #er klopt iets niet aan mijn posities van mijn hemellichamen, soms lijken ze zelf te verdwijnen. Alhoewel dit niet kan als je naar de coördinaten kijkt dus heb ik ervoor gezorgd dat deze op het scherm blijven zelf indien de baan niet klopt
        if planeet.pos[0] < -1:
            planeet.pos[0] = -0.9
        if planeet.pos[0] > 1:
            planeet.pos[0] = 0.9
        if planeet.pos[1] < -1:
            planeet.pos[1] = -0.9
        if planeet.pos[1] > 1:
            planeet.pos[1] = 0.9
            
        if maan.pos[0] < -1:
            maan.pos[0] = -0.9
        if maan.pos[0] > 1:
            maan.pos[0] = 0.9
        if maan.pos[1] < -1:
            maan.pos[1] = -0.9
        if maan.pos[1] > 1:
            maan.pos[1] = 0.9
        
        zon.draw()
        planeet.draw()
        maan.draw()
        win.flip()
        time.sleep(1)
        #ondanks dat ik er niet in geraakt ben om het sterrenstelsel te tekenen heb ik vluchtig geschets hoe ik zou starten aan de presentatie van de botsing
        #ik heb dit geschreven in de laatste 10 minuten dus ik had niet echt de tijd om 1 van de eerste 2 gegeven opties te implementeren.
        #if planeetposbeginx < maan:
        #    botsingtekst.text=planeet is gebotst met zon
        #    win.flip()
        #    time.sleep(1)
        #    break
        #   
        #if maanposbeginx < maan
        #    botsingtekst.text=maan is gebotst met zon
        #    win.flip()
        #    time.sleep(1)
        #    break

win.close()
