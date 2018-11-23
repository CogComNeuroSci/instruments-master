#import modules
from psychopy import visual
import time, numpy

#startvormen
## Esther: Al eens eerste error want norm stond niet tussen quotes
win= visual.Window([600, 600], color= (-1,-1,-1), units= "norm")
sun= visual.Circle(win, radius= 0.15, edges=32, color= (1, 1,-1))
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
## Esther: de coordinaten kloppen ook niet met wat we precies gevraagd hebben
planet= visual.Circle(win, radius=0.07, edges= 32, color="blue", pos=(0.705, 0.236))
moon= visual.Circle(win, radius=0.02, edges=32, color="white", pos=(0.707, 0.248))

#presenteren stationair zonnestelsel
sun.draw()
planet.draw()
moon.draw()
win.flip()
time.sleep(1)
win.close()

#coördinaten planeet
planetx = numpy.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
            
planety = numpy.array([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])

planetxy= numpy.column_stack([planetx, planety])

             
#coördinaten maan
moonx = numpy.array([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.])
            
moony = numpy.array([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])
            
moonxy =numpy.column_stack([moonx, moony])
#ik vind niet hoe ik de positie relatief moet zetten tov het middelpunt van de planet

## Esther: in jouw oplossing kon je hier de arrays bij elkaar optellen ;)

#er wordt verwezen naar de twee kolommen in de array van de planeet om zo de positie te bepalen van de planeet op elke seconde
## Esther: hier was een while loop van 60 iteraties nodig
while x and y <6:
    ## Esther: de indexen die je hieronder tracht te gebruiken houden geen steek, zie je?
    planet.pos=planetxy[planetx, planety]
    planet.draw()
    win.flip()
    time.sleep(1)
    win.close()
    x=x+1
    y=y+1
#growth and color of sun
    sun.Colorspace="rgb"
    growth=0.1
    while growth < 1: #or botsing=True:
   
    
        #de zon zou moeten groeien met telkens 103% van de vorige grootte
        #heb al super veel manieren geprobeerd, maar wil nog steeds niet werken...
        ## Esther: die is niet exact de berekening die we gevraagd hadden: sunradius = sunradius*1.03
        growth=growth+(growth/1.03)
   
        yellowred= -(((growth)/10)-1)
        ## Esther: wat is het nut van deze correctie?
        if yellowred<-1:
            bluegreen=-1
    
        #de middelste waarde van de rgb code moet van 1 naar -1 gaan om van geel naar rood te kunnen veranderen
        ## Esther: je stelt de radius hier gelijk aan een string, dat is vreemd!
        sun.radius="growth"
        sun.color= (1, yellowred, -1)
    
        
        

#het antwoord of er al dan niet een botsing geweest was, moet helemaal op het einde
#dit met een if-statement
if planetxy==1 and moonxy==1:
    feedback= "De planeet en de maan hebben tegelijk de rode reus geraakt"
## Esther: hieronder ontbrak er een = waardoor je een syntax error kreeg
elif planetxy==1 and moonxy==0:
    feedback= "De planeet heeft de rode reus geraakt"
elif planetxy==0 and moonxy==1:
    feedback= "De maan heeft de rode reus geraakt"
else:
    feedback="Geen enkele van de hemellichamen heeft de rode reus geraakt"

feedbacktext= visual.TextStim(win, text= feedback)
feedbacktext.draw()
win.flip()
time.sleep(1)
win.close()
    
#sorry voor deze vreselijke boel!
    
