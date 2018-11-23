# This is the code for test 2, basic version
# by Timmermans Clara on november 21st, 2018


# Part 1: import modules
from psychopy import visual
import time
import numpy as np



# Part 2: initialize variables
## coordinates of the start position of the Planet and Moon
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!
MoonX = Moonx + Planetx
MoonY = Moony + Planety
## Esther: aha, dit is een licht andere interpretatie van onze instuctie, we doelden op radius = radius*1.03
Sungrow = 0.15 + 0.0125 * 60
steps = 60
## coordinates of the different positions of the Planet and Moon
Planetx_array = np.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
Planety_array = np.array([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])
Moonx_array = np.array([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]) # these coordinates are relative to the position of the planet!
Moony_array = np.array([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])   # these coordinates are relative to the position of the planet!
MoonX_array = Planetx_array + Moonx_array
MoonY_array = Planety_array + Moony_array

sungrow_array = np.array([Sungrow])
sungrow_array = np.random.normal(sungrow_array)
count = 0
# Part 3: Initialize graphic elements
win = visual.Window(size = (600,600), color = [-1,-1,-1], units = "norm")
Sun = visual.Circle(win, radius = 0.15, pos= (0,0), fillColor= [1,1,-1], lineColor= [1,1,-1],colorSpace='rgb')
Planet = visual.Circle(win, radius = 0.07, pos= (Planetx, Planety), fillColor = [-1,-1,1], lineColor = [-1,-1,1])
Moon = visual.Circle(win, radius = 0.02, pos = (MoonX, MoonY), fillColor = [1,1,1], lineColor = [1,1,1])


# Part 4: make it work
## sun grow
for growth in range(steps):
    ## Esther: het is nog net iest eleganter om de stimulus aan te maken buiten de loop en hier dan enkel de radius, positie en/of kleur aan te passen
    Sun = visual.Circle(win, radius = 0.15 +0.0125 * growth, pos= (0,0), fillColor= [1,1,-1], lineColor= [1,1,-1],colorSpace='rgb')
    # adjust green rgb values from 1 to -1
    ## Esther: deze while loop zal nooit uitgevoerd worden want steps is 60
    while steps < 60:
        yellow_red = -((np.ndarray.round(sungrow_array)/0.45)-1)
        if yellow_red < -1:
           yellow_red = -1
        Sun.color = (1, yellow_red, -1)
        count = count + 1
#     # if Sun.overlaps(planet):
#            continue
    Sun.draw()
    Planet.draw()
    Moon.draw()
    win.flip()
    time.sleep(0.1)

## ESther: de opeenvolging van de condities in de if...elif stuctuur sluiten uit dat de derde boodschap ooit op het scherm komt
# I didn't get to the part to move the orbits and let them crash but I had an idea how to present the feedback message
# Part 5: print message on screen
#if  planet_collision:
#    message: "The planet has touched the red giant"
#elif moon_collision:
#    message: "The moon has touched the red giant"
#elif planet_collision = moon_collision:
#    message: "The planet and the moon have touched the red giant"
#else:
#    message: "None of the orbits have touched the red giant"
#message = visual.TextStim(win, text = message, pos = (0,0))
#message.draw()




# Part 6: Close the window 
time.sleep(1)
win.close()