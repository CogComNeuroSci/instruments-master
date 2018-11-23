#Importing the modules needed
from psychopy import visual
import time, numpy

#Constructing a window
win = visual.Window([600,600], color = "black", units = "norm")

#Initializing graphic elements: planet and moon and message 
## Esther: let op, de radius van de cirkels in de helft te klein!
planet = visual.Circle(win, radius = 0.035, pos = (0.705,0.236), color = "blue")
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
moon = visual.Circle(win, radius = 0.010, pos = (0.707, 0.356), color = "white")
message = visual.TextStim(win, text = "De planeet heeft de rode neus geraakt.", color = "white")



#Initizializing graphic elemeny: Growing sun and orbiting planet and moon
planetX = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,                       # Construct a for-loop to orbit the planet: for j in planetX --> pos(j,y)
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
planetY = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,                      # For k in planetY --> pos(j,k)
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]

## Esther: dit is niet wat we gevraagd hadden, maar goed dat je hier gewoon wat waarden hebt gemaakt zodat je toch vooruit kon met de loop!
sizes = [0.075, 0.100, 0.125, 0.150, 0.175, 0.200, 0.225, 0.250, 0.275, 0.300, 0.325, 0.350, 0.375, 0.400, 0.425, 0.450, 0.475, 0.5, 0.525, 0.550, 0.575, 0.6, 0.625, 0.650, 0.675, 0.7, 0.735]
for i in sizes:
    ## Esther: het is nog beter om de stimulus aan te maken voor de loop en hier dan enkel de radius te updaten
    sun = visual.Circle(win, radius = i, pos = (0,0), color = "yellow")
    planet.draw()
    moon.draw()
    sun.draw()
    win.flip()
    time.sleep(1)


#Initialize end message 
message.draw()
win.flip()
time.sleep(1)


