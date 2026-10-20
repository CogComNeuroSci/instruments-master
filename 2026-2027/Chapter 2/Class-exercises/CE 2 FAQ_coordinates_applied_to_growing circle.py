# load the necessary modules
from psychopy import visual
import time

# open an experiment window
win = visual.Window(size = (500, 400), units = "height", color = "white")

# the radius of the circles you want
sizes = [.05, .10, .15]

# loop over the three circles
for i in sizes:
    circle = visual.Circle(win, radius = i, pos = (0,0), fillColor = "black")
    circle.draw()
    win.flip()
    time.sleep(1)

## If you look at the output, you'll see that we get a nice circle (not an ellipse) because we are working with the 'height' coordinate system.
## This is necessary because we have a window that doesn't have the same width and height, so we can't use a 'norm' coordinata system (this will result in ellipses, no circles).

## Next, because we are working in the 'height' coordinate system, the values in 'sizes' will be interpreted in this coordinate system.
## As the height' of the screen is 400 pixels, the radius of the first circle will be 400*0.05 = 20 pixels, or 5% of the scree height.
## Likewise the second and third circle will have a height of 10% and 15% of the screen.

## As you know, the radius is half of the circle diameter,
## so the three circles will take up 10%, 20% and 30% of the screen height, respectively.

## To see this more clearly, let's plot a red circle with a radius of 25% of the screen height (so radius = 0.25).
## This should get us a red circle with a diameter that takes up half of the screen height (50%).

circle = visual.Circle(win, radius = 0.25, pos = (0,0), fillColor = "red")
circle.draw()
win.flip()
time.sleep(2)

## Next, let's plot a blue circle with a radius of 50% of the screen height (so radius = 0.5).
## This should get us a blue circle with a diameter that takes up the entire height of the screen (100%).
## Note that although the circle touches the top and bottom of the screen, it doesn't touch the sides of the screen.

circle = visual.Circle(win, radius = 0.5, pos = (0,0), fillColor = "blue")
circle.draw()
win.flip()
time.sleep(2)