#This experiment is made by Nel Tavernier on 21/11/2018 for Test 2

## WARNING:  I was stuck on the part to make te sun bigger so I made different steps with each step a code that is working, except to make the sun bigger and the last one

#Importing modules 
from psychopy import visual 
import time 
import numpy as np 

#Making a window

win = visual.Window([600, 600], color = 'black', units = 'norm', monitor = 'testmonitor')

#Initialization

n_trials = 60
count = 0
planet_counter = 0
moon_counter = 0

radius_sun = 0.075 * 2 ## 7.5 percent of screen 
radius_planet = 0.035 *2 ##3.5 percent of screen 
radius_moon = 0.01 * 2 ## 1 percent of screen 
percent_sun = 0.03 * 2 ## 103 percent

#first coordinates
Planetx = 0.705
Planety = 0.236
Moonx = 0.002   # this coordinate is relative to the position of the planet!
Moony = 0.12    # this coordinate is relative to the position of the planet!

## So that it is not relative anymore
MoonCoordx = Planetx + Moonx
MoonCoordy = Planety + Moony

planet_start_pos = (Planetx, Planety)

moon_start_pos = (MoonCoordx, MoonCoordy)

#second coordinates as lists
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

## So that it is not relative anymore
MoonCoordx = np.add(Planetx, Moonx)
MoonCoordy = np.add(Planety, Moony)

## This is an array with the beginning value and later use numpy.vstack to make the sun bigger. 
radius_sun_array = np.array(radius_sun)

# Graphical elements

sun = visual.Circle(win, radius = radius_sun, color = (1, 1, 0), pos = (0,0))
sun.colorSpace = 'rgb'
planet = visual.Circle(win, radius = radius_planet, color = 'blue', pos = planet_start_pos) 
moon = visual.Circle(win, radius = radius_moon, color = 'white', pos = moon_start_pos)

##Step 1: Displayin the sun, moon and planet      #This works
#sun.draw() 
#planet.draw()
#moon.draw()
#win.flip()
#time.sleep(1)
#


## Step 2: Making the sun big                    #This doesn't work

#for i in range(n_trials): 
#    radius_sun = radius_sun + percent_sun
#    radius_sun_array = np.vstack([radius_sun_array, radius_sun])
#    print(radius_sun_array)
#    print(radius_sun_array.shape)
#    sun.radius = radius_sun_array[i]
#    sun.draw()
#    win.flip
#    time.sleep(0.1)
    



## Step 3: Making the sun red                  #This works

#for i in range (n_trials):
#    count +=1

#    red_making = -((np.array(count)/30)-1)
#    if red_making < 0.03: 
#        red_making = 0
#    print(red_making)

#    sun.color = (1, red_making, 0), pos = (0,0))
#    sun.colorSpace = 'rgb'

#    sun.draw()
#    planet.draw()
#    moon.draw()

#    win.flip()
#    time.sleep(0.1)
#


## Step 4: Making the moon and planet move AND the sun red      #This works
for i in range (n_trials): 
    count +=1
    
    red_making = -((np.array(count)/30)-1)
    if red_making < 0.03: 
        red_making = 0
    
    sun.color = (1, red_making, 0)
    sun.colorSpace = 'rgb'
    
    planet.pos = (Planetx[i], Planety[i])
    moon.pos = (MoonCoordx[i], MoonCoordy[i])
    planet.draw()
    moon.draw()
    sun.draw()
    
    win.flip()
    time.sleep(0.1)




## Step 5Feedback : 'Botsing'                 #This doesn't work but I hope it is already in the right direction :)

#Making criterium for the feedback

#for i in range (n_trials): 
#    count +=1
#    
#    red_making = -((np.array(count)/30)-1)
#    if red_making < 0.03: 
#        red_making = 0
#    
#    sun.color = (1, red_making, 0)
#    sun.colorSpace = 'rgb'
#    
#    planet.pos = (Planetx[i], Planety[i])
#    moon.pos = (MoonCoordx[i], MoonCoordy[i])
#    planet.draw()
#    moon.draw()
#    sun.draw()
#    
#    win.flip()
#    time.sleep(0.1)
#    
#    if np.absolute(planet.pos[i] < radius_sun):
#        
#        crash = True
#        planet_counter += 1
#        
#    if np.absolute(moon.pos[i] < radius_sun): 
#        
#        crash = True 
#        moon_counter +=1
#        
#    else: 
#        crash = False
#        
#
#Feedback tonen
#
#if planet_counter==0 and moon_counter==0:
#    feedback = "Geen enkele van de hemellichamen heeft de rode reus geraakt"
#elif planet_counter==moon_counter:
#    feedback = "De planeet en de maan hebben tegelijk de rode reus geraakt"
#elif planet_counter>moon_counter:
#    feedback = "De planeet heeft de rode reus geraakt"
#else:
#    feedback = "De maan heeft de rode reus geraakt"
#feedback_text = visual.TextStim(win,text = feedback)
#feedback_text.draw()
#win.flip()
#time.sleep(1)


#Closing the window
win.close()






