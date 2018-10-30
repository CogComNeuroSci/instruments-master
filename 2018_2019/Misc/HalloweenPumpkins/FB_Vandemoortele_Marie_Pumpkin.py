import time
from psychopy import visual, event, core
from psychopy.visual import ShapeStim


win = visual.Window([600,400], color = (0,0,0), fullscr = True )

# pompoen + tekst

Pumpkin1 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (0.25,0))
Pumpkin2 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (0.15,0))
Pumpkin3 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.22), pos = (0, 0))
Pumpkin5 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (-0.15,0))
Pumpkin6 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (-0.25,0))


star7Vert = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor='black', lineWidth=2, lineColor='black', pos = (-0.2,0.25))

star7Vert1 = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star71 = ShapeStim(win, vertices=star7Vert1, fillColor='black', lineWidth=2, lineColor='black', pos = (0.2,0.25))

Tand1 = visual.Rect(win, color = (-1, -1, -1), size = (1.5,0.1), pos = (0,-0.1))
Tand2 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.35,-0.1))
Tand3 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.25,-0.1))
Tand4 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.15,-0.1))
Tand5 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.05,-0.1))
Tand6 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.05,-0.1))
Tand7 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.15,-0.1))
Tand8 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.25,-0.1))
Tand9 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.35,-0.1))


stim = visual.TextStim(win, text = "Happy Halloween", color = 'black', pos = (0, -0.75))

Steel = visual.Rect(win, color = 'green', size = (0.15,0.4), pos = (0, 0.7))


while not event.getKeys():
    Pumpkin1.draw()
    Pumpkin2.draw()
    Pumpkin3.draw()
    Pumpkin5.draw()
    Pumpkin6.draw()
    star7.setOri(1, '-')
    star71.setOri(1, '-')
    star7.draw()
    star71.draw()
    Tand1.draw()
    Tand2.draw()
    Tand3.draw()
    Tand4.draw()
    Tand5.draw()
    Tand6.draw()
    Tand7.draw()
    Tand8.draw()
    Tand9.draw()
    stim.draw()
    Steel.draw()
    win.flip()

# enkel pompoen

# Esther: voor de volgende presentatie hoef je de vormen niet meer opnieuw aan te maken, te hoeft enkel te drawen en flippen ;)
# Esther: probeer het eens uit en je zal zien dat je veel code kan besparen!


Pumpkin1 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (0.25,0))
Pumpkin2 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (0.15,0))
Pumpkin3 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.22), pos = (0, 0))
Pumpkin5 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (-0.15,0))
Pumpkin6 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (-0.25,0))


star7Vert = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor='black', lineWidth=2, lineColor='black', pos = (-0.2,0.25))

star7Vert1 = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star71 = ShapeStim(win, vertices=star7Vert1, fillColor='black', lineWidth=2, lineColor='black', pos = (0.2,0.25))

Tand1 = visual.Rect(win, color = (-1, -1, -1), size = (1.5,0.1), pos = (0,-0.1))
Tand2 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.35,-0.1))
Tand3 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.25,-0.1))
Tand4 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.15,-0.1))
Tand5 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.05,-0.1))
Tand6 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.05,-0.1))
Tand7 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.15,-0.1))
Tand8 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.25,-0.1))
Tand9 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.35,-0.1))



Steel = visual.Rect(win, color = 'green', size = (0.15,0.4), pos = (0, 0.7))


while not event.getKeys():
    Pumpkin1.draw()
    Pumpkin2.draw()
    Pumpkin3.draw()
    Pumpkin5.draw()
    Pumpkin6.draw()
    star7.setOri(1, '-')
    star71.setOri(1, '-')
    star7.draw()
    star71.draw()
    Tand1.draw()
    Tand2.draw()
    Tand3.draw()
    Tand4.draw()
    Tand5.draw()
    Tand6.draw()
    Tand7.draw()
    Tand8.draw()
    Tand9.draw()
    Steel.draw()
    win.flip()

# Weer pompoen + tekst

Pumpkin1 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (0.25,0))
Pumpkin2 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (0.15,0))
Pumpkin3 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.22), pos = (0, 0))
Pumpkin5 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (-0.15,0))
Pumpkin6 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (-0.25,0))


star7Vert = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor='black', lineWidth=2, lineColor='black', pos = (-0.2,0.25))

star7Vert1 = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star71 = ShapeStim(win, vertices=star7Vert1, fillColor='black', lineWidth=2, lineColor='black', pos = (0.2,0.25))

Tand1 = visual.Rect(win, color = (-1, -1, -1), size = (1.5,0.1), pos = (0,-0.1))
Tand2 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.35,-0.1))
Tand3 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.25,-0.1))
Tand4 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.15,-0.1))
Tand5 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.05,-0.1))
Tand6 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.05,-0.1))
Tand7 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.15,-0.1))
Tand8 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.25,-0.1))
Tand9 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.35,-0.1))


stim = visual.TextStim(win, text = "Happy Halloween", color = 'black', pos = (0, -0.75))

Steel = visual.Rect(win, color = 'green', size = (0.15,0.4), pos = (0, 0.7))


while not event.getKeys():
    Pumpkin1.draw()
    Pumpkin2.draw()
    Pumpkin3.draw()
    Pumpkin5.draw()
    Pumpkin6.draw()
    star7.setOri(1, '-')
    star71.setOri(1, '-')
    star7.draw()
    star71.draw()
    Tand1.draw()
    Tand2.draw()
    Tand3.draw()
    Tand4.draw()
    Tand5.draw()
    Tand6.draw()
    Tand7.draw()
    Tand8.draw()
    Tand9.draw()
    stim.draw()
    Steel.draw()
    win.flip()

# Pompoen zonder tekst

Pumpkin1 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (0.25,0))
Pumpkin2 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (0.15,0))
Pumpkin3 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.22), pos = (0, 0))
Pumpkin5 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (-0.15,0))
Pumpkin6 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (-0.25,0))


star7Vert = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor='black', lineWidth=2, lineColor='black', pos = (-0.2,0.25))

star7Vert1 = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star71 = ShapeStim(win, vertices=star7Vert1, fillColor='black', lineWidth=2, lineColor='black', pos = (0.2,0.25))

Tand1 = visual.Rect(win, color = (-1, -1, -1), size = (1.5,0.1), pos = (0,-0.1))
Tand2 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.35,-0.1))
Tand3 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.25,-0.1))
Tand4 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.15,-0.1))
Tand5 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.05,-0.1))
Tand6 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.05,-0.1))
Tand7 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.15,-0.1))
Tand8 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.25,-0.1))
Tand9 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.35,-0.1))


Steel = visual.Rect(win, color = 'green', size = (0.15,0.4), pos = (0, 0.7))


while not event.getKeys():
    Pumpkin1.draw()
    Pumpkin2.draw()
    Pumpkin3.draw()
    Pumpkin5.draw()
    Pumpkin6.draw()
    star7.setOri(1, '-')
    star71.setOri(1, '-')
    star7.draw()
    star71.draw()
    Tand1.draw()
    Tand2.draw()
    Tand3.draw()
    Tand4.draw()
    Tand5.draw()
    Tand6.draw()
    Tand7.draw()
    Tand8.draw()
    Tand9.draw()
    Steel.draw()
    win.flip()

# pompoen + tekst

Pumpkin1 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (0.25,0))
Pumpkin2 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (0.15,0))
Pumpkin3 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.22), pos = (0, 0))
Pumpkin5 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (-0.15,0))
Pumpkin6 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (-0.25,0))


star7Vert = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor='black', lineWidth=2, lineColor='black', pos = (-0.2,0.25))

star7Vert1 = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star71 = ShapeStim(win, vertices=star7Vert1, fillColor='black', lineWidth=2, lineColor='black', pos = (0.2,0.25))

Tand1 = visual.Rect(win, color = (-1, -1, -1), size = (1.5,0.1), pos = (0,-0.1))
Tand2 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.35,-0.1))
Tand3 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.25,-0.1))
Tand4 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.15,-0.1))
Tand5 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.05,-0.1))
Tand6 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.05,-0.1))
Tand7 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.15,-0.1))
Tand8 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.25,-0.1))
Tand9 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.35,-0.1))


stim = visual.TextStim(win, text = "Happy Halloween", color = 'black', pos = (0, -0.75))

Steel = visual.Rect(win, color = 'green', size = (0.15,0.4), pos = (0, 0.7))


while not event.getKeys():
    Pumpkin1.draw()
    Pumpkin2.draw()
    Pumpkin3.draw()
    Pumpkin5.draw()
    Pumpkin6.draw()
    star7.setOri(1, '-')
    star71.setOri(1, '-')
    star7.draw()
    star71.draw()
    Tand1.draw()
    Tand2.draw()
    Tand3.draw()
    Tand4.draw()
    Tand5.draw()
    Tand6.draw()
    Tand7.draw()
    Tand8.draw()
    Tand9.draw()
    stim.draw()
    Steel.draw()
    win.flip()

# pompoen zonder tekst

Pumpkin1 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (0.25,0))
Pumpkin2 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (0.15,0))
Pumpkin3 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.22), pos = (0, 0))
Pumpkin5 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.2), pos = (-0.15,0))
Pumpkin6 = visual.Circle(win, color = (1,0.004,-1), size = (0.4,1.1), pos = (-0.25,0))


star7Vert = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star7 = ShapeStim(win, vertices=star7Vert, fillColor='black', lineWidth=2, lineColor='black', pos = (-0.2,0.25))

star7Vert1 = [(0.0,0.125),(0.0225,0.045),(0.0975,0.0775),(0.0475,0.01),(0.1225,-0.0275),(0.04,-0.03),(0.055,-0.1125),(0.0,-0.05),(-0.055,-0.1275),(-0.04,-0.03),(-0.1225,-0.0275),(-0.0475,0.01),(-0.0975,0.0775),(-0.0225,0.045)]
star71 = ShapeStim(win, vertices=star7Vert1, fillColor='black', lineWidth=2, lineColor='black', pos = (0.2,0.25))

Tand1 = visual.Rect(win, color = (-1, -1, -1), size = (1.5,0.1), pos = (0,-0.1))
Tand2 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.35,-0.1))
Tand3 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.25,-0.1))
Tand4 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.15,-0.1))
Tand5 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (-0.05,-0.1))
Tand6 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.05,-0.1))
Tand7 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.15,-0.1))
Tand8 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.25,-0.1))
Tand9 = visual.Rect(win, color = (-1, -1, -1), size = (0.075,0.3), pos = (0.35,-0.1))


Steel = visual.Rect(win, color = 'green', size = (0.15,0.4), pos = (0, 0.7))


while not event.getKeys():
    Pumpkin1.draw()
    Pumpkin2.draw()
    Pumpkin3.draw()
    Pumpkin5.draw()
    Pumpkin6.draw()
    star7.setOri(1, '-')
    star71.setOri(1, '-')
    star7.draw()
    star71.draw()
    Tand1.draw()
    Tand2.draw()
    Tand3.draw()
    Tand4.draw()
    Tand5.draw()
    Tand6.draw()
    Tand7.draw()
    Tand8.draw()
    Tand9.draw()
    Steel.draw()
    win.flip()




win.mouseVisible = True
time.sleep(0.5)
win.close()
