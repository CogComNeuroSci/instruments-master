# Put a picture of a Halloween pumpkin on your screen (downloaded from the Web).

from psychopy import visual
import time 

win = visual.Window(fullscr = True)
rect = visual.ImageStim(win, image = "HalloweenPumpkin.jpg")

rect.draw()
win.flip()
time.sleep(2)
win.close()