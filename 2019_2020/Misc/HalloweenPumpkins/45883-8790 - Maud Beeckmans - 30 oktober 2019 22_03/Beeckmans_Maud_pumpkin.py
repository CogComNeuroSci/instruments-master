# for 3D information: see site 'http://www.djmannion.net/psych_programming/vision/tog_ac/tog_ac.html'

from __future__ import division
from psychopy import visual, event, core
import time
win = visual.Window(fullscr = True, units = 'norm', color = 'grey' )
pumpkin_radius = (0.2,0.5)
pumpkin_1 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = 'orange', lineWidth = 3, lineColor = 'black')
pumpkin_2 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_3 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_4 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (-0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_5 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (-0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_3.draw()
pumpkin_2.draw()
pumpkin_5.draw()
pumpkin_4.draw()
pumpkin_1.draw()


steel_vertices = [ (-0.03,0.4), (-0.06,0.45), (-0.06,0.65), (-0.03,0.7), (0.03,0.7), (0.06,0.65), (0.06,0.45),(0.03,0.4)]
steel = visual.ShapeStim(win, vertices = steel_vertices, fillColor = [-0.067,-0.067,-1.000] , lineWidth = 3, lineColor = [-1.000,-0.600,-1.000])

#steel_radius = (0.025, 0.1)
#steel_1 = visual.Circle(win, radius = steel_radius, edges = 126, fillColor = 'green', pos = (0,0.55))

steel.draw()


L_eye_vertices = [(-0.2,0.05), (-0.2,0.35), (-0.05,0.2)]
L_eye = visual.ShapeStim(win, vertices = L_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
#(voor grotere ogen): R_eye_vertices = [(0.25,0), (0.25,0.4), (0.05,0.2)]
R_eye_vertices = [(0.2,0.05), (0.2,0.35), (0.05,0.2)]
R_eye = visual.ShapeStim(win, vertices = R_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')

L_eye.draw()
R_eye.draw()

#eerste poging: mouth_vertices = [(-0.2,-0.1), (-0.1,-0.3),(-0.05,-0.2), (0,-0.3), (0.05,-0.2),(0.1,-0.3), (0.2,-0.1),(0.1,-0.4),(0.05,-0.3),(0,-0.4),(-0.05,-0.3),(-0.1,-0.4)]
mouth_vertices = [(-0.3,0), (-0.2,-0.1),(-0.15,0), (-0.1,-0.1),(-0.05,0),(0,-0.1),(0.05,0),(0.1,-0.1), (0.15,0),(0.2,-0.1), (0.3,0),(0.2,-0.3),(0.15,-0.2), (0.1,-0.3), (0.05,-0.2), (0,-0.3), (-0.05,-0.2),(-0.1,-0.3), (-0.15,-0.2),(-0.2,-0.3)]
mouth = visual.ShapeStim(win, vertices = mouth_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')

mouth.draw()

# mislukte cirkel in ogen 
# circle_radius = (0.049,0.07)
# L_circle = visual.Circle(win, radius = circle_radius, edges = 126, fillColor = [0.098,-0.890,-0.914], pos = (-0.15,0.2), lineWidth = 1, lineColor = 'black')
# L_circle.draw()


##hier mee bezig: visual.RadialStim(win, 
## https://www.psychopy.org/api/visual/radialstim.html

Happy_halloween = visual.TextStim(win, text = 'Happy Halloween!', color = 'red', bold = True, height = 0.2, pos = (0,-0.7))
Happy_halloween.draw()


win.flip()
time.sleep(1)

pumpkin_radius = (0.2,0.5)
pumpkin_1 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = 'orange', lineWidth = 3, lineColor = 'black')
pumpkin_2 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_3 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_4 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (-0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_5 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (-0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_3.draw()
pumpkin_2.draw()
pumpkin_5.draw()
pumpkin_4.draw()
pumpkin_1.draw()


steel_vertices = [ (-0.03,0.4), (-0.06,0.45), (-0.06,0.65), (-0.03,0.7), (0.03,0.7), (0.06,0.65), (0.06,0.45),(0.03,0.4)]
steel = visual.ShapeStim(win, vertices = steel_vertices, fillColor = [-0.067,-0.067,-1.000] , lineWidth = 3, lineColor = [-1.000,-0.600,-1.000])
steel.draw()

L_eye_vertices = [(-0.2,0.05), (-0.2,0.35), (-0.05,0.2)]
L_eye = visual.ShapeStim(win, vertices = L_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
R_eye_vertices = [(0.2,0.05), (0.2,0.35), (0.05,0.2)]
R_eye = visual.ShapeStim(win, vertices = R_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
L_eye.draw()
R_eye.draw()

mouth_vertices = [(-0.3,0), (-0.2,-0.1),(-0.15,0), (-0.1,-0.1),(-0.05,0),(0,-0.1),(0.05,0),(0.1,-0.1), (0.15,0),(0.2,-0.1), (0.3,0),(0.2,-0.3),(0.15,-0.2), (0.1,-0.3), (0.05,-0.2), (0,-0.3), (-0.05,-0.2),(-0.1,-0.3), (-0.15,-0.2),(-0.2,-0.3)]
mouth = visual.ShapeStim(win, vertices = mouth_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
mouth.draw()

win.flip()
time.sleep (0.5)

pumpkin_radius = (0.2,0.5)
pumpkin_1 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = 'orange', lineWidth = 3, lineColor = 'black')
pumpkin_2 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_3 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_4 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (-0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_5 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (-0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_3.draw()
pumpkin_2.draw()
pumpkin_5.draw()
pumpkin_4.draw()
pumpkin_1.draw()


steel_vertices = [ (-0.03,0.4), (-0.06,0.45), (-0.06,0.65), (-0.03,0.7), (0.03,0.7), (0.06,0.65), (0.06,0.45),(0.03,0.4)]
steel = visual.ShapeStim(win, vertices = steel_vertices, fillColor = [-0.067,-0.067,-1.000] , lineWidth = 3, lineColor = [-1.000,-0.600,-1.000])
steel.draw()

L_eye_vertices = [(-0.2,0.05), (-0.2,0.35), (-0.05,0.2)]
L_eye = visual.ShapeStim(win, vertices = L_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
R_eye_vertices = [(0.2,0.05), (0.2,0.35), (0.05,0.2)]
R_eye = visual.ShapeStim(win, vertices = R_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
L_eye.draw()
R_eye.draw()

mouth_vertices = [(-0.3,0), (-0.2,-0.1),(-0.15,0), (-0.1,-0.1),(-0.05,0),(0,-0.1),(0.05,0),(0.1,-0.1), (0.15,0),(0.2,-0.1), (0.3,0),(0.2,-0.3),(0.15,-0.2), (0.1,-0.3), (0.05,-0.2), (0,-0.3), (-0.05,-0.2),(-0.1,-0.3), (-0.15,-0.2),(-0.2,-0.3)]
mouth = visual.ShapeStim(win, vertices = mouth_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
mouth.draw()

Happy_halloween = visual.TextStim(win, text = 'Happy Halloween!', color = 'red', bold = True, height = 0.2, pos = (0,-0.7))
Happy_halloween.draw()

win.flip()
time.sleep(1)


pumpkin_radius = (0.2,0.5)
pumpkin_1 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = 'orange', lineWidth = 3, lineColor = 'black')
pumpkin_2 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_3 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_4 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (-0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_5 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (-0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_3.draw()
pumpkin_2.draw()
pumpkin_5.draw()
pumpkin_4.draw()
pumpkin_1.draw()


steel_vertices = [ (-0.03,0.4), (-0.06,0.45), (-0.06,0.65), (-0.03,0.7), (0.03,0.7), (0.06,0.65), (0.06,0.45),(0.03,0.4)]
steel = visual.ShapeStim(win, vertices = steel_vertices, fillColor = [-0.067,-0.067,-1.000] , lineWidth = 3, lineColor = [-1.000,-0.600,-1.000])
steel.draw()

L_eye_vertices = [(-0.2,0.05), (-0.2,0.35), (-0.05,0.2)]
L_eye = visual.ShapeStim(win, vertices = L_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
R_eye_vertices = [(0.2,0.05), (0.2,0.35), (0.05,0.2)]
R_eye = visual.ShapeStim(win, vertices = R_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
L_eye.draw()
R_eye.draw()

mouth_vertices = [(-0.3,0), (-0.2,-0.1),(-0.15,0), (-0.1,-0.1),(-0.05,0),(0,-0.1),(0.05,0),(0.1,-0.1), (0.15,0),(0.2,-0.1), (0.3,0),(0.2,-0.3),(0.15,-0.2), (0.1,-0.3), (0.05,-0.2), (0,-0.3), (-0.05,-0.2),(-0.1,-0.3), (-0.15,-0.2),(-0.2,-0.3)]
mouth = visual.ShapeStim(win, vertices = mouth_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
mouth.draw()

win.flip()
time.sleep(0.5)

pumpkin_radius = (0.2,0.5)
pumpkin_1 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = 'orange', lineWidth = 3, lineColor = 'black')
pumpkin_2 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_3 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_4 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (-0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_5 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (-0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_3.draw()
pumpkin_2.draw()
pumpkin_5.draw()
pumpkin_4.draw()
pumpkin_1.draw()


steel_vertices = [ (-0.03,0.4), (-0.06,0.45), (-0.06,0.65), (-0.03,0.7), (0.03,0.7), (0.06,0.65), (0.06,0.45),(0.03,0.4)]
steel = visual.ShapeStim(win, vertices = steel_vertices, fillColor = [-0.067,-0.067,-1.000] , lineWidth = 3, lineColor = [-1.000,-0.600,-1.000])
steel.draw()

L_eye_vertices = [(-0.2,0.05), (-0.2,0.35), (-0.05,0.2)]
L_eye = visual.ShapeStim(win, vertices = L_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
R_eye_vertices = [(0.2,0.05), (0.2,0.35), (0.05,0.2)]
R_eye = visual.ShapeStim(win, vertices = R_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
L_eye.draw()
R_eye.draw()

mouth_vertices = [(-0.3,0), (-0.2,-0.1),(-0.15,0), (-0.1,-0.1),(-0.05,0),(0,-0.1),(0.05,0),(0.1,-0.1), (0.15,0),(0.2,-0.1), (0.3,0),(0.2,-0.3),(0.15,-0.2), (0.1,-0.3), (0.05,-0.2), (0,-0.3), (-0.05,-0.2),(-0.1,-0.3), (-0.15,-0.2),(-0.2,-0.3)]
mouth = visual.ShapeStim(win, vertices = mouth_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
mouth.draw()

Happy_halloween = visual.TextStim(win, text = 'Happy Halloween!', color = 'red', bold = True, height = 0.2, pos = (0,-0.7))
Happy_halloween.draw()

win.flip()
time.sleep(1)

pumpkin_radius = (0.2,0.5)
pumpkin_1 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = 'orange', lineWidth = 3, lineColor = 'black')
pumpkin_2 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_3 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_4 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (-0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_5 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (-0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_3.draw()
pumpkin_2.draw()
pumpkin_5.draw()
pumpkin_4.draw()
pumpkin_1.draw()


steel_vertices = [ (-0.03,0.4), (-0.06,0.45), (-0.06,0.65), (-0.03,0.7), (0.03,0.7), (0.06,0.65), (0.06,0.45),(0.03,0.4)]
steel = visual.ShapeStim(win, vertices = steel_vertices, fillColor = [-0.067,-0.067,-1.000] , lineWidth = 3, lineColor = [-1.000,-0.600,-1.000])
steel.draw()

L_eye_vertices = [(-0.2,0.05), (-0.2,0.35), (-0.05,0.2)]
L_eye = visual.ShapeStim(win, vertices = L_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
R_eye_vertices = [(0.2,0.05), (0.2,0.35), (0.05,0.2)]
R_eye = visual.ShapeStim(win, vertices = R_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
L_eye.draw()
R_eye.draw()

mouth_vertices = [(-0.3,0), (-0.2,-0.1),(-0.15,0), (-0.1,-0.1),(-0.05,0),(0,-0.1),(0.05,0),(0.1,-0.1), (0.15,0),(0.2,-0.1), (0.3,0),(0.2,-0.3),(0.15,-0.2), (0.1,-0.3), (0.05,-0.2), (0,-0.3), (-0.05,-0.2),(-0.1,-0.3), (-0.15,-0.2),(-0.2,-0.3)]
mouth = visual.ShapeStim(win, vertices = mouth_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
mouth.draw()

win.flip()
time.sleep(0.5)

pumpkin_radius = (0.2,0.5)
pumpkin_1 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = 'orange', lineWidth = 3, lineColor = 'black')
pumpkin_2 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_3 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_4 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.671,-0.169,-1.000], pos = (-0.10,0), lineWidth = 3, lineColor = 'black')
pumpkin_5 = visual.Circle(win, radius = pumpkin_radius, edges = 126, fillColor = [0.231,-0.380,-1.000], pos = (-0.20,0), lineWidth = 3, lineColor = 'black')
pumpkin_3.draw()
pumpkin_2.draw()
pumpkin_5.draw()
pumpkin_4.draw()
pumpkin_1.draw()


steel_vertices = [ (-0.03,0.4), (-0.06,0.45), (-0.06,0.65), (-0.03,0.7), (0.03,0.7), (0.06,0.65), (0.06,0.45),(0.03,0.4)]
steel = visual.ShapeStim(win, vertices = steel_vertices, fillColor = [-0.067,-0.067,-1.000] , lineWidth = 3, lineColor = [-1.000,-0.600,-1.000])
steel.draw()

L_eye_vertices = [(-0.2,0.05), (-0.2,0.35), (-0.05,0.2)]
L_eye = visual.ShapeStim(win, vertices = L_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
R_eye_vertices = [(0.2,0.05), (0.2,0.35), (0.05,0.2)]
R_eye = visual.ShapeStim(win, vertices = R_eye_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
L_eye.draw()
R_eye.draw()

mouth_vertices = [(-0.3,0), (-0.2,-0.1),(-0.15,0), (-0.1,-0.1),(-0.05,0),(0,-0.1),(0.05,0),(0.1,-0.1), (0.15,0),(0.2,-0.1), (0.3,0),(0.2,-0.3),(0.15,-0.2), (0.1,-0.3), (0.05,-0.2), (0,-0.3), (-0.05,-0.2),(-0.1,-0.3), (-0.15,-0.2),(-0.2,-0.3)]
mouth = visual.ShapeStim(win, vertices = mouth_vertices, lineWidth = 2, fillColor = [0.984,-0.584,-0.663], lineColor = 'black')
mouth.draw()

Happy_halloween = visual.TextStim(win, text = 'Happy Halloween!', color = 'red', bold = True, height = 0.2, pos = (0,-0.7))
Happy_halloween.draw()

win.flip()
time.sleep(1)


win.close()