# load the necessary modules
import time
from psychopy import visual, monitors

# load (if it exists) or define (if it does not exist) a monitor
mon = monitors.Monitor("my laptop screen")

# set all the necessary parameters to work with visual degrees
mon.setDistance(40) # how many cm is your pp from the screen (measure this in the good old-fashioned way)
mon.setWidth(30) # how wide is the screen in cm
mon.setSizePix((800,500)) # size in pixels

# open an experiment window
win = visual.Window(monitor = mon)


# The goal is to draw a rectangle with a width and height of 0.5 (the default)

stimulus = visual.rect.Rect(win, width = 0.5, height = 0.5, units = "height", color = "blue")
stimulus.draw()
## 0.5 of the height of the screen means 250 pixels wide and heigh, so we get a square of 250*250 pixels
stimulus = visual.rect.Rect(win, width = 0.5, height = 0.5, units = "norm", color = "red")
stimulus.draw()
## 0.5 of the width of the screen is 200 (because the 800 pixels are converted to values from -1 to 1 in the normalized coordinate system)
## 0.5 of the height of the screen is 125 (because the 500 pixels are converted to values from -1 to 1 in the normalized coordinate system)
## Note that because the width and height are determined independently, and because the width and height of the window are not the same, this will result in a rectangle instead of a square.
stimulus = visual.rect.Rect(win, width = 0.5, height = 0.5, units = "deg", color = "yellow")
stimulus.draw()
## here the size can be calculated based on the setting of the window at the top of the script

# display on the screen
win.flip()
time.sleep(2)


# The goal is to draw a rectangle with a size of 0.5

stimulus = visual.rect.Rect(win, size = 0.5, units = "height", color = "blue")
stimulus.draw()
stimulus = visual.rect.Rect(win, size = 0.5, units = "norm", color = "red")
stimulus.draw()
stimulus = visual.rect.Rect(win, size = 0.5, units = "deg", color = "yellow")
stimulus.draw()
## The idea is the same as in the block of code above but all the rectangles are half as large.

# display on the screen
win.flip()
time.sleep(2)


# The goal is to draw a circle with a radius of 0.5 (the default)

stimulus = visual.Circle(win, radius = 0.5, units = "height", color = "blue")
stimulus.draw()
## 0.5 of the height of the screen means a radius of half the height of the screen (250 pixels), so we get a circle with a diameter of the full height of the screen (500 pixels).
stimulus = visual.Circle(win, radius = 0.5, units = "norm", color = "red")
stimulus.draw()
## 0.5 of the width of the screen means that along the horizontal axis, the circle will have a radius of a fourth of the screen width (200 pixels)
## 0.5 of the height of the screen means that along the vertical axis, the circle will have a radius of a fourth of the screen height (125 pixels)
## Note that because the horizontal and vertical radius of the circle are different, we will get an ellipse.
stimulus = visual.Circle(win, radius = 0.5, units = "deg", color = "yellow")
stimulus.draw()
## here the size can be calculated based on the setting of the window at the top of the script (the circle will have a diameter of 1 visual degree)

# display on the screen
win.flip()
time.sleep(2)


# The goal is to draw a circle with a size of 0.5

stimulus = visual.Circle(win, size = 0.5, units = "height", color = "blue")
stimulus.draw()
stimulus = visual.Circle(win, size = 0.5, units = "norm", color = "red")
stimulus.draw()
stimulus = visual.Circle(win, size = 0.5, units = "deg", color = "yellow")
stimulus.draw()
## The idea is the same as in the block of code above but all the circles are half as large.

# display on the screen
win.flip()
time.sleep(2)


# the end!
win.close()