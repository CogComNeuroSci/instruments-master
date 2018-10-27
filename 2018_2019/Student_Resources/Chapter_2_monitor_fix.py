# setting your monitor for well-controlled experimentation, without using the Monitor Center (the GUI interface)

# load the monitor library
from psychopy import monitors

# load the other librarie we'll need
from psychopy import visual
import time

# load (if it exists) or define (if it does not exist) a monitor
mon = monitors.Monitor("my laptop screen")

# set all the necessary parameters to work with visual degrees
mon.setDistance(40) # how many cm is your pp from the screen (measure this in the good old-fashioned way)
mon.setWidth(30) # how wide is the screen in cm
mon.setSizePix((1200,500)) # size in pixels


# Now that the monitor settings are done, use this monitor when opening a window
win = visual.Window(size = [600,400], units = "deg", monitor = mon) # specify object sizes in degrees visual angle

# next line makes sure the pp sees it at exactly 4 degrees (if attributes above are specified correctly, of course!)
square = visual.Rect(win, width = 4, height = 4) 
square.draw()
win.flip()
time.sleep(3)
win.close()