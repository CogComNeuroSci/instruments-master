import time
from psychopy import visual
# Esther: je bent visual hier voor een tweede keer aan het inladen. Dat is niet fout, maar je kan het lijntje code hierboven gewoon weglaten ;)
from psychopy import core, visual, event
# Esther: just so you know, je hebt hier ShapeStim expliciet ingeladen, maar je doet niet hetzelfde met Polygon of Rect
# Esther: opnieuw, dat is geen fout, maar een kleine inconsistentie (meer hierover in Chapter 6!)
from psychopy.visual import ShapeStim

# Esther: testMonitor is de default, dus je mag dat stukje zelfs weglaten hier
win = visual.Window(color = (-1,-1,-1), fullscr = True, monitor="testMonitor")

# Esther: ziet er goed uit, in Chapter 3 zal je zien dat je bv. de fillColor gewoon één keer op voorhand kan aanmaken en daar in de lijnen hieronder naar verwijzen.
# Esther: hetzelfde geldt voor de edges die allemaal de waarde 200 hebben
# Esther: bijvoorbeeld:
# PolygonColorBritt = (0.514, -0.184, -0.678)
# PolygonEdgesBritt = 200
# polygon = visual.Polygon(   win, edges = PolygonEdgesBritt,   radius = (.12,.45), ori = 0,   pos = (-0.22,0), fillColor = PolygonColorBritt, lineColor= None)
# polygon2 = visual.Polygon(   win, edges = PolygonEdgesBritt,   radius = (.12,.45), ori = 0,   pos = (0.22,0), fillColor = PolygonColorBritt, lineColor= None)
# Esther: het voordeel is dat je slechts één keer de waarde hoeft aan te passen in plaats van voor elke polygon apart ;)
# Esther: je kan dit idee ook doortrekken bij de andere vormen die hieronder aangemaakt worden.

polygon = visual.Polygon(   win, edges = 200,   radius = (.12,.45), ori = 0,   pos = (-0.22,0), fillColor = (0.514, -0.184, -0.678), lineColor= None)
polygon2 = visual.Polygon(   win, edges = 200,   radius = (.12,.45), ori = 0,   pos = (0.22,0), fillColor = (0.514, -0.184, -0.678), lineColor= None)
polygon3 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (0.14,0), fillColor = (0.514, -0.184, -0.678), lineColor= None)
polygon4 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (-0.14,0), fillColor = (0.514, -0.184, -0.678), lineColor= None)
polygon5 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (0.08,0), fillColor = (0.514, -0.184, -0.678), lineColor= None)
polygon6 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (-0.08,0), fillColor = (0.514, -0.184, -0.678), lineColor= None)
polygon7 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (0,0), fillColor = (0.514, -0.184, -0.678), lineColor= None)

# Esther: origineel, een gabor in een pompoen :D
gabor = visual.GratingStim(win, tex="tri", mask="gauss", texRes=200, 
size=[0.9, 1.0], sf=[10, 0], ori = 0, name='gabor1', opacity=.7)

triangle = visual.Polygon(win, edges = 3,radius = (.05,0.07),pos = (-0.12,0.15), fillColor = (0.694, -0.278, -0.906), lineColor= 'black', opacity=.6)
triangle2 = visual.Polygon(win, edges = 3,radius = (.05,0.07),pos = (0.12,0.15), fillColor = (0.694, -0.278, -0.906), lineColor= 'black', opacity=.6)

oog_klein = visual.Polygon(win, edges = 3,radius = (.030,0.043),pos = (-0.11,0.1435), fillColor = (0.694, 0.137, -0.796), lineColor = None, opacity=.6)
oog_klein2 = visual.Polygon(win, edges = 3,radius = (.030,0.043),pos = (0.11,0.1435), fillColor = (0.694, 0.137, -0.796),lineColor= None, opacity=.6)

# Esther: je gebruikt hier voor 1 keer in het script degrees in plaats van de standaard norm.
# Esther: dat is op zich niet fout, maar ik weet niet wat je bij je monitor settings hebt ingegeven als de afstand tot het scherm
# Esther: er is dus geen garantie dat je steeltje er bij mij even groot uit ziet als bij jou (het saat nu vlak boven de neus bij mij).
# Esther: in de class exercises van chapter 2 heb ik hier een opmerking over toegevoegd.
steeltje = visual.Rect(win, width = 1.6, height = 2.3, color = 'green', units = 'deg', pos = (0,5.6))

neus = visual.Polygon(win, edges = 3,radius = (.05,0.07),pos = (0,0), fillColor = (0.694, -0.278, -0.906), lineColor= 'black', opacity=.6)
neus2 = visual.Polygon(win, edges = 3,radius = (.03,0.043),pos = (0,-0.012), fillColor = (0.694, 0.137, -0.796), lineColor= None, opacity=.6)

mondVert = [(-0.02, -0.04), (-0.03, -0.065), (-0.04,-0.04) ,(-0.07, -0.04), (-0.06,-0.09),(-0.04, -0.13), (-0.03,-0.1), (-0.02,-0.13),(0.02,-0.13),(0.03, -0.1), (0.04, -0.13), (0.06,-0.09), (0.07, -0.04), (0.04,-0.04) ,(0.03, -0.065), (0.02, -0.04)]
mond2Vert = [(-0.02, -0.04), (-0.03, -0.065), (-0.04,-0.04) ,(-0.07, -0.04), (-0.06,-0.09), (-0.03,-0.1), (-0.02,-0.13),(0.02,-0.13),(0.03, -0.1), (0.06,-0.09), (0.07, -0.04), (0.04,-0.04) ,(0.03, -0.065), (0.02, -0.04)]
mond = ShapeStim(win, vertices= mondVert, fillColor=(0.694, -0.278, -0.906), lineColor='black', opacity=.75, pos=(0, 0), size=2.5)
mond2 = ShapeStim(win, vertices= mond2Vert, fillColor=(0.700, -0.300, -0.890), lineColor=None, opacity=.6, pos=(0, -0.075), size=1.9)

message = visual.TextStim(win, text = 'Happy Halloween', pos = (0, -0.7), color = (0.694, 0.137, -0.796))
message.font = 'Matura MT Script Capitals'






polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()


win.flip()
time.sleep(1)

#########################################################################

polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()


win.flip()
time.sleep(0.5)

#########################################################################

polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()

win.flip()
time.sleep(0.5)

#########################################################################

polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()


win.flip()
time.sleep(0.5)



#########################################################################

polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
polygon.draw()
polygon2.draw()
polygon3.draw()
polygon4.draw()
polygon5.draw()
polygon6.draw()
polygon7.draw()
gabor.draw()
triangle.draw()
triangle2.draw()
oog_klein.draw()
oog_klein2.draw()
steeltje.draw()
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()


win.flip()
time.sleep(0.5)



#########################################################################
win.close()