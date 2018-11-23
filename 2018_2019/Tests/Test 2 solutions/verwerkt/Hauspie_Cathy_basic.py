#Importeer modules
import numpy, time
from psychopy import visual

#Vaste elementen
aantalstappen = 60
startradius_sun = 0.15
radius_planet = 0.07
radius_moon = 0.02
planeet_botsing = numpy.array([])
maan_botsing= numpy.array([])

##Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
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

#Grafische elementen
win = visual.Window(size = [600,600], color = 'black', units = "norm")
sun = visual.Circle(win, color = [1,1,-1], radius = startradius_sun)
sun.colorSpace = "rgb"
planet = visual.Circle(win, color = 'blue', radius = radius_planet)
moon = visual.Circle(win, color = 'white', radius = radius_moon)
Botsing = visual.TextStim(win, text = 'test')

#Laat de zon groeien
for i in range(aantalstappen):
    startradius_sun = startradius_sun*1.03 ##*1.03 want elke stap is 103% van de vorige grootte
    sun.radius = startradius_sun
    
    ##Laat de kleur van de zon veranderen
    green = -((startradius_sun * 2.5)-1)
    if green < -1:
        green = -1
    sun.color = ([1, green, -1])
    
    ##Planeet laten ronddraaien
    planet.pos = (Planetx[i], Planety[i])
    
    ##Maan laten ronddraaien
    moon.pos = (Planetx[i] + Moonx[i], Planety[i] + Moony[i]) ##want de positie van de maan is relatief t.o.v. die van de planeet
    
    ##toon elementen op scherm
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    time.sleep(0.1)
    
    ##Controleer voor botsing
    ##botsing met beide
    if planet.overlaps(sun) and moon.overlaps(sun):
        planeet_botsing = numpy.append(planeet_botsing, 1)
        maan_botsing = numpy.append(maan_botsing, 1)
        Botsing.text = "De planeet en de maan hebben tegelijk de rode neus geraakt"
        Botsing.draw()
        win.flip()
        time.sleep(1)
        break
    ##botsing met planeet
    elif planet.overlaps(sun):
        planeet_botsing = numpy.append(planeet_botsing, 1)
        Botsing.text = "De planeet heeft de rode reus geraakt"
        Botsing.draw()
        win.flip()
        time.sleep(1)
        break
    ##botsing met maan
    elif moon.overlaps(sun):
        maan_botsing = numpy.append(maan_botsing, 1)
        Botsing.text = "De maan heeft de rode reus geraakt"
        Botsing.draw()
        win.flip()
        time.sleep(1)
        break
    else:
        continue

##Indien er geen botsing was
if maan_botsing.size == 0 and planeet_botsing.size == 0:
    Botsing.text = "Geen enkele van de hemellichamen heeft de rode reus geraakt"
Botsing.draw()
win.flip()
time.sleep(1)

#Window sluiten
win.close()