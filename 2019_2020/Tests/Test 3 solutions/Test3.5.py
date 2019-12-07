# importing modules
import time, numpy
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
nblocks             = 2
ntrials             = 16
n1_4                = int(numpy.floor(0.25*ntrials))
n3_4                = int(ntrials - n1_4)
allowedKeys         = ["f","j","b","e"]
congruent_arrows    = ["<<<<<", ">>>>>"]
incongruent_arrows  = [">><>>", "<<><<"]
arrows              = congruent_arrows + incongruent_arrows

# make the trial matrix
### determine the congruence per block
cong_block      = numpy.concatenate([numpy.repeat(0, n3_4), numpy.repeat(1, n1_4)])
incong_block    = numpy.concatenate([numpy.repeat(0, n1_4), numpy.repeat(1, n3_4)])
if info["Participant number"] % 2 == 0:
    congruence  = numpy.concatenate([cong_block, incong_block])
else:
    congruence  = numpy.concatenate([incong_block, cong_block])

### determine the stimuli per block (random)
dir_corResp     = numpy.random.choice([0,1], ntrials * nblocks)

### add the participant info
subject         = numpy.repeat(info["Participant number"], len(dir_corResp))

### make an empty column
empty           = numpy.repeat(-99, len(dir_corResp))

### merge all the information in a trial matrix
trials          = numpy.column_stack([subject, dir_corResp, congruence, empty, empty, empty])
                            
"""
What's in the trial matrix?

0 Subject number
1 TargetDirection/CorResp
2 Congruence
3 RT
4 Resp
5 Accuracy
"""
# initialize a clock to measure the RT
my_clock_RT = core.Clock()

def feedback_message():
    # check whether a response has been given
    if keys is not None:
        
        # determine the accuracy
        ACC = int(keys[0] == allowedKeys[trials[triali,1]])
        
        # determine and display the feedback message
        if ACC == 1:
            Feedback.text = "Correct!"
        else:
            Feedback.text = "Wrong answer!"
        
        # store the trial responses
        trials[triali,3] = RT       
        trials[triali,4] = int(keys[0] == allowedKeys[1])
        
    else:
        
        # determine the accuracy
        ACC = 0
        
        # if no response has been given, encourage the participant to go faster
        Feedback.text = "Too slow!"
    
    # display the feedback message
    Feedback.draw()
    win.flip()
    time.sleep(1)
    
    # store the trial responses
    trials[triali,5] = ACC

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
    
    # reset the response deadline
    deadline = 1
    
    # display the trials in this block
    for triali in range(blocki*ntrials,(blocki+1)*ntrials):
    
        # display the fixation cross
        Fixation.draw()
        win.flip()
        time.sleep(0.5)
        
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard")
    
        # display the target
        Target.text = arrows[trials[triali,1] + trials[triali,2]*2]
        Target.draw()
        win.flip()
                
        # now that the stimulus is on the screen, reset the clocks
        my_clock_RT.reset()
        
        # wait for the response
        keys = event.waitKeys(keyList = allowedKeys, maxWait = deadline)
                
        # register the RT
        RT = my_clock_RT.getTime()
        
        # check whether a response has been given
        if keys is not None:
            
            # escape from the trial loop
            if keys[0] in ["b","e"]:
                break
            
        # display the feedback message
        feedback_message()
        
        # adjust the response deadline
        if trials[triali,5] == 1:
            deadline = deadline - 0.05
        else:
            deadline = deadline + 0.05
        
    # check whether a response has been given
    if keys is not None:
        
        # escape from the block loop
        if keys[0] == "e":
            break
    
    # announce the average accuracy in this block
    average = numpy.mean(trials[blocki*ntrials:(blocki+1)*ntrials,5])
    Block_start.text = "In this block your accuracy was at " + str(int(numpy.round(average*100,0))) + "%."
    Block_start.draw()
    win.flip()
    time.sleep(2)
        
# display the goodbye message
Goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

# close the experiment window
win.close()
print(trials)