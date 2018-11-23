import time, numpy as np
from psychopy import visual

## stationary solar sytem: celectial bodies positions
#Planetx_stat = 0.705
#Planety_stat = 0.236
#Moonx_stat = 0.002   # this coordinate is relative to the position of the planet!
#Moony_stat = 0.12    # this coordinate is relative to the position of the planet!

# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
Planetx = np.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
Planety = np.array([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])
Moonx = np.array([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.])
Moony = np.array([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])
#window aanmaken
win=visual.Window(size=[600,600], color="black", units="norm")

#variabelen
straal=0.15
colorstep=2/60 ##kleurenrange is 2(van -1  tot 1), we nemen 60 stappen
botsingmoon=False
botsingplanet=False
Moonx360=np.repeat(Moonx, 6)
Moony360=np.repeat(Moony,6)

#visual elements
sun=visual.Circle(win, radius=0.15, pos=(0,0), color=[1,1,-1])
planet=visual.Circle(win, radius=0.07, pos=(0,0), color=[-1,-1,1])
moon=visual.Circle(win, radius=0.02, pos=(0,0), color=[1,1,1])
endtxt= visual.TextStim(win, text="leeg", color="white", pos=(0,0))


#in 60 stappen: grootte en kleur van de zon aanpassen, loopen over lijstposities

for i in range(Planetx.shape[0]):
    planet.pos= (Planetx[i], Planety[i])
    straal= straal*1.03
    toRed= -(colorstep*i-1)  ##om ons groene kleur van 1 -->-1 te laten gaan
    for moonspin in range(6):   ##voor elke planeetstap zijn er 6 maanstappen 
        ## Esther: de coordinaten die we gegeven hadden implementeren al de zes rotaties van de maan rond de planeet
        ## Esther: dus eigenlijk hoefde je hier helemaal niet zelf code voor te schrijven.
        ## Esther: kijk eens goed naar de herhalende posities op de zes lijntjes met coordinaten voor de maan bovenaan in het script!
        #ik ben nog op zoek naar een manier om mijn maan 6 keer rond de aarde te laten draaien
        #voor 1 ronde van de planeet rond te zon: 60 planeetstappen
        #er zijn dus 360 maanstappen rond de ron
        #dus voor 1 planeetstap: 6 maanstappen
        moon.pos=(Planetx[i]+Moonx360[i+moonspin], Planety[i]+Moony360[i+moonspin])
        sun.color=[1, toRed, -1]
        sun.radius=straal
        
        sun.draw()
        planet.draw()
        moon.draw()
        win.flip()

        if planet.overlaps(sun):
            botsingplanet=True
        if moon.overlaps(sun):
            botsingmoon=True
            
    ## Dit eerste if-statement is niet nodig want dat wordt al geregeld door de for-loop
    if straal>0.883740465606862 or botsingplanet==True or botsingmoon==True: ##als we botsen of we hebben 60 stappen straalberekening doorlopen: stop
        break

#eindboodschap
## Esther: pas op, deze opeenvolgende statements hadden in een if...elif structuur moeten zitten!
if botsingplanet==True and botsingmoon==True:
    endtxt.text="De planeet en de maan hebben tegelijk de rode reus geraakt"
if botsingplanet==True:
    endtxt.text="De planeet heeft de rode reus geraakt"
if botsingmoon==True:
    endtxt.text="De maan heeft de rode reus geraakt"
if botsingmoon==False and botsingplanet==False:
    endtxt.text="Geen enkele van de hemellichamen heeft de rode reus geraakt"
endtxt.draw()
win.flip()
time.sleep(1)
win.close()