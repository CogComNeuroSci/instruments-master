from psychopy import visual
import time
win = visual.Window(size = [600,600], color = 'black', monitor="testmonitor", units="norm")

basestim = visual.Polygon(win, edges = 999,radius = 0.10,pos = (0,0), lineColor = 'black', fillColor = 'orangered', size= (8,5.7))

eye1=visual.Polygon(win,edges = 3, radius = 0.12, pos = (0.25, 0.15),lineColor = 'black', fillColor = 'black',size = (1.5,1))
eye2=visual.Polygon(win,edges = 3, radius = 0.12, pos = (-0.25, 0.15),lineColor = 'black', fillColor = 'black',size = (1.5,1))

lowermouth=visual.Polygon(win,edges = 999, radius = 0.05, pos = (0,-0.2),lineColor = 'black', fillColor = 'black', size = (10,5))
uppermouth=visual.Polygon(win, edges = 999, radius = 0.05, pos = (0,-0.05),lineColor = 'orangered', fillColor = 'orangered', size = (11,4))

nose=visual.Polygon(win,edges = 3, radius = 0.09, pos = (0,-0.1),lineColor='black', fillColor = 'black')

tooth1=visual.Polygon(win,edges = 4, radius = 0.1, pos = (-0.1,-0.2),lineColor = 'orangered', fillColor = 'orangered', size = (1,1.3))
tooth2=visual.Polygon(win,edges = 4, radius = 0.1, pos = (0.1,-0.2),lineColor = 'orangered', fillColor = 'orangered', size = (1,1.3))

toppart1=visual.Polygon(win,edges = 999, radius = 0.015, pos = (0,0.5),lineColor = (-0.318,-0.176,-0.608), fillColor = (-0.318,-0.176,-0.608), size = (17,5))
toppart2=visual.Polygon(win,edges = 4, radius = 0.015, pos = (0,0.6), lineColor = (-0.318,-0.176,-0.608), fillColor = (-0.318,-0.176,-0.608), size = (12,5), ori=-50)
toppart3=visual.Polygon(win,edges = 4, radius = 0.015, pos = (0.04,0.73), lineColor = (-0.318,-0.176,-0.608), fillColor = (-0.318,-0.176,-0.608), size = (12,5), ori = -50)
toppart4=visual.Polygon(win,edges = 4, radius = 0.014, pos = (0.067,0.82), lineColor = (-0.318,-0.176,-0.608), fillColor = (-0.318,-0.176,-0.608), size = (7,7), ori=62)
toppart5=visual.Polygon(win,edges = 4, radius = 0.012, pos = (0.115,0.807), lineColor = (-0.318,-0.176,-0.608), fillColor = (-0.318,-0.176,-0.608), size = (11,7), ori = 50)

halloweentext=visual.TextStim(win, text = "Happy Halloween!", height = 0.14, color = 'orangered', font = "Blackadder ITC", pos = (0,-0.7))

basestim.draw()
toppart1.draw()
toppart2.draw()
toppart3.draw()
toppart4.draw()
toppart5.draw()
eye1.draw()
eye2.draw()
lowermouth.draw()
uppermouth.draw()
tooth1.draw()
tooth2.draw()
nose.draw()
halloweentext.draw()

win.flip()
time.sleep(5)

win.close()