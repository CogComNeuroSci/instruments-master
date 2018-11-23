#De nodige modules importeren
from psychopy import visual
import time
import numpy

#Het window maken
win=visual.Window(size=(600,600), color= 'black', units = 'norm')

################################
##Het stationair zonnestelsel ##
################################

# De constante variabelen initializeren
##stationary solar sytem: celectial bodies positions
planeetx = 0.705
planeety = 0.236
maanx = 0.002   # this coordinate is relative to the position of the planet!
maany = 0.12    # this coordinate is relative to the position of the planet!


#grafische elementen initialiseren
zon = visual.Circle(win, lineColor= "yellow", fillColor = "yellow", radius=0.15)
planeet = visual.Circle(win, lineColor = "blue", fillColor = "blue", radius=0.07, pos=(planeetx, planeety))
##coördinaten planeet bijtellen want relatief ten opzichte van de planeet kijken
maan = visual.Circle(win, lineColor= "white", fillColor = "White", radius=0.02, pos=(maanx+planeetx, maany+planeety)) 

#grafische elementen tekenen
zon.draw()
planeet.draw()
maan.draw()


win.flip()
time.sleep(1)

###############################
##Van gele zon tot rode reus###
###############################


# De constante variabelen initializeren
##stationary solar sytem: celectial bodies positions
planeetx = 0.705
planeety = 0.236
maanx = 0.002   # this coordinate is relative to the position of the planet!
maany = 0.12    # this coordinate is relative to the position of the planet!

#De niet-constante variabelen initialiseren
##De groei van de zon: hierbij gaat elke nieuwe waarde gelijk zijn aan vorige waarde * 1.03. Het startpunt is 0.15, erna vermenigvuldigen we telkens met 1.03 tot de macht van het indexnummer i van de vermenigvuldigingen
##We nemen 60 stappen dus range(60)
## Geel is [0.5,0.5,0], rood is [1, 0, 0]. We maken een overgang tussen die twee. Startkleur is geel.
for i in range(60):
    if i >= 1:
        nieuwegroottezon = 0.15 * (1.03 ** i)
        ##we moeten er ook voor zorgen dat als de eerste waarde uit nieuwekleurzon groter dreigt te worden dan 1, dit wordt teruggebracht tot 1
        kleurbeveiliging = 0.5 + (0.1 * i)
        if kleurbeveiliging > 1:
#            nieuwekleurzon = [1, -(1- (0.1*i)), 0]
            nieuwekleurzon = [1, -i/100, -i/100]
        else:
            nieuwekleurzon = [kleurbeveiliging, 1-(0.1*i)-0.5, 0]
    else:
        nieuwegroottezon = 0.15
        nieuwekleurzon = [0.5, 0.5, 0]
    #grafische elementen initialiseren
    zon = visual.Circle(win, lineColor= nieuwekleurzon, fillColor = nieuwekleurzon, radius=nieuwegroottezon)
    planeet = visual.Circle(win, lineColor = "blue", fillColor = "blue", radius=0.07, pos=(planeetx, planeety))
    ##coördinaten planeet bijtellen want relatief ten opzichte van de planeet kijken
    maan = visual.Circle(win, lineColor= "white", fillColor = "White", radius=0.02, pos=(maanx+planeetx, maany+planeety)) 
    #grafische elementen tekenen
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(1)





###########
##Botsing## Dit zou bij in de loop moeten, aangezien er voor elke i opnieuw gekeken wordt wat al dan niet overlapt. Dit draait echter niet dus daarom heb ik hem in comment gezet. Er zal dan de bijbehorende boodschap geprint moeten worden, waarbij er maar één boodschap mogelijk is.
###########

#
#if zon.overlaps(planeet) and zon.overlaps(maan):
#    boodschap.text= "De planeet en de maan hebben tegelijk de rode reus geraakt"
#elif zon.overlaps(planeet):
#    boodschap.text="De planeet heeft de rode reus geraakt"
#elif zon.overlaps(maan):
#    boodschap.text = "De maan heeft de rode reus geraakt"
#else:
#    boodschap.text = "Geen enkele van de hemellichamen heeft de rode reus geraakt"
##Boodschap voor de botsing
#boodschap = visual.TextStim(win, text = "boodschap.text", color = 'white')
#boodschap.draw()

win.close()

###########
##Rotatie met herhaling voorgaande delen
###########


#De nodige modules importeren
from psychopy import visual
import time
import numpy

#Het window maken
win=visual.Window(size=(600,600), color= 'black', units = 'norm')


# De constante variabelen initializeren
##stationary solar sytem: celectial bodies positions
planeetx = 0.705
planeety = 0.236
maanx = 0.002   # this coordinate is relative to the position of the planet!
maany = 0.12    # this coordinate is relative to the position of the planet!


#grafische elementen initialiseren
zon = visual.Circle(win, lineColor= "yellow", fillColor = "yellow", radius=0.15)
planeet = visual.Circle(win, lineColor = "blue", fillColor = "blue", radius=0.07, pos=(planeetx, planeety))
##coördinaten planeet bijtellen want relatief ten opzichte van de planeet kijken
maan = visual.Circle(win, lineColor= "white", fillColor = "White", radius=0.02, pos=(maanx+planeetx, maany+planeety)) 

#grafische elementen tekenen
zon.draw()
planeet.draw()
maan.draw()


win.flip()
time.sleep(1)




# De constante variabelen initializeren
##stationary solar sytem: celectial bodies positions
planeetx = 0.705
planeety = 0.236
maanx = 0.002   # this coordinate is relative to the position of the planet!
maany = 0.12    # this coordinate is relative to the position of the planet!

#De niet-constante variabelen initialiseren en tekenen

##Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
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
##De relatieven zijn relatief ten opzichte van de planeet
##Daarom dient er een niet-relatieve versie aangemaakt te worden, zowel voor x als voor y.
maanrelatiefx = [   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.]
maanrelatiefy = [   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12]
##Een lege lijst aanmaken
maanx = []
##Deze lege lijst als volgt invullen
for i in range(len(planeetx)):
    maanxlocatie = planeetx[i]+ maanrelatiefx[i]
    maanx.append(maanxlocatie)
print(maanx)

maany = []
for i in range(len(planeety)):
    maanylocatie = planeety[i]+ maanrelatiefy[i]
    maany.append(maanylocatie)
print(maany)

##Verder gebruiken we enkel planeetx, planeety, maanx en maany
## We maken arrays met de coördinaten (x,y) voor elke locatie. Dit is echter niet noodzakelijk
#planeetlocatie=numpy.column_stack((planeetx, planeety))
#maanlocatie=numpy.column_stack((maanx, maany))


##De groei van de zon: hierbij gaat elke nieuwe waarde gelijk zijn aan vorige waarde * 1.03. Het startpunt is 0.15, erna vermenigvuldigen we telkens met 1.03 tot de macht van het indexnummer i van de vermenigvuldigingen
##We nemen 60 stappen dus range(60)
## Geel is [0.5,0.5,0], rood is [1, 0, 0]. We maken een overgang tussen die twee. Startkleur is geel.
for i in range(60):
    if i >= 1:
        nieuwegroottezon = 0.15 * (1.03 ** i)
        ##we moeten er ook voor zorgen dat als de eerste waarde uit nieuwekleurzon groter dreigt te worden dan 1, dit wordt teruggebracht tot 1
        kleurbeveiliging = 0.5 + (0.1 * i)
        if kleurbeveiliging > 1:
            nieuwekleurzon = [1, -(1- (0.1*i)), 0]
        else:
            nieuwekleurzon = [kleurbeveiliging, 1-(0.1*i)-0.5, 0]
    else:
        nieuwegroottezon = 0.15
        nieuwekleurzon = [0.5, 0.5, 0]
    #grafische elementen initialiseren
    zon = visual.Circle(win, lineColor= nieuwekleurzon, fillColor = nieuwekleurzon, radius=nieuwegroottezon)
    planeet = visual.Circle(win, lineColor = "blue", fillColor = "blue", radius=0.07, pos=(planeetx, planeety))
    ##coördinaten planeet bijtellen want relatief ten opzichte van de planeet kijken
    maan = visual.Circle(win, lineColor= "white", fillColor = "White", radius=0.02, pos=(maanx, maany)) 
    #grafische elementen tekenen
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(1)

