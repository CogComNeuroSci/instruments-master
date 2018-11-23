##nodige modules importeren
import time
from psychopy import visual

##scherm aanmaken
win = visual.Window(size = [600,600],color = (-1,-1,-1), units = "norm")


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

##definieer de startwaarden van de variabelen
zonnestraal      = 0.15
i                = 0 
planeet_counter  = 0
maan_counter     = 0

##laat de zon groeien en van kleur veranderen in 60 stappen
for i in range(60):
    
    ## Esther: het is nog beter om de grafische elementen voor de loop aan te maken 
    
    zon         = visual.Circle(win, lineColor=(1, 1 - i*0.03, 0 - i*0.016),fillColor = (1, 1 - i*0.03, 0 - i*0.016), radius = zonnestraal )  
    
    ## Esther: je mocht geel ook definiëren als [1,1,-1], dat was waarschijnlijk gemakkelijker
    
    ##uitleg kleur: van geel = [1,1,0] naar rood = [1,-1,-1]   dus de G en B componenten moeten respectievelijk met 2 en 1 eenheden verminderen
    ##dit moet geleidelijk gebeuren dus gebruik i 
    ##aangezien i op het einde 60 is kan je een formule maken voor de kleurverandering van bijvoorbeeld de G-component: 
        ## eindwaardeG = startwaarde - i*x
        ##          -1 =      1      - 60*x
        ## als je de vgl oplost krijg je dat x = 2/60 ofwel 0.03
    ##idem ditto voor de B component
    
    ##laat de straal van de zon telkens met 3% tov de vorige straal groeien
    zonnestraal = zonnestraal + zonnestraal*0.03
    
    ##definieer de coordinaten van de planeet en maan als voor elke loop het i-de element uit de lijsten
    ##bij de maan is dit relatief tov de planeet dus altijd de coord van de planeet PLUS die uit de moon-lijsten
    planeet     = visual.Circle(win,lineColor = "blue",   fillColor = "blue",   radius = 0.07, pos = (Planetx[i], Planety[i]) )
    maan        = visual.Circle(win,lineColor = "white",  fillColor = "white",  radius = 0.02, pos = (Planetx[i]+Moonx[i], Planety[i]+Moony[i]) )
    
    ##60 loops in stappen van 1
    i = i + 1
    
    ##presenteer de stimuli 
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    
    ##zorg ervoor dat de loop stopt bij een botsing en registreer welke botsing er voorviel door een variabele, gedefinieerd als counter, 
        ##met 1 te laten vermeerderen. Indien er geen botsing is blijft de counter op 0 staan. 
    if zon.overlaps(planeet) == True:
        planeet_counter += 1
        break
    elif zon.overlaps(maan) == True:
        maan_counter += 1
        break

##Presenteer de tekst op het einde adhv waar de maan tegen gebotst is. Presenteer dit voor 1 seconde.
if planeet_counter == 0 and maan_counter == 0:
    boodschap = "Geen enkele van de hemellichamen heeft de rode reus geraakt."
elif planeet_counter == maan_counter:
    boodschap = "De planeet en de maan hebben tegelijk de rode reus geraakt."
elif planeet_counter  > maan_counter:
    boodschap = "De planeet heeft de rode reus geraakt. "
else:
    boodschap = "De maan heeft de rode reus geraakt."

eindscherm = visual.TextStim(win,text = boodschap)
eindscherm.draw()
win.flip()
time.sleep(1)

##sluit alles af
win.close()
