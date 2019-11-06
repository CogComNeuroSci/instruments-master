from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time
win = visual.Window(size = [800,600], color = 'black')
pumpkinVert = [(0.0, 0.75), (0.13, 0.63), (0.26, 0.75), (0.75, 0.5), (0.75, -0.5), (0.26, -0.75), (0.13, -0.63), (0.0, -0.75), (-0.13, -0.63), (-0.26, -0.75), (-0.75, -0.5), (-0.75, 0.5), (-0.26, 0.75), (-0.13, 0.63)]
pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor=(0.835,0.271,-0.780), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.835,0.271,-0.780), lineColorSpace = 'rgb')
pumpkin.draw()
lijn1Vert = [(-0.26, 0.75), (-0.6, 0.2), (-0.6, -0.2), (-0.26, -0.75)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, lineWidth=2, lineColor = (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn1.draw()
lijn2Vert = [(-0.13, 0.63), (-0.3, 0.1), (-0.3, -0.1), (-0.13, -0.63)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn2.draw()
lijn3Vert = [(0.13, 0.63), (0.3, 0.1), (0.3, -0.1), (0.13, -0.63)] 
lijn3 = ShapeStim(win, vertices=lijn3Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn3.draw()
lijn4Vert = [(0.26, 0.75), (0.6, 0.2), (0.6, -0.2), (0.26, -0.75)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn4.draw()
neusVert = [(0.0,0.15), (0.1,-0.1), (-0.1,-0.1)]
neus = ShapeStim(win, vertices=neusVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neus.draw()
oog1Vert = [(-0.15, 0.2), (-0.45, 0.2), (-0.45, 0.5), (-0.35, 0.3)]
oog1 = ShapeStim(win, vertices=oog1Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog1.draw()
oog2Vert = [(0.15, 0.2), (0.45, 0.2), (0.45, 0.5), (0.35, 0.3)]
oog2 = ShapeStim(win, vertices=oog2Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog2.draw()
steelVert = [(0.0, 0.75), (0.0, 0.9), (0.13, 1), (0.26, 0.85), (0.13, 0.75), (0.07, 0.8)]
steel = ShapeStim(win, vertices=steelVert, fillColor=(-0.373,0.098,-0.733), fillColorSpace = 'rgb', lineWidth=2, lineColor=(-0.373,0.098,-0.733), lineColorSpace = 'rgb')
steel.draw()
mondVert = [(0.1, -0.35), (0.1, -0.25), (0.3, -0.25), (0.3, -0.35), (0.5, -0.35), (0.5, -0.25), (0.7, 0.0), (0.5, -0.5), (0.3, -0.5), (0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.3, -0.5), (-0.5, -0.5), (-0.7, 0.0), (-0.5, -0.25), (-0.5, -0.35), (-0.3, -0.35), (-0.3, -0.25), (-0.1, -0.25), (-0.1, -0.35)]
mond = ShapeStim(win, vertices=mondVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
mond.draw()
schaduw1Vert = [(-0.7, 0.0), (-0.45, -0.45),(-0.3, -0.45), (-0.3, -0.5), (-0.5, -0.5)]
schaduw1 = ShapeStim(win, vertices=schaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw1.draw()
schaduw2Vert = [(0.7, 0.0), (0.45, -0.45),(0.3, -0.45), (0.3, -0.5), (0.5, -0.5)]
schaduw2 = ShapeStim(win, vertices=schaduw2Vert, fillColor= (0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw2.draw()
schaduw3Vert = [(-0.3, -0.35), (-0.25, -0.25), (-0.3, -0.25)]
schaduw3 = ShapeStim(win, vertices=schaduw3Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw3.draw()
schaduw4Vert = [(0.3, -0.35), (0.25, -0.25), (0.3, -0.25)]
schaduw4 = ShapeStim(win, vertices=schaduw4Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw4.draw()
schaduw7Vert = [(0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.25, -0.35), (-0.05, -0.35), (-0.05, -0.45), (0.05, -0.45), (0.05, -0.35), (0.25, -0.35)]
schaduw7 = ShapeStim(win, vertices=schaduw7Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw7.draw()
lijn5Vert = [(-0.1, -0.4), (-0.05, -0.35)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn5.draw()
lijn6Vert = [(-0.1, -0.5), (-0.05, -0.45)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn6.draw()
lijn7Vert = [(0.1, -0.4), (0.05, -0.35)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn7.draw()
lijn8Vert = [(0.1, -0.5), (0.05, -0.45)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn8.draw()
lijn9Vert = [(-0.5, -0.5), (-0.45, -0.45)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn9.draw()
lijn10Vert = [(0.5, -0.5), (0.45, -0.45)]
lijn10 = ShapeStim(win, vertices=lijn10Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn10.draw()
oogSchaduw1Vert = [(-0.45, 0.5), (-0.4, 0.4),(-0.4, 0.25), (-0.25, 0.25), (-0.15, 0.2), (-0.45, 0.2)]
oogSchaduw1 = ShapeStim(win, vertices= oogSchaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw1.draw()
oogSchaduw2Vert = [(0.45, 0.5), (0.4, 0.4),(0.4, 0.25), (0.25, 0.25), (0.15, 0.2), (0.45, 0.2)]
oogSchaduw2 = ShapeStim(win, vertices= oogSchaduw2Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw2.draw()
lijn11Vert = [(-0.45, 0.2), (-0.4, 0.25)]
lijn11 = ShapeStim(win, vertices=lijn11Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn11.draw()
lijn12Vert = [(0.45, 0.2), (0.4, 0.25)]
lijn12 = ShapeStim(win, vertices=lijn12Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn12.draw()
neusSchaduwVert = [(0.1,-0.1), (-0.1, -0.1), (-0.075, -0.05), (0.075, -0.05)]
neusSchaduw = ShapeStim(win, vertices= neusSchaduwVert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neusSchaduw.draw()
stim = visual.TextStim(win, text = "Happy Halloween!", font = 'Juice ITC', color = 'red', pos = [0.0, -0.85], bold = True, italic = False, height = 0.2)
stim.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0, 0.75), (0.13, 0.63), (0.26, 0.75), (0.75, 0.5), (0.75, -0.5), (0.26, -0.75), (0.13, -0.63), (0.0, -0.75), (-0.13, -0.63), (-0.26, -0.75), (-0.75, -0.5), (-0.75, 0.5), (-0.26, 0.75), (-0.13, 0.63)]
pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor=(0.835,0.271,-0.780), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.835,0.271,-0.780), lineColorSpace = 'rgb')
pumpkin.draw()
lijn1Vert = [(-0.26, 0.75), (-0.6, 0.2), (-0.6, -0.2), (-0.26, -0.75)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, lineWidth=2, lineColor = (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn1.draw()
lijn2Vert = [(-0.13, 0.63), (-0.3, 0.1), (-0.3, -0.1), (-0.13, -0.63)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn2.draw()
lijn3Vert = [(0.13, 0.63), (0.3, 0.1), (0.3, -0.1), (0.13, -0.63)] 
lijn3 = ShapeStim(win, vertices=lijn3Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn3.draw()
lijn4Vert = [(0.26, 0.75), (0.6, 0.2), (0.6, -0.2), (0.26, -0.75)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn4.draw()
neusVert = [(0.0,0.15), (0.1,-0.1), (-0.1,-0.1)]
neus = ShapeStim(win, vertices=neusVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neus.draw()
oog1Vert = [(-0.15, 0.2), (-0.45, 0.2), (-0.45, 0.5), (-0.35, 0.3)]
oog1 = ShapeStim(win, vertices=oog1Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog1.draw()
oog2Vert = [(0.15, 0.2), (0.45, 0.2), (0.45, 0.5), (0.35, 0.3)]
oog2 = ShapeStim(win, vertices=oog2Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog2.draw()
steelVert = [(0.0, 0.75), (0.0, 0.9), (0.13, 1), (0.26, 0.85), (0.13, 0.75), (0.07, 0.8)]
steel = ShapeStim(win, vertices=steelVert, fillColor=(-0.373,0.098,-0.733), fillColorSpace = 'rgb', lineWidth=2, lineColor=(-0.373,0.098,-0.733), lineColorSpace = 'rgb')
steel.draw()
mondVert = [(0.1, -0.35), (0.1, -0.25), (0.3, -0.25), (0.3, -0.35), (0.5, -0.35), (0.5, -0.25), (0.7, 0.0), (0.5, -0.5), (0.3, -0.5), (0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.3, -0.5), (-0.5, -0.5), (-0.7, 0.0), (-0.5, -0.25), (-0.5, -0.35), (-0.3, -0.35), (-0.3, -0.25), (-0.1, -0.25), (-0.1, -0.35)]
mond = ShapeStim(win, vertices=mondVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
mond.draw()
schaduw1Vert = [(-0.7, 0.0), (-0.45, -0.45),(-0.3, -0.45), (-0.3, -0.5), (-0.5, -0.5)]
schaduw1 = ShapeStim(win, vertices=schaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw1.draw()
schaduw2Vert = [(0.7, 0.0), (0.45, -0.45),(0.3, -0.45), (0.3, -0.5), (0.5, -0.5)]
schaduw2 = ShapeStim(win, vertices=schaduw2Vert, fillColor= (0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw2.draw()
schaduw3Vert = [(-0.3, -0.35), (-0.25, -0.25), (-0.3, -0.25)]
schaduw3 = ShapeStim(win, vertices=schaduw3Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw3.draw()
schaduw4Vert = [(0.3, -0.35), (0.25, -0.25), (0.3, -0.25)]
schaduw4 = ShapeStim(win, vertices=schaduw4Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw4.draw()
schaduw7Vert = [(0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.25, -0.35), (-0.05, -0.35), (-0.05, -0.45), (0.05, -0.45), (0.05, -0.35), (0.25, -0.35)]
schaduw7 = ShapeStim(win, vertices=schaduw7Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw7.draw()
lijn5Vert = [(-0.1, -0.4), (-0.05, -0.35)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn5.draw()
lijn6Vert = [(-0.1, -0.5), (-0.05, -0.45)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn6.draw()
lijn7Vert = [(0.1, -0.4), (0.05, -0.35)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn7.draw()
lijn8Vert = [(0.1, -0.5), (0.05, -0.45)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn8.draw()
lijn9Vert = [(-0.5, -0.5), (-0.45, -0.45)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn9.draw()
lijn10Vert = [(0.5, -0.5), (0.45, -0.45)]
lijn10 = ShapeStim(win, vertices=lijn10Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn10.draw()
oogSchaduw1Vert = [(-0.45, 0.5), (-0.4, 0.4),(-0.4, 0.25), (-0.25, 0.25), (-0.15, 0.2), (-0.45, 0.2)]
oogSchaduw1 = ShapeStim(win, vertices= oogSchaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw1.draw()
oogSchaduw2Vert = [(0.45, 0.5), (0.4, 0.4),(0.4, 0.25), (0.25, 0.25), (0.15, 0.2), (0.45, 0.2)]
oogSchaduw2 = ShapeStim(win, vertices= oogSchaduw2Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw2.draw()
lijn11Vert = [(-0.45, 0.2), (-0.4, 0.25)]
lijn11 = ShapeStim(win, vertices=lijn11Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn11.draw()
lijn12Vert = [(0.45, 0.2), (0.4, 0.25)]
lijn12 = ShapeStim(win, vertices=lijn12Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn12.draw()
neusSchaduwVert = [(0.1,-0.1), (-0.1, -0.1), (-0.075, -0.05), (0.075, -0.05)]
neusSchaduw = ShapeStim(win, vertices= neusSchaduwVert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neusSchaduw.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0, 0.75), (0.13, 0.63), (0.26, 0.75), (0.75, 0.5), (0.75, -0.5), (0.26, -0.75), (0.13, -0.63), (0.0, -0.75), (-0.13, -0.63), (-0.26, -0.75), (-0.75, -0.5), (-0.75, 0.5), (-0.26, 0.75), (-0.13, 0.63)]
pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor=(0.835,0.271,-0.780), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.835,0.271,-0.780), lineColorSpace = 'rgb')
pumpkin.draw()
lijn1Vert = [(-0.26, 0.75), (-0.6, 0.2), (-0.6, -0.2), (-0.26, -0.75)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, lineWidth=2, lineColor = (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn1.draw()
lijn2Vert = [(-0.13, 0.63), (-0.3, 0.1), (-0.3, -0.1), (-0.13, -0.63)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn2.draw()
lijn3Vert = [(0.13, 0.63), (0.3, 0.1), (0.3, -0.1), (0.13, -0.63)] 
lijn3 = ShapeStim(win, vertices=lijn3Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn3.draw()
lijn4Vert = [(0.26, 0.75), (0.6, 0.2), (0.6, -0.2), (0.26, -0.75)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn4.draw()
neusVert = [(0.0,0.15), (0.1,-0.1), (-0.1,-0.1)]
neus = ShapeStim(win, vertices=neusVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neus.draw()
oog1Vert = [(-0.15, 0.2), (-0.45, 0.2), (-0.45, 0.5), (-0.35, 0.3)]
oog1 = ShapeStim(win, vertices=oog1Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog1.draw()
oog2Vert = [(0.15, 0.2), (0.45, 0.2), (0.45, 0.5), (0.35, 0.3)]
oog2 = ShapeStim(win, vertices=oog2Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog2.draw()
steelVert = [(0.0, 0.75), (0.0, 0.9), (0.13, 1), (0.26, 0.85), (0.13, 0.75), (0.07, 0.8)]
steel = ShapeStim(win, vertices=steelVert, fillColor=(-0.373,0.098,-0.733), fillColorSpace = 'rgb', lineWidth=2, lineColor=(-0.373,0.098,-0.733), lineColorSpace = 'rgb')
steel.draw()
mondVert = [(0.1, -0.35), (0.1, -0.25), (0.3, -0.25), (0.3, -0.35), (0.5, -0.35), (0.5, -0.25), (0.7, 0.0), (0.5, -0.5), (0.3, -0.5), (0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.3, -0.5), (-0.5, -0.5), (-0.7, 0.0), (-0.5, -0.25), (-0.5, -0.35), (-0.3, -0.35), (-0.3, -0.25), (-0.1, -0.25), (-0.1, -0.35)]
mond = ShapeStim(win, vertices=mondVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
mond.draw()
schaduw1Vert = [(-0.7, 0.0), (-0.45, -0.45),(-0.3, -0.45), (-0.3, -0.5), (-0.5, -0.5)]
schaduw1 = ShapeStim(win, vertices=schaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw1.draw()
schaduw2Vert = [(0.7, 0.0), (0.45, -0.45),(0.3, -0.45), (0.3, -0.5), (0.5, -0.5)]
schaduw2 = ShapeStim(win, vertices=schaduw2Vert, fillColor= (0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw2.draw()
schaduw3Vert = [(-0.3, -0.35), (-0.25, -0.25), (-0.3, -0.25)]
schaduw3 = ShapeStim(win, vertices=schaduw3Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw3.draw()
schaduw4Vert = [(0.3, -0.35), (0.25, -0.25), (0.3, -0.25)]
schaduw4 = ShapeStim(win, vertices=schaduw4Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw4.draw()
schaduw7Vert = [(0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.25, -0.35), (-0.05, -0.35), (-0.05, -0.45), (0.05, -0.45), (0.05, -0.35), (0.25, -0.35)]
schaduw7 = ShapeStim(win, vertices=schaduw7Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw7.draw()
lijn5Vert = [(-0.1, -0.4), (-0.05, -0.35)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn5.draw()
lijn6Vert = [(-0.1, -0.5), (-0.05, -0.45)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn6.draw()
lijn7Vert = [(0.1, -0.4), (0.05, -0.35)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn7.draw()
lijn8Vert = [(0.1, -0.5), (0.05, -0.45)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn8.draw()
lijn9Vert = [(-0.5, -0.5), (-0.45, -0.45)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn9.draw()
lijn10Vert = [(0.5, -0.5), (0.45, -0.45)]
lijn10 = ShapeStim(win, vertices=lijn10Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn10.draw()
oogSchaduw1Vert = [(-0.45, 0.5), (-0.4, 0.4),(-0.4, 0.25), (-0.25, 0.25), (-0.15, 0.2), (-0.45, 0.2)]
oogSchaduw1 = ShapeStim(win, vertices= oogSchaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw1.draw()
oogSchaduw2Vert = [(0.45, 0.5), (0.4, 0.4),(0.4, 0.25), (0.25, 0.25), (0.15, 0.2), (0.45, 0.2)]
oogSchaduw2 = ShapeStim(win, vertices= oogSchaduw2Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw2.draw()
lijn11Vert = [(-0.45, 0.2), (-0.4, 0.25)]
lijn11 = ShapeStim(win, vertices=lijn11Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn11.draw()
lijn12Vert = [(0.45, 0.2), (0.4, 0.25)]
lijn12 = ShapeStim(win, vertices=lijn12Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn12.draw()
neusSchaduwVert = [(0.1,-0.1), (-0.1, -0.1), (-0.075, -0.05), (0.075, -0.05)]
neusSchaduw = ShapeStim(win, vertices= neusSchaduwVert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neusSchaduw.draw()
stim = visual.TextStim(win, text = "Happy Halloween!", font = 'Juice ITC', color = 'red', pos = [0.0, -0.85], bold = True, italic = False, height = 0.2)
stim.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0, 0.75), (0.13, 0.63), (0.26, 0.75), (0.75, 0.5), (0.75, -0.5), (0.26, -0.75), (0.13, -0.63), (0.0, -0.75), (-0.13, -0.63), (-0.26, -0.75), (-0.75, -0.5), (-0.75, 0.5), (-0.26, 0.75), (-0.13, 0.63)]
pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor=(0.835,0.271,-0.780), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.835,0.271,-0.780), lineColorSpace = 'rgb')
pumpkin.draw()
lijn1Vert = [(-0.26, 0.75), (-0.6, 0.2), (-0.6, -0.2), (-0.26, -0.75)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, lineWidth=2, lineColor = (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn1.draw()
lijn2Vert = [(-0.13, 0.63), (-0.3, 0.1), (-0.3, -0.1), (-0.13, -0.63)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn2.draw()
lijn3Vert = [(0.13, 0.63), (0.3, 0.1), (0.3, -0.1), (0.13, -0.63)] 
lijn3 = ShapeStim(win, vertices=lijn3Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn3.draw()
lijn4Vert = [(0.26, 0.75), (0.6, 0.2), (0.6, -0.2), (0.26, -0.75)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn4.draw()
neusVert = [(0.0,0.15), (0.1,-0.1), (-0.1,-0.1)]
neus = ShapeStim(win, vertices=neusVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neus.draw()
oog1Vert = [(-0.15, 0.2), (-0.45, 0.2), (-0.45, 0.5), (-0.35, 0.3)]
oog1 = ShapeStim(win, vertices=oog1Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog1.draw()
oog2Vert = [(0.15, 0.2), (0.45, 0.2), (0.45, 0.5), (0.35, 0.3)]
oog2 = ShapeStim(win, vertices=oog2Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog2.draw()
steelVert = [(0.0, 0.75), (0.0, 0.9), (0.13, 1), (0.26, 0.85), (0.13, 0.75), (0.07, 0.8)]
steel = ShapeStim(win, vertices=steelVert, fillColor=(-0.373,0.098,-0.733), fillColorSpace = 'rgb', lineWidth=2, lineColor=(-0.373,0.098,-0.733), lineColorSpace = 'rgb')
steel.draw()
mondVert = [(0.1, -0.35), (0.1, -0.25), (0.3, -0.25), (0.3, -0.35), (0.5, -0.35), (0.5, -0.25), (0.7, 0.0), (0.5, -0.5), (0.3, -0.5), (0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.3, -0.5), (-0.5, -0.5), (-0.7, 0.0), (-0.5, -0.25), (-0.5, -0.35), (-0.3, -0.35), (-0.3, -0.25), (-0.1, -0.25), (-0.1, -0.35)]
mond = ShapeStim(win, vertices=mondVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
mond.draw()
schaduw1Vert = [(-0.7, 0.0), (-0.45, -0.45),(-0.3, -0.45), (-0.3, -0.5), (-0.5, -0.5)]
schaduw1 = ShapeStim(win, vertices=schaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw1.draw()
schaduw2Vert = [(0.7, 0.0), (0.45, -0.45),(0.3, -0.45), (0.3, -0.5), (0.5, -0.5)]
schaduw2 = ShapeStim(win, vertices=schaduw2Vert, fillColor= (0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw2.draw()
schaduw3Vert = [(-0.3, -0.35), (-0.25, -0.25), (-0.3, -0.25)]
schaduw3 = ShapeStim(win, vertices=schaduw3Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw3.draw()
schaduw4Vert = [(0.3, -0.35), (0.25, -0.25), (0.3, -0.25)]
schaduw4 = ShapeStim(win, vertices=schaduw4Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw4.draw()
schaduw7Vert = [(0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.25, -0.35), (-0.05, -0.35), (-0.05, -0.45), (0.05, -0.45), (0.05, -0.35), (0.25, -0.35)]
schaduw7 = ShapeStim(win, vertices=schaduw7Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw7.draw()
lijn5Vert = [(-0.1, -0.4), (-0.05, -0.35)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn5.draw()
lijn6Vert = [(-0.1, -0.5), (-0.05, -0.45)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn6.draw()
lijn7Vert = [(0.1, -0.4), (0.05, -0.35)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn7.draw()
lijn8Vert = [(0.1, -0.5), (0.05, -0.45)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn8.draw()
lijn9Vert = [(-0.5, -0.5), (-0.45, -0.45)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn9.draw()
lijn10Vert = [(0.5, -0.5), (0.45, -0.45)]
lijn10 = ShapeStim(win, vertices=lijn10Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn10.draw()
oogSchaduw1Vert = [(-0.45, 0.5), (-0.4, 0.4),(-0.4, 0.25), (-0.25, 0.25), (-0.15, 0.2), (-0.45, 0.2)]
oogSchaduw1 = ShapeStim(win, vertices= oogSchaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw1.draw()
oogSchaduw2Vert = [(0.45, 0.5), (0.4, 0.4),(0.4, 0.25), (0.25, 0.25), (0.15, 0.2), (0.45, 0.2)]
oogSchaduw2 = ShapeStim(win, vertices= oogSchaduw2Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw2.draw()
lijn11Vert = [(-0.45, 0.2), (-0.4, 0.25)]
lijn11 = ShapeStim(win, vertices=lijn11Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn11.draw()
lijn12Vert = [(0.45, 0.2), (0.4, 0.25)]
lijn12 = ShapeStim(win, vertices=lijn12Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn12.draw()
neusSchaduwVert = [(0.1,-0.1), (-0.1, -0.1), (-0.075, -0.05), (0.075, -0.05)]
neusSchaduw = ShapeStim(win, vertices= neusSchaduwVert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neusSchaduw.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0, 0.75), (0.13, 0.63), (0.26, 0.75), (0.75, 0.5), (0.75, -0.5), (0.26, -0.75), (0.13, -0.63), (0.0, -0.75), (-0.13, -0.63), (-0.26, -0.75), (-0.75, -0.5), (-0.75, 0.5), (-0.26, 0.75), (-0.13, 0.63)]
pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor=(0.835,0.271,-0.780), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.835,0.271,-0.780), lineColorSpace = 'rgb')
pumpkin.draw()
lijn1Vert = [(-0.26, 0.75), (-0.6, 0.2), (-0.6, -0.2), (-0.26, -0.75)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, lineWidth=2, lineColor = (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn1.draw()
lijn2Vert = [(-0.13, 0.63), (-0.3, 0.1), (-0.3, -0.1), (-0.13, -0.63)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn2.draw()
lijn3Vert = [(0.13, 0.63), (0.3, 0.1), (0.3, -0.1), (0.13, -0.63)] 
lijn3 = ShapeStim(win, vertices=lijn3Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn3.draw()
lijn4Vert = [(0.26, 0.75), (0.6, 0.2), (0.6, -0.2), (0.26, -0.75)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn4.draw()
neusVert = [(0.0,0.15), (0.1,-0.1), (-0.1,-0.1)]
neus = ShapeStim(win, vertices=neusVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neus.draw()
oog1Vert = [(-0.15, 0.2), (-0.45, 0.2), (-0.45, 0.5), (-0.35, 0.3)]
oog1 = ShapeStim(win, vertices=oog1Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog1.draw()
oog2Vert = [(0.15, 0.2), (0.45, 0.2), (0.45, 0.5), (0.35, 0.3)]
oog2 = ShapeStim(win, vertices=oog2Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog2.draw()
steelVert = [(0.0, 0.75), (0.0, 0.9), (0.13, 1), (0.26, 0.85), (0.13, 0.75), (0.07, 0.8)]
steel = ShapeStim(win, vertices=steelVert, fillColor=(-0.373,0.098,-0.733), fillColorSpace = 'rgb', lineWidth=2, lineColor=(-0.373,0.098,-0.733), lineColorSpace = 'rgb')
steel.draw()
mondVert = [(0.1, -0.35), (0.1, -0.25), (0.3, -0.25), (0.3, -0.35), (0.5, -0.35), (0.5, -0.25), (0.7, 0.0), (0.5, -0.5), (0.3, -0.5), (0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.3, -0.5), (-0.5, -0.5), (-0.7, 0.0), (-0.5, -0.25), (-0.5, -0.35), (-0.3, -0.35), (-0.3, -0.25), (-0.1, -0.25), (-0.1, -0.35)]
mond = ShapeStim(win, vertices=mondVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
mond.draw()
schaduw1Vert = [(-0.7, 0.0), (-0.45, -0.45),(-0.3, -0.45), (-0.3, -0.5), (-0.5, -0.5)]
schaduw1 = ShapeStim(win, vertices=schaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw1.draw()
schaduw2Vert = [(0.7, 0.0), (0.45, -0.45),(0.3, -0.45), (0.3, -0.5), (0.5, -0.5)]
schaduw2 = ShapeStim(win, vertices=schaduw2Vert, fillColor= (0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw2.draw()
schaduw3Vert = [(-0.3, -0.35), (-0.25, -0.25), (-0.3, -0.25)]
schaduw3 = ShapeStim(win, vertices=schaduw3Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw3.draw()
schaduw4Vert = [(0.3, -0.35), (0.25, -0.25), (0.3, -0.25)]
schaduw4 = ShapeStim(win, vertices=schaduw4Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw4.draw()
schaduw7Vert = [(0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.25, -0.35), (-0.05, -0.35), (-0.05, -0.45), (0.05, -0.45), (0.05, -0.35), (0.25, -0.35)]
schaduw7 = ShapeStim(win, vertices=schaduw7Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw7.draw()
lijn5Vert = [(-0.1, -0.4), (-0.05, -0.35)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn5.draw()
lijn6Vert = [(-0.1, -0.5), (-0.05, -0.45)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn6.draw()
lijn7Vert = [(0.1, -0.4), (0.05, -0.35)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn7.draw()
lijn8Vert = [(0.1, -0.5), (0.05, -0.45)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn8.draw()
lijn9Vert = [(-0.5, -0.5), (-0.45, -0.45)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn9.draw()
lijn10Vert = [(0.5, -0.5), (0.45, -0.45)]
lijn10 = ShapeStim(win, vertices=lijn10Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn10.draw()
oogSchaduw1Vert = [(-0.45, 0.5), (-0.4, 0.4),(-0.4, 0.25), (-0.25, 0.25), (-0.15, 0.2), (-0.45, 0.2)]
oogSchaduw1 = ShapeStim(win, vertices= oogSchaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw1.draw()
oogSchaduw2Vert = [(0.45, 0.5), (0.4, 0.4),(0.4, 0.25), (0.25, 0.25), (0.15, 0.2), (0.45, 0.2)]
oogSchaduw2 = ShapeStim(win, vertices= oogSchaduw2Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw2.draw()
lijn11Vert = [(-0.45, 0.2), (-0.4, 0.25)]
lijn11 = ShapeStim(win, vertices=lijn11Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn11.draw()
lijn12Vert = [(0.45, 0.2), (0.4, 0.25)]
lijn12 = ShapeStim(win, vertices=lijn12Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn12.draw()
neusSchaduwVert = [(0.1,-0.1), (-0.1, -0.1), (-0.075, -0.05), (0.075, -0.05)]
neusSchaduw = ShapeStim(win, vertices= neusSchaduwVert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neusSchaduw.draw()
stim = visual.TextStim(win, text = "Happy Halloween!", font = 'Juice ITC', color = 'red', pos = [0.0, -0.85], bold = True, italic = False, height = 0.2)
stim.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0, 0.75), (0.13, 0.63), (0.26, 0.75), (0.75, 0.5), (0.75, -0.5), (0.26, -0.75), (0.13, -0.63), (0.0, -0.75), (-0.13, -0.63), (-0.26, -0.75), (-0.75, -0.5), (-0.75, 0.5), (-0.26, 0.75), (-0.13, 0.63)]
pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor=(0.835,0.271,-0.780), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.835,0.271,-0.780), lineColorSpace = 'rgb')
pumpkin.draw()
lijn1Vert = [(-0.26, 0.75), (-0.6, 0.2), (-0.6, -0.2), (-0.26, -0.75)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, lineWidth=2, lineColor = (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn1.draw()
lijn2Vert = [(-0.13, 0.63), (-0.3, 0.1), (-0.3, -0.1), (-0.13, -0.63)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn2.draw()
lijn3Vert = [(0.13, 0.63), (0.3, 0.1), (0.3, -0.1), (0.13, -0.63)] 
lijn3 = ShapeStim(win, vertices=lijn3Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn3.draw()
lijn4Vert = [(0.26, 0.75), (0.6, 0.2), (0.6, -0.2), (0.26, -0.75)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn4.draw()
neusVert = [(0.0,0.15), (0.1,-0.1), (-0.1,-0.1)]
neus = ShapeStim(win, vertices=neusVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neus.draw()
oog1Vert = [(-0.15, 0.2), (-0.45, 0.2), (-0.45, 0.5), (-0.35, 0.3)]
oog1 = ShapeStim(win, vertices=oog1Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog1.draw()
oog2Vert = [(0.15, 0.2), (0.45, 0.2), (0.45, 0.5), (0.35, 0.3)]
oog2 = ShapeStim(win, vertices=oog2Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog2.draw()
steelVert = [(0.0, 0.75), (0.0, 0.9), (0.13, 1), (0.26, 0.85), (0.13, 0.75), (0.07, 0.8)]
steel = ShapeStim(win, vertices=steelVert, fillColor=(-0.373,0.098,-0.733), fillColorSpace = 'rgb', lineWidth=2, lineColor=(-0.373,0.098,-0.733), lineColorSpace = 'rgb')
steel.draw()
mondVert = [(0.1, -0.35), (0.1, -0.25), (0.3, -0.25), (0.3, -0.35), (0.5, -0.35), (0.5, -0.25), (0.7, 0.0), (0.5, -0.5), (0.3, -0.5), (0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.3, -0.5), (-0.5, -0.5), (-0.7, 0.0), (-0.5, -0.25), (-0.5, -0.35), (-0.3, -0.35), (-0.3, -0.25), (-0.1, -0.25), (-0.1, -0.35)]
mond = ShapeStim(win, vertices=mondVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
mond.draw()
schaduw1Vert = [(-0.7, 0.0), (-0.45, -0.45),(-0.3, -0.45), (-0.3, -0.5), (-0.5, -0.5)]
schaduw1 = ShapeStim(win, vertices=schaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw1.draw()
schaduw2Vert = [(0.7, 0.0), (0.45, -0.45),(0.3, -0.45), (0.3, -0.5), (0.5, -0.5)]
schaduw2 = ShapeStim(win, vertices=schaduw2Vert, fillColor= (0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw2.draw()
schaduw3Vert = [(-0.3, -0.35), (-0.25, -0.25), (-0.3, -0.25)]
schaduw3 = ShapeStim(win, vertices=schaduw3Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw3.draw()
schaduw4Vert = [(0.3, -0.35), (0.25, -0.25), (0.3, -0.25)]
schaduw4 = ShapeStim(win, vertices=schaduw4Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw4.draw()
schaduw7Vert = [(0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.25, -0.35), (-0.05, -0.35), (-0.05, -0.45), (0.05, -0.45), (0.05, -0.35), (0.25, -0.35)]
schaduw7 = ShapeStim(win, vertices=schaduw7Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw7.draw()
lijn5Vert = [(-0.1, -0.4), (-0.05, -0.35)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn5.draw()
lijn6Vert = [(-0.1, -0.5), (-0.05, -0.45)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn6.draw()
lijn7Vert = [(0.1, -0.4), (0.05, -0.35)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn7.draw()
lijn8Vert = [(0.1, -0.5), (0.05, -0.45)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn8.draw()
lijn9Vert = [(-0.5, -0.5), (-0.45, -0.45)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn9.draw()
lijn10Vert = [(0.5, -0.5), (0.45, -0.45)]
lijn10 = ShapeStim(win, vertices=lijn10Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn10.draw()
oogSchaduw1Vert = [(-0.45, 0.5), (-0.4, 0.4),(-0.4, 0.25), (-0.25, 0.25), (-0.15, 0.2), (-0.45, 0.2)]
oogSchaduw1 = ShapeStim(win, vertices= oogSchaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw1.draw()
oogSchaduw2Vert = [(0.45, 0.5), (0.4, 0.4),(0.4, 0.25), (0.25, 0.25), (0.15, 0.2), (0.45, 0.2)]
oogSchaduw2 = ShapeStim(win, vertices= oogSchaduw2Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw2.draw()
lijn11Vert = [(-0.45, 0.2), (-0.4, 0.25)]
lijn11 = ShapeStim(win, vertices=lijn11Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn11.draw()
lijn12Vert = [(0.45, 0.2), (0.4, 0.25)]
lijn12 = ShapeStim(win, vertices=lijn12Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn12.draw()
neusSchaduwVert = [(0.1,-0.1), (-0.1, -0.1), (-0.075, -0.05), (0.075, -0.05)]
neusSchaduw = ShapeStim(win, vertices= neusSchaduwVert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neusSchaduw.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0, 0.75), (0.13, 0.63), (0.26, 0.75), (0.75, 0.5), (0.75, -0.5), (0.26, -0.75), (0.13, -0.63), (0.0, -0.75), (-0.13, -0.63), (-0.26, -0.75), (-0.75, -0.5), (-0.75, 0.5), (-0.26, 0.75), (-0.13, 0.63)]
pumpkin = ShapeStim(win, vertices=pumpkinVert, fillColor=(0.835,0.271,-0.780), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.835,0.271,-0.780), lineColorSpace = 'rgb')
pumpkin.draw()
lijn1Vert = [(-0.26, 0.75), (-0.6, 0.2), (-0.6, -0.2), (-0.26, -0.75)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, lineWidth=2, lineColor = (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn1.draw()
lijn2Vert = [(-0.13, 0.63), (-0.3, 0.1), (-0.3, -0.1), (-0.13, -0.63)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn2.draw()
lijn3Vert = [(0.13, 0.63), (0.3, 0.1), (0.3, -0.1), (0.13, -0.63)] 
lijn3 = ShapeStim(win, vertices=lijn3Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn3.draw()
lijn4Vert = [(0.26, 0.75), (0.6, 0.2), (0.6, -0.2), (0.26, -0.75)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn4.draw()
neusVert = [(0.0,0.15), (0.1,-0.1), (-0.1,-0.1)]
neus = ShapeStim(win, vertices=neusVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neus.draw()
oog1Vert = [(-0.15, 0.2), (-0.45, 0.2), (-0.45, 0.5), (-0.35, 0.3)]
oog1 = ShapeStim(win, vertices=oog1Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog1.draw()
oog2Vert = [(0.15, 0.2), (0.45, 0.2), (0.45, 0.5), (0.35, 0.3)]
oog2 = ShapeStim(win, vertices=oog2Vert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oog2.draw()
steelVert = [(0.0, 0.75), (0.0, 0.9), (0.13, 1), (0.26, 0.85), (0.13, 0.75), (0.07, 0.8)]
steel = ShapeStim(win, vertices=steelVert, fillColor=(-0.373,0.098,-0.733), fillColorSpace = 'rgb', lineWidth=2, lineColor=(-0.373,0.098,-0.733), lineColorSpace = 'rgb')
steel.draw()
mondVert = [(0.1, -0.35), (0.1, -0.25), (0.3, -0.25), (0.3, -0.35), (0.5, -0.35), (0.5, -0.25), (0.7, 0.0), (0.5, -0.5), (0.3, -0.5), (0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.3, -0.5), (-0.5, -0.5), (-0.7, 0.0), (-0.5, -0.25), (-0.5, -0.35), (-0.3, -0.35), (-0.3, -0.25), (-0.1, -0.25), (-0.1, -0.35)]
mond = ShapeStim(win, vertices=mondVert, fillColor='yellow', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
mond.draw()
schaduw1Vert = [(-0.7, 0.0), (-0.45, -0.45),(-0.3, -0.45), (-0.3, -0.5), (-0.5, -0.5)]
schaduw1 = ShapeStim(win, vertices=schaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw1.draw()
schaduw2Vert = [(0.7, 0.0), (0.45, -0.45),(0.3, -0.45), (0.3, -0.5), (0.5, -0.5)]
schaduw2 = ShapeStim(win, vertices=schaduw2Vert, fillColor= (0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw2.draw()
schaduw3Vert = [(-0.3, -0.35), (-0.25, -0.25), (-0.3, -0.25)]
schaduw3 = ShapeStim(win, vertices=schaduw3Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw3.draw()
schaduw4Vert = [(0.3, -0.35), (0.25, -0.25), (0.3, -0.25)]
schaduw4 = ShapeStim(win, vertices=schaduw4Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw4.draw()
schaduw7Vert = [(0.3, -0.4), (0.1, -0.4), (0.1, -0.5), (-0.1, -0.5), (-0.1, -0.4), (-0.3, -0.4), (-0.25, -0.35), (-0.05, -0.35), (-0.05, -0.45), (0.05, -0.45), (0.05, -0.35), (0.25, -0.35)]
schaduw7 = ShapeStim(win, vertices=schaduw7Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
schaduw7.draw()
lijn5Vert = [(-0.1, -0.4), (-0.05, -0.35)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn5.draw()
lijn6Vert = [(-0.1, -0.5), (-0.05, -0.45)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn6.draw()
lijn7Vert = [(0.1, -0.4), (0.05, -0.35)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn7.draw()
lijn8Vert = [(0.1, -0.5), (0.05, -0.45)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn8.draw()
lijn9Vert = [(-0.5, -0.5), (-0.45, -0.45)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn9.draw()
lijn10Vert = [(0.5, -0.5), (0.45, -0.45)]
lijn10 = ShapeStim(win, vertices=lijn10Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn10.draw()
oogSchaduw1Vert = [(-0.45, 0.5), (-0.4, 0.4),(-0.4, 0.25), (-0.25, 0.25), (-0.15, 0.2), (-0.45, 0.2)]
oogSchaduw1 = ShapeStim(win, vertices= oogSchaduw1Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw1.draw()
oogSchaduw2Vert = [(0.45, 0.5), (0.4, 0.4),(0.4, 0.25), (0.25, 0.25), (0.15, 0.2), (0.45, 0.2)]
oogSchaduw2 = ShapeStim(win, vertices= oogSchaduw2Vert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
oogSchaduw2.draw()
lijn11Vert = [(-0.45, 0.2), (-0.4, 0.25)]
lijn11 = ShapeStim(win, vertices=lijn11Vert, lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn11.draw()
lijn12Vert = [(0.45, 0.2), (0.4, 0.25)]
lijn12 = ShapeStim(win, vertices=lijn12Vert, lineWidth=2, lineColor= (0.561,-0.529,-0.725), lineColorSpace = 'rgb', closeShape = False)
lijn12.draw()
neusSchaduwVert = [(0.1,-0.1), (-0.1, -0.1), (-0.075, -0.05), (0.075, -0.05)]
neusSchaduw = ShapeStim(win, vertices= neusSchaduwVert, fillColor=(0.882,-0.106,-1.000), fillColorSpace = 'rgb', lineWidth=2, lineColor=(0.561,-0.529,-0.725), lineColorSpace = 'rgb')
neusSchaduw.draw()
stim = visual.TextStim(win, text = "Happy Halloween!", font = 'Juice ITC', color = 'red', pos = [0.0, -0.85], bold = True, italic = False, height = 0.2)
stim.draw()
win.flip()
time.sleep(1)