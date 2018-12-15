# import modules
from psychopy import visual, event, core, gui
import numpy, pylab

# create a dialog box
info = {"Participant number":0, "Participant name":"Incognito", "Gender":["male", "female", "third gender"], "Age":0, "Handedness":["right", "left", "ambidextrous"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Experiment")

# initialize the window
win = visual.Window([600,500], units = "norm")

# cross all the Gabor properties
OrientationTrials       = [330, 30, 330, 30, 330, 30, 330, 30]
SpacialFrequencyTrials  = [2, 2, 20, 20, 2, 2, 20, 20]
CorResp                 = ["f", "j", "f", "j", "f", "j", "f", "j"]

# add a default RT that will be overwritten during the trial loop
RT = numpy.repeat(numpy.nan,len(CorResp))

# add a default response that will be overwritten during the trial loop
Resp = numpy.repeat("",len(CorResp))

# allow to store the accuracy
Accuracy = numpy.repeat(numpy.nan,len(CorResp))

# allow to verify the presentation time
PresentationTimeCheck = numpy.repeat(numpy.nan,len(CorResp))

# add the participant info
Subject     = numpy.repeat(info["Participant number"],len(CorResp))
Gender      = numpy.repeat("".join(info["Gender"]),len(CorResp))
Age         = numpy.repeat(info["Age"],len(CorResp))
Handedness  = numpy.repeat("".join(info["Handedness"]),len(CorResp))

# combine arrays in trial matrix
trials      = numpy.column_stack([Subject, Gender, Age, Handedness, OrientationTrials, SpacialFrequencyTrials, CorResp, RT, Resp, Accuracy, PresentationTimeCheck])

# initialize the variables
nblocks     = 3
ntrials     = trials.shape[0]

# repeat the trial matrix for the blocks
trials      = numpy.tile(trials, (nblocks, 1))

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.")
Instructions    = visual.TextStim(win, text = "OK", height = 0.05)
Block_start     = visual.TextStim(win, text = "OK")
Feedback        = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!")
GaborMask       = visual.GratingStim(win, mask = "circle", ori = 0, sf = 10)
Gabor           = visual.GratingStim(win, mask = "circle")

Instructions.text = (   "In this experiment you will see Gabor patches with vertical stripes.\n" +
                        "Briefly, this orientation will change to one with a slight right of left tilt.\n" +
                        "Indicate as quickly as possible whether the tilt is oriented to the left or the right.\n\n" +
                        "Press the f key for the left tilt (from top left to bottom right).\n" +
                        "Press the j key for the right tilt (from top right to bottom left).\n\n" +
                        "Press the space bar to start the experiment.")

def feedback_message():
    
    ## determine the feedback message
    if int(trials[i,9]) == 1:
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Wrong answer!"
    
    ## display the message
    Feedback.draw()
    win.flip()
    core.wait(1)

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
for b in range(nblocks):
    
    # announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    # display the trials in this block
    for i in range(b*ntrials,(b+1)*ntrials):
        
        # set the color word and the font color for this trial
        Gabor.ori   = int(trials[i,4])
        Gabor.sf    = int(trials[i,5])
        
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
        trials[i,10] = my_clock_check.getTime()
        
        # wait for the response
        keys = event.waitKeys(keyList = ["f","j","escape"])
        
        # register the RT
        RT = my_clock_RT.getTime()
        
        # escape from the trial loop
        if keys[0] == "escape":
            break
        
        # store the RT
        trials[i,7] = RT
        
        # store the response information
        trials[i,8] = keys[0]
        
        # determine accuracy
        trials[i,9] = int(trials[i,8] == trials[i,6])
        
        # display the feedback message
        feedback_message()
    
    # escape from the block loop
    if keys[0] == "escape":
        break

# display the goodbye message
Goodbye.draw()
win.flip()
core.wait(1)

# close the experiment window
win.close()
print(trials)
