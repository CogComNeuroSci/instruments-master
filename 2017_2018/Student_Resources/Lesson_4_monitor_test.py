# setting your monitor for well-controlled experimentation, without using the Builder
from psychopy import monitors
mon = monitors.Monitor("mijn laptop scherm") # loads (if it exists) or defines (if it does not exist) a monitor setting
mon.setDistance(40) # how many cm is your pp from the screen (measure this in the good old-fashioned way)
mon.setWidth(30) # how wide is the screen in cm
mon.setSizePix((1200,500)) # size in pixels
# here ends the monitor setting. in a separate (or the same) experiment file, you can now do something like this:
from psychopy import visual
import time
venster = visual.Window(size=[600,400],units = "deg", monitor=mon) # specify object sizes in degrees visual angle
# next line makes sure the pp sees it at exactly 4 degrees (if attributes above are specified correctly, of course!)
vierkant = visual.Rect(venster,size=4) 
vierkant.draw()
venster.flip()
time.sleep(3)
venster.close()