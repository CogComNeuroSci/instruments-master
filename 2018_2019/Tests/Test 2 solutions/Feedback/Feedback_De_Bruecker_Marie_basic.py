# loading modules
from psychopy import visual, event
import time
import numpy as np
from numpy import random

# initialization
n_trials1 = 1 #blauwe planeet draait 1 keer rond de zon
n_trials2 = 6 #witte maan draait 6 keer rond de planeet
startpos_blue_planet = (0.705, 0.236)
startpos_white_moon = (0.707, 0.248)
## ESther: dubbele punt in plaats van = ?
#pos_yellow_sun : (0.0, 0.0)


# prepare graphic elements
win = visual.Window([600,600], color = "black")
## ESther: let op, de radii van de stimuli is de helft van wat er gevraagd was!
yellow_sun = visual.Circle(win, lineColor = "yellow", fillColor = "yellow", pos = (0.0,0.0), radius = 0.075)
blue_planet = visual.Circle(win, lineColor = "blue", fillColor = "blue", pos = (0.705, 0.236), radius = 0.035)
white_moon = visual.Circle(win, lineColor = "white", fillColor = "white", pos = (0.707, 0.248), radius = 0.01)

# stationary solar sytem: celectial bodies positions
blue_planetx = 0.705
blue_planety = 0.236
white_moonx = 0.002   # this coordinate is relative to the position of the planet!
white_moony = 0.12    # this coordinate is relative to the position of the planet!



# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
blue_planetx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
blue_planety = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
white_moonx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
white_moony = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

#hemellichamen laten roteren
for trial in range(n_trials1):
    pos_blue_planet = startpos_blue_planet
    position_yellow_sun = pos_yellow_sun
    while crash == False:
        pos_blue_planet = pos_blue_planet + blue_planetx + blue_planety
        position_yellow_sun = position_yellow_sun
        
        pos_blue_planet[blue_planetx] = np.maximum(pos_blue_planet[blue_planetx], blue_planety)
        pos_blue_planet[blue_planety] = np.maximum(pos_blue_planet[blue_planety], blue_panetx)
        
        

for trial in range (n_trials2):
    pos_white_moon = startpos_white_moon
    pos_blue_planet = startpos_blue_planet
    while crash == False:
        pos_white_moon = pos_white_moon + white_moonx + white_moony
        pos_blue_planet = pos_blue_planet + blue_planetx + blue_planety
        
       
        
        pos_blue_planet[blue_planetx] = np.maximum(pos_blue_planet[blue_planetx], blue_planety)
        pos_blue_planet[blue_planety] = np.maximum(pos_blue_planet[blue_planety], blue_panetx)
        pos_white_moon[white_moonx] = np.maximum(white_moon[white_moonx], white_moony)
        pos_white_moon[white_moony] = np.maximum(white_moon[white_moony], white_moonx)
        

# botsing checken
## Esther: syntac foutje: een dubbele punt vergeten aan het einde van de lijn hieronder
        if np.absolute(pos_blue_planet[blue_planetx])< position_yellow_sun or np.absolute(pos_blue_planet[blue_planety])< position_yellow_sun:
            ## Esther: de code hieronder was niet voldoende geindenteerd
            crash = True
            feedback_text.draw()
            win.flip()
            time.sleep(1)
        
        ## Esther: idem hier, syntaxfout
        if np.absolute(pos_white_moon[white_moonx])< position_yellow_sun or np.absolute(pos_white_moon[white_moony])< position_yellow_sun:
            ## Esther: idem hier, indentatiefout
            crash = True
            feedback_text.draw()
            win.flip()
            time.sleep(1)

# the radius of the circles you want
## Esther: dit bevat slechts 1 element
sizes = [(0.075*1.03)+i]
## Esther: aansturing van de loop werkt niet op deze manier
for i in sizes(60):
    yellow_sun = visual.Circle(win, radius = i, pos = (0,0), fillColor = "yellow")
## Esther: indentatiefout
circle.draw()
win.flip()
 


    


# print feedback on screen and finish
if yellow_sun == blue_planet == white_moon:
    feedback = "De planeet en de maan hebben tegelijk de rode reus geraakt."
elif yellow_sun == blue_planet:
    feedback = "De planeet heeft de rode reus geraakt."
elif yellow_sun == white_moon:
    feedback = "De maan heeft de rode reus geraakt."
else:
    ## Esther: die laatste moet je wel nog opslaan in feedback!
    "Geen enkele van de hemellichamen heeft de rode reus geraakt."
feedback_text = visual.TextStim(win,text=feedback)
feedback_text.draw()

## Esther: deze mochten waarschijnlijk weg hier?
yellow_sun.draw()
blue_planet.draw()
white_moon.draw()

win.flip()
time.sleep(1)
win.close()