from psychopy import visual
import time
from psychopy.visual import ShapeStim

win = visual.Window(size=(500, 400), color = 'darkgreen')

pumpkinVert = [(-0.5, 0), (-0.4,0.5), (-0.3,0.55), (-0.2, 0.5), (-0.1,0.55), (0,0.5), (0.1,0.55), (0.2,0.5), (0.3,0.55), (0.4,0.5), (0.5,0), (0.4,-0.5), (0.3, -0.55), (0.2, -0.5), (0.1, -0.55), (0, -0.5), (-0.1,-0.55), (-0.2,-0.5), (-0.3, -0.55), (-0.4,-0.5)]
pumpkin = ShapeStim(win, vertices = pumpkinVert, size = 1, fillColor = [0.859,-0.106,-0.906], lineColor = [0.859,-0.106,-0.906])
pumpkin.draw()

triangle = visual.Polygon(win, edges = 3,radius = .10, pos = (-0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle.draw()

triangle2 = visual.Polygon(win, edges = 3,radius = .10, pos = (0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle2.draw()

mouthVert = [(-0.2, -0.25), (-0.15, -0.15), (-0.1, -0.2), (-0.05, -0.15), (0, -0.2), (0.05, -0.15), (0.1, -0.2), (0.15, -0.15), (0.2, -0.25), (0.15, -0.35), (0.1, -0.3), (0.05, -0.35), (0, -0.3), (-0.05, -0.35), (-0.1, -0.3), (-0.15, -0.35), (-0.2, -0.25)]
mouth = ShapeStim(win, vertices = mouthVert, fillColor = 'black', lineColor = 'black')
mouth.draw()

rectangle2 = visual.Rect(win, width = 0.1, height = .1, pos = (0,0.55), fillColor = 'black', lineColor = 'black')
rectangle2.draw()

tekst = visual.TextStim(win, text = "HAPPY HALLOWEEN!", color = 'red', pos = (0, -0.8), bold = True)
tekst.draw()

win.flip()
time.sleep(1)
# Esther: het is niet nodig om het vester te sluiten, de bedoeling is meestal dat je binnen hetzelfde veld blijft werken
win.close()

# Esther: je maakt hieronder de grafische elementen opnieuw aan, maar dat is helemaal niet nodig, die bestaat al ;)
# ESther: deze hoef je vanaf hier niet meer opnieuw aan te maken want ze bestaan reeds.
# Esther: het enige wat je hieronder hoeft te herhalen zijn de .draw(), .flip() en .sleep() commando's.
# Esther: probeer het eens uit en je zal zien dat je heel wat lijnen code gewoon kan schrappen.

# Esther: en om het nog een tikje eleganter te maken, kan je gewoon eerst alle grafische elementen maken en dan pas beginnen met drawen en flippen. You see?

win = visual.Window(size=(500, 400), color = 'darkgreen')

pumpkinVert = [(-0.5, 0), (-0.4,0.5), (-0.3,0.55), (-0.2, 0.5), (-0.1,0.55), (0,0.5), (0.1,0.55), (0.2,0.5), (0.3,0.55), (0.4,0.5), (0.5,0), (0.4,-0.5), (0.3, -0.55), (0.2, -0.5), (0.1, -0.55), (0, -0.5), (-0.1,-0.55), (-0.2,-0.5), (-0.3, -0.55), (-0.4,-0.5)]
pumpkin = ShapeStim(win, vertices = pumpkinVert, size = 1, fillColor = [0.859,-0.106,-0.906], lineColor = [0.859,-0.106,-0.906])
pumpkin.draw()

triangle = visual.Polygon(win, edges = 3,radius = .10, pos = (-0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle.draw()

triangle2 = visual.Polygon(win, edges = 3,radius = .10, pos = (0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle2.draw()

mouthVert = [(-0.2, -0.25), (-0.15, -0.15), (-0.1, -0.2), (-0.05, -0.15), (0, -0.2), (0.05, -0.15), (0.1, -0.2), (0.15, -0.15), (0.2, -0.25), (0.15, -0.35), (0.1, -0.3), (0.05, -0.35), (0, -0.3), (-0.05, -0.35), (-0.1, -0.3), (-0.15, -0.35), (-0.2, -0.25)]
mouth = ShapeStim(win, vertices = mouthVert, fillColor = 'black', lineColor = 'black')
mouth.draw()

rectangle2 = visual.Rect(win, width = 0.1, height = .1, pos = (0,0.55), fillColor = 'black', lineColor = 'black')
rectangle2.draw()

win.flip()
time.sleep(0.5)
win.close()



win = visual.Window(size=(500, 400), color = 'darkgreen')

pumpkinVert = [(-0.5, 0), (-0.4,0.5), (-0.3,0.55), (-0.2, 0.5), (-0.1,0.55), (0,0.5), (0.1,0.55), (0.2,0.5), (0.3,0.55), (0.4,0.5), (0.5,0), (0.4,-0.5), (0.3, -0.55), (0.2, -0.5), (0.1, -0.55), (0, -0.5), (-0.1,-0.55), (-0.2,-0.5), (-0.3, -0.55), (-0.4,-0.5)]
pumpkin = ShapeStim(win, vertices = pumpkinVert, size = 1, fillColor = [0.859,-0.106,-0.906], lineColor = [0.859,-0.106,-0.906])
pumpkin.draw()

triangle = visual.Polygon(win, edges = 3,radius = .10, pos = (-0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle.draw()

triangle2 = visual.Polygon(win, edges = 3,radius = .10, pos = (0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle2.draw()

mouthVert = [(-0.2, -0.25), (-0.15, -0.15), (-0.1, -0.2), (-0.05, -0.15), (0, -0.2), (0.05, -0.15), (0.1, -0.2), (0.15, -0.15), (0.2, -0.25), (0.15, -0.35), (0.1, -0.3), (0.05, -0.35), (0, -0.3), (-0.05, -0.35), (-0.1, -0.3), (-0.15, -0.35), (-0.2, -0.25)]
mouth = ShapeStim(win, vertices = mouthVert, fillColor = 'black', lineColor = 'black')
mouth.draw()

rectangle2 = visual.Rect(win, width = 0.1, height = .1, pos = (0,0.55), fillColor = 'black', lineColor = 'black')
rectangle2.draw()

tekst = visual.TextStim(win, text = "HAPPY HALLOWEEN!", color = 'red', pos = (0, -0.8), bold = True)
tekst.draw()

win.flip()
time.sleep(1)
win.close()



win = visual.Window(size=(500, 400), color = 'darkgreen')

pumpkinVert = [(-0.5, 0), (-0.4,0.5), (-0.3,0.55), (-0.2, 0.5), (-0.1,0.55), (0,0.5), (0.1,0.55), (0.2,0.5), (0.3,0.55), (0.4,0.5), (0.5,0), (0.4,-0.5), (0.3, -0.55), (0.2, -0.5), (0.1, -0.55), (0, -0.5), (-0.1,-0.55), (-0.2,-0.5), (-0.3, -0.55), (-0.4,-0.5)]
pumpkin = ShapeStim(win, vertices = pumpkinVert, size = 1, fillColor = [0.859,-0.106,-0.906], lineColor = [0.859,-0.106,-0.906])
pumpkin.draw()

triangle = visual.Polygon(win, edges = 3,radius = .10, pos = (-0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle.draw()

triangle2 = visual.Polygon(win, edges = 3,radius = .10, pos = (0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle2.draw()

mouthVert = [(-0.2, -0.25), (-0.15, -0.15), (-0.1, -0.2), (-0.05, -0.15), (0, -0.2), (0.05, -0.15), (0.1, -0.2), (0.15, -0.15), (0.2, -0.25), (0.15, -0.35), (0.1, -0.3), (0.05, -0.35), (0, -0.3), (-0.05, -0.35), (-0.1, -0.3), (-0.15, -0.35), (-0.2, -0.25)]
mouth = ShapeStim(win, vertices = mouthVert, fillColor = 'black', lineColor = 'black')
mouth.draw()

rectangle2 = visual.Rect(win, width = 0.1, height = .1, pos = (0,0.55), fillColor = 'black', lineColor = 'black')
rectangle2.draw()

win.flip()
time.sleep(0.5)
win.close()



win = visual.Window(size=(500, 400), color = 'darkgreen')

pumpkinVert = [(-0.5, 0), (-0.4,0.5), (-0.3,0.55), (-0.2, 0.5), (-0.1,0.55), (0,0.5), (0.1,0.55), (0.2,0.5), (0.3,0.55), (0.4,0.5), (0.5,0), (0.4,-0.5), (0.3, -0.55), (0.2, -0.5), (0.1, -0.55), (0, -0.5), (-0.1,-0.55), (-0.2,-0.5), (-0.3, -0.55), (-0.4,-0.5)]
pumpkin = ShapeStim(win, vertices = pumpkinVert, size = 1, fillColor = [0.859,-0.106,-0.906], lineColor = [0.859,-0.106,-0.906])
pumpkin.draw()

triangle = visual.Polygon(win, edges = 3,radius = .10, pos = (-0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle.draw()

triangle2 = visual.Polygon(win, edges = 3,radius = .10, pos = (0.25,0.1), fillColor = 'black', lineColor = 'black')
triangle2.draw()

mouthVert = [(-0.2, -0.25), (-0.15, -0.15), (-0.1, -0.2), (-0.05, -0.15), (0, -0.2), (0.05, -0.15), (0.1, -0.2), (0.15, -0.15), (0.2, -0.25), (0.15, -0.35), (0.1, -0.3), (0.05, -0.35), (0, -0.3), (-0.05, -0.35), (-0.1, -0.3), (-0.15, -0.35), (-0.2, -0.25)]
mouth = ShapeStim(win, vertices = mouthVert, fillColor = 'black', lineColor = 'black')
mouth.draw()

rectangle2 = visual.Rect(win, width = 0.1, height = .1, pos = (0,0.55), fillColor = 'black', lineColor = 'black')
rectangle2.draw()

tekst = visual.TextStim(win, text = "HAPPY HALLOWEEN!", color = 'red', pos = (0, -0.8), bold = True)
tekst.draw()

win.flip()
time.sleep(1)
win.close()