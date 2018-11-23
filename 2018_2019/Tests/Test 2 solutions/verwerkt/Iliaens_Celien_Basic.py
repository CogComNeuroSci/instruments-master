import numpy, time
from psychopy import visual, event
import math

# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
aardeX = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
aardeY = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
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
            0.12,   0.091,  0.019, -0.061, -0.113,-0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]


################
#Basiselementen#
################

#Window 
win= visual.Window(size = (600,600), fullscr = False, units = 'norm', color = 'black')

#initele radius zon 
rad_zon = 0.15

#tekst botsing
botsmaan = visual.TextStim(win, text = "De maan heeft de rode reus geraakt.")
botsaarde = visual.TextStim(win, text = "De planeet heeft de rode reus geraakt.")
botsallebei = visual.TextStim(win, text = "De planeet en de maan hebben tegelijk de rode reus geraakt.")

#initiele positie maan
iniposx= aardeX[0] + Moonx[0]
iniposy=aardeY[0] + Moony[0]

#initiele totale radius aarde + zon (AZ) en initiele totale radius maan + zon (MZ)
radAZ = 0.22
radMZ = 0.17

#Initiele afstand aarde-zon en initiele afstand maan-zon
afstAZ = math.sqrt(aardeX[0]**2 + aardeY[0]**2)
afstMZ = math.sqrt(iniposx**2 + iniposy**2)

##########
#Beweging#
##########


for i in range(60):
    a= 0
    
    while radAZ <= afstAZ and radMZ <= afstMZ and rad_zon < 1:
        
        #verandering grootte radius en kleur zon
        rad_zon = rad_zon*1.03
        color_zon = (1,1 - ((1/30)*a), -1)
        
        #verandering grootte totale radius aarde/maan + zon
        radAZ = 0.07 + rad_zon
        radMZ = 0.02 + rad_zon
        
        #Coordinaten maan 
        maanX = Moony[a] + aardeX[a]
        maanY = Moony[a] + aardeY[a]
        
        #Afstand aarde-zon update
        afstAZ = math.sqrt(aardeX[a]**2 + aardeY[a]**2)
        afstMZ = math.sqrt(maanY**2 + maanX**2)
        
        aarde = visual.Circle(win, radius = 0.07, pos = (aardeX[a], aardeY[a]), lineColor = 'blue', fillColor = 'blue')
        maan = visual.Circle(win, radius = 0.02, pos = (maanX, maanY), lineColor = 'white', fillColor = 'white')
        zon = visual.Circle(win, radius = rad_zon, pos = (0,0), lineColor = color_zon, fillColor = color_zon)
        
        zon.draw()
        aarde.draw()
        maan.draw()
        win.flip()
        time.sleep(0.1)
        
        a = a+1
        
        #Aarde botst met zon
        if radAZ >= afstAZ:
            botsaarde.draw()
            win.flip()
            time.sleep(1)
        
        #Maan botst met zon
        if radMZ >= afstMZ:
            botsmaan.draw()
            win.flip()
            time.sleep(1)
            
        #Aarde en maan botsen met zon
        if radMZ >= afstMZ and radAZ >= afstAZ:
            botsallebei.draw()
            win.flip()
            time.sleep()

