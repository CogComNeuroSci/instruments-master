# Importing modules
import numpy, time
from psychopy import visual
from scipy.spatial import distance

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(size = [600, 600], color = (-1,-1,-1), units = "norm")

# Prepare the graphical elements
sun     = visual.Circle(win, radius=0.15, color = [1,1,-1])
planet  = visual.Circle(win, radius=0.07, color = "blue")
moon    = visual.Circle(win, radius=0.02, color = "white")
message = visual.TextStim(win, text="None of the celestial bodies collided")

# Initialize the redder color
less_green = 2

# Initialize the collision trackers
planetCollision = False
moonCollision = False

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

# Let the sun grow to a red giant
for step in range(len(Planetx)):
    
    # set the horizontal and vertical position for the planet and moon at this point in time
    planet.pos  = [Planetx[step],Planety[step]]
    moon.pos    = [Planetx[step]+Moonx[step],Planety[step]+Moony[step]]
    
    # the red dwarf turns into a red giant
    less_green = less_green*0.98
    sun.color = [1,less_green-1,-1]
    sun.radius = sun.radius*1.02
    
    # display the celestial bodies
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    time.sleep(0.1)
    
    # verify whether the sun hit a celestial object
    if (distance.euclidean(sun.pos, planet.pos) - sun.radius - planet.radius) <= 0:
        planetCollision = True
    
    if (distance.euclidean(sun.pos, moon.pos) - sun.radius - moon.radius) <= 0:
        moonCollision = True
    
    if planetCollision == True or moonCollision == True:
        break

# verify what text to display
if planetCollision == True and moonCollision == True:
    message.text = "The planet and moon hit the red giant at the same time"
elif planetCollision == True :
    message.text = "The planet hit the red giant"
elif moonCollision == True:
    message.text = "The moon hit the red giant"

# display the message
message.draw()
win.flip()
time.sleep(1)

# the end!
win.close()