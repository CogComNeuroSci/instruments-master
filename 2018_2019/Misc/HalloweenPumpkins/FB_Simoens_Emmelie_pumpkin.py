from psychopy import visual
from psychopy.visual import ShapeStim
import time

win = visual.Window([600,400])


#achtergrond
foto = "achtergrond.jpg"
achtergrond = visual.ImageStim(win,foto)

#achtergrond spookje
foto2 = "spook.jpg"
spook = visual.ImageStim(win,foto2, pos= (0.6, -0.5), size = 0.2)

#achtergrond Kat
foto3 = "kat.jpg"
kat = visual.ImageStim(win, foto3, pos = (-0.6, -0.5), size = 0.3)

#pompoen
pompoen = visual.Circle(win, fillColor = 'orange', pos = (0, 0.25))

#oog 1 van de pompoen
Eye1Vert =[(-0.4, 0), (0, 0.5), (0.4, 0)]
Eye1 = ShapeStim(win, vertices=Eye1Vert, fillColor='black', lineWidth=0, size=0.20, pos=(-0.20, 0.4))

#wit oog 1
Eye1bVert = [(-0.4, 0), (0, 0.5), (0.4, 0)]
Eye1b = ShapeStim(win, vertices=Eye1bVert, fillColor='white', lineWidth=0, size=0.10, pos=(-0.20, 0.4))

#pupil oog 1
Eye1cVert = [(-0.4, 0), (0, 0.5), (0.4, 0)]
Eye1c = ShapeStim(win, vertices=Eye1cVert, fillColor='black', lineWidth=0, size=0.05, pos=(-0.20, 0.4))

#oog 2 van de pompoen
Eye2Vert =[(-0.4, 0), (0, 0.5), (0.4, 0)]
Eye2 = ShapeStim(win, vertices=Eye1Vert, fillColor='black', lineWidth=0, size=0.20, pos=(0.20, 0.4))

#wit oog 2
Eye2bVert =[(-0.4, 0), (0, 0.5), (0.4, 0)]
Eye2b = ShapeStim(win, vertices=Eye2bVert, fillColor='white', lineWidth=0, size=0.10, pos=(0.20, 0.4))

#pupil oog 2
Eye2cVert =[(-0.4, 0), (0, 0.5), (0.4, 0)]
Eye2c = ShapeStim(win, vertices=Eye2cVert, fillColor='black', lineWidth=0, size=0.05, pos=(0.20, 0.4))

#neus van de pompoen
NoseVert = [(-0.4, 0), (0, 0.5), (0.4, 0)]
Nose = ShapeStim(win, vertices=NoseVert, fillColor='black', lineWidth=0, size=0.20, pos=(0, 0.20))


#mond van de pompoen
MouthVert = [(-0.7,0),(0.7,0),(0,-0.5)]
Mouth = ShapeStim(win, vertices=MouthVert, fillColor='black', lineWidth=0.6, size=0.30, pos=(0, 0.02))

#steeltje van de pompoen
rect = visual.Rect(win,width=0.15, height=0.35, fillColor = 'green', pos = (0, 0.75))


#TekstHappyHalloween
stim = visual.TextStim(win,text="Happy Halloween!", color=(-1,-1,-1), pos=(0, -0.5), font = "herculanum")


#flikkeren Happy Halloween
achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
#kat.draw()
#spook.draw()
#stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
#kat.draw()
#spook.draw()
#stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
#kat.draw()
#spook.draw()
#stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
#kat.draw()
#spook.draw()
#stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
#kat.draw()
#spook.draw()
#stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
#kat.draw()
#spook.draw()
#stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
#kat.draw()
#spook.draw()
#stim.draw()
time.sleep(0.5)
win.flip()

achtergrond.draw()
pompoen.draw()
Eye1.draw()
Eye1b.draw()
Eye1c.draw()
Eye2.draw()
Eye2b.draw()
Eye2c.draw()
Nose.draw()
Mouth.draw()
rect.draw()
kat.draw()
spook.draw()
stim.draw()
time.sleep(0.5)
win.flip()


win.close()

