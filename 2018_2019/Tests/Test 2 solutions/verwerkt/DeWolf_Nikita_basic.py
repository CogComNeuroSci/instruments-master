#part 1: import/load the modules
from psychopy import visual
import time
import numpy as np
from psychopy.visual import ShapeStim


#Part two: make the window in which the stimuli will be presented, make it normalized, with width and height of 600 and add a black background
## ESther: pas op, hier zet je de coordinaten op pixels in plaats van het genormaliseerd systeem
win = visual.Window([600, 600], color = (-1, -1, -1), units = 'pix')

#Part three: initialization
 #stationary solar sytem: celectial bodies positions
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!
 #Thus, the position of the moon and the position of the planet we define as:
position_moon = (0.002, 0.12)
position_planet = (0.705, 0.236)
colorSunChange = ['yellow', 'gold', 'goldenrod', 'peru', 'chocolate', 'brown', 'darkred', 'firebrick']
PlanetVert = [(0.014, 0.5),(0.099, 0.496), (0.182, 0.487), (0.264, 0.472),(0.342, 0.452), (0.417, 0.427), (0.487, 0.397), (0.552, 0.362), (0.61, 0.324), (0.661, 0.281), 
             (0.705, 0.236), (0.741, 0.188), (0.769, 0.138), (0.788, 0.086), (0.798, 0.033), (0.799, -0.02),(0.792, -0.073), (0.775, -0.125), (0.749, -0.175), (0.715, -0.224),
             (0.673, -0.27),(0.624, -0.313), (0.567, -0.353), (0.504, -0.388), (0.435, -0.419), (0.362, -0.466), (0.284, -0.467), (0.203, -0.484), (0.12, -0.494),(0.035, -0.5),
            (-0.049, -0.499), (0.134, -0.493),(-0.217, -0.481),(-0.297, -0.464),(-0.374, -0.442),(-0.447, -0.415),(-0.515, -0.383),(-0.577, -0.346),(-0.632, -0.306),(-0.681, -0.263),
            (-0.721, -0.216),(-0.754, -0.167),(-0.778, -0.116),(-0.793, -0.064),(-0.8, -0.011), (-0.797, 0.042),(-0.786, 0.095),(-0.765, 0.146),(-0.736, 0.196),(-0.699, 0.244),
            (-0.653, 0.288),(-0.601, 0.33),(-0.541, 0.368),(-0.476, 0.402),(-0.405, 0.431),(-0.33, 0.456),(-0.251, 0.475),(-0.169, 0.489),(-0.085, 0.497),(-0, 0.5)]
MoonVert = [(0.002,0.12),(0.079, 0.091),(0.118, 0.019),(0.103, -0.061),(0.04, -0.113),(-0.042, -0.112),(-0.104, -0.059),(-0.118, 0.021),(-0.077, 0.092),(-0, 0.12),
            (0.002, 0.12),(0.079, 0.091), (0.118, 0.019), (0.103, -0.061), (0.04, -0.113),(-0.042, -0.112),(-0.104, -0.59),(-0.118, 0.021),(-0.077, 0.092),(-0., 0.12), 
            (0.002, 0.12),(0.079, 0.091), (0.118, 0.019), (0.103, -0.061), (0.04, -0.113),(-0.042, -0.112),(-0.104, -0.59),(-0.118, 0.021),(-0.077, 0.092),(-0., 0.12),
            (0.002, 0.12),(0.079, 0.091), (0.118, 0.019), (0.103, -0.061), (0.04, -0.113),(-0.042, -0.112),(-0.104, -0.59),(-0.118, 0.021),(-0.077, 0.092),(-0., 0.12),
            (0.002, 0.12),(0.079, 0.091), (0.118, 0.019), (0.103, -0.061), (0.04, -0.113),(-0.042, -0.112),(-0.104, -0.59),(-0.118, 0.021),(-0.077, 0.092),(-0., 0.12),
            (0.002, 0.12),(0.079, 0.091), (0.118, 0.019), (0.103, -0.061), (0.04, -0.113),(-0.042, -0.112),(-0.104, -0.59),(-0.118, 0.021),(-0.077, 0.092),(-0., 0.12)]

#Part four: create the graphic elements or stimuli
  #Make planet
sizes = [0.05, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45]
for i in sizes:
    sun= visual.Circle(win, radius =i, pos=(0,0), units = 'norm', fillColor = "yellow", lineColor="yellow")
    sun.draw()
    win.flip()
    time.sleep(1)
planet = visual.Circle(win, pos= (0.705, 0.236), color = 'blue', units= 'norm', radius=0.1)
planet.draw()
win.flip()

moon = visual.Circle(win, pos=(0.002, 0.12), color = 'WhiteSmoke', units= 'norm', radius=0.15)
moon.draw()
win.flip()

#Unfortunately, I couldn't get to display the planet and moon at the same time as the sun. Due to lack of time I couldn't find a way to fix this, just like the color of the sun :(

#Rotation of planet and moon

# Registration whether moon, planet or both have hit the sun (at the same time)
   #Due to lack of time I couldn't get to finish this part. However, I know you have to use the if... elif... else statement, and use time.sleep(1) to let it display for one second.


#Draw the graphic elements
time.sleep(1)
win.close()

