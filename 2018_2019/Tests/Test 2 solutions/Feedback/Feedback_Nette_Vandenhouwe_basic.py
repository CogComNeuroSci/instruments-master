#importeer de nodige modules:
import numpy, time
from psychopy import visual

#maak het window aan:
win = visual.Window(size=[600,600],color=[-1,-1,-1],units="norm")

#Initialiserende variabelen:
##stationary solar sytem: celectial bodies positions
## Esther: let op, op deze manier zijn de radii van je hemellichamen de helft te klein
startRadiusZon=0.075
startWaardeB=1
Planeetx = 0.705
Planeety = 0.236
Maanx = 0.002   ##this coordinate is relative to the position of the planet!
Maany = 0.12    ##this coordinate is relative to the position of the planet!

##we bereken de coördinaten van de maan tov van de planeet:
Maanx=Planeetx+Maanx
Maany=Planeety+Maany


#maak een array aan om de radii van de zon in op te slaan en een array om de veranderende waarde van B in de rgb-code in op te slaan:
#daarna de 60 sizes generen en in de array opslaan en ook de 60 verschillende B-waarden generen en in de array opslaan
sizesZon=numpy.array([startRadiusZon])
waardeB=numpy.array([startWaardeB])

for i in range(59):
    newsize=sizesZon[i]*1.03
    sizesZon=numpy.vstack([sizesZon,newsize])

    geel_rood= -((i/30)-1)
    waardeB=numpy.vstack([waardeB,geel_rood])

## Esther: het was niet echt nodig om dit in één array te steken, maar het staat je vrij!
##we voegen deze 2 array's samen:
ArrayZon=numpy.column_stack([sizesZon,waardeB])

print(ArrayZon)


#de 60 coördinaten van de planeet en maan:
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

#de 4 lijsten samenbrengen in een array met 4 kolommen:
ArrayPlaneetMaan=numpy.column_stack([Planetx,Planety,Moonx,Moony])
print(ArrayPlaneetMaan)

##we veranderen de coördinaten van de maan zodat ze tov van de planeet gedefinieerd zijn:
for i in range(len(ArrayPlaneetMaan)):
    ArrayPlaneetMaan[i,2]=ArrayPlaneetMaan[i,0] + ArrayPlaneetMaan[i,2]
    ArrayPlaneetMaan[i,3]=ArrayPlaneetMaan[i,1] + ArrayPlaneetMaan[i,3]
## Esther: aangezien je met een array werkt, hoed je eigenlijk niet eens een loop te gebruiken ;)
## Esther: gewoon de i weglaten zou voldoende moeten zijn

#de array van de zon en de array van de planeet en de maan samen brengen:
ArrayZonPlaneetMaan=numpy.column_stack([ArrayZon,ArrayPlaneetMaan])

print(ArrayZonPlaneetMaan)


#aanmaken van de zon, de planeet, de maan en de feedbacktekst:
zon = visual.Circle(win, radius = startRadiusZon, pos = (0,0), lineColor=[1,1,-1], fillColor = [1,1,-1],edges=128)
planeet = visual.Circle(win, radius = 0.035, pos = (Planeetx,Planeety),lineColor=[-1,-1,1], fillColor = [-1,-1,1],edges=128)
maan = visual.Circle(win, radius = 0.01, pos = (Maanx,Maany), lineColor=[1,1,1], fillColor = [1,1,1],edges=128)

## Esther: het is nog beter om 1 stimulus aan te maken en dan gewoon de text te updaten
TekstPLaneet=visual.TextStim(win,text="De planeet heeft de rode reus geraakt.",color=[1,1,1])
TekstMaan=visual.TextStim(win,text="De maan heeft de rode reus geraakt.",color=[1,1,1])
TekstPLaneetMann=visual.TextStim(win,text="De planeet en de maan hebben de rode reus  tegelijk geraakt.",color=[1,1,1])


#Het stationair zonnestelsel voor 1 seconde laten zien:
zon.draw()
planeet.draw()
maan.draw()
win.flip()
time.sleep(1)


#de zon gradueel laten groeien tot een rode reus terwijl de maan en de planeet er rond draaien:
for i in range(len(ArrayZonPlaneetMaan)):
    ##het groeien van de zon + de kleurverandering:
    zon.radius=ArrayZonPlaneetMaan[i,0]
    zon.lineColor=[1,ArrayZonPlaneetMaan[i,1],-1]
    zon.fillColor=[1,ArrayZonPlaneetMaan[i,1],-1]
    
    ##de planeet draait 1 keer rond de zon:
    planeet.pos=(ArrayZonPlaneetMaan[i,2],ArrayZonPlaneetMaan[i,3])
    
    ##de maan draait 6 keer rond de zon:
    maan.pos=(ArrayZonPlaneetMaan[i,4],ArrayZonPlaneetMaan[i,5])
        
    ##alle stimuli tekenen en het window flippen:
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    
#Ik had geen tijd meer om een oplossing te vinden voor het detecteren van de botsing, ik heb wel al de teksten aangemaakt die ik zou laten verschijnen op het scherm.
#Ik had het idee om te werken met overlap.ShapeStim maar dit was niet mogelijk aangezien ik mijn cirkels hier niet mee heb gemaakt.
#Ik had gewerkt met 3 if-statements en dan 'if ShapeStim.overlap(planeet) == true: print(TekstMaan)'
#   if overlap(planeet)==True:
#        TekstPLaneet.draw()
#        win.flip()
#        time.sleep(1)

#Het window sluiten:
win.close()
    