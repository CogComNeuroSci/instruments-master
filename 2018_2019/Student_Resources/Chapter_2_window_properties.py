##########################
## Printing on a window ##
##########################

## Of course we start off with importing the visual module and the time module, as explained in the course text of Chapter 2
from psychopy import visual
import time 

## You define a name for the window: in our case this is 'win'
## This command just says that whenever you call 'win', you actually refer back to the particular window named 'win' which is displayed automatically on the initial call
## Keep in mind that the name of your window is arbitrary, you can call your window 'win', 'window', even 'My_awesome_computer_screen', it would not make a difference
    ## However, note that 'My awesome computer screen' would not work as a variable name, as spaces are forbidden characters when defining a variable name
## We can see the most basic command used to open a window right below

win = visual.Window()

## Several arguments can be filled in between the brackets
## These arguments define extra properties of the window
## For an overview of all the parameters used to define the properties of a window, we refer to the webpage PsychoPy offers:
    ## http://www.psychopy.org/api/visual/window.html
## To illustrate the characteristics of the screen, we will print a text on screen, and alter the properties of the window in the process
## More specifically, the code below creates a screen that prints "Example text to explain the properties of 'visual.Window()'" as a text on screen
## The window will remain there for two seconds

text1 = "Example text to explain the properties of 'visual.Window()'"
TextOnScreen = visual.TextStim(win, text = text1)

TextOnScreen.draw()
win.flip()
time.sleep(2)
win.close()

## Below, we will highlight the most important arguments of 'visual.Window()'

## size: define the size of your window, usually the size is defined in pixels 
    ## Note: if you want to fill your entire screen with your window, just use 'fullscr = True'
## uncomment ONE of the 'win2 = ' command by deleting the ## in front of the code, and run the program
## Look at how the window size changes depending on what you defined between the brackets!
## Also, do not forget to uncomment the ## before the 'fullscr = True' code, then you will see that the window fills your entire screen
    ## Note that you have to delete the ## of only one line of code, if you would delete all the ##, then the first three windows would be overwritten by the next one
    ## and only the fourth (in this case the 'fullscr'-code) would remain on screen for two seconds

## win2 = visual.Window(size = (500, 400))
## win2 = visual.Window(size = (800, 600))
## win2 = visual.Window(size = (120, 80))
win2 = visual.Window(fullscr = True)

text1 = "Example text to explain the properties of 'visual.Window()'"
TextOnScreen = visual.TextStim(win2, text = text1)

TextOnScreen.draw()
win2.flip()
time.sleep(2)
win2.close()

## The attentive programmer might have noticed that we defined a new window: 'win2'
## We did this by closing win with the command (win.close()), and defining a new window which has a new size
## The reason is that you cannot alter the basic properties of a window once it is defined (however, you can still put different stimuli on the screen)
    ## More specifically, if we defined 'win' at the beginning of my code, and later in the code, we want to redefine the size of my window, we cannot alter 'win'
    ## In other words: we should create a new window which has the properties we desire
    ## Therefore, we define 'win2' (or 'My_awesome_computer_screen' if you really want to), which has the size we need
## From now on, we will create new screens that have the properties we want to illustrate

## pos: define the location of your window
    ## The default value is in the center: the center of your window will be in the middle of your screen
    ## We can alter the position to make sure that the center of your window is in another position
    ## The first number between the brackets represents the x coordinate, the second one represents the y coordinate 
    ## Again, we can comment out the commands one by one and look at the effect it has

## win3 = visual.Window(pos = (500, 400))
## win3 = visual.Window(pos = (100, 400))
## win3 = visual.Window(pos = (400, 400))
## win3 = visual.Window(pos = (1000, 600))
win3 = visual.Window(pos = (100, 100))

text1 = "Example text to explain the properties of 'visual.Window()'"
TextOnScreen = visual.TextStim(win3, text = text1)

TextOnScreen.draw()
win3.flip()
time.sleep(2)
win3.close()

## color: define the color of your window
    ## Notice here that there are three major ways of defining the color of your window:
        ## 1) color=[1,-1,-1]
            ## Define your color based on the RGB (Red Green Blue) index
            ## Every color can be created by mixing these three basic colors
            ## The numbers define how much of each you add, with 1 meaning the maximum, and -1 meaning the minimum
            ## In the code above, we have a high amount of red, and a minimum of green and blue, meaning that our screen will be red
            ## Black has the index [-1,-1,-1] (i.e. no colors)
            ## White has the code [1,1,1], as this is a mix of all basic colors
            ## Keep in mind that the RGB code can also be defined with numbers ranging from 0 to 255, where 255 is the maximum
            ## To use this definition, we should define the 'colorSpace' as 'rgb255' (an example below illustrates this approach)
        ## 2) color= 'red'
            ## By far the easiest way to define color is by typing the color you need between ''
            ## In point two, our window will also be colored red, without having to define the RGB index
            ## Mind that this approach is convenient when the exact color shade does not really matter, but the RGB approach can be used to create specific colors
            ## while this approach cannot do that
            ## A complete overview of the colors we can define by words is offered on:
                ## https://www.w3schools.com/colors/color_tryit.asp?color=Snow
        ## 3) color= #FFFAFA
            ## Following the last link, we can also see a the 'HEX' code beside the color names
            ## This is rather advanced, so we'll leave it up to you to explore if this interests you

win4 = visual.Window(color = 'WhiteSmoke')
## win4 = visual.Window(color = [255,250,250], colorSpace = 'rgb255')
## win4 = visual.Window(color = '#FFFAFA')

text1 = "Example text to explain the properties of 'visual.Window()'"
TextOnScreen = visual.TextStim(win4, text = text1, color = 'black')

TextOnScreen.draw()
win4.flip()
time.sleep(2)
win4.close()

## units: defines the default units of stimuli initialized in the window
## For a more elaborate explanation of the units of window, we refer to:
    ## http://www.psychopy.org/general/units.html#units
## Here, we provide a short overview of all units:
    ## None: the default value
    ## height: normalized: stimulus scaled to screen:
        ## Here, everything is specified relative to the height of the window (!! window, NOT your physical monitor)
    ## norm: normalized: stimulus scaled to screen:
        ## In normalized units, the window ranges from -1 to 1, both for the x and y-axis
        ## This definition takes differences in screen size into account (i.e. the code can be used on multiple screens without alteration)
    ## deg: stimulus size fixed to screen:
        ## uses degrees of visual angle to set the size and location: depends on location of the participant respective to the monitor
        ## IMPORTANT: to work, this type of unit requires information about the monitor width in cm and pixels and the viewing distance in cm
            ## This can be changed in the Tools > Monitor Center
            ## There, the needed information can be filled in
            ## If it does not work out, you can ignore this, as the 'norm' and 'height' units are used more often
        ## There are three types:
            ## deg
            ## degFlatPos
            ## degFlat
    ## cm: stimulus size fixed to screen:
        ## Set the size and location of the stimulus in centimeters on the screen
        ## IMPORTANT: to work, this type of unit requires information about the screen width in cm and pixels and the viewing distance in cm
    ## pix:
        ## specify the size and location of your stimulus in pixels, mind that computer monitors differ in size, and this unit definition does not take this into account
        ## IMPORTANT: to work, this type of unit requires information about the size of the monitor (not window) in pixels
    ## To illustrate the various definitions of size and units of size, we will alter the text shown on screen

## None
win5 = visual.Window(color = 'WhiteSmoke')
rectangle = visual.Rect(win5, width = .3, height = .25, pos = (0,0), fillColor = 'black')

## height
## win5 = visual.Window(units='height', color = '#FFFAFA')
## rectangle = visual.Rect(win5, width = .3, height = .25, pos = (0,0), fillColor = 'black')

## Norm
## win5 = visual.Window(units='norm', color = '#FFFAFA')
## rectangle = visual.Rect(win5, width = .3, height = .25, pos = (0,0), fillColor = 'black')
## or
## win5 = visual.Window(units='norm', color = '#FFFAFA')
## rectangle = visual.Rect(win5, width = .3, height = .25, pos = (-.5,-.5), fillColor = 'black')

## Deg
## win5 = visual.Window([800,600], units='deg', color = '#FFFAFA')
## rectangle = visual.Rect(win5, width = .3, height = .25, pos = (0,0), fillColor = 'black')

## cm
## win5 = visual.Window()
## rectangle = visual.Rect(win5, width = .3, height = .25, units = 'cm', pos = (0,0), fillColor = 'black')

## pix
## win5 = visual.Window([800,600], units = 'pix', color = '#FFFAFA')
## rectangle = visual.Rect(win5, width = .3, height = .25, pos = (0,0), fillColor = 'black')

rectangle.draw()
win5.flip()
time.sleep(2)
win5.close()

## We finish with some very advanced stuff (this bit is for those who like to delve a bit deeper)
## Define the height and width of your stimulus based on your monitor resolution
## Here, it depends on the value that is returned from the code we see below
## As the resolution of the monitor is expressed in pixels, you'll also have to express the dimensions of the rectangle in pixels

import platform
import ctypes
resolution = []
if (platform.system() == 'Windows'): 
    user32 = ctypes.windll.user32
    
    width = user32.GetSystemMetrics(0)
    width = width
    
    height = user32.GetSystemMetrics(1)
    height = height
    
    resolution.append(width)
    resolution.append(height)

print(resolution)

win6 = visual.Window(color = 'WhiteSmoke')
rectangle = visual.Rect(win6, width = ((resolution[0])/8), height = ((resolution[1])/8), units = 'pix', pos = (0,0), fillColor = 'black')

rectangle.draw()
win6.flip()
time.sleep(2)
win6.close()

#########
## END ##
#########