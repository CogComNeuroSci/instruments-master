from __future__ import division

from psychopy import visual, event, core


win = visual.Window([800, 800])

import time 
bat= "bat.png"

picture1= visual.ImageStim(win,image = bat,pos=(-0.7,0.2),size= 0.2,ori= 10,opacity = 0.7)
picture2= visual.ImageStim(win,image = bat,pos=(-0.8,0.6),size=0.2,ori = 350, opacity = 0.7)
picture3= visual.ImageStim(win,image = bat,pos=(-0.8,-0.4),size=0.2,ori= 40, opacity = 0.7)
picture4= visual.ImageStim(win,image = bat,pos=(-0.4,-0.7),size=0.2, ori= 20, opacity = 0.7)
picture5= visual.ImageStim(win,image = bat,pos=(0.3,-0.6),size=0.2,ori= 320, opacity = 0.7)
picture6= visual.ImageStim(win,image = bat,pos=(0.85,0.75),size=0.2, ori= 330, opacity = 0.7)
picture7= visual.ImageStim(win,image = bat,pos=(0.8,0.2),size=0.2,ori= 325, opacity = 0.7)
picture8= visual.ImageStim(win,image = bat,pos=(0.6,-0.3),size=0.2,ori= 340, opacity = 0.7)
picture9= visual.ImageStim(win,image = bat,pos=(-0.3,0.8),size= 0.2,ori= 325,opacity = 0.7)
picture10= visual.ImageStim(win,image = bat,pos=(0.5,0.6),size= 0.2,ori= 20,opacity = 0.7)


pompoen= visual.Circle(win, edges =99, radius= 0.5, color = "orange")

grating = visual.GratingStim(win, mask = "circle", ori = 0, color= 'black', tex = 'saw', sf= 6, contrast= 0.5, size= 1.01, blendmode= 'avg', opacity= 0.4)
#creating some lines on the pumpkin

eye1= visual.Polygon(win, edges= 3, radius= 0.1, pos= [-0.2,0.2], color= "black")
eye10 = visual.Polygon(win, edges = 3, radius= 0.05, pos= [-0.2,0.2], color = "Gold")
eye2= visual.Polygon(win, edges= 3, radius= 0.1, pos= [0.2,0.2], color= "black")
eye20= visual.Polygon(win, edges= 3, radius= 0.05, pos= [0.2,0.2], color= "Gold")
# two different colours 

from psychopy.visual import ShapeStim
n= [(-0.05,0.05),(0,-0.05),(0.05,0.05)]
nose= ShapeStim(win, vertices= n, fillColor= 'black', lineColor= "black")

l= [(-0.1,-0.3),(-0.2,-0.1),(-0.08,-0.2),(0,-0.1),(0.08,-0.2),(0.2,-0.1),(0.1,-0.3)]
mound= ShapeStim(win, vertices= l, fillColor ='black', lineColor='black')

blushing1 = visual.Circle(win, radius=0.05, opacity= 0.5, color= 'LightCoral', pos=(-0.35,-0.05))
blushing2 = visual.Circle(win, radius=0.05, opacity= 0.5, color= 'LightCoral', pos=( 0.35, -0.05))

r= [(0.025,0.50),(0.005, 0.60), (-0.12, 0.64),(-0.11,0.60),(-0.03,0.555), (-0.025,0.50)]
rectangle = ShapeStim(win, vertices= r, fillColor= 'black') 

text1= visual.TextStim(win, text= "Happy", color= "orange", pos= (0,0.8), font= "Trattatello", height= 0.15)
text2 = visual.TextStim(win, text= "Halloween!", color= "orange", pos= [0,-0.8], font= "Trattatello", height= 0.35)


while not event.getKeys():


    picture1.draw()
    picture2.draw()
    picture3.draw()
    picture4.draw()
    picture5.draw()
    picture6.draw()
    picture7.draw()
    picture8.draw()
    picture9.draw()
    picture10.draw()
    pompoen.draw()
    grating.draw()
    eye1.draw()
    eye10.draw()
    eye2.draw()
    eye20.draw()
    nose.draw()
    mound.draw() 
    blushing1.draw() 
    blushing2.draw() 
    rectangle.draw() 
    text1.draw() 
    text2.draw()
    
    win.flip()
    time.sleep(1)



    picture1.draw()
    picture2.draw()
    picture3.draw()
    picture4.draw()
    picture5.draw()
    picture6.draw()
    picture7.draw()
    picture8.draw()
    picture9.draw()
    picture10.draw()
    pompoen.draw()
    grating.draw()
    eye1.draw()
    eye2.draw()
    nose.draw()
    mound.draw() 
    blushing1.draw() 
    blushing2.draw() 
    rectangle.draw() 

    win.flip()
    time.sleep(0.5)







win.close()
core.quit()