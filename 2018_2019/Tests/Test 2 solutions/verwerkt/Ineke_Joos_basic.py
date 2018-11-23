# Test 2 IEP 21/11/18 Ineke Joos

# import modules

from psychopy import visual, event
import time, numpy

# display preparation

win= visual.Window([600,600], color=(-1,-1,-1), units="norm")

# define startvalues

pos_zon = (0,0)
start_pos_planeet = (0.705, 0.236)
start_pos_maan = (0.705+0.002, 0.236+0.12) # add start_pos_maan to start_pos_plaat to get start position for moon relative to position of planet
start_straal_zon = 0.075*2 # straal is (15/2 = 7.5)% van window en window gaat van -1 tot 1 dus in totaal lengte/breedte van 2
straal_planeet = 0.035*2 # straal is (7/2 = 3.5)% van window en window gaat van -1 van 1 dus in totaal lengte/breedte van 2
straal_maan = 0.001*2 # straal is (2/2 = 1)% van window en window gaat van -1 van 1 dus in totaal lengte/breedte van 2



## Coordinates of planet and moon 

# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)

planeet_x = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
planeet_y = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
maan_x = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
maan_y = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

# put x- and y coordinates into one list 

## planet

coordinates_planeet = list(zip(planeet_x, planeet_y))

## moon: x- en y-coordinates of planet have to be added to coordinates of moon

for i in range(len(planeet_x)):
    maan_x_coordinaten = planeet_x[i] + maan_x[i]
    maan_y_coordinaten = planeet_y[i] + maan_y[i]
    

#coordinaten_maan = list(zip(maan_x_coordinaten, maan_y_coordinaten))
#print(coordinaten_maan)

# define graphical elements

zon = visual.Circle(win,lineColor=(1, 1, 0),fillColor=(1, 1, 0),pos= pos_zon,radius=start_straal_zon)
planeet = visual.Circle(win,lineColor=(-1, -1, 1),fillColor=(-1, -1, 1),pos=start_pos_planeet,radius= straal_planeet)
maan = visual.Circle(win,lineColor=(1, 1, 1),fillColor=(1, 1, 1),pos=start_pos_maan,radius= straal_maan)

# make radius of sun grow 

radius_array = numpy.array([])
radius = start_straal_zon

for step in range(60):
    
    # let radius of sun grow in 60 steps
    
    ## eah step radius grows with 3% compared to the size of the previous step
    
    radius = radius + radius*0.03
    radius_array= numpy.append([radius_array], radius)
    
    # determine color gradient
    
    ## startcolor = yellow: (1, 1, -1), endcolor = red: (1, -1, -1) --> only green (rGb) changes from 1 to -1
    ## value of color ranges from -1 to 1
    ## value of radius ranges from 0 to 1 (approximately) --> multiply this with 2 so range is [0,2] and then subtract 1 to make sure range is [-1,1]
    
    green_array = -((radius_array*2)-1)
    adjusted_green = green_array[step]
    
    # make sure green_ does not become smaller than -1

    if adjusted_green < -1:
        adjusted_green = -1
        
    # inserting color values and drawing sun 
    
    zon = visual.Circle(win,lineColor=(1, adjusted_green, -1),fillColor=(1, adjusted_green, -1),pos= pos_zon,radius=radius)
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)

# botsing

## botsing tussen zon en maan

#if visual.helpers.circlesOverlap(zon, maan) == True:
#    botsingmaan = visual.TextStim(win, text="De maan heeft de rode reus geraakt")
#    botsingmaan.draw()
#    win.flip()
#    time.sleep(1)
#    
#    ## botsing tussen zon en planeet 
#    
#    elif visual.helpers.circlesOverlap(zon, planeet) == True:
#        botsingplaneet = visual.TextStim(win, text=" De planeet heeft de rode reus geraakt")
#        botsingplaneet.draw()
#        win.flip()
#        time.sleep(1)
#    
#    ## botsing tussen zon, planeet en maan 
#    
#    elif visual.helpers.circlesOverlap(zon, maan) == True and visual.helpers.circlesOverlap(zon, planeet) == True:
#        botsingbeide = visual.TextStim(win, text=" De planeet en de maan hebben tegelijk de rode reus geraakt")
#        botsingbeide.draw()
#        win.flip()
#        time.sleep(1
#    else: 
#        continue 



# close window
win.close()


