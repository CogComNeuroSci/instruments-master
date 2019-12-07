# importing modules
from psychopy import visual, event, gui

# create a dialog box
info = {"Participant name":"Unknown", "Participant number":0, "Age":0, "Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary = info, title = "Flanker task")

# display preparation
win = visual.Window(size = [1000, 700], units = "norm")

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.")
Instructions    = visual.TextStim(win, text = "OK", height = 0.05)
Block_start     = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!\n\nPress the space bar to end the experiment.")

Instructions.text = (   "In this experiment you will see five arrows and you need to respond to the central arrow.\n" +
                        "Indicate as quickly as possible whether the central arrow points to the left or the right.\n\n" +
                        "Press the f key for a left pointing arrow.\n" +
                        "Press the j key for a right pointing arrow.\n\n" +
                        "Press the space bar to start the experiment.")

# initialize the experiment properties
nblocks = 2

# display the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the blocks
for b in range(nblocks):
    
    # announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = "space")

# display the goodbye message
Goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

# close the experiment window
win.close()
