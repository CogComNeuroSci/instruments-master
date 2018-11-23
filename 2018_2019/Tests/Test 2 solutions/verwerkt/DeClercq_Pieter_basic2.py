from psychopy import visual, event
import time
import numpy 
from numpy import random

#window aanmaken
win=visual.Window(size=[800,800], color='black')

#zon
zon=visual.Circle(win, pos=(0,0), radius=0.075, fillColor=(1,1,-1),lineColor=(1,1,-1), units='norm')
straal=0.075

#planeet
planeetx = 0.705
planeety = 0.236
planeet=visual.Circle(win, radius=0.035, pos=(planeetx,planeety), fillColor='blue',lineColor='blue')


#maan
maanx=0.002
maany=0.12
maan=visual.Circle(win, radius=0.01, pos=((planeetx+maanx),(planeety+maany)), fillColor='white', lineColor='white')


botsing=False


while zon.radius < 1 and botsing==False:
    zon.radius = zon.radius+(zon.radius*0.03) #omdat de volgende 103% van de vorige moet zijn
    #hier wou ik zon.radius maal 2 doen, omdat hij dan mooi van 1 naar -1 zou gaan. Maar dit ging niet, het werd helemaal op het einddus met wat trial and error heb
    zon.fillColor=(1,1-(zon.radius*1.90),-1)
    zon.lineColor=(1,1-(zon.radius*1.90),-1)
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    
    #nu maak ik arrays aan van de minimum en maximum waarden tot waar de zon mag komen.
    planeet.pos[0] = numpy.maximum(planeet.pos[0],-1)
    planeet.pos[1] = numpy.maximum(planeet.pos[1],-1)
    planeet.pos[0] = numpy.minimum(planeet.pos[0],+1)
    planeet.pos[1] = numpy.minimum(planeet.pos[1],+1)
    
    #nu hetzelfde voor de maan:
    
    maan.pos[0] = numpy.maximum(maan.pos[0],-1)
    maan.pos[1] = numpy.maximum(maan.pos[1],-1)
    maan.pos[0] = numpy.minimum(maan.pos[0],+1)
    maan.pos[1] = numpy.minimum(maan.pos[1],+1)
    
    #nu is het idee dat als de absolute waarde van de positie van de planeet plots kleiner wordt dan de straal van de zon, ik een botsing heb.  
    
    if numpy.absolute(planeet.pos[0])<zon.radius and numpy.absolute(planeet.pos[1])<zon.radius:
        botsing=True
        botsingplaneettekst=visual.TextStim(win, text="De planeet heeft de rode reus geraakt")
        botsingplaneettekst.draw()
        win.flip()
        time.sleep(1)
    #nu opnieuw zelfde voor maan:
    if numpy.absolute(maan.pos[0])<zon.radius and numpy.absolute(maan.pos[1])<zon.radius:
        botsing=True
        botsingmaantekst=visual.TextStim(win, text="De maan heeft de rode reus geraakt")
        botsingmaantekst.draw()
        win.flip()
        time.sleep(1)
    #nu voor allebei:
    if numpy.absolute(planeet.pos[0])<zon.radius and numpy.absolute(planeet.pos[1])<zon.radius and numpy.absolute(planeet.pos[0])<zon.radius and numpy.absolute(planeet.pos[1])<zon.radius:
        botsing=True
        botsingallebei=visual.TextStim(win, text="De planeet en de maan hebben tegelijk de rode reus geraakt")
        botsingmallebei.draw()
        win.flip()
        time.sleep(1)




win.close()