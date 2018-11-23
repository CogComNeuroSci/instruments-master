# Importeren modules
from psychopy import visual
import time

# Aanmaken window
win = visual.Window([600,600], units = "norm", color = (-1,-1,-1))

# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
planeetx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
planeety = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
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

# extra variabelen
startpositie_zon        = (0,0)
start_radius_zon        = 0.15
groeien_zon             = 0.03
aanpassen_geel_zon      = -0.0166 ## het tweede element in de rgb-code van de kleur van de zon wordt per stap verminderd met 0.02

startpositie_planeet    = (planeetx[0],planeety[0])
startpositie_maan       = (planeetx[0] + maanx[0],planeety[0] + maany[0])

botsing = False
stap_grootte= 1
stappen_nr = 0

# Aanmaken objecten
zon     = visual.Circle(win, fillColor = (1,1,0), lineColor = (1,1,0),radius = start_radius_zon, pos = startpositie_zon)
planeet = visual.Circle(win, fillColor = (0,0,1), lineColor = (0,0,1),radius = 0.07, pos = startpositie_planeet)
maan    = visual.Circle(win, fillColor = (1,1,1), lineColor = (1,1,1),radius = 0.02, pos = startpositie_maan)
eindboodschap           = visual.TextStim(win, text="hier komt de boodschap")

# Van gele zon tot rode reus
while botsing == False and stappen_nr < 60:
    ##zon laten groeien
    stappen_nr      += stap_grootte
    zon.radius      = zon.radius + zon.radius * groeien_zon
    ##zon roder laten worden
    zon.fillColor[1]   = zon.fillColor[1] + aanpassen_geel_zon
    zon.lineColor[1]   = zon.lineColor[1] + aanpassen_geel_zon
    ## rotatie planeet rond zon
    planeet.pos     = (planeetx[stappen_nr-1],planeety[stappen_nr-1])       ## stappen_nr-1 want de lijst begint bij element 0 en de stap is bij de eerste keer 1 in deze loop
    ## rotatie maan rond planeet
    maan.pos        = (planeetx[stappen_nr-1] + maanx[stappen_nr-1],planeety[stappen_nr-1] + maany[stappen_nr-1])
    ## beslissing botsing true of false, indien het TRUE wordt, betekent dit het einde van de loop
    if visual.helpers.polygonsOverlap(zon, planeet) or visual.helpers.polygonsOverlap(zon, maan):
        botsing = True
    ## iedere stap: tonen stimuli
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.2)

# Beslissing eindboodschap
if visual.helpers.polygonsOverlap(zon, planeet) == True and visual.helpers.polygonsOverlap(zon, maan) == True:
    eindboodschap.text = "De planeet en de maan hebben tegelijk de rode reus geraakt!"
elif visual.helpers.polygonsOverlap(zon, planeet) == False and visual.helpers.polygonsOverlap(zon, maan) == False:
    eindboodschap.text = "Geen enkele van de hemellichamen heeft de rode reus geraakt!"
elif visual.helpers.polygonsOverlap(zon, planeet) == False and visual.helpers.polygonsOverlap(zon, maan) == True:
        eindboodschap.text = "De maan heeft de rode reus geraakt!"
else:
        eindboodschap.text = "De planeet heeft de rode reus geraakt!"

# Tonen eindboodschap
eindboodschap.draw()
win.flip()
time.sleep(1)

# Sluiten scherm
win.close()