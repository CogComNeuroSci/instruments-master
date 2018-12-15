# import modules
from psychopy import visual, event, core, gui
import numpy, pylab

# create a dialog box
info = {"Participant number":0, "Participant name":"Incognito", "Gender":["male", "female", "third gender"], "Age":0, "Handedness":["right", "left", "ambidextrous"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Experiment")

# initialize the window
win = visual.Window([600,500], units = "norm")

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.")
Instructions    = visual.TextStim(win, text = "OK", height = 0.05)
Block_start     = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!")
GaborMask       = visual.GratingStim(win, mask = "circle", ori = 0, sf = 10)
Gabor           = visual.GratingStim(win, mask = "circle")

Instructions.text = (   "In this experiment you will see Gabor patches with vertical stripes.\n" +
                        "Briefly, this orientation will change to one with a slight right of left tilt.\n" +
                        "Indicate as quickly as possible whether the tilt is oriented to the left or the right.\n\n" +
                        "Press the f key for the left tilt (from top left to bottom right).\n" +
                        "Press the j key for the right tilt (from top right to bottom left).\n\n" +
                        "Press the space bar to start the experiment.")

# initialize a clock to measure the RT
my_clock_RT = core.Clock()

# initialize a clock to verify the presentation duration
my_clock_check = core.Clock()

# display the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = ["space"])

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])

# display the blocks
for b in range(3):
    
    # announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    # display the trials in this block
    for i in range(1):
        
        # display the pre-stimulus mask on the screen
        GaborMask.draw()
        win.flip()
        core.wait(1)
        
        # calculate wait time
        wait_time = (1000/60)*(b+1)/1000
        
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        # draw the stimulus on the back buffer
        Gabor.draw()
        win.flip()
        
        # now that the stimulus is on the screen, reset the clocks
        my_clock_RT.reset()
        my_clock_check.reset()
        
        # wait for the duration of the presentation
        core.wait(wait_time)
        
        # remove the stimulus from the screen (replace it by the post-stimulus mask)
        GaborMask.draw()
        win.flip()
        
        # verify the presentation time
        print(my_clock_check.getTime())
        
        # wait for the response
        keys = event.waitKeys(keyList = ["f","j","escape"])
        
        # register the RT
        RT = my_clock_RT.getTime()
        print(RT)
        
        # escape from the trial loop
        if keys[0] == "escape":
            break
    
    # escape from the block loop
    if keys[0] == "escape":
        break

# display the goodbye message
Goodbye.draw()
win.flip()
core.wait(1)

# close the experiment window
win.close()
