#import modules
import time, numpy
from psychopy import visual, event
from numpy import random

#Window
win = visual.Window(size = (600,600), color = (-1,-1,-1), units ="norm")


#coordinates
blauwx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,

             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,

             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,

            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,

            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,

            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]

blauwy = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,

             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,

             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,

            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,

            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,

             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]

maanx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,

            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,

            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,

            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,

            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,

            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]

maany = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,

            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,

            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,

            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,

            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,

            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

#initializing
blauw_x = 0.705
blauw_y = 0.236
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via rekenen met getallen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
maan_x = (blauw_x + 0.002)
maan_y = (blauw_y + 0.12)
startpositieblauw = (blauw_x, blauw_y)
startpositiemaan = (maan_x, maan_y)
tijd_stap = 0.1        #seconden
max_tijd = 6            # seconden
tijd_size = .03
start_radius_zon = 0.075*2

#graphs

zon = visual.Circle(win, radius = start_radius_zon, fillColor = "yellow", lineColor = "yellow", pos = (0,0))

planeet = visual.Circle(win, radius = 0.035*2, fillColor = "blue", lineColor = "blue", pos = startpositieblauw)

maan = visual.Circle(win, radius = 0.01*2, fillColor = "white", lineColor = "white", pos = startpositiemaan)

botsing = visual.TextStim(win, text = "test")

#radius_array = numpy.array([zon.radius])

#array_coordinaten = numpy.array([blauwx, blauwy, maanx, maany])

#coordinaten = numpy.column.stack([blauwx, blauwy, maanx, maany])

#planeet.pos = (blauwx, blauwy)

#op het scherm laten verschijnen
zon.draw()
planeet.draw() 
maan.draw()
win.flip()
time.sleep(1)


#zon laten groeien

    #extra variabelen:

tijd = 0
zon.radius = start_radius_zon

while tijd < max_tijd:
    tijd = tijd + tijd_stap
    zon.radius = zon.radius + zon.radius*tijd_size
    
    if zon.radius > 0.75:
        break
    

    
    #kleur wijziging van (1,-1,-1) naar (255,255, 0), niet gelukt
    ## Esther: dat was ook niet nodig, je mag binnen -1 en 1 blijven in psychopy ;)
    
    #radius_array = numpy.vstack([radius_array, zon.radius])
    
    #yellow_red = ((numpy.ndarray.round(zon.radius))-1)
    #if yellow_red < -1:
        #yellow_red = -1
    #if yellow_red > 1:
        #yellow_red = 1
    
    #zon.color = ([yellow_red, yellow_red, yellow_red], "rgb")
    
    #roteren:  ik wil de coordinaten uit mijn array halen en ze zo laten roteren, dit is echter ook niet gelukt
    ## Esther: een array was niet nodig gezien we hier geen gebruik hoeven te maken van de volledige geschiedenis van alle posities van de planeet en maan ;)
    #for i in range(coordinaten):
        #planeet.pos = (blauwx[i],blauwy[i])
        #planeet.draw()
        #win.flip()
        #time.sleep(0.1)
    
    #botsing
    
    
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    
    
    if "f" in event.getKeys():
        break




