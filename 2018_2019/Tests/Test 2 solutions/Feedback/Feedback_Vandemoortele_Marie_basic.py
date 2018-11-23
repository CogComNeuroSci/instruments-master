# part 1: loading modules
from psychopy import visual, event
import time, numpy

# part 2: initialization
n_trials = 60
Zon_radius_start = 0.075*2 
Zon_radius_max = 0.075*120
Zon_fillColor = (1,1,-1)
Zon_lineColor = (1,1,-1)
Planeet_counter = 0
Maan_counter = 0

## Positions in the stationary solar system
Planeet_position = (0.705, 0.236)
Maan_position = (Planeet_position[0]+0.002, Planeet_position[1]+0.12)

## Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
#Planeet_position_x = numpy.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
#             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
#             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
#            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
#            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
#            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
#Planeet_position_y = ([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
#             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
#             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
#            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
#            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
#             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])
#Maan_position_x = ([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
#            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.])
#Maan_position_y = ([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
#            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])

#trials = numpy.column_stack([Planeet_position_x, Planeet_position_y, Maan_position_x, Maan_position_y])

# part 3: prepare graphic elements
win = visual.Window([600, 600], units = "norm", color = "black")
Zon = visual.Circle(win, lineColor = Zon_lineColor, fillColor = Zon_fillColor, units = "norm", pos = (0,0), radius = Zon_radius_start)
Planeet = visual.Circle(win, lineColor = "blue", fillColor = "blue", units = "norm", pos = Planeet_position, radius = 0.035*2)
Maan = visual.Circle(win, lineColor = "white", fillColor = "white", units = "norm",  pos = Maan_position, radius = 0.01*2)

# part 4: Zon laten groeien en veranderen in een rode reus
for trial in range(n_trials):
    Zon.radius = Zon_radius_start
    Zon.lineColor = Zon_lineColor
    Zon.fillColor = Zon_fillColor
    #geel_rood = -
    crash = False
    #Planeet.pos = Planeet_position
    #Maan.pos = Maan_position
    
    ## ESther: deze structuur met de for-loop en de while-loop is niet meteen wat we in gedachten hadden
    while crash == False or Zon.radius < Zon_radius_max:
        Zon.radius = Zon.radius + Zon_radius_start*0.03 
        #Zon.lineColor = (-1, , -1)
        #Zon.fillColor = (-1, , -1)
        Zon.draw()
        Planeet.draw()
        Maan.draw()
        win.flip()
        time.sleep(0.05)
        
        
    ## Esther: deze vergelijking is niet de oplossing van de oefening
    if zon.radius == Planeet.pos[0] or zon.radius == Maan.pos[1]:
            crash = True
            Planeet_counter +=1
            Maan_counter +=1
            win.flip()
            sleep(1)

#for i in range(trials.shape[0]):
    #Planeet.pos = trials[i, 0]
    #Maan.pos = trials[i,1]

# part 5: print results on screen and finish

if Planeet_counter > 0 and Maan_counter > 0:
    feedback = "De planeet en de maan hebben tegelijk de rode reus geraakt"
elif Planeet_counter > 0 and Maan_counter == 0:
    feedback = "De planeet heeft de rode reus geraakt"
elif Planeet_counter == 0 and Maan_counter > 0:
    feedback = "De maan heeft de rode reus geraakt"
else:
    feedback = "Geen enkele van de hemellichamen heeft de rode reus geraakt"

feedback_text = visual.TextStim(win, text = feedback)
feedback_text.draw()
win.flip()
time.sleep(1)
win.close()