##code voor zonnestelsel

##modules laden
from psychopy import visual, event
import time, numpy


##display
win = visual.Window([600,600], color = "black", units = "norm")


##coordinaten 
# stationary solar sytem: celectial bodies positions

Planetx = 0.705

Planety = 0.236

Moonx = 0.002   # this coordinate is relative to the position of the planet!

Moony = 0.12    # this coordinate is relative to the position of the planet!



# coordinates

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
            
            
            

#initialisatie grafische elementen
zon = visual.Circle(win, fillColor = [1,1,0], radius = 0.075, pos = (0,0) , )
planeet = visual.Circle(win, fillColor = "blue", radius = 0.035, pos = (Planetx , Planety))
maan = visual.Circle(win, fillColor = "white", radius = 0.01, pos = (Planetx + Moonx , Planety +Moony))

#stationair zonnestelsel
zon.draw()
planeet.draw()
maan.draw()
win.flip()
time.sleep(1)

# normaal gezien while loop integreren : zon laten groeien en kleur veranderen in 60 stappen tenzij botsen 
# met planeet of maan

for i in range(60):
    zon.setfillColor[1] = (0.016, operation = "-")
    zon.radius = (1.03, operation = "*") 
    zon.draw()
    win.flip()
    
    
    #controleren of zon en hemellichamen ellkaar raken
    if sun.overlaps(planeet):
        break
    elif sun.overlaps(moon):
        break
        

#hemellichamen laten roteren

for i,j in range(len(Planetx), range(len(Planety):
    planeet.pos[i,j]
    
for i,j in range(len(Moonx), range(len(Moony):
    maan.pos[i,j]
    
 
#tekst botsing

if sun.overlaps(planeet) == True: 
    feedback = "De planeet heeft de rode reus geraakt"
elif sun.overlaps(maan) == True:
    feedback = "De maan heeft de rode reus geraakt"
feedback_tekst = visual.TextStim(win, text = feedback)
feedback_tekst.draw()
win.flip()

   
    
    
    
    
     
   
   
    
   
