#test2

#importeer eerst modules 
import numpy, time
from psychopy import visual


# stationary solar sytem: celectial bodies positions
ZonRadius= 0.15 
GZon= 1 #enkel deze RGB waarde moet van 1 naar -1


#counts per botsing om feedback te geven achteraf
countboth= 0
countmaan= 0
countplaneet = 0


#Lijst met coordinaten om de hemellichamen te laten roteren
PlanetxList = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]PlanetyList = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]MoonxList = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]MoonyList = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

#window en startstimuli aanmaken
win = visual.Window(size=[600,600], units='norm',color='black')


for i in range(60):
    Planetx = PlanetxList[i]
    Planety = PlanetyList[i]
    Moonx = MoonxList[i]
    Moony = MoonyList[i]
    zon= visual.Circle(win, radius= ZonRadius, fillColor= (1,GZon,-1))
    planeet= visual.Circle(win, radius= 0.07, fillColor= (-1,-1,1),pos=(Planetx,Planety))
    maan= visual.Circle(win, radius= 0.02, fillColor=(1,1,1),pos=(Planetx + Moonx,Planety + Moony))
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    ZonRadius+= ZonRadius*0.03 #103 procent betekent 3 procent toevoegen
    GZon+= -0.03333333333333333 #-2 in stappen van 60 (dus -2/60)

    #overlap condities => break. if not => continue
    if zon.overlaps(planeet) and zon.overlaps(maan):
        countboth+= 1
        break
    elif zon.overlaps(planeet):
        countplaneet+= 1
        break
    elif zon.overlaps(maan):
        countmaan+=1
        break
    else:
        continue
#if statements om feedback te geven achteraf
if countboth == 1:
    feedback= visual.TextStim(win, text= 'De planeet en de maan hebben tegelijk de rode reus geraakt')
elif countplaneet == 1:
    feedback= visual.TextStim(win, text= 'De planeet heeft de rode reus geraakt')
elif countmaan == 1:
    feedback= visual.TextStim(win, text= 'De maan heeft de rode reus geraakt')
else:
    feedback= visual.TextStim(win, text= 'Geen enkele van de hemellichamen heeft de rode reus geraakt')
feedback.draw()
win.flip()
time.sleep(1)
win.close()

#om te controleren of feedback die gegeven werd juist is
print(countboth)
print(countmaan)
print(countplaneet)

