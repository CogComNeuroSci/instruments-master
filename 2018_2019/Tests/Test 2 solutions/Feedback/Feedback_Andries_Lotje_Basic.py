#test 2
#import modules
import numpy, time
from psychopy import visual

#positie maan en planeet+size
#pos_planeet: 0.705-2, 0.236-12)
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!
pos_maan= (0.703,0.224)
pos_planeet= (0.705,0.236)
#radius_zon=0.15
#radius_maan=0.07
#radius_planeet=0.02

#window
win= visual.Window([600,600],color = (-1,-1,-1), units = "norm")
zon= visual.Circle(win,lineColor="yellow", fillColor="yellow",radius=0.15)
## Esther: de radius van de maan en de planeet zijn gewisseld!
maan= visual.Circle(win,lineColor="white", fillColor="white",pos=pos_maan, radius=0.07)
planeet= visual.Circle(win,lineColor="blue", fillColor="blue", pos=pos_planeet, radius=0.02)

#zon laten groeien
#for loop waar je 60x doorgaat (aantal vanop opgave) en telkens de radius te vergroten
#het werkt niet omdat hij telkens die 0.15 opnieuw neemt en gewoon terug + 0.04doet maar ik vind niet hoe ik het moet aanpassen dat hij die waarde telkens opnieuw gebruikt

radius_begin=0.15
for radius_zon in range(60):
    ## Esther: telkens je door de loop gaat tel je terug 0.04 op bij de beginwaarde van de zon en daardoor blijft de radius van de zon altijd gelijk
    radius_zon =radius_begin+0.04
    zon= visual.Circle(win,lineColor="yellow", fillColor="yellow",radius=radius_zon)
    zon.draw()

#botsing
#lukte nog niet omdat ik derest nog niet gevonden had

#roteren hemellichamen
#geen idee hoe ik hieraan moest beginnen..
#proberen opzoeken maar zonder succes
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


#stimuli op scherm laten verschijnen

maan.draw()
planeet.draw()

win.flip()
time.sleep(1)
win.close()