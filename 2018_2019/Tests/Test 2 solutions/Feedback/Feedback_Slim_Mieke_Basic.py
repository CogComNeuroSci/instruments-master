# This script is written for the second test of "Instrumenten van de Experimentele Psychology" 
# This script is a visualisation of a simple solar system. First, a stationary solar system consisted of a sun, a planet and a moon will be shown on a screen. 
# Secondly, this stationary system transitions into a dynamic solar system with a growing sun and moving celestial bodies.
# Author: Mieke Slim
# Gemaakt tijdens een inhaalmoment: 23/11/2018 

# Import modules
from psychopy import visual
import time
import numpy

# Generate a window
win = visual.Window(size = (600, 600), color = (-1, -1, -1))

# Generate the variables (positions):
## I haven't used the stationary positions that were given in the start file, see my comment on line 51 and 52
## Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
Planetxorb = numpy.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
Planetyorb = numpy.array([  0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])
Moonxorb = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
Moonyorb = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

## Other variable: initial radius of the sun 
sunradius = 0.15

# Stationary solar system (graphics + drawing). The positions are determined based on the list of the orbits, so there is a smooth transition
# between the stationary and the dynamic solar system (so I did not use the stationary positions given in the start file).
sun = visual.Circle(win, radius = sunradius, color = (1, 1, -1))
planet = visual.Circle(win, radius = 0.07, pos = (Planetxorb[0], Planetyorb[0]), color = (-1, -1, 1))
moon = visual.Circle(win, radius = 0.02, pos = ((Moonxorb[0] + Planetxorb[0]),(Moonyorb[0] + Planetyorb[0])), color = (1, 1, 1))
sun.draw()
planet.draw()
moon.draw()
win.flip()
time.sleep(1)

# Dynamic solar system
# Growth and colour change of the sun
for step in range(60):
    sunradius = 1.03 * sunradius
    ## Esther: het is nog net een tikje beter om de stimulus elementen aan te maken buiten de loop en dan in de loop enkel de radius, positie en kleur aan te passen.
    sun = visual.Circle(win, units = 'norm', radius = sunradius, color = (1, 1 - (step/20), -1)) ## The '20' in the RGB code is based on some tinkering, as I thought it gave the 'prettiest' result.
    planet = visual.Circle(win, radius = 0.07, pos = (Planetxorb[step], Planetyorb[step]), color = (-1, -1, 1))
    moon = visual.Circle(win, radius = 0.02, pos = ((Moonxorb[step] + Planetxorb[step]),(Moonyorb[step] + Planetyorb[step])), color = (1, 1, 1))

    # The code below generates the collision of the celestial bodies
    ## Esther: let op, je code houdt nu geen rekening met de mogelijkheid dat de drie tegelijk botsen!
    if sun.overlaps(planet):
        ## Esther: de indentering kon hier nog net een beetje strakker (1 level naar links)
            Botsing = visual.TextStim(win, text = "Botsing! De zon heeft de planeet geraakt", color = "white")
            Botsing.draw()
            win.flip()
            time.sleep(1)
            break
    elif sun.overlaps(moon):
        Botsing = visual.TextStim(win, text = "Botsing! De zon heeft de maan geraakt", color = "white")
        Botsing.draw()
        win.flip()
        time.sleep(1)
        break
    else:
        pass ## It is unnecessary to provide a text stimulus that would be displayed if there is no collision (as mention in the text instructions)
             ## There will always be a collision, as the other celestial bodies always moves around the growing sun.
    ## Esther: I see, but we would have liked to see some code that takes that possibility into account, for instance when the growth of the sun is set to a lower speed

    # Draw the graphics and flip them onto the screen
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    time.sleep(0.1)

#Close the window
win.close()


