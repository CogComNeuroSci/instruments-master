# Draw a square in a Window that is exactly four visual degrees (irrespective of screen physical properties).

from psychopy import visual
import time 

win = visual.Window(fullscr = True, monitor = "testMonitor", units = "deg")
rect = visual.rect.Rect(win, width = 1, height = 4, color = (1, 1, 1))

rect.draw()
win.flip()
time.sleep(2)
win.close()