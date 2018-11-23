## Esther: super goed, zo mogelijk perfecte code, enkel dingen die van persoonlijke smaak afhangen. Proficiat Remy!

#test2

#importeer eerst modules 
import numpy, time, math
from psychopy import visual

#counts per botsing om feedback te geven achteraf
countbeide= 0
countmaan= 0
countplaneet = 0

#window aanmaken
win = visual.Window(size=[600,600], units='norm',color='black')

#we zetten de startwaarde van de hoeken op 0(graden) waarbij hoekp = hoek planeet en hoekm= hoek maan
hoekp=0
hoekm=0

# beginwaarden voor de zon (de radius en de G waarde van RGB die van 1 naar -1 moet gaan)
ZonRadius= 0.15 
GZon= 1 

aantalloops=60
for keertje in range(aantalloops):
    Planetx= 0.8*math.cos(math.radians(hoekp)) #ellipsen hebben een verschillende straal voor x- en y-as, de hoeken moeten in radialen staan voor deze berekening
    Planety= 0.5*math.sin(math.radians(hoekp))
    Moonx= 0.12*math.cos(math.radians(hoekm)) #cirkels hebben dezelfde straal voor x- en y-as
    Moony= 0.12*math.sin(math.radians(hoekm))
    
    zon= visual.Circle(win, radius= ZonRadius, fillColor= (1,GZon,-1))
    planeet= visual.Circle(win, radius= 0.07, fillColor= (-1,-1,1),pos=(Planetx,Planety))
    maan= visual.Circle(win, radius= 0.02, fillColor=(1,1,1),pos=(Planetx + Moonx,Planety + Moony))
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    hoekp+= 360/aantalloops #360 graden in aantalloops stappen, we maken precies 1 cirkel ((De hoeken gewoon in graden. We veranderen dit naar radialen aan het begin van de loop voor we de positie bepalen))
    hoekm+= 360/(aantalloops/6) #aantalloops gedeeld door het aantal rotaties = hoeveel stapjes je zet per cirkel. 360/ dit aantal.
    ZonRadius+= ZonRadius*0.03 #103 procent betekent 3 procent toevoegen
    GZon+= -2/aantalloops #(van 1 naar -1) -2 in gelijdelijke stappen (gedeeld door het aantalloops)

    #overlap condities => break. if not => continue
    if zon.overlaps(planeet) and zon.overlaps(maan):
        countbeide+= 1
        break
    elif zon.overlaps(planeet):
        countplaneet+= 1
        break
    elif zon.overlaps(maan):
        countmaan+=1
        break
    else:
        continue
#if statements om feedback te geven achteraf
if countbeide == 1:
    feedback= visual.TextStim(win, text= 'De planeet en de maan hebben tegelijk de rode reus geraakt')
elif countplaneet == 1:
    feedback= visual.TextStim(win, text= 'De planeet heeft de rode reus geraakt')
elif countmaan == 1:
    feedback= visual.TextStim(win, text= 'De maan heeft de rode reus geraakt')
else:
    feedback= visual.TextStim(win, text= 'Geen enkele van de hemellichamen heeft de rode reus geraakt')
feedback.draw()
win.flip()
time.sleep(1)
win.close()

#om te controleren of feedback die gegeven werd juist is
print(countbeide)
print(countmaan)
print(countplaneet)
