#Project: Test 2 (basisversie)
#Date: 21/11/18
#Author: Geysen Steven (01611639)

#Modules

from psychopy import visual, monitors, core, event
import time, numpy as np
from time import sleep


#Screen and safety buttons

mon = monitors.Monitor('my laptop screen')
mon.setDistance(40)
mon.setWidth (38)
mon.setSizePix((1536,864))

win = visual.Window(size = (600,600) , color = 'black', units = 'norm', monitor = mon)

for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)
    ##in case something somewhere goes wrong


#Components

counter = 0
## Esther: het is nog beter om slechts 1 stimulus aan te maken en daar dan de text van te updaten
earth_text = visual.TextStim(win, text = 'De planeet heeft de rode reus geraakt')
moon_text = visual.TextStim(win, text = 'De maan heeft de rode reus geraakt')
both_text = visual.TextStim(win, text = 'De planeet en de maan hebben tegelijk de rode reus geraakt')
none_text = visual.TextStim(win, text = 'Geen enkele van de hemellichamen heeft de rode reus geraakt')


##Positions

earth_pos_x = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ]
earth_pos_y = [    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ]
moon_pos_x = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
moon_pos_y = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]


#Planets and their properties

##Sun
## Esther: pas op, je radii zijn de helft te klein!
sun = visual.Circle(win, radius = (0.75), pos = (0,0),lineColor = 'Yellow', fillColor = (-1,1,1))
sun_color = [1,1-((counter/30)),-1]
sun_sizes = np.array([0.075])


##Earth
earth = visual.Circle(win, radius = (0.035), pos = (0.705,0.236), lineColor = 'blue', fillColor = 'blue')


##Moon
moon = visual.Circle(win, radius = (0.01), pos = (0.70641,0.305), lineColor = 'white', fillColor = 'white')



while sun_sizes < 2:

##Uitzetten van sun

    for i in sun_sizes:
        ## Esther: het is nog beter om de stimuli aan te maken voor de loop en hier dan enkel de kleur, positie en radius te updaten
        sun = visual.Circle(win, radius = (i),lineColor = sun_color, fillColor = sun_color)
        
        ## Esther: hm, je heht hier wel iets heel freaky gedaan met het gebruik van sun_sizes in de for-loop.
        ## Esther: het houdt eigenlijk geen steek, maar gelukkig werkt het wel
        sun_sizes= sun_sizes+(sun_sizes*0.03)    ##van klein naar groot
        sun_color = [1,1-((counter/30)),-1]     ##van geel naar rood
        if 1-((counter/30))< -1:                ##dat het zeker rood blijft
            sun_color = 'red'


        earth = visual.Circle(win, radius = (0.035), pos = (earth_pos_x[counter+1], earth_pos_y[counter+1]), lineColor = 'blue', fillColor = 'blue')
        ## ESther: je had enkel de positie van de maan moeten optellen bij de positie van de zon, niets ingewikkelders
        moon = visual.Circle(win, radius = (0.01), pos = ((earth_pos_x[counter+1]+earth_pos_x[counter+1]*moon_pos_x[counter+1]), (earth_pos_y[counter+1]+earth_pos_y[counter+1]*moon_pos_y[counter+1])), lineColor = 'white', fillColor = 'white')

        sun.draw()
        earth.draw()
        moon.draw()
        win.flip()

        if counter == 1:                        ##om het 1 seconde te laten staan in het begin
            time.sleep(1)
        else:                                   ##om te sneller te laten groeien
            time.sleep(0.2)

##Overlaps

    if sun.overlaps(earth):                     ##als aarde eerst geraakt wordt
        earth_text.draw()
        win.flip()
        time.sleep(1)
        win.close()

    elif sun.overlaps (moon):                   ##als maan eerst geraakt wordt
        moon_text.draw()
        win.flip()
        time.sleep(1)
        win.close()

    ## Esther: deze had helemaal aan het begin van de if...elif moeten staan, anders wordt deze nooit uitgevoerd
    elif sun.overlaps (earth and moon):         ##als iedereen geraakt wordt
        both_text.draw()
        win.flip()
        time.sleep(1)
        win.close ()

    elif counter > 50 and sun.overlaps (earth or moon) == False:    ##als 2.5s nog niemand geraakt is
        none_text.draw()
        win.flip()
        time.sleep(1)
        win.close ()

    counter += 1

