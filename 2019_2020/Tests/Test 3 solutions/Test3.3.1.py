# importing modules
import time
from psychopy import visual, event, gui, core

# create a dialog box
info = {"Participant name":"Unknown", "Participant number":0, "Age":0, "Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary = info, title = "Flanker task")

# display preparation
win = visual.Window(size = [1000, 700], units = "norm")

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.")
Instructions    = visual.TextStim(win, text = "OK", height = 0.05)
Block_start     = visual.TextStim(win, text = "OK")
Fixation        = visual.TextStim(win, text = "+")
Target          = visual.TextStim(win, text = "<<<<<")
Feedback        = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!\n\nPress the space bar to end the experiment.")

Instructions.text = (   "In this experiment you will see five arrows and you need to respond to the central arrow.\n" +
                        "Indicate as quickly as possible whether the central arrow points to the left or the right.\n\n" +
                        "Press the f key for a left pointing arrow.\n" +
                        "Press the j key for a right pointing arrow.\n\n" +
                        "Press the space bar to start the experiment.")

# initialize the experiment properties
nblocks         = 2
ntrials         = 1
allowedKeys     = ["f","j","b","e"]

# initialize a clock to measure the RT
my_clock_RT = core.Clock()

# display the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the blocks
for blocki in range(nblocks):
    
    # announce what block is about to start
    Block_start.text = "Block " + str(blocki+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    # display the trials in this block
    for triali in range(ntrials):
    
        # display the fixation cross
        Fixation.draw()
        win.flip()
        time.sleep(0.5)
        
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard")
    
        # display the target
        Target.draw()
        win.flip()
                
        # now that the stimulus is on the screen, reset the clocks
        my_clock_RT.reset()
        
        # wait for the response
        keys = event.waitKeys(keyList = allowedKeys, maxWait = 1)
                
        # register the RT
        RT = my_clock_RT.getTime()
        
        # check whether a response has been given
        if keys is not None:
            
            # escape from the trial loop
            if keys[0] in ["b","e"]:
                break
            
            # determine the accuracy
            ACC = int(keys[0] == "f")
            
            # determine and display the feedback message
            if ACC == 1:
                Feedback.text = "Correct!"
            else:
                Feedback.text = "Wrong answer!"
            
        else:
            
            # determine the accuracy
            ACC = 0
            
            # if no response has been given, encourage the participant to go faster
            Feedback.text = "Too slow!"
        
        # display the feedback message
        Feedback.draw()
        win.flip()
        time.sleep(1)
        
        print(keys)
        print(RT)
        print(ACC)

    # check whether a response has been given
    if keys is not None:
        
        # escape from the block loop
        if keys[0] == "e":
            break
        
# display the goodbye message
Goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

# close the experiment window
win.close()
