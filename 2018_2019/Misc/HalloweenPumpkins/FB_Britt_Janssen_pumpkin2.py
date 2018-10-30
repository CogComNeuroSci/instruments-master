import time
from psychopy import visual
from psychopy import core, visual, event
from psychopy.visual import ShapeStim

win = visual.Window(color = (-1,-1,-1), fullscr = True, monitor="testMonitor")


polygon = visual.Polygon(   win, edges = 200,   radius = (.12,.45), ori = 0,   pos = (-0.22,0), fillColor = (0.929,0.020,-0.835), lineColor= None)
polygon2 = visual.Polygon(   win, edges = 200,   radius = (.12,.45), ori = 0,   pos = (0.22,0), fillColor = (0.929,0.020,-0.835), lineColor= None)
polygon3 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (0.14,0), fillColor = (0.929,0.020,-0.835), lineColor= None)
polygon4 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (-0.14,0), fillColor = (0.929,0.020,-0.835), lineColor= None)
polygon5 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (0.08,0), fillColor = (0.929,0.020,-0.835), lineColor= None)
polygon6 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (-0.08,0), fillColor = (0.929,0.020,-0.835), lineColor= None)
polygon7 = visual.Polygon(   win, edges = 200,   radius = (.12,.43), ori = 0,   pos = (0,0), fillColor = (0.929,0.020,-0.835), lineColor= None)

gabor = visual.GratingStim(win, tex="tri", mask="gauss", texRes=200, 
size=[0.9, 1.0], sf=[10, 0], ori = 0, name='gabor1', opacity=.7)

triangle = visual.Polygon(win, edges = 3,radius = (.05,0.07),pos = (-0.12,0.15), fillColor = (0.694, -0.278, -0.906), lineColor= 'black', opacity=.6)
triangle2 = visual.Polygon(win, edges = 3,radius = (.05,0.07),pos = (0.12,0.15), fillColor = (0.694, -0.278, -0.906), lineColor= 'black', opacity=.6)

oog_klein = visual.Polygon(win, edges = 3,radius = (.030,0.043),pos = (-0.11,0.1435), fillColor = (0.694, 0.137, -0.796), lineColor = None, opacity=.6)
oog_klein2 = visual.Polygon(win, edges = 3,radius = (.030,0.043),pos = (0.11,0.1435), fillColor = (0.694, 0.137, -0.796),lineColor= None, opacity=.6)

neus = visual.Polygon(win, edges = 3,radius = (.05,0.07),pos = (0,0), fillColor = (0.694, -0.278, -0.906), lineColor= 'black', opacity=.6)
neus2 = visual.Polygon(win, edges = 3,radius = (.03,0.043),pos = (0,-0.012), fillColor = (0.694, 0.137, -0.796), lineColor= None, opacity=.6)

mondVert = [(-0.02, -0.04), (-0.03, -0.065), (-0.04,-0.04) ,(-0.07, -0.04), (-0.06,-0.09),(-0.04, -0.13), (-0.03,-0.1), (-0.02,-0.13),(0.02,-0.13),(0.03, -0.1), (0.04, -0.13), (0.06,-0.09), (0.07, -0.04), (0.04,-0.04) ,(0.03, -0.065), (0.02, -0.04)]
mond2Vert = [(-0.02, -0.04), (-0.03, -0.065), (-0.04,-0.04) ,(-0.07, -0.04), (-0.06,-0.09), (-0.03,-0.1), (-0.02,-0.13),(0.02,-0.13),(0.03, -0.1), (0.06,-0.09), (0.07, -0.04), (0.04,-0.04) ,(0.03, -0.065), (0.02, -0.04)]
mond = ShapeStim(win, vertices= mondVert, fillColor=(0.694, -0.278, -0.906), lineColor='black', opacity=.75, pos=(0, 0), size=2.5)
mond2 = ShapeStim(win, vertices= mond2Vert, fillColor=(0.700, -0.300, -0.890), lineColor=None, opacity=.6, pos=(0, -0.075), size=1.9)

message = visual.TextStim(win, text = 'HAPPY HALLOWEEN', pos = (0, -0.7), color = (0.929,0.020,-0.835))
message2 = visual.TextStim(win, text = 'HAPPY HALLOWEEN', pos = (0.007, -0.697), color = (0.929,0.020,-0.835), opacity=.6)


steelVert = [(0.23, 0.4), (0.27, 0.42), (0.268,0.35) ,(0.29,0.3), (0.25, 0.29),(0.21, 0.3), (0.228,0.35)]
steel = ShapeStim(win, vertices= steelVert, fillColor= 'green', lineColor=None, pos=(-0.47,-0.175), size=1.9)

steel2Vert = [(0.25, 0.41), (0.27, 0.42), (0.268,0.35) ,(0.29,0.3), (0.27, 0.295), (0.248,0.34)]
steel2 = ShapeStim(win, vertices= steel2Vert, fillColor= (-0.890,-0.129,-0.843), lineColor=None, pos=(-0.47,-0.175), size=1.9, opacity=.6)





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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()
message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(1)


############################################

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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()
#message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


############################################
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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()
message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


############################################
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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()
#message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


############################################
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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()
message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


############################################
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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()
#message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()
message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


############################################
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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
#message.draw()
#message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


############################################
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
neus.draw()
neus2.draw()
mond.draw()
mond2.draw
message.draw()
message2.draw()
steel.draw()
steel2.draw()


win.flip()
time.sleep(0.5)


############################################
############################################
win.close()