## Of course we start off with importing the visual module as explained in the course text of Lesson 4
## note however, that we'll also be importing and using the modules event and core
from psychopy import visual, event, core
import time 

#####################
## Shape drawing 1 ##
#####################

win = visual.Window(size=(500, 400), units='height', color = 'white')

print ('# Shape drawing 1 #')

## Here, we are going to draw basic stimuli
## Keep in mind that we can draw basic stimuli using Python, these shapes can then be used in our experiments 
## When the stimuli become more complex, we will have to load stimuli from a file and display them on screen
## Now, we are going to start by defining some simple shapes
## We will display them on screen later on, but for now, we will stick with defining the properties of our shapes
## Note that some of the code on drawing shapes can be found in Demos > Stimuli > shapes.py of the Psychopy Coder menu

## Here we draw four different shapes, a rectangle, a circle, a triangle (which is in this case a polygon with 3 edges), and an 8 sided polygon
## These shapes can all be drawn using the functions that PsychoPy offers
    ## We recommend to take a look at the PsychoPy site (http://www.psychopy.org/api/visual.html) to explore these functions yourself!
    ## After defining our shapes, we print them on screen
    ## We make sure that the shapes are drawn (.draw) and are displayed on the window (win.flip, keep in mind that what comes before the flip depends on how you defined the window)
    ## We wait for 2 seconds before we show the next stimulus
    ## At the end, we close the window, indicating that we have seen everything and don't need this window anymore for now

## Note that you can also set the window to fullscreen by deleting 'size=(500, 400)' and putting 'fullscr = True' between the brackets
    ## also note that, in that case, you also have to correct your width, height.. as these stay the same, while the window size changes...

rectangle = visual.Rect(win, width = .3, height = .25, pos=(0,0), fillColor = 'black')
circle = visual.Circle(win, radius = .10, pos=(0,0), fillColor = 'black')
triangle = visual.Polygon(win, edges=3, radius=.10, pos=(0,0), fillColor = 'black')
polygon = visual.Polygon(win, edges=8, radius=.10, pos=(0,0), fillColor = 'black')

rectangle.draw()
win.flip()
time.sleep(2)
circle.draw()
win.flip()
time.sleep(2)
triangle.draw()
win.flip()
time.sleep(2)
polygon.draw()
win.flip()
time.sleep(2)
win.close()

#####################
## Shape drawing 2 ##
#####################

win2 = visual.Window(size=(500, 400), units='height', color = 'white')

print ('# Shape drawing 2 #')

## In this example, we show an example from the 'shapes.py' file from the Coder menu, mentioned above
## Here, the shape of the stimulus is actually defined by specifying the xy coordinates of each vertex (Google vertex if you don't know it)
## Keep in mind that the coordinates are interpreted relative to the center of the field 
## If the operation is too slow (with very complex stimuli such as 'coast' in Shapes), setVertices() can be used
## Below, 'donutVert' contains the coordinates for the vertices
## ShapeStim uses the collection of coordinates to create a stimulus
## Notice here that we specified that this stimulus has to appear in win2, and not in win as we specified earlier

donutVert = [[(-.2,-.2),(-.2,.2),(.2,.2),(.2,-.2)],[(-.15,-.15),(-.15,.15),(.15,.15),(.15,-.15)]]
donut = visual.ShapeStim(win2, vertices=donutVert, fillColor='orange', lineWidth=0, size=.75, pos=(0,0))

donut.draw()
win2.flip()
time.sleep(2)
win2.close()

#####################
## Shape drawing 3 ##
#####################

win3 = visual.Window(size=(500, 400), units='height', color = 'white')

print ('# Shape drawing 3 #')

## As we have seen, shapes can be drawn and manipulated in height, edges, position and color in Python
## However, if we wanted to show a very complex shape to a participant, we would have struggled using this approach
## Luckily, Python (or more specifically PsychoPy) allows us to display pictures on screen in an easy fashion
## Below, we show how to define a picture, and flash it on screen

## Download a picture of choice. Call it my_image.jpg (or whatever name you like), and place it in your working directory

stim = 'my_image.jpg'
stimulus = visual.ImageStim(win3, image= stim, size = .9)

stimulus.draw()
win3.flip()
time.sleep(2)
win3.close()

#####################
## Shape drawing 4 ##
#####################

win4 = visual.Window(size=(500, 400), units='height', color = 'white')

print ('# Shape drawing 4 #')

## If you wanted to display a simple text on screen, you can also use PsychoPy for this
## The cleanest way to do this is by defining what you wanted to say up front, and assign this to a variable
## Later in the script, you just call this variable, without having to type everything in the TextStim function
## An example of this is displayed below

## Note that the character '\n' is used to start a new line
## By using the '\n' twice, you can leave some white space between the displayed sentences

## Try to write something yourself!

instructions = "In this scene \nthere a 47 people. \n \nNone of them \ncan be seen. \n \n'MontyPython Quote Generator'"

ExampleText = visual.TextStim(win4, text=instructions,units='norm', height=0.12, color='Black',pos=[0,0], alignHoriz='center',flipHoriz=False)

ExampleText.draw()
win4.flip()
time.sleep(4)
win4.close()
core.quit()

#########
## END ##
#########
