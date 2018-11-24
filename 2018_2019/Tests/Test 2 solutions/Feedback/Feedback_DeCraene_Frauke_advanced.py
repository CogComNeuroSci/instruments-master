## Esther: super goed, zo mogelijk perfecte code (op die ene ontbrekende melding na). Proficiat Frauke!


from psychopy import visual
import time, numpy,math

#create window
win = visual.Window([600,600], color='black')


#create planets in startposition
##diameter of sun is 15% -> 0.30 so radius is 0.30/2 = 0.15
##same logic for the other radii
sun = visual.Circle(win, radius = 0.15, lineColor=[1,1,-1], fillColor=[1,1,-1])
planet = visual.Circle(win, radius = 0.07, lineColor=[-1,-1,1], fillColor=[-1,-1,1])
moon = visual.Circle(win, radius = 0.02, lineColor=[1,1,1], fillColor=[1,1,1])


#create array for changing size and color
##60 steps to get from yellow [1,1,-1] to red [1,-1,-1]
##Green value needs to change 2 units in 60 steps
ColorArray = numpy.array([])
for colorchange in range(180):
    ColorArray=numpy.append(arr=ColorArray, values=1-colorchange*(2/179))

SizeArray = numpy.array([0.15])
for sizechange in range(179):
    SizeArray=numpy.append(arr=SizeArray, values=SizeArray[sizechange]*1.03)

SunChanges = numpy.column_stack([ColorArray, SizeArray])


#Create TextStim for crashes
bothcrash = visual.TextStim(win,text= "De planeet en de maan hebben tegelijk de rode reus geraakt")
mooncrash = visual.TextStim(win,text= "De maan heeft de rode reus geraakt")
planetcrash = visual.TextStim(win,text= "De planeet heeft de rode reus geraakt")



for rotation in range (180):
    #create 180 steps to complete ellipse, 30 for a circle (6 moonrotations for every planetrotation
    #circle/ellipse x = a*cos t and y=b*sin t   0 < t < 2*pi 
    ##a = horizontal axis   b= vertical axis
    ## same a and b -> circle   different a and b -> ellipse
    t1 = (rotation * 2*math.pi)/180
    OrbitPlanetx=0.8*math.cos(t1)
    OrbitPlanety=0.5*math.sin(t1)
    
    t2 = (rotation * 2*math.pi)/30
    OrbitMoonx=0.12*math.cos(t2)
    OrbitMoony=0.12*math.sin(t2)
    
    planet.pos= [OrbitPlanetx,OrbitPlanety]
    moon.pos= [OrbitPlanetx+OrbitMoonx,OrbitPlanety+OrbitMoony]

    #sun color and radius change
    sun.fillColor = [1,SunChanges[rotation,0],-1]
    sun.lineColor=sun.fillColor
    sun.radius= SunChanges[rotation,1]
    
    #draw all shapes
    sun.draw()
    planet.draw()
    moon.draw()
    win.flip()
    
    #detect crash
    if sun.overlaps(moon) ==  True and sun.overlaps(planet) == True:
        bothcrash.draw()
        win.flip()
        time.sleep(1)
        break
    elif sun.overlaps(moon) ==  True :
        mooncrash.draw()
        win.flip()
        time.sleep(1)
        break
    elif sun.overlaps(planet) ==  True :
        planetcrash.draw()
        win.flip()
        time.sleep(1)
        break
win.close()