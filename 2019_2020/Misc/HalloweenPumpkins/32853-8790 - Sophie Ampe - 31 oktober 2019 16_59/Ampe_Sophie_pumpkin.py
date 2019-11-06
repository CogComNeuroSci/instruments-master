from psychopy import visual
import time
#Put an orange pumpkin
win = visual.Window(fullscr = True, monitor = 'testMonitor', units = 'height')
pumpkin = visual.Circle(win, radius=0.5, pos=(0,0), edges=32, fillColor='orange', lineColor='orange', size=(0.8,0.5))
pumpkin.draw()
happy = visual.TextStim(win, text="Happy Halloween!", pos=(0,-0.35), height=0.09, color=(-1,-1,-1))
happy.draw()
mouth = visual.Line(win, start=(-0.1, -0.1), end=(0.1, -0.1))
mouth.draw()
eyes1 = visual.Circle(win, radius=0.5, pos=(-0.19,0.1), edges=32, fillColor='black', lineColor='black', size=(0.08,0.08))
eyes1.draw()
eyes2 = visual.Circle(win, radius=0.5, pos=(0.19,0.1), edges=32, fillColor='black', lineColor='black', size=(0.08,0.08))
eyes2.draw()
win.flip() 
time.sleep(3) 
win.close()
