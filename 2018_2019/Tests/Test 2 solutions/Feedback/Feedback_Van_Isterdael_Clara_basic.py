#Basic file of test 2 of IEP: a simple solar system

#I did not have enough time to complete the exercise: i could not think of a way to rotate the planet & moon. I was able to gradually enlarge the sun until it collides with eather planet or moon.
#because of this, certain arguments will be uncommented. These are from my start at an attempt to make the orbits move
# If i were to uncomment these arguments, my script probably would not work. This way, i have a working (although incomplete) script

## Step 1: import relevant modules
#Visual for the visualisation of stimuli on the screen (drawing shapes etc.)
from psychopy import visual
#time for timing our displays (how long should certain stimuli be seen
import time
#numpy for numerical operations with arrays etc.
import numpy as np

##Display prepartation

#create a window in which the stimuli will be displayed
win = visual.Window(size = [600,600], color = (-1,-1,-1), units = "norm")

##initialize variables
#we will define the planet & moon coordinates here already, so they can easily be altered
PlanetX = 0.705
PlanetY = 0.236

#the moon coordinates are defined relatively to the planet
MoonX = PlanetX+0.002
MoonY = PlanetY + 0.12



# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
#PlanetX = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
#             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
#             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
#            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
#            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
#            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
#PlanetY = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
#             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
#             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
#            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
#            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
#             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
#these are the relative positions of the moon, positioned to the planet
#MoonX_rel = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
#MoonY_rel = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]


#these are the absolute coordinates of the moon (defined relatively to the planet)
#MoonX = PlanetX+MoonX_rel
#MoonY = PlanetY + MoonY_rel

#conditions np.column_stack([PlanetX, PlanetY, MoonX, MoonY])

#seeing radius & color of the sun will be changing later on in the script, it is also a variable that must be defined
# 0.15 diameter means a radius = 0.075 of the screen. but seeing as the heigt of the screen = 2, radius = 0.075*2=0.15 (this also counts for radius of moon & planet)
SunRadius = 0.15
SunColor = (1,1,-1)



##creating the visual stimuli to be shown on the screen
#the sun is a yellow circle that is positioned in the middle of the screen
Sun = visual.Circle(win, radius = SunRadius, color = SunColor, pos = (0,0))

#the planet is a blue circle of 0.07 diameter (radius = 0.035) that is positioned in x-coordinate 0.705 & y-coordinate 0.236 (absolute coordinates)
Planet = visual.Circle(win, radius = 0.07, color = (-1,-1,1), pos = (PlanetX, PlanetY))

# the moon is a white circle of 0.02 diameter (radius = 0.01) that is positioned relative to the Planet
# it's coordinates relative to Planet are: (0.002, 0.12)
Moon = visual.Circle(win, radius = 0.02, color = (1,1,1), pos = (MoonX, MoonY))

#Feedback is about whether the growing sun has collided with the planet & the Moon
Feedback = visual.TextStim(win, text = "test")

#initialise an array to track the collisions
#the first row will show whether the red nose collided with the planet, the second row will show whether it collided with the moon
Collision_array = np.array(["Does the red nose overlap with the planet?","Does the red nose overlap with the moon?"])
print(Collision_array.shape)


##from a yellow sun to a red nose
#in this for-loop, i will do 2 actions: make the sun grow AND gradually change it from yellow to red
# I am pretty sure there is an optimal way to do this, and this is not it. But this works as well
#We will use 60 steps: the sun will grow 60 times
for i in range(60):
    #for every iteration the radius will grow 3% larger than before
    #we will save the radius as thus
    Sun.radius = 1.03*Sun.radius
    
    # for the color, we have to go from (1,1,-1) (= yellow) to (1, -1,-1) (red): of the RGB code, the Red & Blue index will remain the same, only the green index will gradually become less
    # this will result in a color code of (1,x,-1) where x varies between iterations (it becomes less & less)
    #i ranges from 0 to 60. Our color ranges from -1 to 1.
    #by dividing i by 30 & subtracting it by 1, the range of i will change to (-1;1) (this is what we do in (i/30)-1
    # we will multiply this wit -1 because it changes from 1 to -1 instead of the other way around
    Sun.color= (1,(-((i/30)-1)),-1)
    
    #time for a registration of a collision: the sun collides with the moon or planet if Sun.overlaps() is True for either of the two statements (that is why I use an or-statement)
    
    #For full information & certainty, I checked whether this if-else-structure would work in another script:
    # I used the same structure, but replaced Sun.overlaps(Planet) with A & Sun.overlaps(Moon) with B.
    # i could change the values of A & B  (values were either True or False to represent the Boolean statemens .overlaps() results) to check whether it was correct (and for each if,elif,else statement i got what i expected)
    if Sun.overlaps(Planet) or Sun.overlaps(Moon):
        #If the sun indeed does overlap with the planet or moon, the sun has to stop growing & planet & moon have to stop moving: the while-loop must stop (this is done by the break-command)
        #for the feedback message, we must check the collisions
        
        #if sun collides with both:
        if Sun.overlaps(Planet)and Sun.overlaps(Moon):
            Feedback.text= "De planeet en de maan hebben tegelijk de rode neus geraakt."
        
        #if this isn't the case, we will check whether sun collides with the planet
        elif Sun.overlaps(Planet):
            Feedback.text= "De planeet heeft de rode neus geraakt."
        
        #if sun doesn't collide with the planet, it must collide with the moon
        elif Sun.overlaps(Moon):
            Feedback.text= "De maan heeft de rode neus geraakt."
            
        ## Esther: let op, deze break wordt nooit uitgevoerd!
        break
    #if the or-statement isn't true, this means there is no collision
    else:
        Feedback.text = "Geen enkele van de hemellichamen heeft de rode neus geraakt."
    
#    #to store whether the sun collide with the planet or the moon
#    Collision = np.array([Sun.overlaps(Planet),Sun.overlaps(Moon)])
#    Collision_array= np.vstack([Collision_array, Collision])
    
    
    ##display the stimuli
    Sun.draw()
    Planet.draw()
    Moon.draw()
    win.flip()
    time.sleep(0.1)

#print(Collision_array)

Feedback.draw()

win.flip()

##Close the experiment window
time.sleep(1)
win.close()