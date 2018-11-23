#Goal of this study: making "het zonnestelsel"

# Importing
from psychopy import visual
import time
import numpy

# Making variables
planet_x_begin    = 0.705     ## coordination on the x-as
planet_y_begin    = 0.236     ## coordination on the y-as
moon_x_begin      = 0.002     ## coordination on the x-as
moon_y_begin      = 0.12      ## coordination on the y-as
trial_planet      = 1         ## planet goes 1 time round the sun
trial_moon        = 6         ## moon goes 6 times round the planet

sun_begin   = 0.15      ## Beginsize of the sun
sun_end     = ( sun_begin + (sun_begin * 1.03)  )**60 ##the sun grows each time 1.03, and that 60 times

# Coordinates planet and moon
planet_x_steps = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
                     0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
                     0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
                    -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
                    -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
                    -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
planet_y_steps = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
                     0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
                     -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
                    -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
                    -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
                     0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
moon_x_steps = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
                    0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
                    0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
                    0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
                    0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
                    0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
moon_y_steps = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
                    0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
                    0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
                    0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
                    0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
                    0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]


# Making graphics
win         = visual.Window( [600, 600], color = "black", units="norm")
## Esther: let op, je hemellichamen zijn half zo klein als de bedoeling was!
sun         = visual.Circle(win, radius = 0.075, pos = (0,0), fillColor = "yellow")
planet      = visual.Circle(win, radius = 0.035, pos = (planet_x_begin,planet_y_begin), fillColor = "blue")
## Esther: de coordinaten van de maan en de planeet moesten nog bij elkaar opgeteld worden!
moon        = visual.Circle(win, radius = 0.010, pos = (moon_x_begin, moon_y_begin), fillColor = "white")
stim_botsing= visual.TextStim(win, text="Botsing!!!", pos = (0.0, 0.5) ) ## text when moon or planet hits sun

## Esther: dit kon je eenvoudiger doen door 1 tekstobject te maken en dan enkel nog de .text info te updaten.
message1    = visual.TextStim(win, text="De planeet en de maan hebben tegelijk de rode reus geraakt", pos = (0.0, 0.5) )
message2    = visual.TextStim(win, text="De planeet heeft de rode reus geraakt", pos = (0.0, 0.5) )
message3    = visual.TextStim(win, text="De maan heeft de rode reus geraakt", pos = (0.0, 0.5) )
message4    = visual.TextStim(win, text="Geen enkele van de hemellichamen heeft de rode reus geraakt", pos = (0.0, 0.5) )

# Displaying "het zonnestelsel"
sun.draw()
planet.draw()
moon.draw()

win.flip()
time.sleep(1)

# Making an array

sunny_array = numpy.array( [planet_x_steps, planet_y_steps, moon_x_steps, moon_y_steps] )


# Making the sun larger until it hits the planet or moon
##Goal: making the sun larger with 103% of the previous sun
##Sun stops growing until it hits a planet or moon
##This happens after the 60 steps
##Condition: while-loop

sizes_sun = sun_begin ** 60
print(sizes_sun)

while numpy.any(sunny_array > sun_end) == False:  
    
    ##The sun keeps growing until step 60,
    ##The moment it reaches step 60, message comes saying planet, moon or both had hit the sun
    for i in range(sizes_sun): 
    ## Esther: hier was je een paar haakjes vergeten!
    #for i in range sizes_sun: 
        ## Esther: de visuele stimulus sun kan niet gelijk zijn aan een getal
        if sun == sun_begin:
            sun = visual.Circle(win, radius = 0.075, pos = (0,0), fillColor = "yellow")
            sun.draw()
            win.flip()
            time.sleep(1)
            
        else:
            ## Esther: op zich is de if-else structuur hieronder correct!
            if moon and planet == sun:
                print(message1)
            elif planet == sun:
                print(message2)
            elif moon == sun:
                print(message3)
            else:
                print(message4)
    
    ## Esther: hier moets je *1.03 doen, niet plus!
    sun_begin += 1.03 ##make the sun always with 1.03 bigger
    
        ##planet rotate around the sun while the moon rotate around the planet
        for i in range 
    
    sun.draw()
    win.flip()
    time.sleep(1)

time.sleep(1)
win.close()
    

