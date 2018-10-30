from psychopy import visual
import time 
win = visual.Window(fullscr=True,color='black')
# Esther: tot hier perfect, maar misschien hier en daar een witlijntje en een lijntje comments om je code op te vrolijken en uit te leggen?

# Esther: ik zie dat je een bepaalde tint organje hebt gezocht en die blijft gebruiken.
# Esther: een handige shortcut hier is om op voorhand dat oranje te definiëren:
# OrangjePieter = (0.851,-0.075,-1.000)
# Esther: daarna kan je dan naar die OranjePieter verwijzen, zoals hier:
# Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = OrangjePieter,lineColor=OrangjePieter)
# Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = OrangjePieter,lineColor=OrangjePieter)
# Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = OrangjePieter,lineColor=OrangjePieter)
# Esther: als je achteraf dan toch een andere tint oranje wil kiezen, hoef je dat maar op 1 plaats aan te passen ;)


pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)

# Esther: Vanaf hier maak je telkens opnieuw de visuele objecten aan (pumpkinVert, pumpkin, kop etc.) terwijl die eigenlijk al gemaakt zijn.
# Esther: dat is niet nodig. Het volstaat om enkel de .draw() te herhalen
# Esther: weer heel wat lijnen code minder!
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
HappyHalloween = visual.TextStim(win, text = "Happy Halloween!", color='red',font='Stencil',pos=(0.0,-0.7))
HappyHalloween.draw()
win.flip()
time.sleep(1)
pumpkinVert = [(0.0,0.46),(-.1,0.46),(-0.2,.44),(-.3,0.39),(-0.4,0.28),(-0.42,0.26),(-0.44,0.23),(-0.46,0.19),(-0.48,0.11),(-0.495,0.03),(-0.5,0.0),(0.0,0.46),(0.1,0.46),(0.2,0.44),(0.3,0.39),(0.4,0.28),(0.42,0.26),(0.44,0.23),(0.46,0.19),(0.48,0.11),(0.495,0.03),(0.5,0.0),(0.0,-0.46),(0.1,-0.46),(0.2,-0.44),(0.3,-0.39),(0.4,-0.28),(0.42,-0.26),(0.44,-0.23),(0.46,-0.19),(0.48,-0.11),(0.495,-0.03),(0.5,0.0),(0.0,-0.46),(-0.1,-0.46),(-0.2,-0.44),(-0.3,-0.39),(-0.4,-0.28),(-0.42,-0.26),(-0.44,-0.23),(-0.46,-0.19),(-0.48,-0.11),(-0.495,-0.03),(-0.5,0.0)]
pumpkin = visual.ShapeStim(win, vertices = pumpkinVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
pumpkin.draw()
kopVert=[(0.03,0.46),(-0.03,0.56),(0.03,0.66),(-0.03,0.66),(-0.09,0.56),(-0.03,0.46)]
kop=visual.ShapeStim(win, vertices = kopVert, fillColor = (-0.129,-0.569,-1.000),lineColor = (-0.129,-0.569,-1.000))
kop.draw()
neusVert=[(-0.05,0.05),(0.05,0.05),(0,-0.05)]
neus=visual.ShapeStim(win, vertices = neusVert, fillColor = 'black', lineColor='black')
neus.draw()
LoogVert = [(-0.11,0.18),(-0.21,0.18),(-0.16,0.28)]
Loog=visual.ShapeStim(win, vertices = LoogVert, fillColor = 'black',lineColor='black')
Loog.draw()
RoogVert = [(0.11,0.18),(0.21,0.18),(0.16,0.28)]
Roog = visual.ShapeStim(win, vertices = RoogVert, fillColor = 'black',lineColor='black')
Roog.draw()
MondVert = [(-0.25,-0.10),(-0.20,-0.18),(-0.15,-0.20),(0.15,-0.20),(0.20,-0.18),(0.25,-0.10),(0.20,-0.28),(0.15,-0.30),(-0.15,-0.30),(-0.20,-0.28),(-0.25,-0.10)]
Mond= visual.ShapeStim(win, vertices = MondVert, fillColor = 'black',lineColor='black')
Mond.draw()
LtandVert = [(-0.10,-0.20),(-0.06,-0.20),(-0.08,-0.25)]
Ltand = visual.ShapeStim(win, vertices = LtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Ltand.draw()
RtandVert = [(0.10,-0.20),(0.06,-0.20),(0.08,-0.25)]
Rtand = visual.ShapeStim(win, vertices = RtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Rtand.draw()
OtandVert = [(-0.02,-0.30),(0.02,-0.30),(0.0,-0.25)]
Otand = visual.ShapeStim(win, vertices =OtandVert, fillColor = (0.851,-0.075,-1.000),lineColor=(0.851,-0.075,-1.000))
Otand.draw()
win.flip()
time.sleep(0.5)
win.close()
