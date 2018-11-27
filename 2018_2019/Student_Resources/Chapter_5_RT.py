# import the necessary modules
from psychopy import event, visual, core

# Initialize the window
win = visual.Window([400, 400], color = "white")

# Initialize the graphical elements
starVert = [(0.0,0.5),(0.09,0.18),(0.39,0.31),(0.19,0.04),(0.49,-0.11),(0.16,-0.12),(0.22,-0.45),(0.0,-0.2),(-0.22,-0.45),(-0.16,-0.12),(-0.49,-0.11),(-0.19,0.04),(-0.39,0.31),(-0.09,0.18)]
star = visual.ShapeStim(win, vertices=starVert, fillColor='blue', lineWidth=2, lineColor='white')

# Initialize a clock to measure the RT
my_clock1 = core.Clock()
my_clock2 = core.Clock()
my_clock3 = core.Clock()

# Perform a few trials
for trial in range(3):
    
    # Reset the clock a the start of the trial
    my_clock1.reset()
    
    # Display the star on the screen
    star.draw()
    
    # Clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    
    # Reset the clock before flipping the screen
    my_clock2.reset()
    
    # Flip the star on the screen
    win.flip()
    
    # Now that the star is on the screen, reset the clock
    my_clock3.reset()
    
    # Wait for the response
    keys = event.waitKeys()
    #core.wait(0.01)
    
    # Register the RT
    RT1 = my_clock1.getTime() * 1000
    RT2 = my_clock2.getTime() * 1000
    RT3 = my_clock3.getTime() * 1000
    
    # Print the RT on the screen
    print("Your RT is not {0} ms, nor {1} ms; it's {2} ms".format(round(RT1,1),round(RT2,1),round(RT3,1)))
    print("The measurement error is either {0} ms, or {1} ms".format(round(RT1-RT3,1),round(RT2-RT3,1)))

# Close the experiment window
win.close()
core.quit()
