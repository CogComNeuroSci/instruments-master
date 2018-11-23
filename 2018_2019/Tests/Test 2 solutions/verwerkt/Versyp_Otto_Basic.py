#importeren modules
from psychopy import visual
import time,numpy

#window maken
win=visual.Window(size=[600,600],units="norm",color="black")

#coordinaten
# stationary solar sytem: celectial bodies positions
Planetxstart = 0.705
Planetystart = 0.236
Moonxstart = 0.002   # this coordinate is relative to the position of the planet!
Moonystart = 0.12    # this coordinate is relative to the position of the planet!
Maanxstart=Planetxstart+Moonxstart
Maanystart=Planetystart+Moonystart
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

#botsingtellers
botsingplaneet=0
botsingmaan=0

#startradius zon
startradius=0.15
radius=startradius

#stimuli maken maar nog niet tekenen
zon=visual.Circle(win,radius=startradius,color=[1,1,-1])
planeet=visual.Circle(win,radius=0.07,color="blue",pos=(Planetxstart,Planetystart))
maan=visual.Circle(win,radius=0.02,color="white",pos=(Maanxstart,Maanystart))
botsingtekst=visual.TextStim(win, text="ok")

#teken startopstelling sterrenstelsel -> mochten we laten vallen
#planeet.draw()
#maan.draw()
#zon.draw()
#win.flip()
#time.sleep(1)


while botsingmaan==0 and botsingplaneet==0:
    for i in range(60):
        #veranderen radius en zorgen dat het stopt wanneer de radius groter is dan 1
        radius=radius+radius*0.03
        if radius > 1:
            break
        zon.radius=radius
        #positie van planeet bepalen door trial en lijst met coordinaten, positie maan is relatief tov planeet dus deze twee optellen
        planeet.pos=(Planetx[i],Planety[i])
        maan.pos=(Planetx[i]+Moonx[i],Planety[i]+Moony[i])
        #veranderen kleur, bereikt -1 na 60 trials
        t=1-(1/30)*i
        if t < -1:
            t=-1
        zon.color=[1,t,-1]
        #tekenen stimuli
        planeet.draw()
        maan.draw()
        zon.draw()
        win.flip()
        #bepalen wat de zon heeft geraakt en eindigen loop
        if zon.overlaps(planeet):
            botsingplaneet=botsingplaneet+1
            break
        elif zon.overlaps(maan):
            botsingmaan=botsingmaan+1
            break
        time.sleep(0.05)

#tekst laten verschijnen op basis van wat de zon heeft geraakt
if botsingmaan==0 and botsingplaneet==1:
    botsingtekst.text="De planeet heeft de rode reus geraakt."
elif botsingmaan==1 and botsingplaneet==0:
    botsingtekst.text="De maan heeft de rode reus geraakt."
elif botsingmaan==1 and botsingplaneet==1:
    botsingtekst.text="De planeet en de maan hebben tegelijk de rode reus geraakt."

botsingtekst.draw()
win.flip()
time.sleep(1)
win.close()


