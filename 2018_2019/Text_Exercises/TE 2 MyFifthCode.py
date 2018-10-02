from psychopy import visual
import time 
win = visual.Window([300,200])

apple_picture = "Apple-icon.png"
picture = visual.ImageStim(win, image = apple_picture)
picture.draw()

win.flip()
time.sleep(2)
win.close()