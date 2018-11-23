#importing modules
from psychopy import visual
import time

#initialize variables
radius_sun=2*0.075
radius_planet=2*0.035
radius_moon=2*0.01
n_steps=60


#changing coordinates of planet and moon
planetx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
planety = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
moonx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
moony = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

#define visual elements
win=visual.Window(size=[600,600],color=(-1,-1,-1), units="norm")
sun=visual.Circle(win,radius=radius_sun,color=(1,1,-1),pos=(0,0))

#initialize variables
change=0
crash=False

for change in range(n_steps):
    #change coordinates of planet and moon
    x1=planetx[change]
    y1=planety[change]
    x2=planetx[change]+moonx[change]
    y2=planety[change]+moony[change]

    #define planet and moon
    planet=visual.Circle(win,radius=radius_planet,color=(-1,-1,1),pos=(x1,y1))
    moon=visual.Circle(win,radius=radius_moon,color=(1,1,1),pos=(x2,y2))

    #change shape of sun
    sun.radius=sun.radius*1.03

    #change color of sun
    green=-((change/30)-1)
    if green < -1:
        green = -1
    sun.color=(1,green,-1)

    #put stimuli on screen
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    time.sleep(0.1)

    #update value of change
    change+=1

    #stop when planet and/or moon crashes with sun
    if sun.overlaps(planet) or sun.overlaps(moon):
        break

#feedback about whether a crash happend and between which shapes
if sun.overlaps(planet):
    feedback="De planeet heeft de rode neus geraakt."
elif sun.overlaps(moon):
    feedback="De maan heeft de rode neus geraakt."
elif sun.overlaps(planet) and sun.overlaps(moon):
    feedback="De planeet en de maan hebben tegelijk de rode neus geraakt."
else:
    feedback="Geen enkele van de hemellichamen heeft de rode neus geraakt."

feedback_text=visual.TextStim(win, text= feedback)
feedback_text.draw()
win.flip()
time.sleep(1)
win.close()