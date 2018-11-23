from psychopy import visual, event
import time
import numpy 
from numpy import random

#window aanmaken
win=visual.Window(size=[800,800], color='black')

## Esther: let op, de cirkels zijn half zo groot als ze zouden moeten zijn!
#zon
zon=visual.Circle(win, pos=(0,0), radius=0.075, fillColor=(1,1,-1),lineColor=(1,1,-1), units='norm')
straal=0.075

#planeet
planeetx = 0.705
planeety = 0.236
planeet=visual.Circle(win, radius=0.035, pos=(planeetx,planeety), fillColor='blue',lineColor='blue')


#maan
maanx=0.002
maany=0.12
maan=visual.Circle(win, radius=0.01, pos=((planeetx+maanx),(planeety+maany)), fillColor='white', lineColor='white')

#coordinaten van beiden:
planeetx = [0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661, 0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715, 0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035, -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681, -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699, -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
planeety = [0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281, 0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224, -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5, -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263, -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244, 0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
maanx = [0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0., 0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0., 0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0., 0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0., 0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,  0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
maany = [0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12, 0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12, 0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12, 0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12, 0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12, 0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]


matrix=numpy.column_stack([planeetx, planeety, maanx, maany])


botsing=False


## Esther: deze combinatie van while loop en for-loop is niet wat we op het oog hadden.
while zon.radius < 1 and botsing==False:
    for i in range(len(matrix)):
        zon.radius = zon.radius+(zon.radius*0.03) #omdat de volgende 103% van de vorige moet zijn
        
        #hier wou ik zon.radius maal 2 doen, omdat hij dan mooi van 1 naar -1 zou gaan. Maar dit ging niet, het werd helemaal op het einddus met wat trial and error heb
        ## Esther: je hoefde hier niet gebruik te maken van de radius van de zon om de kleur te bepalen. Dat is mogelijk, maar niet verplicht in deze opdracht
        zon.fillColor=(1,1-(zon.radius*1.90),-1)
        zon.lineColor=(1,1-(zon.radius*1.90),-1)
        
        planeet.pos=(matrix[i,0],matrix[i,1])
        maan.pos=(matrix[i,0]+matrix[i,2],matrix[i,1]+matrix[i,3])
    
        #nu maak ik arrays aan van de minimum en maximum waarden tot waar de zon mag komen.
        planeet.pos[0] = numpy.maximum(planeet.pos[0],-1)
        planeet.pos[1] = numpy.maximum(planeet.pos[1],-1)
        planeet.pos[0] = numpy.minimum(planeet.pos[0],+1)
        planeet.pos[1] = numpy.minimum(planeet.pos[1],+1)
    
        #nu hetzelfde voor de maan:
    
        maan.pos[0] = numpy.maximum(maan.pos[0],-1)
        maan.pos[1] = numpy.maximum(maan.pos[1],-1)
        maan.pos[0] = numpy.minimum(maan.pos[0],+1)
        maan.pos[1] = numpy.minimum(maan.pos[1],+1)
        zon.draw()
        planeet.draw()
        maan.draw()
        win.flip()
        time.sleep(0.1)
    
        #nu is het idee dat als de absolute waarde van de positie van de planeet plots kleiner wordt dan de straal van de zon, ik een botsing heb.  
        ## ESther: deze approach dekt niet volledig het idee dat welke vorm van overlap al gedetecteerd wordt als een botsing
        ## ESther: de volgorde van de if...elif statements sluit nu de laatste optie uit.
        if numpy.absolute(planeet.pos[0])<zon.radius and numpy.absolute(planeet.pos[1])<zon.radius:
            botsing=True
            botsingplaneettekst=visual.TextStim(win, text="De planeet heeft de rode reus geraakt")
            botsingplaneettekst.draw()
            win.flip()
            time.sleep(1)
        #nu opnieuw zelfde voor maan:
        elif numpy.absolute(maan.pos[0])<zon.radius and numpy.absolute(maan.pos[1])<zon.radius:
            botsing=True
            botsingmaantekst=visual.TextStim(win, text="De maan heeft de rode reus geraakt")
            botsingmaantekst.draw()
            win.flip()
            time.sleep(1)
        #nu voor allebei:
        elif numpy.absolute(planeet.pos[0])<zon.radius and numpy.absolute(planeet.pos[1])<zon.radius and numpy.absolute(maan.pos[0])<zon.radius and numpy.absolute(maan.pos[1])<zon.radius:
            botsing=True
            botsingallebei=visual.TextStim(win, text="De planeet en de maan hebben tegelijk de rode reus geraakt")
            botsingallebei.draw()
            win.flip()
            time.sleep(1)




win.close()