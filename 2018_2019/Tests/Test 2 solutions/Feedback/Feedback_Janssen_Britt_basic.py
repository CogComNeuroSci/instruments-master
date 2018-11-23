## Esther: 1 witregeltje volstaat ;)


## Importeren van de modules

from psychopy import visual, monitors, core, event
import time, numpy, math



win = visual.Window(size = [600, 600] , color = 'black', units = 'norm')



## een toets om uit het experiment te geraken

for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)





## onvernderbare waarden:



## wilt vb de straal van de zon op 7.5% van de totale breedte/hoogte van het scherm
## van 600 pixels naar 45 pixels doe je gedeemd door 600 en dan maal 45
## er is een afstand van -1 tot 1, dus in totaal een afstand van 2

## Esther: voor de radius volstond 0.15, 0.07 en 0.02 ;)
## Esther: "norm" hoef je hier niet meer te definiëren, dat wordt overgenomen van de visual.Window
zon = visual.Circle(win, fillColor = 'yellow', pos = (0,0), lineColor = None, radius = ((2/600)*45), units = 'norm')
planeet = visual.Circle(win, fillColor = 'blue', pos = (0.705, 0.236), lineColor = None, radius = ((2/600)*21), units = 'norm')
maan = visual.Circle(win, fillColor = 'white', pos = (0.707,0.356), lineColor = None, radius = ((2/600)*6), units = 'norm')
## Esther: we hadden liever dat je de coordinaten van de maan bekomt via code in plaats van via hoofdrekenen
## Esther: die expliciete codering was nodig voor de rest van de opdracht!

## Esther: het was nog eleganter om 1 text stimulus te maken en dan enkel de text te updaten eens de botsing zich voordoet
text_planeet = visual.TextStim(win, text = 'De planeet heeft de rode reus geraakt')
text_maan = visual.TextStim(win, text = 'De maan heeft de rode reus geraakt')
text_planeet_en_maan = visual.TextStim(win, text = 'De planeet en de maan hebben tegelijk de rode reus geraakt')
text_niets = visual.TextStim(win, text = 'Geen enkel van de hemallichamen hebben de rode reus geraakt')





## veranderbare waarden

start_zon = numpy.array([(2/600)*45])
i = start_zon


kleur_start = 1
kleur = kleur_start








## op het scherm laten verschijnen

## 1 seconde het zonnestelsel presenteren:
#zon.draw()
#planeet.draw()
#maan.draw()
#win.flip()
#time.sleep(1)



## euclidische afstand tussen 2 punten (zon en planeet) om te berekenen of ze raken of niet
x1p = 0
y1p = 0
x2p= 0.705
y2p = 0.236

afstp = math.sqrt(((x1p - x2p)**2) + ((y1p - y2p)**2))
print(afstp)



## euclidische afstand tussen 2 punten (zon en maan) om te berekenen of ze raken of niet
x1m = 0
y1m = 0
x2m= 0.707
y2m = 0.356


afstm = math.sqrt(((x1m - x2m)**2) + ((y1m - y2m)**2))
print(afstm)






## willen registreren hoeveel welke gebeurtenis gebeurt dus gaan we een counter installeren per gebeurtenis

counter_maan = 0
counter_planeet = 0
counter_planeet_en_maan = 0
counter_niets = 0









## planeten laten roteren
## moet er arrays van maken om zo er iedere keer een andere waarde uit te kunnen halen

# Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
Planetx = numpy.array([  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,
             0.705,  0.741,  0.769,  0.788,  0.798,  0.799,  0.792,  0.775,  0.749,  0.715,
             0.673,  0.624,  0.567,  0.504,  0.435,  0.362,  0.284,  0.203,  0.12,   0.035,
            -0.049, -0.134, -0.217, -0.297, -0.374, -0.447, -0.515, -0.577, -0.632, -0.681,
            -0.721, -0.754, -0.778, -0.793,   -0.8, -0.797, -0.786, -0.765, -0.736, -0.699,
            -0.653, -0.601, -0.541, -0.476, -0.405, -0.33,  -0.251, -0.169, -0.085, -0.   ])
Planety = numpy.array([    0.5,  0.496,  0.487,  0.472,  0.452,  0.427,   0.397,  0.362,  0.324,  0.281,
             0.236,  0.188,  0.138,  0.086,   0.033, -0.02,  -0.073, -0.125, -0.175, -0.224,
             -0.27, -0.313, -0.353, -0.388, -0.419, -0.446, -0.467, -0.484, -0.494, -0.5,
            -0.499, -0.493, -0.481, -0.464, -0.442, -0.415, -0.383, -0.346, -0.306, -0.263,
            -0.216, -0.167, -0.116, -0.064, -0.011,  0.042,  0.095,  0.146,  0.196,  0.244,
             0.288,   0.33,  0.368,  0.402,  0.431,  0.456,  0.475,  0.489,  0.497,  0.5  ])
Moonx = numpy.array([   0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.,
            0.002,  0.079,  0.118,  0.103,  0.04,  -0.042, -0.104, -0.118, -0.077, -0.])
Moony = numpy.array([   0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12,
            0.12,   0.091,  0.019, -0.061, -0.113, -0.112, -0.059,  0.021,  0.092,  0.12])
            







## de positie van de maan is weer relatief aan de positie van de planeet dus je gaat bij ieder x-coord van de maan, het x coord van de planeet bij moeten tellen
## idem voor de y_coord
#array_x = ([0.705])
#array_y = ([0.236])
#Moonx = Moonx + array_x
#Moony = Moony + array_y
## het lukt nog niet om de maan rond de planeet te laten draaien, had tijd te kort










for y in range(60):
    
    
    
    ## om de kleur van de zon te laten veranderen:
    ## geel in RGB is (1, 1, -1) en rood in RGB is (1, -1, -1)
    ## dus moeten het middelste getal laten variëren van 1 naar -1
    
    

    ## Esther: het is nog beter om hier enkel de kleur, radius en positie te updaten in plaats van de stimuli telkens opnieuw aan te maken
    zon = visual.Circle(win, fillColor = (1, kleur, -1), pos = (0,0), lineColor = None, radius = i, units = 'norm')
    planeet = visual.Circle(win, fillColor = 'blue', pos = (Planetx[y], Planety[y]), lineColor = None, radius = ((2/600)*21), units = 'norm')
    maan = visual.Circle(win, fillColor = 'white', pos = (Moonx[y],Moony[y]), lineColor = None, radius = ((2/600)*12), units = 'norm')
    
    zon.draw()
    planeet.draw()
    maan.draw()
    
    
    
    
    ## willen de straal laten stijgen met 103%
    ## Iedere keer dat men door de loop gaat, willen we dat de straal stijgt met 103%
    i += (i*(3/100))
    
    
    
    ## kleur iedere keer een beetje laten veranderen
    kleur = kleur - (2/70)
    
    
    
    
    ## nu de afstand tss middelpunten van zon en planeet min de straal van de zon en de planeet
    afst_pl = afstp - ((2/600)*21) - i
    afst_m = afstm - ((2/600)*6) - i
    
    
    
    if afst_pl <= 0:
        win.flip()
        text_planeet.draw()
        counter_planeet += 1
        win.flip()
        time.sleep(1)
        win.close()
     
     
    if afst_m <= 0:
        win.flip()
        text_maan.draw()
        counter_maan += 1
        win.flip()
        time.sleep(1)
        win.close()

    ## Esther: pas op! deze vergelijking moet eerst komen en de rest moet in een elif hierop volgen
    ## Esther: anders krijg je te output
    if afst_m <= 0 and afst_pl <= 0:
        win.flip()
        ## Esther: .draw() vergeten hier
        text_planeet_en_maan()
        counter_planeet_en_maan += 1
        win.flip()
        time.sleep(1)
        win.close()
    
    
    # klopt nog iets niet aan
#    if afst_m > 0 and afst_pl > 0:
#        win.flip()
#        text_niets.draw()
#        counter_niets += 1
#        time.sleep(1)
    
    
    win.flip()
    time.sleep(0.1)




## Aflsuiten programma

win.close()