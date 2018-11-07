# Importing modules
import numpy, time
from psychopy import visual

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

# Initialize the orbit settings
PlanetAxisH = 0.8
PlanetAxisV = 0.5
MoonAxisH = 0.12
MoonAxisV = 0.12

# Initialize the radians for the orbit
PlanetAngles    = numpy.linspace(1, 360, num=300)* numpy.pi / 180.
MoonAngles      = numpy.tile(numpy.linspace(1, 360, num=50)* numpy.pi / 180.,6)

# Restrict the number of planetary angles to match those of the moon (quick fix)
PlanetAngles = PlanetAngles[range(MoonAngles.shape[0]),]

# Compute the orbit for the planet around a midpoint
Planetx = PlanetAxisH * numpy.sin(PlanetAngles)
Planety = PlanetAxisV * numpy.cos(PlanetAngles)

# Compute the orbit for the moon around a midpoint
Moonx = MoonAxisH * numpy.sin(MoonAngles)
Moony = MoonAxisV * numpy.cos(MoonAngles)

# Combine the horzontal and verical coordinates for the two celestial bodies
PlanetaryOrbit  = numpy.column_stack([Planetx,Planety])
LunarOrbit      = numpy.column_stack([Moonx,Moony])

# Temporary graphical representation of the orbit
#PlanetArc = visual.ShapeStim(win, vertices = PlanetaryOrbit)
#LunarArc  = visual.ShapeStim(win, vertices = LunarOrbit)

# Let the sun grow to a red giant
for step in range(len(PlanetAngles)):
    
    # set the horizontal and vertical position for the planet and moon at this point in time
    planet.pos  = PlanetaryOrbit[step,]
    moon.pos    = PlanetaryOrbit[step,] + LunarOrbit[step,]
    
    # reposition the LunarArc
    #LunarArc.pos = PlanetaryOrbit[step,]
    
    # the red dwarf turns into a red giant
    less_green = less_green*0.98
    sun.color = [1,less_green-1,-1]
    sun.radius = sun.radius*1.02
    
    # display the celestial bodies
    #PlanetArc.draw()
    #LunarArc.draw()
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    time.sleep(0.01)
    
    # verify whether the sun hit a celestial object
    if sun.overlaps(planet):
        planetCollision = True
    
    if sun.overlaps(moon):
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