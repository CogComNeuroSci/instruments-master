#TEST 2: CODIING SOLAR SYSTEM - BY HELENA CORENS 

#Step 1: import modules 
from psychopy import visual, event,core
import time, numpy

#Step 2: in case of emmergency, ESCAPE:
for key in ['q', 'escape']:
    event.globalKeys.add(key, func=core.quit)

#Step 3: info about the visuals:
start_rad_sun = 0.075            #15%/2; startpositie --> laten uitdijen
pos_sun = (0,0)
rad_planet = 0.034          #7%/2
pos_planetx = 0.705
pos_planety= 0.236  #startpositie
rad_moon = 0.01             #2%/2
pos_moonx = (pos_planetx + 0.002)     #Startpositie; 'Relatief tov positie planeet': dus daarom pos_moon_x=0.705 + 0.002/ pos_moon_y=0.236 + 0.12
pos_moony = (pos_planety + 0.12)
presenting_time = 1 

Yellow = (1,1,0)
Red = (1,-1,-1)

#General Window Graphics
win = visual.Window([600,600], color = (-1,-1,-1), units = 'norm') 

#Graphics SUN
x=0.05
start_rad_sun = 0.075
while start_rad_sun < 0.1:
    start_rad_sun += (start_rad_sun*x)
    stim_sun = visual.Circle(win, radius = start_rad_sun, pos = (0,0), fillColor = 'yellow')
    stim_sun.draw()

Radius_Sun = numpy.array([0.075,0.08,0.085,0.09,0.095,0.1,0.105,0.110])
### Ik zit vast

##color changing
### niet gelukt

#Graphics PLANET
stim_planet = visual.Circle(win, radius = 0.034, pos = (0.705,0.236), fillColor = "blue")

#Graphics MOON
stim_moon = visual.Circle(win, radius = 0.01, pos = (pos_moonx,pos_moony), fillColor = "white")

# stationary solar sytem: celectial bodies positions


# Crash
##voor de botsing gebruik maken van boolean --> TRUE / FALSE 


#Drawing the visuals
stim_sun.draw()
stim_planet.draw()
stim_moon.draw()

win.flip()
time.sleep(5)

win.close()






