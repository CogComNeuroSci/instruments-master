#Coding zonnestelsel

#import
from __future__ import division
from psychopy import visual
from time import sleep
from psychopy import visual, event, core
from math import cos, sin, pi

#make a window
win=visual.Window(color='black',units='pix',size=(600,600))

#Initialize
Radius_sun = 0.15
t_ellipse=0
t_circle=0
nb_trials=300

#coordinates

## Series of positions for orbits (the coordinates for the moon are again relative to the position of the planet!)
Planetx = []
Planety = []
Moonx = []
Moony = []


#visual Stimuli
##De zon, de blauwe planeet, en de witte maan
Sun      = visual.Circle(win,radius=Radius_sun,fillColor=[1,1,-1],pos=(0,0),units='norm') ##geel
Planet   = visual.Circle(win,radius=0.07,fillColor=[-1,-1,1],units='norm') ##blauw
Moon     = visual.Circle(win,radius=0.02,fillColor=[1,1,1],units='norm') ##wit

##Text
Botsing  = visual.TextStim(win)

#Coding

##Zon laten vergrootte en verroode + planeten in beweging brengen
for i in range (nb_trials):
    
    ##Appending the coordinates of the Planet
    Ellipse_x       = 0.8*cos(t_ellipse)
    Ellipse_y       = 0.5*sin(t_ellipse)
    Planetx.append(Ellipse_x)
    Planety.append(Ellipse_y)
    
    ##Appending the coordinates of the Moon
    Circle_x       = 0.12*cos(t_circle)
    Circle_y       = 0.12*sin(t_circle)
    Moonx.append(Circle_x)
    Moony.append(Circle_y)
    print(Moonx)
    
    ##changing t value
    t_ellipse= t_ellipse+2*pi/nb_trials
    t_circle = t_circle+2*pi/(nb_trials/6)
    
    ##change positions of planet and moon
    Planet.pos=((Planetx[i],Planety[i]))
    Moon.pos  =((Planetx[i]+Moonx[i],Planety[i]+Moony[i]))
    
    ##change size of Sun
    Sun.radius=(Radius_sun+0.005*Radius_sun)
    Radius_sun=Radius_sun+0.005*Radius_sun
    
    ##change color of Sun
    Sun.fillColor=([1,1-i/(nb_trials/2),-1])   ##more red
    
    ##draw
    Planet.draw()
    Moon.draw()
    Sun.draw()
    win.flip()
    
    ##If statements
    if Sun.overlaps (Moon) and Sun.overlaps(Planet):
        Botsing.text=("De planeet en de maan hebben tegelijk de rode reus geraakt")
    elif Sun.overlaps (Planet):
        Botsing.text=("De planeet heeft de rode reus geraakt")
    elif Sun.overlaps (Moon):
        Botsing.text=("De maan heeft de rode reus geraakt")
    else:
        Botsing.text=("Niks heeft de rode reus geraakt")
        

##Toon de finale text
Botsing.draw()
win.flip()
sleep(2)