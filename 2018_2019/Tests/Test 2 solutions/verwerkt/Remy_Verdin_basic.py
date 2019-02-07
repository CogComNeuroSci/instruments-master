#test2

#importeer eerst modules 
import numpy, time
from psychopy import visual


# stationary solar sytem: celectial bodies positions
ZonRadius= 0.15 
GZon= 1 #enkel deze RGB waarde moet van 1 naar -1


#counts per botsing om feedback te geven achteraf
countboth= 0
countmaan= 0
countplaneet = 0


#Lijst met coordinaten om de hemellichamen te laten roteren
PlanetxList = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,

#window en startstimuli aanmaken
win = visual.Window(size=[600,600], units='norm',color='black')


for i in range(60):
    Planetx = PlanetxList[i]
    Planety = PlanetyList[i]
    Moonx = MoonxList[i]
    Moony = MoonyList[i]
    zon= visual.Circle(win, radius= ZonRadius, fillColor= (1,GZon,-1))
    planeet= visual.Circle(win, radius= 0.07, fillColor= (-1,-1,1),pos=(Planetx,Planety))
    maan= visual.Circle(win, radius= 0.02, fillColor=(1,1,1),pos=(Planetx + Moonx,Planety + Moony))
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    ZonRadius+= ZonRadius*0.03 #103 procent betekent 3 procent toevoegen
    GZon+= -0.03333333333333333 #-2 in stappen van 60 (dus -2/60)

    #overlap condities => break. if not => continue
    if zon.overlaps(planeet) and zon.overlaps(maan):
        countboth+= 1
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
if countboth == 1:
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
print(countboth)
print(countmaan)
print(countplaneet)
