# modules importeren
from psychopy import visual
import time
import numpy

# window aanmaken
win = visual.Window([600, 600], color = (-1, -1, -1), units = "norm")

# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
planetx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
planety = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
moonx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
moony = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]

# aanmaken van de stimuli
zon = visual.Circle (win, radius = 0.075*2, pos = (0,0), fillColor = (0,0,-1), lineColor = (0, 0, -1))
planeet = visual.Circle (win, radius = 0.035*2, pos = (0.705, 0.236), fillColor = (-1, -1, 1), lineColor = (-1, -1, 1))
## de coördinaten van de maan zijn afhankelijk van de positie waar de maan zich bevindt. De positie van de maan is dan (0,0) en hierop moeten de coördinaten van de maan afgesteld zijn.
maan = visual.Circle (win, radius = 0.02*2, pos = (0.707, 0.248), fillColor = (1, 1, 1), lineColor = (1, 1, 1))

# zon laten groeien
radius1 = 0.075
## om de zon te laten groeien met 103% van de vorige grootte, moet je de huidige radius maal 1.03 doen. Dit moet ke dan optellen bij de huidige radius
adjustment = radius1*1.03

# kleur van de zon veranderen: van (0, -0.1, -1) naar (1, 0, 0)
##a = ((radius1/50)-1) ## rood van 0 naar 1 laten gaan
##b = -((radius1/50)-1) ## groen van 0 naar -1 laten gaan

# counter maken
count = 0



# zon laten groeien en stoppen als de radius 1 is
while radius1 < 1: ## als de radius groter is dan 1, dan past de zon niet meer op het scherm en stopt de loop
    radius1 = radius1 + adjustment
    zon2 = visual.Circle (win, radius = radius1, pos = (0,0), fillColor = (0,0,-1), lineColor = (0, 0, -1))
    ## in de while-loop moet je ook een planeet en een maan aanmaken, bij pos van planeet moet je dan de (planetx, planety) plaatsen.
    ## in de while-loop moet je ook een planeet en een maan aanmaken, bij pos van maan moet je dan de (moonx, moony) plaatsen. Dit is afhankelijk van de positie de maan planeet.
    count=+ 1
    zon2.draw()
    planeet.draw ()
    maan.draw ()
    win.flip ()
    time.sleep (0.1)
    count=+ 1
    print (count)
    
    # botsing maken, deze loop er wel zorgt voor dat na elke vergroting van de radius de tekst verschijnt
    if zon2.overlaps(maan):
        text1 = visual.TextStim (win, text = "De maan heeft de rode reus geraakt")
        text1.draw ()
        time.sleep (1)
    if zon2.overlaps(planeet):
        text2 = visual.TextStim (win, text = "De planeet heeft de rode reus geraakt")
        text2.draw ()
        time.sleep (1)
    if zon2.overlaps (maan) and zon2.overlaps (planeet):
        text3 = visual.TextStim (win, text = "De planeet en de maan hebben tegelijk de zon geraakt")
        text3.draw ()
        time.sleep (1)
    else:
        text4 = visual.TextStim (win, text = "Geen enkel van de hemellichamen heeft de rode reus geraakt")
        text4.draw ()
        time.sleep (1)

win.close ()