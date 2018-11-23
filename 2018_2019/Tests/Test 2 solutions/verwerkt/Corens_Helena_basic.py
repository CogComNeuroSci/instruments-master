#TEST 2: CODIING SOLAR SYSTEM - BY HELENA CORENS 

#Step 1: import modules 
from psychopy import visual, event,core
import time, numpy

#Step 2: in case of emmergency, ESCAPE:
for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)

#Step 3: info about the visuals:
start_rad_sun = 0.075            #15%/2; startpositie --> laten uitdijen
pos_sun = (0,0)
rad_planet = 0.034          #7%/2
pos_planetx = 0.705
pos_planety= 0.236  #startpositie
rad_moon = 0.01             #2%/2
pos_moonx = (pos_planetx + 0.002)     #Startpositie; 'Relatief tov positie planeet': dus daarom pos_moon_x=0.705 + 0.002/ pos_moon_y=0.236 + 0.12
pos_moony = (pos_planety + 0.12)
presenting_time = 1 

Yellow = (1,1,0)
Red = (1,-1,-1)

#General Window Graphics
win = visual.Window([600,600], color = (-1,-1,-1), units = 'norm') 

#Graphics SUN
x=0.05
start_rad_sun = 0.075
while start_rad_sun < 0.1:
    start_rad_sun += (start_rad_sun*x)
    stim_sun = visual.Circle(win, radius = start_rad_sun, pos = (0,0), fillColor = 'yellow')
    stim_sun.draw()

Radius_Sun = numpy.array([0.075,0.08,0.085,0.09,0.095,0.1,0.105,0.110])
### Ik zit vast

##color changing
### niet gelukt

#Graphics PLANET
stim_planet = visual.Circle(win, radius = 0.034, pos = (0.705,0.236), fillColor = "blue")

#Graphics MOON
stim_moon = visual.Circle(win, radius = 0.01, pos = (pos_moonx,pos_moony), fillColor = "white")

# stationary solar sytem: celectial bodies positionsPlanetx = 0.705Planety = 0.236Moonx = 0.002   # this coordinate is relative to the position of the planet!Moony = 0.12    # this coordinate is relative to the position of the planet!# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)Planetx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]Planety = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]Moonx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]Moony = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]


# Crash
##voor de botsing gebruik maken van boolean --> TRUE / FALSE 


#Drawing the visuals
stim_sun.draw()
stim_planet.draw()
stim_moon.draw()

win.flip()
time.sleep(5)

win.close()







