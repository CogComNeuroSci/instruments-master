from psychopy import visual
import time
win= visual.Window(fullscr=True, color=[-0.5, -0.5, -0.5])

# Esther: missing images!

#background
spinnenweb="spinnenweb.png"
web=visual.ImageStim(win, image= spinnenweb, pos=(0.7,0.65), size=(0.6, 0.7))
web.draw()
moon="fullmoon.png"
maan=visual.ImageStim(win, image=moon, size=(0.2,0.3), pos=(-0.7, 0.7))
maan.draw()
vleermuize="bat.png"
bat=visual.ImageStim(win, image=vleermuize, size=(0.2,0.2), pos=(-0.6, 0.6))
bat.draw()

#pompoen
pumpkin= visual.Circle(win, color='orange')
pumpkin.draw()
mond=visual.Circle(win, color='black', size=(0.5, 0.5), pos=(0, -0.05))
mond.draw()
overmond=visual.Circle(win, color='orange', size=(0.7, 0.5), pos=(0,0.05))
overmond.draw()
eye1 = visual.ShapeStim(win, vertices=((0, -0.15), (-0.05, 0), (0.05, 0)), pos=(-0.15,0.2), fillColor='black', lineColor='black')
eye1.draw()
eye2 = visual.ShapeStim(win, vertices=((0, -0.15), (-0.05, 0), (0.05, 0)), pos=(0.15,0.2), fillColor='black', lineColor='black')
eye2.draw()
steel= visual.Rect(win, pos=(0, 0.52), color='green', height=0.15, width=0.04)
steel.draw()

#pompoen verschijnT 1 sec
win.flip()
time.sleep(1)

#background en tekst
spinnenweb="spinnenweb.png"
web=visual.ImageStim(win, image= spinnenweb, pos=(0.7,0.65), size=(0.6, 0.7))
web.draw()
moon="fullmoon.png"
maan=visual.ImageStim(win, image=moon, size=(0.2,0.3), pos=(-0.7, 0.7))
maan.draw()
vleermuize="bat.png"
bat=visual.ImageStim(win, image=vleermuize, size=(0.2,0.2), pos=(-0.6, 0.6))
bat.draw()
tekst= visual.TextStim(win, text= 'Happy Halloween!', pos=(0,-0.7), font='Algerian')
tekst.draw()
win.flip()
time.sleep(0.5)

#background
spinnenweb="spinnenweb.png"
web=visual.ImageStim(win, image= spinnenweb, pos=(0.7,0.65), size=(0.6, 0.7))
web.draw()
moon="fullmoon.png"
maan=visual.ImageStim(win, image=moon, size=(0.2,0.3), pos=(-0.7, 0.7))
maan.draw()
vleermuize="bat.png"
bat=visual.ImageStim(win, image=vleermuize, size=(0.2,0.2), pos=(-0.6, 0.6))
bat.draw()

#pompoen
pumpkin= visual.Circle(win, color='orange')
pumpkin.draw()
mond=visual.Circle(win, color='black', size=(0.5, 0.5), pos=(0, -0.05))
mond.draw()
overmond=visual.Circle(win, color='orange', size=(0.7, 0.5), pos=(0,0.05))
overmond.draw()
eye1 = visual.ShapeStim(win, vertices=((0, -0.15), (-0.05, 0), (0.05, 0)), pos=(-0.15,0.2), fillColor='black', lineColor='black')
eye1.draw()
eye2 = visual.ShapeStim(win, vertices=((0, -0.15), (-0.05, 0), (0.05, 0)), pos=(0.15,0.2), fillColor='black', lineColor='black')
eye2.draw()
steel= visual.Rect(win, pos=(0, 0.52), color='green', height=0.15, width=0.04)
steel.draw()

#pompoen verschijnT 1 sec
win.flip()
time.sleep(1)

#background en tekst
spinnenweb="spinnenweb.png"
web=visual.ImageStim(win, image= spinnenweb, pos=(0.7,0.65), size=(0.6, 0.7))
web.draw()
moon="fullmoon.png"
maan=visual.ImageStim(win, image=moon, size=(0.2,0.3), pos=(-0.7, 0.7))
maan.draw()
vleermuize="bat.png"
bat=visual.ImageStim(win, image=vleermuize, size=(0.2,0.2), pos=(-0.6, 0.6))
bat.draw()
tekst= visual.TextStim(win, text= 'Happy Halloween!', pos=(0,-0.7), font='Algerian')
tekst.draw()
win.flip()
time.sleep(0.5)