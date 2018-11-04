# Importing modules
import numpy, time
from psychopy import visual

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(size = [600, 600], color = (-1,-1,-1), units = "norm")

# Prepare the graphical elements
sun     = visual.Circle(win, radius=0.15, color = "yellow")
planet  = visual.Circle(win, radius=0.07, color = "blue")
moon    = visual.Circle(win, radius=0.02, color = "white")

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

print(PlanetaryOrbit)
print(LunarOrbit)

# Temporary graphical representation of the orbit
#PlanetArc = visual.ShapeStim(win, vertices = PlanetaryOrbit)
#LunarArc  = visual.ShapeStim(win, vertices = LunarOrbit)

# Let the celestial bodies spin around
for step in range(len(PlanetAngles)):
    
    # set the horizontal and vertical position for the planet and moon at this point in time
    planet.pos  = PlanetaryOrbit[step,]
    moon.pos    = PlanetaryOrbit[step,] + LunarOrbit[step,]
    
    # reposition the LunarArc
    #LunarArc.pos = PlanetaryOrbit[step,]
    
    # display the celestial bodies
    #PlanetArc.draw()
    #LunarArc.draw()
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    time.sleep(0.01)

# the end!
win.close()