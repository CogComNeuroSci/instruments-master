#Import modules
from psychopy import visual, event, core, gui
import time, numpy 

#Initialize the window
win = visual.Window ([600, 500], units = "norm")

#Initialize dialog box
#If I run the experiment the dialogue box does appear but nothing more happens. I can't check any of the boxes or type information.
info = {"Participant number":0, "Participant name": "Unknown", "Age":0, "Gender":["male", "female", "3rd gender"], "Hand preference": ["left", "right", "ambidexter"]}
infoDlg = gui.DlgFromDict (dictionary = info, title = "Gabor experiment")
if infoDlg.OK:
    print(info)
else:
    print("User Cancelled")


#Initialze the variables 
nblocks = 3
ntrials = 8
participant = info["Participant number"]

#Initialize Gabor stimulus
Gabor_Left = visual.GratingStim (win, mask = "circle", ori = -30, sf = 2)
Gabor_Right = visual.GratingStim (win, mask = "circle", ori = 30, sf = 20) 

#Correct response
CorResp = numpy.array (["f", "j"])

#Add participant information
Subject = numpy.repeat(info["Participant number"], len(CorResp))
Gender = numpy.repeat("".join(info["Gender"]), len(CorResp))
Age = numpy.repeat(info["Age"], len(CorResp))
Preference = numpy.repeat(''.join(info["Hand preference"], len(CorResp))

# combine arrays in trial matrix
Trials = numpy.column_stack([CorResp, Subject, Gender, Age, Preference])

#Initialize graphical elements
Welcome = visual.TextStim (win, text = "Welcome "  + info["Participant name"] + "!\n\nPress the space bar to continue.")
Instructions = visual.TextStim (win, text = "You will be presented a Gabor stimulus. Your job is to decide whether the stimulus is oriented to the left (press f) or oriented to the right (press j).\n\nPress the space bar to continue.")
Goodbye = visual.TextStim (win, text = "This is the end of the experiment. Thanks you for participating!")


# Initialize a clock to measure the RT
my_clock = core.Clock()

# display the welcome message
Welcome.draw()
win.flip()
### Esther: "space" hoeft niet tot een lijst omgevormd te worden 
event.waitKeys(keyList = ["space"])

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])



# Display the stimuli in two blocks
for b in range(nblocks):
    
    # announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])

    # in 8 trials --> 4 Gabor stimulus left and 4 Gabor stimulus right
    for i in range(b*ntrials,(b+1)*ntrials):
        if ntrials%2 == 0:
            Gabor_Left.draw()
        else:
            Gabor_Right.draw()
        
        #Clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        #Display the stimulus on the screen
        win.flip()
        
        #Now that the stimulus is on the screen, reset the clock
        my_clock.reset()
        
        #Wait for the response
        keys = event.waitKeys(keyList = ["f","j","escape"])
        
        #Register the RT
        RT = my_clock.getTime()
        
        #Escape from the trial loop
        if keys[0] == "escape":
            break
    
    #Escape from the block loop
    if keys[0] == "escape":
        break

#Display goodbye message and close experiment (window) 
Goodbye.draw()
win.flip()
time.sleep(1)
win.clos()