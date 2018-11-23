#Importeren van nodige modulen
from psychopy import visual
import time

#Coördinaten planeten
## stationary solar sytem: celectial bodies positions
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   ## this coordinate is relative to the position of the planet!
Moony = 0.12    ## this coordinate is relative to the position of the planet!

## Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
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

#Aanmaken windom
Zonnestelsel = visual.Window([600,600], units = "norm", color = (-1,-1,-1))

#grootte zon doen toenemen
## Esther: door 0.15 te typen maak je al een float, dus float() voegt niets toe
R_zon = float(0.15)
while R_zon < 0.8:
    R_zon = R_zon*1.03
    
    ##Aanmaken stimuli
    ## Esther: ik denk dat R_zon ook prima was in plaats van float("{0}".format(R_zon)) ;)
    Zon = visual.Circle(Zonnestelsel, units = "norm", radius = float("{0}".format(R_zon)), lineColor = (1,1,-1), fillColor = (1,1,-1))
    ## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
    ## Esther: die expliciete codering was nodig voor de rest van de opdracht!
    Planeet = visual.Circle(Zonnestelsel, units = "norm", radius = 0.07, pos = (0.705,0.236), lineColor = (-1,-1,1), fillColor = (-1,-1,1))
    Maan = visual.Circle(Zonnestelsel, units = "norm", radius = 0.02, pos = (0.707, 0.356), lineColor = (1,1,1), fillColor = (1,1,1))
    
    ##Stimuli tekenen
    Planeet.draw()
    Maan.draw()
    Zon.draw()
    
    ##Openen window
    Zonnestelsel.flip()
    time.sleep(0.01)

Zonnestelsel.close()