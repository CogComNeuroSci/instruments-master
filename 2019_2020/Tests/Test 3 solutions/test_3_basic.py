# Test 3, a solution

# import modules
from psychopy import visual, event, core, gui, data
import numpy, os

# file management and participant info

info = {"Participant number":0, "Participant name":"Incognito", "Gender":["male", "female", "third gender"], "Age":0, "Handedness":["right", "left", "ambidextrous"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Flanker Experiment")

# Initialize variables
## number of blocks
nBlocks = 2

## number of trials per block
nBlockTrials = 16

## Total number of trials
nTrials=nBlocks*nBlockTrials

# Initialize experiment structure and data matrix
## counterbalancing Congruency_levels
if info["Participant number"]%2==0:
    Congruency_levels=[3/4, 1/4]
else:
    Congruency_levels=[1/4, 3/4]

## seperately initialize congruent and incongruent stimuli
Congruent_stim=['>>>>>', '<<<<<']
Incongruent_stim=['<<><<', '>><>>']

Ncongruent=len(Congruent_stim)
Nincongruent=len(Incongruent_stim)

## other variables
Responses=['j','f']
allowed_keys=['j','f', 'b', 'e']


Stimulus=numpy.repeat("",nTrials)
Congruency=numpy.repeat("", nTrials)
Resp=numpy.repeat("", nTrials)
CorResp=numpy.repeat("", nTrials)
RT=numpy.repeat(-1, nTrials)
Accuracy=numpy.repeat(-1, nTrials)

## add the participant info
Subject     = numpy.repeat(info["Participant number"],nTrials)
Gender      = numpy.repeat("".join(info["Gender"]),nTrials)
Age         = numpy.repeat(info["Age"],nTrials)
Handedness  = numpy.repeat("".join(info["Handedness"]),nTrials)

## combine arrays in trial matrix
trials      = numpy.column_stack([Subject, Gender, Age, Handedness, Stimulus, Congruency, CorResp, RT, Resp, Accuracy])

# initializing graphical elements

## window
win_width       = 1000
win_height      = 700
win             = visual.Window([win_width,win_height])

## messages and stimuliWelcome         = visual.TextStim(win, text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.")Instructions    = visual.TextStim(win, text = "OK", height = 0.05)Block_start     = visual.TextStim(win, text = "OK")Feedback        = visual.TextStim(win, text = "OK")Goodbye         = visual.TextStim(win, text = "Goodbye!")Stim            = visual.TextStim(win, text="OK",)
fixation        = visual.TextStim(win, text="+")
Instructions.text = (   "In this experiment you will see 5 arrows pointing to left or right.\n" +                        "Indicate as quickly as possible whether the MIDDLE arrow is pointing to the left or the right.\n\n" +                        "Press the f key for the left direction (from top left to bottom right).\n" +                        "Press the j key for the right direction (from top right to bottom left).\n\n" +                        "Press the space bar to start the experiment.")def feedback_message():    ## determine the feedback message
    if trials[i,7]=='nan':
        Feedback.text = "Too late!"    elif int(trials[i,9]) == 1:        Feedback.text = "Correct!"    elif int(trials[i,9])==0:        Feedback.text = "Wrong!"        ## display the message    Feedback.draw()    win.flip()    core.wait(1)

# initialize a clock to measure the RTmy_clock = core.Clock()

# display the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the blocks
for b in range(nBlocks):
    
    # announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    # Complete data structure
    currentTrials = numpy.array(range(nBlockTrials)) + b*nBlockTrials
    
    trials[currentTrials,4]=numpy.concatenate((numpy.repeat(Congruent_stim, ((nBlockTrials/len(Congruent_stim))*Congruency_levels[b])), numpy.repeat(Incongruent_stim, ((nBlockTrials/len(Congruent_stim))*(1-Congruency_levels[b])))))
    trials[currentTrials,6]=numpy.concatenate((numpy.repeat(Responses, ((nBlockTrials/len(Responses))*Congruency_levels[b])), numpy.repeat(Responses, ((nBlockTrials/len(Responses))*(1-Congruency_levels[b])))))
    trials[currentTrials,5]=numpy.concatenate((numpy.repeat(['Congruent'], (nBlockTrials*Congruency_levels[b])), numpy.repeat(['Incongruent'], (nBlockTrials)*(1-Congruency_levels[b]))))
    
    # (Re)-initialize response deadline
    deadline =1
    
    # display the trials in this block
    for i in range(b*nBlockTrials,(b+1)*nBlockTrials):
        
        # display the fixation cross on the screen
        fixation.draw()
        win.flip()
        core.wait(0.5)
        
        # set the stimulus text 
        Stim.text   = trials[i,4]
        
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        # draw the stimulus on the back buffer
        Stim.draw()
        win.flip()
        
        # now that the stimulus is on the screen, reset the clocks
        my_clock.reset()
        
        # wait for the response
        print(deadline)
        keys = event.waitKeys(keyList = allowed_keys, maxWait=deadline)
        print(keys)
        
        #register the RT
        RT = my_clock.getTime()
        
        if keys != None:
            if keys[0]=='b' or keys[0]=='e':
                break
            # store the RT
            trials[i,7] = RT
        
            # store the response information
            trials[i,8] = keys[0]
        
            # determine accuracy
            trials[i,9] = int(trials[i,8] == trials[i,6])
        else:
            trials[i,9]=int(0)
        
        # display the feedback message
        feedback_message()
    
    if keys != None:    
        if keys[0]=='e':
            break
            

# display the goodbye message
Goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

# close the experiment window
win.close()
#print(trials)
