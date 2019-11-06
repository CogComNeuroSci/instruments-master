from __future__ import division
from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import time
beeld=visual.Window(fullscr=True, monitor="pc_sofie")

steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))

tekst=visual.TextStim(beeld,text='HAPPY HALLOWEEN!!!', font="Algerian", color=(1,-1,-1),bold=True, pos=(0,-0.7))

steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()
tekst.draw()

beeld.flip()
time.sleep(1)


steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))


steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()

beeld.flip()
time.sleep(0.5)

steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))

tekst=visual.TextStim(beeld,text='HAPPY HALLOWEEN!!!', font="Algerian", color=(1,-1,-1),bold=True, pos=(0,-0.7))

steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()
tekst.draw()

beeld.flip()
time.sleep(0.5)

steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))


steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()

beeld.flip()
time.sleep(0.5)

steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))

tekst=visual.TextStim(beeld,text='HAPPY HALLOWEEN!!!', font="Algerian", color=(1,-1,-1),bold=True, pos=(0,-0.7))

steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()
tekst.draw()

beeld.flip()
time.sleep(0.5)


steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))


steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()

beeld.flip()
time.sleep(0.5)

steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))

tekst=visual.TextStim(beeld,text='HAPPY HALLOWEEN!!!', font="Algerian", color=(1,-1,-1),bold=True, pos=(0,-0.7))

steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()
tekst.draw()

beeld.flip()
time.sleep(0.5)

steelVert=[(-0.01,0),(-0.01,0.15),(0.01,0.15),(0.01,0)]
steel=ShapeStim(beeld,vertices=steelVert,fillColor=(0.5,1,-1),lineWidth=5,lineColor=(-1,-1,-1),size=5)

circle=visual.Circle(beeld,radius=0.5, edges=50, fillColor=(1,0.2,-1),lineColor=(-1,-1,-1),lineWidth=5)

eye1Vert=[(-0.07,0),(-0.05,0.05),(-0.03,0)]
eye1=ShapeStim(beeld,vertices=eye1Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

eye2Vert=[(0.07,0),(0.05,0.05),(0.03,0)]
eye2=ShapeStim(beeld,vertices=eye2Vert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=5)

mouthVert=[(-0.02,-0.02),(-0.04,0),(-0.06,-0.02),(-0.08,0),(-0.1,-0.02),(-0.1,-0.08),(-0.08,-0.06),(-0.06,-0.08),(-0.04,-0.06),(-0.02,-0.08),(0,-0.06),(0.02,-0.08,),(0.04,-0.06),(0.06,-0.08),(0.08,-0.06),(0.1,-0.08),(0.1,-0.02),(0.08,0),(0.06,-0.02),(0.04,0),(0.02,-0.02),(0,0)]
mouth=ShapeStim(beeld,vertices=mouthVert,fillColor=(1,1,-0.5),lineWidth=5,lineColor=(-1,-1,-1),size=3,pos=(0,-0.07))


steel.draw()
circle.draw()
eye1.draw()
eye2.draw()
mouth.draw()

beeld.flip()
time.sleep(0.5)

beeld.close()