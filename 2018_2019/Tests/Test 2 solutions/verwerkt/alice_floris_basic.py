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


# Making graphics
win         = visual.Window( [600, 600], color = "black", units="norm")
sun         = visual.Circle(win, radius = 0.075, pos = (0,0), fillColor = "yellow")
planet      = visual.Circle(win, radius = 0.035, pos = (planet_x_begin,planet_y_begin), fillColor = "blue")
moon        = visual.Circle(win, radius = 0.010, pos = (moon_x_begin, moon_y_begin), fillColor = "white")
stim_botsing= visual.TextStim(win, text="Botsing!!!", pos = (0.0, 0.5) ) ## text when moon or planet hits sun

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
    for i in range sizes_sun: 
        if sun == sun_begin:
            sun = visual.Circle(win, radius = 0.075, pos = (0,0), fillColor = "yellow")
            sun.draw()
            win.flip()
            time.sleep(1)
            
        else:
            if moon and planet == sun:
                print(message1)
            elif planet == sun:
                print(message2)
            elif moon == sun:
                print(message3)
            else:
                print(message4)
        
    sun_begin += 1.03 ##make the sun always with 1.03 bigger
    
        ##planet rotate around the sun while the moon rotate around the planet
        for i in range 
    
    sun.draw()
    win.flip()
    time.sleep(1)

time.sleep(1)
win.close()
    
