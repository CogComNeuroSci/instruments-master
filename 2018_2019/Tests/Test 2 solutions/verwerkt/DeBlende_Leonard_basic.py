#import modules
import time, numpy
from psychopy import visual, event
from numpy import random

#Window
win = visual.Window(size = (600,600), color = (-1,-1,-1), units ="norm")


#coordinates
blauwx = [  0.014,  0.099,  0.182,  0.264,  0.342,  0.417,  0.487,  0.552,  0.61,   0.661,

#initializing
blauw_x = 0.705
blauw_y = 0.236
maan_x = (blauw_x + 0.002)
maan_y = (blauw_y + 0.12)
startpositieblauw = (blauw_x, blauw_y)
startpositiemaan = (maan_x, maan_y)
tijd_stap = 0.1        #seconden
max_tijd = 6            # seconden
tijd_size = .03
start_radius_zon = 0.075*2

#graphs

zon = visual.Circle(win, radius = start_radius_zon, fillColor = "yellow", lineColor = "yellow", pos = (0,0))

planeet = visual.Circle(win, radius = 0.035*2, fillColor = "blue", lineColor = "blue", pos = startpositieblauw)

maan = visual.Circle(win, radius = 0.01*2, fillColor = "white", lineColor = "white", pos = startpositiemaan)

botsing = visual.TextStim(win, text = "test")

#radius_array = numpy.array([zon.radius])

#array_coordinaten = numpy.array([blauwx, blauwy, maanx, maany])

#coordinaten = numpy.column.stack([blauwx, blauwy, maanx, maany])

#planeet.pos = (blauwx, blauwy)

#op het scherm laten verschijnen
zon.draw()
planeet.draw() 
maan.draw()
win.flip()
time.sleep(1)


#zon laten groeien

    #extra variabelen:

tijd = 0
zon.radius = start_radius_zon

while tijd < max_tijd:
    tijd = tijd + tijd_stap
    zon.radius = zon.radius + zon.radius*tijd_size
    
    if zon.radius > 0.75:
        break
    

    
    #kleur wijziging van (1,-1,-1) naar (255,255, 0), niet gelukt
    
    #radius_array = numpy.vstack([radius_array, zon.radius])
    
    #yellow_red = ((numpy.ndarray.round(zon.radius))-1)
    #if yellow_red < -1:
        #yellow_red = -1
    #if yellow_red > 1:
        #yellow_red = 1
    
    #zon.color = ([yellow_red, yellow_red, yellow_red], "rgb")
    
    #roteren:  ik wil de coordinaten uit mijn array halen en ze zo laten roteren, dit is echter ook niet gelukt
    #for i in range(coordinaten):
        #planeet.pos = (blauwx[i],blauwy[i])
        #planeet.draw()
        #win.flip()
        #time.sleep(0.1)
    
    #botsing
    
    
    zon.draw()
    planeet.draw()
    maan.draw()
    win.flip()
    time.sleep(0.1)
    
    
    if "f" in event.getKeys():
        break



