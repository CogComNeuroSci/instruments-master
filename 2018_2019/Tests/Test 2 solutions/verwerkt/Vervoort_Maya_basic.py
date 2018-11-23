#Import stuff
import numpy, time
from psychopy import visual
from time import sleep


#Define the window
##Screen should be 600x600 pixels
win = visual.Window(size = (600,600), color = [-1,-1,-1], units = "norm")

#Define important variables
time_trial = 0.1
time = 0
time_end = 6

## Size of the planets 
## Esther: helaas leidt dit tot radii die de helft te klein zijn
    ## Size of the sun at the beginning
radius_sun = 0.15/2
    ##Size of the earth and the moon
radius_earth = 0.07/2
radius_moon = 0.02/2

##Positions of the earth and moon
earthx = 0.705
earthy = 0.236
    ##Since position of the moon is relative to the position of the earth
moonx = earthx + 0.002
moony = earthy + 0.12

##Coordinates of moving planets
earthx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
earthy = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
moonx_unadjusted = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
moony_unadjusted = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

##Colors
white = [1,1,1]
blue = [-1, -1, 1]
yellow = [1,1,-1]
red = [1,-1,-1]
##Start for adjusted_color
adjusted_color = 1

#Make the planets move
Crash = False
## Esther: deze while loop komt waarschijnlijk van test 2 en heeft je op het verkeerde been gezet
while Crash == False and time <= time_end:
    for i in range(len(earthx)):
            ##Define time
            time = time + time_trial
            
            ##Define radius of the sun
            ##Define moonx and moony
            moonx = moonx_unadjusted[i]+earthx[i]
            moony = moony_unadjusted[i]+earthy[i]
            radius_sun = radius_sun*1.03
            
            ##Figure out how to adjust the color of the sun
            ##Red and Yellow have the same R and B values --> R = 1, B = -1
            ##Only the middle value needs to change from 1 to -1
            color_sun = [1, adjusted_color, -1]
            
            ##Defining the shapes
                ##Still need positions!!
                ##Is radius in percent or size of the screen?
            sun = visual.Circle(win, radius = radius_sun, pos = (0,0), fillColor = color_sun, lineColor = color_sun)
            earth = visual.Circle(win, radius = radius_earth, pos = (earthx[i], earthy[i]),fillColor = [-1,-1,1], lineColor = [-1,-1,1])
            moon = visual.Circle(win, radius = radius_moon, pos = (moonx, moony), fillColor = [1,1,1], lineColor = [1,1,1])
            
            adjusted_color = adjusted_color - ((i+1)/30)
            if adjusted_color <-1:
                adjusted_color = -1
            
            Text = "Geen enkele van de hemellichamen heeft de rode reus geraakt"
            
            #Draw stimuli on the screen
            sun.draw()
            earth.draw()
            moon.draw()
            win.flip()
            sleep(time_trial)
        
            ## Esther: helaas, je baseren op Test 2 van vorig jaar was hier in je nadeel
            #Test for crash
            ##Don't know how to define boards for the sun yet
            ##Something didn't work out here... Probably a wrong way to do this
                ##But it took so long to type and figure out, so I'll just leave it here
                ##I think it has something to do with the radius value (which is probably always positive),
                ##while the x's and y's are negative sometimes (quadrants 2,3,4)
                ##But I didn't have enough time to change this
                ##I would make sure all the negative values become positive (adding '-' in front of them)
                ##and then making sure they are SMALLER than or EQUAL to radius_sun
            ##For the moon in the 4 quadrants
            if moonx>=0 and moony>=0:
                if moonx <= radius_sun and moony<=radius_sun:
                    Crash = True
                    Text = "De maan heeft de rode reus geraakt"
                    win.flip()
            if moonx>=0 and moony<=0:
                if moonx<=radius_sun and moony>=radius_sun:
                    Crash = True
                    Text = "De maan heeft de rode reus geraakt"
                    win.flip()
            if moonx<=0 and moony<=0:
                if moonx>=radius_sun and moony>=radius_sun:
                    Crash = True
                    Text = "De maan heeft de rode reus geraakt"
                    win.flip()
            if moonx<=0 and moony>=0:
                if moonx >=radius_sun and moony<=radius_sun:
                    Crash = True
                    Text = "De maan heeft de rode reus geraakt"
                    win.flip()
            ##For the earth in the four quadrants
            if earthx[i]>=0 and earthy[i] >=0:
                if earthx[i] <= radius_sun and earthy[i]<=radius_sun:
                    Crash = True
                    Text = "De planeet heeft de rode reus geraakt"
                    win.flip()
            if earthx[i]>=0 and earthy[i]<=0:
                if earthx[i]<=radius_sun and earthy[i]>=radius_sun:
                    Crash = True
                    Text = "De planeet heeft de rode reus geraakt"
                    win.flip()
            if earthx[i]<=0 and earthy[i]<=0:
                if earthx[i]>=radius_sun and earthy[i]>=radius_sun:
                    Crash = True
                    Text = "De planeet heeft de rode reus geraakt"
                    win.flip()
            if earthx[i]<=0 and earthy[i]>=0:
                if earthx[i] >=radius_sun and earthy[i]<=radius_sun:
                    Crash = True
                    Text = "De planeet heeft de rode reus geraakt"
                    win.flip()
            ##For both planets at the same time
            if earthx[i]>=0 and earthy[i] >=0 and moonx>=0 and moony>=0:
                if earthx[i] <= radius_sun and earthy[i]<=radius_sun and moonx <= radius_sun and moony<=radius_sun:
                    Crash = True
                    Text = "De planeet en de maan hebben tegelijk de rode reus geraakt"
                    win.flip()
            if earthx[i]>=0 and earthy[i]<=0 and moonx>=0 and moony<=0:
                if earthx[i]<=radius_sun and earthy[i]>=radius_sun and moonx<=radius_sun and moony>=radius_sun:
                    Crash = True
                    Text = "De planeet en de maan hebben tegelijk de rode reus geraakt"
                    win.flip()
            if earthx[i]<=0 and earthy[i]<=0 and moonx<=0 and moony<=0:
                if earthx[i]>=radius_sun and earthy[i]>=radius_sun and moonx>=radius_sun and moony>=radius_sun:
                    Crash = True
                    Text = "De planeet en de maan hebben tegelijk de rode reus geraakt"
                    win.flip()
            if earthx[i]<=0 and earthy[i]>=0 and moonx<=0 and moony>=0:
                if earthx[i] >=radius_sun and earthy[i]<=radius_sun and moonx >=radius_sun and moony<=radius_sun:
                    Crash = True
                    Text = "De planeet en de maan hebben tegelijk de rode reus geraakt"
                    win.flip()
    ##Display the feedback about the crash
    feedback = visual.TextStim(win, text = Text)
    feedback.draw()
    win.flip()
    sleep(1)
    
    #Close the screen
    win.close()
