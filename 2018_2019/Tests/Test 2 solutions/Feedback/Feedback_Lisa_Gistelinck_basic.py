#Ik heb geen geheel kunnen vormen van het experiment
#Heb elk stukje apart bekeken en '#' geplaatst waar ik vast zat of niet verder kon
#heb geprobeerd om een 'algemene structuur' toe te passen


#modules importeren
import numpy as np
import time
from psychopy import visual
import math

#variabelen bepalen
zon_positie=(0,0)
## Esther: deze radii zullen de helft te klein zijn
zon_radius=0.075*1              ##15 procent
## Esther: de posities van de maan moesten opgeteld worden bij de posities van de planeet
maan_positie=(0.002,0.12)
maan_radius=0.01*1              ##2 procent
planeet_positie=(0.705,0.12)
planeet_radius=0.035*1          ##7 procent
counter=0

##visuele zonnestelsel tekenen
#window bepalen
win=visual.Window(size=[600,600], units='norm', color='black')

#tekenen van de maan, zon en planeet
zon=visual.Circle(win,radius= zon_radius,fillColor='yellow',lineColor='yellow', pos=zon_positie)
maan=visual.Circle(win,radius=maan_radius, fillColor='white',lineColor='white',pos=maan_positie)
planeet=visual.Circle(win, radius=planeet_radius, fillColor='blue',lineColor='blue',pos=planeet_positie)

zon.draw()
maan.draw()
planeet.draw()
win.flip()
time.sleep(1)

#de zon laten vegroten
#adjustement=1.03*2
#vergroten = zon_grootte+ adjustement
size=[0.075, 0.077,0.079,0.081,0.084,0.9,0.95,1] 
#size=zon_grootte*1.03 ->dit zou het ongeveer moeten zijn, maar code werkt dan niet
print(size)

for i in size():
    ## Esther: het is nog beter om enkel de radius, kleur en positie aan te passen in de loop in plaats van de stimulus telkens opnieuw te maken ;)
    zon=visual.Circle(win,radius= i,fillColor='yellow',lineColor='yellow', pos=zon_positie)
    zon.draw()
    maan.draw()
    planeet.draw()
    win.flip()
    time.sleep(1)
    
    ## Esther: enkel de waarde van groen moet dalen om van geel naar rood te gaan.
    #kleur laten veranderen
    #geel =(255, 255, 0)       en     rood=(1,-1,-1)
    blauw_groen = -((np.ndarray.round(value)/50)-1)
        if blauw_groen < -1:
            blauw_groen = -1
    Kleur_zon  = (1, blauw_groen, blauw_groen)
    kleur_zon.draw()

#botsing 
## Esther: range moet uitaard een inhoud hebben
for trial in range():
    
    #als zon de maan of planeet raakt
    botsing= True
    zon.pos = zon_positie
    maan.pos = maan_positie
    
    while botsing == #:
        
        #terwijl we de zon laten vergroten laten we maan en de planeet cirkelen rond de zon
        #deze while loop zou dan ten einde moeten lopen als de zon één van de twee hemellichamen raakt
        #in deze while loop zou ik een for-loop toepassen (deze checkt of ze raken of niet)


        #checken of de rode reus de maan raakt OF de planeet raakt
        if #als de maan de rode reus rakt:
            
            botsing= True
            moon_counter += 1
            win.flip()
            sleep(1)
            
        if #als de planeet de rode reus raakt:
            
            botsing = True
            planeet_counter += 1
            win.flip()
            sleep(1)
        
        #een escape toet toegevoegd om uit de loop te geraken
        if "f" in event.getKeys():
            break

# resultaten laten printen als ze botsen 
if zon==0 and moon==0:
    feedback = "de planeet en de maan hebben de rode reus tegelijk geraakt!"
elif #laat ik even leeg:
    feedback = "de maan heeft de rode reus geraakt"
elif #laat ik even leeg:
    feedback = "de planeet heeft de rode reus geraakt!"
else #laat ik even leeg:
    feedback = 'geen enkele van de hemellichamen heeft de rode reus geraakt!'



#hemellichamen laten roteren
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
#planeet1.pos=(Planetx,Planety)
#stim.setOri(180)
#maan.setOri(1, '-')
#rotation_moon=moon.transform.rotate(Planeet1,90)

#Zon=(0,0)
#maan=(0.002,0.012)
#NewPointA=rotate(zon,maan,10)

moon = (0.002, 0.12)
planeet= (0, 0)
print(rotate(planeet,moo, math.radians(10)))


