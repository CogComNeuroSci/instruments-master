from __future__ import division

from psychopy import visual, event, core
from psychopy.visual import ShapeStim
import psychopy.event
clock = core.Clock()

win = visual.Window(size=(500, 400), color = (-0.3,-1,-0.2), units='height')

# pompoen

circle = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=150,
    fillColor= "Orange",
    lineColor=[-1, -1, -1],
    edges=128,
    lineWidth=3)

#Steel

stengelVert = [(0.04,0.36),(0.03,0.37),(0.07,0.44),(-0.08,0.47),(-0.03,0.37),(-0.04,0.36)]
stengel = ShapeStim(win, vertices=stengelVert, fillColor='green', lineWidth=2, lineColor='black')

# neus

triangle1Vert = [(0.07,-0.05),(0,0.05),(-0.07,-0.05)]
triangle1 = ShapeStim(win, vertices=triangle1Vert, fillColor='black', lineWidth=2, lineColor='black')

# ogen

triangle2Vert = [(-0.05,0.09),(-0.06,0.12),(-0.20,0.21),(-0.24,0.09)]
triangle2 = ShapeStim(win, vertices=triangle2Vert, fillColor='black', lineWidth=2, lineColor='black')

triangle3Vert = [(0.05,0.09),(0.06,0.12),(0.20,0.21),(0.24,0.09)]
triangle3 = ShapeStim(win, vertices=triangle3Vert, fillColor='black', lineWidth=2, lineColor='black')

# mond

mondVert = [(-0.29,-0.03),(-0.2,-0.27),(-0.2,-0.25),(-0.04,-0.25),(-0.05,-0.21),(0.05,-0.21),(0.04,-0.25),(0.2,-0.25),(0.2,-0.27),(0.29,-0.03),
(0.15,-0.1),(0.16,-0.14),(0.11,-0.15),(0.12,-0.11),(0,-0.15),
(-0.12,-0.11),(-0.11,-0.15),(-0.16,-0.14),(-0.15,-0.1)]
mond = ShapeStim(win, vertices=mondVert, fillColor='black', lineWidth=2, lineColor='black')

# bovenste lijnen

lijntopVert = [(0.025,0.38),(0.05,0.43)]
lijntop = ShapeStim(win, vertices=lijntopVert, lineWidth=4, lineColor='DarkGreen')


lijn1Vert = [(0.04,0.36),(0.07,0.355),(0.1,0.345),(0.07,0.355)]
lijn1 = ShapeStim(win, vertices=lijn1Vert, fillColor='DarkOrange', lineWidth=4, lineColor='DarkOrange')

lijn2Vert = [(-0.04,0.36),(-0.07,0.355),(-0.1,0.345),(-0.07,0.355)]
lijn2 = ShapeStim(win, vertices=lijn2Vert, fillColor='DarkOrange', lineWidth=4, lineColor='DarkOrange')

lijn3Vert = [(0.01,0.36),(0.02,0.35),(0.03,0.33),(0.02,0.35)]
lijn3 = ShapeStim(win, vertices=lijn3Vert, fillColor='DarkOrange', lineWidth=4, lineColor='DarkOrange')

lijn4Vert = [(-0.01,0.36),(-0.02,0.35),(-0.03,0.33),(-0.02,0.35)]
lijn4 = ShapeStim(win, vertices=lijn4Vert, fillColor='DarkOrange', lineWidth=4, lineColor='DarkOrange')

# lijnen wenkbrauwen

lijn5Vert = [(-0.07,0.15),(-0.06,0.22)]
lijn5 = ShapeStim(win, vertices=lijn5Vert, lineWidth=4, lineColor='DarkOrange')

lijn6Vert = [(-0.07,0.15),(-0.14,0.195)]
lijn6 = ShapeStim(win, vertices=lijn6Vert, lineWidth=4, lineColor='DarkOrange')

lijn7Vert = [(0.07,0.15),(0.06,0.22)]
lijn7 = ShapeStim(win, vertices=lijn7Vert, lineWidth=4, lineColor='DarkOrange')

lijn8Vert = [(0.07,0.15),(0.14,0.195)]
lijn8 = ShapeStim(win, vertices=lijn8Vert, lineWidth=4, lineColor='DarkOrange')

# kin

lijn9Vert = [(0,-0.37),(0,-0.34)]
lijn9 = ShapeStim(win, vertices=lijn9Vert, lineWidth=4, lineColor='DarkOrange')


lijnmond1Vert = [(-0.09,-0.12),(-0.09,-0.08)]
lijnmond1 = ShapeStim(win, vertices=lijnmond1Vert, lineWidth=4, lineColor='DarkOrange')

lijnmond2Vert = [(-0.26,-0.04),(-0.26,0)]
lijnmond2 = ShapeStim(win, vertices=lijnmond2Vert, lineWidth=4, lineColor='DarkOrange')

lijnmond3Vert = [(0.09,-0.12),(0.09,-0.08)]
lijnmond3 = ShapeStim(win, vertices=lijnmond3Vert, lineWidth=4, lineColor='DarkOrange')

lijnmond4Vert = [(0.26,-0.04),(0.26,0)]
lijnmond4 = ShapeStim(win, vertices=lijnmond4Vert, lineWidth=4, lineColor='DarkOrange')

# bloed

bloed1Vert = [(-0.5,0.25),(-0.35,0.27),(-0.36,0.28),(-0.2,0.3),(-0.31,0.18),(-0.325,0.22)]
bloed1 = ShapeStim(win, vertices=bloed1Vert, fillColor='DarkRed', lineWidth=2, lineColor='black')

bloed2Vert = [(0.5,-0.25),(0.35,-0.27),(0.36,-0.28),(0.2,-0.3),(0.31,-0.18),(0.325,-0.22)]
bloed2 = ShapeStim(win, vertices=bloed2Vert, fillColor='DarkRed', lineWidth=2, lineColor='black')

# graf

grafVert = [(-0.49,-0.5),(-0.54,-0.25),(-0.34,-0.23),(-0.39,-0.5)]
graf = ShapeStim(win, vertices=grafVert, fillColor='DarkGray', lineWidth=3, lineColor='black')

zijgrafVert = [(-0.34,-0.23),(-0.33,-0.24),(-0.38,-0.5),(-0.39,-0.5)]
zijgraf = ShapeStim(win, vertices=zijgrafVert, fillColor='Black', lineWidth=3, lineColor='black')


graftekst1 = visual.TextStim(win, text = "R.I.P.", font ="Impact", color = (-1,-1,-1), height = 0.05, pos = (-0.44,-0.3))
graftekst2 = visual.TextStim(win, text = "Frederik", font= "Impact", color = (-1,-1,-1), height = 0.03, pos = (-0.44,-0.37))

# bewegend oog

eye1 = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=18,
    fillColor= "white",
    lineColor=[-1, -1, -1],
    edges=
    128)


test_offset = 178

for offset in [-1, +1]:

    eye1.pos = [test_offset * offset, -82]


eye2 = psychopy.visual.Circle(
    win=win,
    units="pix",
    radius=7,
    fillColor= "black",
    lineColor=[-1, -1, -1],
    edges=128)


test_offset = 185

for offset in [-1, +1]:

    eye2.pos = [test_offset * offset, -79]





# Tekst

Tekst1 = visual.TextStim(win, text = "Happy", ori = -10,color = "Darkgreen", font = "Trattatello", height = 0.15, pos = (-0.35,0.35))


Tekst2 = visual.TextStim(win, text = "halloween!", ori = -10,color = "DarkGreen", font = "Trattatello", height = 0.15, pos = (0.27,-0.35))



# Kruis

boo = visual.TextStim(win, text = " ✟ ", font = "Comic sans MS",color = "Black", height = 0.3, pos = (0.33,0.33))



# drawing

while not event.getKeys():
    boo.draw()
    bloed1.draw()
    bloed2.draw()
    zijgraf.draw()
    graf.draw()
    graftekst1.draw()
    graftekst2.draw()
    circle.draw()
    lijn9.draw()
    lijnmond1.draw()
    lijnmond2.draw()
    lijnmond3.draw()
    lijnmond4.draw()
    triangle1.draw()
    triangle2.draw()
    triangle3.draw()
    mond.draw()
    lijn1.draw()
    lijn2.draw()
    lijn3.draw()
    lijn4.draw()
    stengel.draw()
    lijn5.draw()
    lijn6.draw()
    lijn7.draw()
    lijn8.draw()
    lijntop.draw()
    eye1.draw()
    Tekst1.draw()
    Tekst2.draw()
    eye2.setOri(0.75, '-')  # rotate
    eye2.setSize(eye2.ori % 360 / 360)  # shrink
    eye2.draw()
    boo.setOri(0.2, '-')  # rotate
    
    # Timer
    
    if(int(clock.getTime()*2) % 1.5 == 1):
        Tekst1.pos = (1, 1)
    else:
        Tekst1.pos = (-0.35,0.35)
        
    if(int(clock.getTime()*2) % 1.5 == 1):
        Tekst2.pos = (1, 1)
    else:
        Tekst2.pos = (0.27,-0.35)
        
        
        
    win.flip()





win.close()
core.quit()






