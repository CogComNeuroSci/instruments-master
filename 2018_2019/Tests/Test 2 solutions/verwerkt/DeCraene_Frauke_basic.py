from psychopy import visual
import time, numpy

#create window
win = visual.Window([600,600], color='black')


# stationary solar sytem: celectial bodies positions
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!


# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
OrbitPlanetx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
OrbitPlanety = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
OrbitMoonx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
OrbitMoony = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

#create planets in startposition
##diameter of sun is 15% -> 0.30 so radius is 0.30/2 = 0.15
##same logic for the other radii
sun = visual.Circle(win, radius = 0.15, lineColor=[1,1,-1], fillColor=[1,1,-1])
planet = visual.Circle(win, radius = 0.07, lineColor=[-1,-1,1], fillColor=[-1,-1,1], pos= [Planetx,Planety])
moon = visual.Circle(win, radius = 0.02, lineColor=[1,1,1], fillColor=[1,1,1], pos= [Planetx+Moonx,Planety+Moony])


#create array for changing size and color
##60 steps to get from yellow [1,1,-1] to red [1,-1,-1]
##Green value needs to change 2 units in 60 steps
ColorArray = numpy.array([])
for colorchange in range(60):
    ColorArray=numpy.append(arr=ColorArray, values=1-colorchange*(2/59))

SizeArray = numpy.array([0.15])
for sizechange in range(59):
    SizeArray=numpy.append(arr=SizeArray, values=SizeArray[sizechange]*1.03)

SunChanges = numpy.column_stack([ColorArray, SizeArray])


#Create TextStim for crashes
bothcrash = visual.TextStim(win,text= "De planeet en de maan hebben tegelijk de rode reus geraakt")
mooncrash = visual.TextStim(win,text= "De maan heeft de rode reus geraakt")
planetcrash = visual.TextStim(win,text= "De planeet heeft de rode reus geraakt")

##Display stationary situation for 1sec
#sun.draw()
#planet.draw()
#moon.draw()
#win.flip()
#time.sleep(1)


for rotation in range (len(OrbitMoonx)):
    #determine moon ans planet position
    planet.pos= [OrbitPlanetx[rotation ],OrbitPlanety[rotation ]]
    moon.pos= [OrbitPlanetx[rotation ]+OrbitMoonx[rotation ],OrbitPlanety[rotation ]+OrbitMoony[rotation ]]

    #sun color and radius change
    sun.fillColor = [1,SunChanges[rotation ,0],-1]
    sun.lineColor=sun.fillColor
    sun.radius= SunChanges[rotation ,1]

    #draw all shapes
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    
    #detect crash
    if sun.overlaps(moon) ==  True and sun.overlaps(planet) == True:
        bothcrash.draw()
        win.flip()
        time.sleep(1)
        break
    elif sun.overlaps(moon) ==  True :
        mooncrash.draw()
        win.flip()
        time.sleep(1)
        break
    elif sun.overlaps(planet) ==  True :
        planetcrash.draw()
        win.flip()
        time.sleep(1)
        break

win.close()