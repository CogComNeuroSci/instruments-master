# import modules
from psychopy import visual, core, event
import time, numpy

# initialize the window
win = visual.Window(size = (600,600), units = "norm", color = "black")

for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)

# Initialize variables

sun_size_start = 0.075 
sun_size = sun_size_start
adjustment = 1.03
sun_size_steps = 60
planet_size = 0.035
moon_size = 0.010
planet_start_pos = [0.705,0.236]
moon_start_pos = [0.707,0.356]
planet_pos = planet_start_pos
moon_pos = moon_start_pos


Planetx = numpy.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
Planety = numpy.array([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])

Moonx = numpy.array([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.])
Moony = numpy.array([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])

#planet and moon orbit

##planet_xy = numpy.column_stack([Planetx, Planety])
##planet_pos = planet_start_pos + planet_xy

##moon_xy = numpy.column_stack([Moonx, Moony])
##moon_pos = moon_start_pos.pos + moon_xy


# Initialize the graphical elements

sun = visual.Circle(win, radius = sun_size_start, pos = (0,0)) #fillColor = "yellow")
planet = visual.Circle(win, radius = planet_size, pos = planet_start_pos, lineColor = "blue", fillColor = "blue") #pos wordt variabele
moon = visual.Circle(win, radius = moon_size, pos = moon_start_pos, lineColor = "white", fillColor = "white") #pos wordt variabele


#stationary solar stellar

for i in range (1):
    if i == 0:
        sun.radius = sun_size_start
        sun.color = "yellow"
        sun.draw()
        planet.pos = planet_pos
        planet.draw()
        moon.pos = moon_pos
        moon.draw()
        win.flip()
        time.sleep(1)

#growing sun + getting redder

sun_size_array = numpy.array([sun_size]) ##sun_size = sun_size_start = 0.075
print(sun_size_array)


while numpy.any(sun_size_array > 60) == False:
    
     ## update the current size
    sun_size = adjustment*sun_size
    print(sun_size)
    sun_size_array = numpy.vstack([sun_size_array, sun_size])
    print(sun_size_array)
    
    ## for the 1 value
    for f in range(sun_size_array.shape[1]): #f = sun_size (radius) -> 60 stappen
        
        ##the evolving value
        for i in range(0,sun_size_array.shape[0]): #i = sun_size_array 
            
            ##color adjustment (this is the moment I got stuck and wasted a lot of time)
            adjusted_color = sun_size ##I wanted to try the following: lowering the size would result in a rise of the adjusted color between 0 and 1. But I coundn't find something.
            if adjusted_color > 0:
                adjusted_color = 0
            if adjusted_color < 0:
                adjusted_color = 0
            
            if f == 0:
                sun.Color = (1,adjusted_color,0)
                
                ##size adjustment
                sun.radius = sun_size  
        
        ##drawing the objects
        planet.draw()
        moon.draw()
        sun.draw()
        win.flip()
        time.sleep(0.01)

#closing the window
win.close()






