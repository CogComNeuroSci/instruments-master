from psychopy import visual, core
from psychopy.visual import ShapeStim
win = visual.Window(fullscr = True , units='norm')

#pompoen maken
pumpkinVert = [(-3/10,3/10),(-3/10,2/10),(-4/10,2/10),(-4/10,1/10),(-1/2,1/10),(-1/2,-3/10),(-4/10,-3/10),(-4/10,-4/10),(-3/10,-4/10),(-3/10,-1/2),(-2/10,-1/2),(-2/10,-6/10),(2/10,-6/10),(2/10,-1/2),(3/10,-1/2),(3/10,-4/10),(4/10,-4/10),(4/10,-3/10),(1/2,-3/10),(1/2,1/10),(4/10,1/10),(4/10,2/10),(3/10,2/10),(3/10,3/10)]
pumpkin = ShapeStim(win, vertices = pumpkinVert, fillColor='orange', lineWidth=0.5, pos=(0,0))

#steeltje van de pompoen
steeltjeVert = [(0,1/2),(0,4/10),(-15/100,4/10),(-15/100,3/10),(1/10,3/10),(1/10,4/10),(2/10,4/10),(2/10,1/2),(0,1/2)]
steeltje = ShapeStim(win, vertices = steeltjeVert, fillColor='green', lineWidth=0.5, pos=(0,0))


#ogen van de pompoen 
oogVert= [(-3/10,1/10),(-2/10,-1/10),(-1/10,1/10)]
oog= ShapeStim(win, vertices = oogVert, fillColor='black', lineWidth=0.5, pos=(0,0))

pupilVert=[(-25/100,5/100),(-2/10,0),(-15/100,5/100)]
pupil=ShapeStim(win, vertices = pupilVert, fillColor='white', lineWidth=0.5, pos=(0,0))

tweedeoogVert= [(1/10,1/10),(2/10,-1/10),(3/10,1/10)]
tweedeoog= ShapeStim(win, vertices = tweedeoogVert, fillColor='black', lineWidth=0.5, pos=(0,0))

tweedepupilVert=[(25/100,5/100),(2/10,0),(15/100,5/100)]
tweedepupil=ShapeStim(win, vertices = tweedepupilVert, fillColor='white', lineWidth=0.5, pos=(0,0))

#mond van de pompoen 
mondVert = [(-3/10,-2/10),(-3/10,-3/10),(-2/10,-3/10),(-2/10,-35/100),(2/10,-35/100),(2/10,-3/10),(3/10,-3/10),(3/10,-2/10)]
mond= ShapeStim(win, vertices = mondVert, fillColor='red', lineWidth=0.5, pos=(0,0))

binnenkantmondVert= [(-15/100,-35/100),(-1/10,-3/10),(-5/100,-35/100),(0,-3/10),(5/100,-35/100),(1/10,-3/10),(15/100,-35/100),(2/10,-2/10),(15/100,-25/100),(1/10,-2/10),(5/100,-25/100),(0,-2/10),(-5/100,-25/100),(-1/10,-2/10),(-15/100,-25/100),(-2/10,-2/10)]
binnenkantmond=ShapeStim(win, vertices = binnenkantmondVert, fillColor='darkred', lineWidth=0.5, pos=(0,0))

#tekst Halloween
stim = visual.TextStim(win, text = "Happy Halloween",font ='Algerian', color = 'darkorange', pos = (0,8/10))

pumpkin.draw()
steeltje.draw()
oog.draw()
pupil.draw()
tweedeoog.draw()
tweedepupil.draw()
mond.draw()
binnenkantmond.draw()
stim.draw()


win.flip()
core.wait(10)
win.close()
core.quit()