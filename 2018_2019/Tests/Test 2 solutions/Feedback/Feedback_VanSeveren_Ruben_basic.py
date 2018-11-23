from psychopy import visual
import time
import numpy

#stationary solar sytem: celectial bodies positions
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!

# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
Planetxorbit = ([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
Planetyorbit = ([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])

#make a column of x and y coordinates
Planet_coordinates = numpy.column_stack([Planetxorbit,Planetyorbit])

Moonxorbit = ([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.])
Moonyorbit = ([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])

#Make a column of x and y coordinates
Moon_coordinates = numpy.column_stack([Moonxorbit, Moonyorbit])




#window maken
win = visual.Window(size = (600,600), color = "black", units = "norm")

#zon maken en laten groeien

Radius = 0.075
Adjusted_radius = Radius*0.3
for i in range(60):
    
    ## Esther: het is nog beter als je de stimuli aanmaakt buiten de loop en in de loop dan enkel de radius, positie en kleur aanpast
    Sun = visual.Circle(win, radius = Radius, color = "yellow")
    ## Esther: let op, dit is niet de aanpassing vna 103% op elke pass door de loop die we gevraagd hadden!
    Radius = Radius + Adjusted_radius
    Value_array = numpy.append(Radius, Adjusted_radius)
    #kleur aanpassen
    
    Sun.draw()
    ## Esther: deze time.sleep staat verkeerd!
    time.sleep(0.1)

    #Planeet en maan maken
    ## Esther: let op, de stimuli zijn de helft kleiner dan we gevraagd hadden!
    Planet = visual.Circle(win, radius = 0.035, pos = (Planet_coordinates[i,0],Planet_coordinates[i,1]), color = "blue")
    ## Esther: pas op, je hebt hier bij de maan verkeerde coordinaten opgeteld!
    Moon = visual.Circle(win, radius = 0.01, pos = ((Planet_coordinates[i,0] + Moon_coordinates[i,0]),(Planet_coordinates[i,1] + Moon_coordinates[i,0])), color = "white")
    Planet.draw()
    Moon.draw()
    win.flip()
    time.sleep(0.1)







