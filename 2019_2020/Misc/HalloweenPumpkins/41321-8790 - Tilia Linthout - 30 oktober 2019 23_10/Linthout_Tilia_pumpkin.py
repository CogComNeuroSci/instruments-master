from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim

import time

win = visual.Window(size=(1366,768), units='deg', monitor= 'My monitor', color= 'black')
#My monitor met size 1366,768

#_____________________________________________________________________________________________________________________________________________________________

##pumpkinVert= [(-10,10), (10,10), (-10,-10), (10,-10)]
##pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor='orange', size=.5, lineColor='red')
##zandloperfiguur want deze volgorde wordt gehanteerd?: -10,10 wordt verbonden met 10,10

##pumpkin.draw()
##win.flip()

pompoenvormVert= [(-32.5,0),(-32.2,1.8), (-31.7,3.8), (-30.5,6), (-29,7.7),(-27,9.4),(-25,11), (-22.7,12.6),(-20.3,13.8), (-18.3,14.4),(-15.3,14.8), (-12.5,14.9), (-10.3,14.8), (-6.9,14.2), (-4.9,13.3), (-3,12.8), (-2,12.6), (0,12.8), (1,13),(2.5,13.8),(5,15.1),(7.8,16.3),(9.9,17.5), (14.1,17.9), (17.3, 17.7), (20, 17), (22.6, 16.2),(25,15),(26.1,13.3),(26.8,11.1),(27.3,8.6),(27.8,5.9),(27.7,3.7),(27.2,2),(26.6,0), (25.5,-2.5), (24,-5), (21.8,-8.8), (20.5, -10.5),(19.2,-12.4),(17.7,-14),(15.2,-16.5),(13.2,-18.2),(11,-19), (9,-19.5), (7.5,-19.8),(5.5,-19.6),(3.8,-19.2),(2.8,-18.5),(1.2,-19.2), (-2.3,-19.7),(-5,-20),(-7.9,-20.2),(-10.3,-20), (-12.6,-19.2),(-13.8,-18.3),(-14.5,-18.9),(-15.9,-19.1),(-17.8,-19.4),(-19.7,-19.6),(-22,-19.2),(-23,-19),(-24,-18.5),(-25,-18),(-26,-17),(-28,-14.3),(-29,-12.8),(-30,-11.1),(-31,-9),(-31.8,-6.9),(-32.3,-4.1),(-32.5,-2)]
pompoenvorm= ShapeStim(win, vertices=pompoenvormVert, fillColor='#FF8000', size= .5, lineColor='#FF0000', lineWidth= 3)
#numphy.arrayerror: check of je overal puntjes hebt en geen komma's in je getallen!
pompoenvorm.draw()
#kleurensite: rapidtables.com

#steeltjeVert= [(-2,12.6),(-2.6,13.8),(-2.5,15),(-2.3,16.4),(-2,17.5),(-1.5,18.6), (0,12.8)]
#steeltje= ShapeStim(win, vertices=steeltjeVert,fillColor='#4C9900',size= .5,lineColor='darkgreen')
#steeltje.draw()

#steeltjedeel2Vert=[(-0.5,-19.6),(0.9,20.2),(2.1,20.8),(3.3,20.9),(4.7,20.8),(5.4,20.1),(6,19.8),(6.8,19.1),(6.9,18.5),(6.6,17.7),(6.1,17),(5.2,16.7),(4.2,16.5),(3.4,16.8),(3,17.5),(3.1,18.4),(3.6,18.9),(4.3,18.8),(4.8,18.5),(4.9,18),(4.3,17.6),(5.2,17.7),(5.4,18.3)(5.1,19.1),(4.8,19.7),(3.7,19.9),(2.6,19.8),(2,18.7),(1.8,17.3),(1.9,16),(2.2,15),(3.65384,14.3),(2.5,13.8),(1,13),(0,12.8), (-1.5,18.6)]
#steeltjedeel2=ShapStim(win, vertices=steeltjedeel2Vert,fillColor='green',size=.5,linecolor='darkgreen')
#steeltjedeel2.draw()
#error:tuple object is not callable

pompoenlijn1Vert=[(-13.8,-18.3),(-14.9,-15.5),(-15.2,-13),(-15.3,-10),(-15.1,-6.1),(-14.9,-5.2)]
pompoenlijn1= ShapeStim(win, vertices=pompoenlijn1Vert, size=.5, lineColor= '#CC6600',lineWidth= 3, closeShape=False)
pompoenlijn1.draw()

pompoenlijn2Vert=[(-2.3,-19.7),(-2.1,-17), (-1.8,-9.9), (-1.7,-8.2)]
pompoenlijn2= ShapeStim(win, vertices=pompoenlijn2Vert, size=.5, lineColor= '#CC6600',lineWidth= 3, closeShape=False)
pompoenlijn2.draw()

pompoenlijn3Vert=[(2.8,-18.5), (5,-16.4),(5.9,-15.4),(8.8,-10.6), (10,-7), (10.5,-4),(10.3,-3.2)]
pompoenlijn3= ShapeStim(win, vertices=pompoenlijn3Vert, size=.5, lineColor= '#CC6600',lineWidth= 3, closeShape=False)
pompoenlijn3.draw()


steeltjeVert= [(-2,12.6),(-2.5,13.8),(-2.4,14.9),(-2.2,16.4),(-2,17.5),(-1.4,18.6),(-0.5,19.5),(0.8,20.2),(2.1,20.8),(3.3,20.9),(3.7,19.9),(2.5,19.7),(2,18.9),(1.8,17.3),(1.9,16),(2.5,13.8),(1,13), (0,12.8)]
steeltje= ShapeStim(win, vertices= steeltjeVert, fillColor= '#4C9900', size= .5, lineColor= 'brown', lineWidth= 3)
steeltje.draw()

wenkbrauw1Vert=[(-7.5,9.7),(-7.9,11),(-8.5,12.5),(-10,11.9),(-11.6,11),(-13.2,9.5),(-14.5,7.9),(-12.8,8.5),(-9.3,9.3)]
wenkbrauw1= ShapeStim(win, vertices=wenkbrauw1Vert,fillColor='yellow',size= .5,lineColor='brown', lineWidth= 3)
wenkbrauw1.draw()

wenkbrauw2Vert=[(4,11),(4.9,11.1),(7,11),(8.8,10.6),(10.3,10),(11.2,9.2), (11.1,10.1),(10.8,10.9),(9.6,12), (8.5,12.9),(6.9,13.7),(5.5,14),(4.9,13.5),(4.2,12.2)]
wenkbrauw2= ShapeStim(win, vertices=wenkbrauw2Vert, fillColor= 'yellow', size=.5, lineColor= 'brown',lineWidth=3 )
wenkbrauw2.draw()

mondVert=[(0,-10.9),(1.6,-10.7),(3.5,-10.5),(4.3,-10),(4.2,-7.2),(6.8,-7),(7,-6.9),(8.1,-6.5),(9.8,-6),(10.7,-5.5),(12.3,-4.8),(13.9,-4),(14.8,-3.2),(15.4,-2.8),(15.1,-3.5), (14.7,-4.4),(14.4,-5.5),(14,-6.5),(13.5,-7.3), (13,-8.2),(12.5,-9.2),(12,-10),(10.9,-11.4),(9,-13),(7.1,-14.5),(4,-16),(1.5,-16.5),(-1,-16.7),(-4.2,-16.5),(-4.8,-16.1),(-5,-13.2),(-5.8,-13.4),(-7.1,-13.6),(-9,-13.5),(-10.9,-13.3),(-12.2,-13),(-13.1,-15.3),(-14.6,-14),(-15.5,-12),(-16.2,-10.2),(-17,-8),(-17.5,-6),(-17,-6.9),(-16,-7.5),(-15,-8.1),(-13.8,-8.6),(-12.8,-8.8),(-11,-8.9),(-8.2,-8.7),(-6,-8.4),(-4,-8.1),(-4.2,-10.8),(-2.9,-11)]
mond= ShapeStim(win, vertices=mondVert, fillColor='yellow', size=.5, lineColor= 'brown',lineWidth= 3)
mond.draw()

oog1= visual.Polygon(win, edges=100, radius=2.8, fillColor="white", pos=[-4,0.9], lineColor= '#331900',lineWidth= 3)
oog1.draw()
#pos= center of stim??

pupiel1= visual.Polygon(win, edges= 100, radius= 0.6, fillColor= "black", pos= [-2.5,1.8])
pupiel1.draw()

oog2= visual.Polygon(win, edges=100, radius=3.2, fillColor="white", pos=[3,1.5], lineColor= '#331900', lineWidth= 3)
oog2.draw()

pupiel2=visual.Polygon(win,edges= 100, radius= 0.6, fillColor= "black", pos= [2,2.5])
pupiel2.draw()

blinkendpupiel1= visual.Polygon(win, edges= 100, radius= 0.07, fillColor= "white", pos= [-2.6,1.9])
blinkendpupiel1.draw()

blinkendpupiel2= visual.Polygon(win, edges= 100, radius= 0.07, fillColor= "white", pos= [2,2.5])
blinkendpupiel2.draw()

blaadjeVert= [(21.8,-8.8),(23,-7.2),(24,-6.2),(26.4,-5.4),(28.8,-4.6),(30.9,-4.4),(33,-4.6), (34.9,-4.9),(36.2,-5),(38,-4.7),(37.5,-5.8),(37,-7),(36.4,-8.8),(35.5,-10.2), (34.6,-12),(33.5,-13.2),(32.4,-14.8),(31,-16), (29.9,-17),(28.2,-17.8),(26.5,-18.3),(24,-18.7),(21.6,-18.4),(19.6,-18), (15.2,-16.5)]
blaadje= ShapeStim(win, vertices=blaadjeVert, fillColor='green', size=.5, lineColor= 'brown',lineWidth= 3)
blaadje.draw()

bladnerf1Vert=[(19.2,-12.4),(22.2,-12.3), (26,-12), (29.5,-10.5), (32.5,-9), (36,-6)]
bladnerf1= ShapeStim(win, vertices=bladnerf1Vert, fillColor='green', size=.5, lineColor= '#003300',lineWidth= 3, closeShape=False)
bladnerf1.draw()

bladnerf2Vert= [(22.2,-12.3),(24.1,-7.8)]
bladnerf2= ShapeStim(win, vertices=bladnerf2Vert, fillColor='green', size=.5, lineColor= '#003300',lineWidth= 3, closeShape=False)
bladnerf2.draw()

bladnerf3Vert= [(26,-12),(28,-7.2)]
bladnerf3= ShapeStim(win, vertices=bladnerf3Vert, fillColor='green', size=.5, lineColor= '#003300',lineWidth= 3, closeShape=False)
bladnerf3.draw()

bladnerf4Vert=[(29.5,-10.5),(30,-8.5)]
bladnerf4= ShapeStim(win, vertices=bladnerf4Vert, fillColor='green', size=.5, lineColor= '#003300',lineWidth= 3, closeShape=False)
bladnerf4.draw()

bladnerf5Vert= [(22.2,-12.3),(25.7,-15.3)]
bladnerf5= ShapeStim(win, vertices=bladnerf5Vert, fillColor='green', size=.5, lineColor= '#003300',lineWidth= 3, closeShape=False)
bladnerf5.draw()

bladnerf6Vert=[(26,-12),(29.9,-13.9)]
bladnerf6= ShapeStim(win, vertices=bladnerf6Vert, fillColor='green', size=.5, lineColor= '#003300',lineWidth= 3, closeShape=False)
bladnerf6.draw()


bladnerf7Vert= [(29.5,-10.5),(30.8,-11.1)]
bladnerf7= ShapeStim(win, vertices=bladnerf7Vert, fillColor='green', size=.5, lineColor= '#003300',lineWidth= 3, closeShape=False)
bladnerf7.draw()




#blaadjeVert= [(21.8,-8.8),(23,-7.2),(24,-6.2),(26.4,-5.4),(28.8,-4.6),(30.9,-4.4),(33,-4.6), (34.9,-4.9),(36.2,-5),(38,-4.7),(37.5,-5.8),(37,-7),(36.4,-8.8),(35.5,-10.2), (34.6,-12),(33.5,-13.2),(32.4,-14.8),(31,-16), (29.9,-17),(28.2,-17.8),(26.5,-18.3),(24,-18.7),(21.6,-18.4), (19.6,-18)]
#error tuple object not callable


win.flip()
#alles binnen dezelfde win.flip om het allemaal op hetzelfde scherm te krijgen

time.sleep(10)




win.close()


