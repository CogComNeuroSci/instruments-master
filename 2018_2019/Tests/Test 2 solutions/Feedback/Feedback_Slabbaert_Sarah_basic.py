#modules invoegen
from psychopy import visual
import time
import numpy

#window aanmaken
win= visual.Window([600,600], color= [-1,-1,-1], units= 'norm')

#startpositie van maan en planeet
startposition_planeetx = 0.705
startposition_planeety = 0.236
startposition_maanx = 0.002
startposition_maany = 0.12

count= 0

#diameter van de stimuli
##hooghte is 2 (van -1 tot 1) daar moet het percentage van genomen worden
radius_zon= (0.15*2)/2
radius_planeet= (0.07*2)/2
radius_maan= (0.02*2)/2

#startkleur van de zon
kleur_zon= [1,1,-1]

#visuals invoeren
## radium is straal dus diameter delen dor 2
##zon 
zon= visual.Circle(win, radius= radius_zon, color= kleur_zon)

##maan
maan= visual.Circle(win, radius= radius_maan, color= [1,1,1], pos= (startposition_maanx + startposition_planeetx, startposition_maany + startposition_planeety))

##planeet
planeet= visual.Circle(win, radius=radius_planeet , color= [-1,-1,1], pos= (startposition_planeetx, startposition_planeety))

#alles 1sec op scherm laten verschijnen
zon.draw()
planeet.draw()
maan.draw()

win.flip()
time.sleep(1)

#posities van de planeet en de maan 
##een array van de coordinaten maken
planeetx = numpy.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
planeety = numpy.array([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])
maanx = numpy.array([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.])
maany = numpy.array([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])

## ESther: het was natuurlijk de bedoeling dat het groeien van de zon en het roteren van de planeten tegelijkertijd gebeurden
while count<5:
    #zon in straal laten toenemen
    zon= visual.Circle(win, radius= radius_zon, color= kleur_zon)
    
    ##straal neemt toe met 103% van de vorige straal
    add= 1.03*radius_zon
    ##add moet bij de vorige straal gevoegd worden
    radius_zon= add+radius_zon
    print(radius_zon)
    count +=1
    
    #kleur aanpassen
    ##hier moet een forloop tussen
    count+=1
    c= -(1/50)-1
    if c<-1:
        c=-1
        zon.color=[1,c, -1]
    
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.5)


positie_array= numpy.vstack([planeetx, planeety, maanx, maany])

for i in range(positie_array.shape[1]):
    planeet= visual.Circle(win, radius=radius_planeet, color= [-1,-1,1], pos= (planeetx[i], planeety[i]))
    maan= visual.Circle(win, radius= radius_maan, color= [1,1,1], pos= (maanx[i] + planeetx[i], maany[i] + planeety[i]))
    
    print(planeet.pos)
    print(maan.pos)
    
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.2)

#if zon max grootte or planeet raakt zon of maan raakt zon
    #break
    

## Esther: je denkwijze is volledig correct!
#hier moet en while loop om de counter te laten toenemen
##if maan_counter=1 and planeet_counter=1:
##    tekst"De planeet en de maan hebben tegelijk de rode reus geraakt"
##elif maan_counter =1:
##    tekst= "De maan heeft de rode reus geraakt"
##elif planeet_counter = 1:
##    tekst= "De planeet heeft de rode reus geraakt"
##else:
##    tekst=" Geen enkele van de hemellichamen heeft de rode reus geraakt"
##    
##feedback= visual.textStim(win, text= tekst)
##feedback.draw()
##win.flip()
##time.sleep(1)


win.close()