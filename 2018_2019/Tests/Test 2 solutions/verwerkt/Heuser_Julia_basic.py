#importion modules
from psychopy import visual,event
import time
from time import sleep
import numpy as np
from psychopy import visual


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


#startelementen
rad_zon=.15
pos_zon=(0,0)
n_trials=60
pos_planet_start=(0.014,0.5)
pos_moon_start=(0.002,0.12)
#planet_counter=0
#moon_counter=0
#zon_counter=0
#idee was om met counter de grote en positie te regelen


#startelementen visuel
win= visual.Window([600,600],color="black", units="norm")
planet= visual.Circle(win,radius = 0.07, pos = pos_planet_start, fillColor = "Blue", lineColor = "Blue")
moon=  visual.Circle(win,radius = 0.02, pos =pos_moon_start, fillColor = "white", lineColor = "White")
zon=visual.Circle(win,lineColor="yellow",fillColor="yellow",pos=pos_zon,radius=rad_zon)
planet.draw()
moon.draw()
zon.draw()
win.flip()
time.sleep(1)
#idee hier om stationair zonnestelset 1 seconde te tonen, maar positie werkt niet?!

#crash_text_gelijk = visual.TextStim(win,text="De planeet en de maand hebben tegelijk de rode reud geraakt")
#crash_text_planeet=visual.TextStim(win,text="De planeet heeft de rode reus geraakt")
#crash_text_maan=visual.TextStim(win,text="De maan heeft de rode reus geraakt")
#crash_text_not=visual.TextStim(win, text="Geen enkele van de hemellichamen heeft de rode reus geraakt")


#eigenlijk was het idee om de zon te laten groien door .15*1.03 te doen, maar omdat dat blijkbaar niet werkt zoals + nu met enkele warden in sizes

sizes=(.15, .16, .17,.18,.19,.20,.25,.30,.4,.5,.6,.7,.8,2)

for i in sizes:
    circle=visual.Circle(win, radius=i,pos=(0,0), fillColor=(1,1,-1))
    circle.draw()
    
    #i=sizes*1.03
    win.flip()
    time.sleep(0.1)



for i in range(60):
        planet= visual.Circle(win,radius = 0.07, pos = (Planetx[i],Planety[i]), fillColor = "Blue", lineColor = "Blue")
        planet.draw()
        moon=  visual.Circle(win,radius = 0.02, pos = (Planetx[i]+Moonx[i],Moony[i]+Planety[i]), fillColor = "white", lineColor = "White")
        moon.draw()
        time.sleep(0.05)
        win.flip()

#probleem bij stimuli te gelijker tijd op scherm te tonen, omdat dan beweging niet meer lukt