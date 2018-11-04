# Importing modules
import numpy, time
from psychopy import visual
from scipy.spatial import distance

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(size = [600, 600], color = (-1,-1,-1), units = "norm")

# stationary solar sytem: celectial bodies positions
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!

# Prepare the graphical elements
sun     = visual.Circle(win, radius=0.15, color = [1,1,-1])
planet  = visual.Circle(win, radius=0.07, color = "blue", pos = [Planetx,Planety])
moon    = visual.Circle(win, radius=0.02, color = "white", pos = [Planetx+Moonx,Planety+Moony])
message = visual.TextStim(win, text="None of the celestial bodies collided")

# Initialize the redder color
less_green = 2

# Initialize the collision trackers
planetCollision = False
moonCollision = False

# Let the sun grow to a red giant
for step in range(60):
    
    # the red dwarf turns into a red giant
    less_green = less_green*0.96
    sun.color = [1,less_green-1,-1]
    sun.radius = sun.radius * 1.03
    
    # display the celestial bodies
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    time.sleep(0.01)
    
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