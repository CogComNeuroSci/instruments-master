from psychopy import visual
from psychopy.visual import ShapeStim
import time

#window
win = visual.Window(fullscr=True,color=[-0.851,-0.843,-0.780])



 
#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

win.flip()
time.sleep(1)
#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

#tekst
Tekst= visual.TextStim(win, text="Happy Halloween!", font='Matura MT Script Capitals', color=[0.020,-0.984,-0.984], height= 0.2, bold=True, pos=(0,-0.8))
Tekst.draw()


win.flip()
time.sleep(0.5)
#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()


#tekst
Tekst= visual.TextStim(win, text="Happy Halloween!", font='Matura MT Script Capitals', color=[0.020,-0.984,-0.984], height= 0.2, bold=True, pos=(0,-0.8))
Tekst.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

#tekst
Tekst= visual.TextStim(win, text="Happy Halloween!", font='Matura MT Script Capitals', color=[0.020,-0.984,-0.984], height= 0.2, bold=True, pos=(0,-0.8))
Tekst.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

#tekst
Tekst= visual.TextStim(win, text="Happy Halloween!", font='Matura MT Script Capitals', color=[0.020,-0.984,-0.984], height= 0.2, bold=True, pos=(0,-0.8))
Tekst.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

#tekst
Tekst= visual.TextStim(win, text="Happy Halloween!", font='Matura MT Script Capitals', color=[0.020,-0.984,-0.984], height= 0.2, bold=True, pos=(0,-0.8))
Tekst.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

#tekst
Tekst= visual.TextStim(win, text="Happy Halloween!", font='Matura MT Script Capitals', color=[0.020,-0.984,-0.984], height= 0.2, bold=True, pos=(0,-0.8))
Tekst.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

win.flip()
time.sleep(0.5)

#ellips
pompoen= visual.Circle(win,radius=.75,edges=99,color=[0.812,-0.247,-0.961],pos=[0,0.07])
pompoen.draw()

#achtergrond figuur
bg= visual.Circle(win,radius=.6,edges=99,color='yellow',pos=[0,0.07])
bg.draw()


#linkse blok
rectLinks= visual.Rect(win, width=0.3, height=0.5, color=[0.812,-0.247,-0.961], pos=[-0.3,-0.25])
rectLinks.draw()
rectLinks= visual.Rect(win, width=0.6, height=0.1, color=[0.812,-0.247,-0.961], pos=[0,-0.5])
rectLinks.draw()

RaamLniveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[-0.3,-0.3])
RaamLniveau1.draw()

#dak links
dakLinks= visual.Polygon(win, edges=3, radius= 0.25, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.3,0.1])
dakLinks.draw()

Dakraam= visual.Rect(win, width=0.07, height=0.1, color='yellow', pos=[-0.3,0])
Dakraam.draw()
DakraamTop= visual.Polygon(win, edges=3, radius= 0.04, lineColor= 'yellow', fillColor= 'yellow', pos=[-0.3,0.07])
DakraamTop.draw()

#lange rechthoek rechts
rectRechts= visual.Rect(win, width=0.5, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,-0.3])
rectRechts.draw()

RaamR1niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0,-0.3])
RaamR1niveau1.draw()
RaamR2niveau1= visual.Rect(win, width=0.1, height=0.25, color='yellow', pos=[0.2,-0.3])
RaamR2niveau1.draw()

dakRechts= visual.Polygon(win, edges=3, radius= 0.1, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.3,-0.1])
dakRechts.draw()

#niveau 2
niveau2= visual.Rect(win, width=0.3, height=0.4, color=[0.812,-0.247,-0.961], pos=[0.1,0])
niveau2.draw()

RaamLniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.05,0])
RaamLniveau2.draw()
RaamRniveau2= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.15,0])
RaamRniveau2.draw()

Niv2dakLinks= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[-0.02,0.23])
Niv2dakLinks.draw()
Niv2dakRechts= visual.Polygon(win, edges=3, radius= 0.06, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.22,0.23])
Niv2dakRechts.draw()

#niveau 3
niveau3= visual.Rect(win, width=0.15, height=0.3, color=[0.812,-0.247,-0.961], pos=[0.1,0.3])
niveau3.draw()

Raamniveau3= visual.Rect(win, width=0.06, height=0.2, color='yellow', pos=[0.1,0.3])
Raamniveau3.draw()

Niv3dak= visual.Polygon(win, edges=3, radius= 0.12, lineColor= [0.812,-0.247,-0.961], fillColor= [0.812,-0.247,-0.961], pos=[0.1,0.5])
Niv3dak.draw()

#sterren
star1Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star1 = ShapeStim(win, vertices=star1Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
star1.draw()

star2Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star2 = ShapeStim(win, vertices=star2Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.25,0.45))
star2.draw()

star3Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star3 = ShapeStim(win, vertices=star3Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.1, 0.15))
star3.draw()

star4Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star4 = ShapeStim(win, vertices=star4Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.3,0.3))
star4.draw()

star5Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star5 = ShapeStim(win, vertices=star5Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.45, -0.1))
star5.draw()

star6Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star6 = ShapeStim(win, vertices=star6Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (0.53, 0.1))
star6.draw()

star7Vert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor=[0.812,-0.247,-0.961], lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos= (-0, 0.55))
star7.draw()


#steeltje
steelVert= [(6.5,7.3),(8,7.5),(7,6),(6,6)]
steel = ShapeStim(win, vertices=steelVert, fillColor='green', lineWidth=0.1, lineColor=[0.812,-0.247,-0.961],size=(0.07,0.1), pos=(-0.5,0.2))
steel.draw()

#tekst
Tekst= visual.TextStim(win, text="Happy Halloween!", font='Matura MT Script Capitals', color=[0.020,-0.984,-0.984], height= 0.2, bold=True, pos=(0,-0.8))
Tekst.draw()

win.flip()
time.sleep(1)
win.close()