"""
Test 3: a Simon task implementation
Esther De Loof and Tom Verguts, december 2017

"""

# import modules
from __future__ import division
from psychopy import visual, event, core, gui
import numpy as np
from numpy import random

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window(size=[win_width,win_height])

# initializing
n_blocks    = 2
n_trials    = 10
stim_size   = 0.2
position    = [-0.8,0.8]
fix_time    = 0.5
deadlineplus= 0.1
FB_time     = 1
text_width  = 0.9
my_clock    = core.Clock()
FB_options  = ["Fout!","Goed!","Te traag!"]

def check_input_device():
    info = {"Participant number":0,"Name":""}
    gui.DlgFromDict(dictionary=info,title="Simon task")
    return info

participant_info = check_input_device()

if participant_info["Participant number"]%2 == 0:
    colors = ["red","yellow","green","blue"]
else:
    colors = ["green","blue","red","yellow"]

# graphical elements
stimulus        = visual.Rect(win,width=stim_size,height=stim_size)
fixation        = visual.TextStim(win,text="+")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the Simon task!\n"+
                                                "Respond to the color of the square\n"+
                                                "and ignore its location.\n\n"+
                                                "Push the space bar to proceed.").format(participant_info["Name"]),
                                   wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (letter 'f' on the keyboard)\n"+
                                                "when the square is {0} or {1}.\n\n"+
                                                "Push right (letter 'j' on the keyboard)\n"+
                                                "when the square is {2} or {3}.\n\n"+
                                                "Push the space bar to start the experiment.").format(colors[0],colors[1],colors[2],colors[3]),
                                   wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "The is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                   wrapWidth = win_width*text_width)
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
feedbackTrial   = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
feedbackBlock   = visual.TextStim(win,text="",wrapWidth = win_width*text_width)

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
for block in range(n_blocks):
    
    block_OK        = 0
    retake_counter  = 0
    
    # start of the block retake loop
    while block_OK == 0 and retake_counter < 5:
        
        ## initialize the RT, ACC and CONG for the current block
        RTcong      = []
        RTincong    = []
        ACC         = []
        CONG        = []
        
        blockstart.text = ( "Welcome to part {} of 2!\n\n"+
                            "Push the space bar to start.").format(block+1)
        blockstart.draw()
        win.flip()
        event.waitKeys(keyList = "space")
        
        # start of the trial loop
        for trial in range(n_trials):
            
            ## on the first trial, reset the deadline
            if trial == 0:
                deadline_cong   = 1.5
                deadline_incong = 1.5
            
            ## determine the color of the left and right square
            trial_col = random.randint(0,len(colors))
            trial_pos = random.randint(0,len(position))
            
            ## will we use the deadline for a congruent or incongruent trial?
            if trial_col == trial_pos:
                deadline = deadline_cong
            else:
                deadline = deadline_incong
            print(deadline)
            
            ## display the fixation cross on the screen
            fixation.draw()
            win.flip()
            core.wait(fix_time)
            
            ## display the square on the screen
            stimulus.pos = [position[trial_pos],0]
            stimulus.lineColor = colors[trial_col]
            stimulus.fillColor = colors[trial_col]
            stimulus.draw()
            win.flip()
            
            ## wait for the response or response deadline
            event.clearEvents(eventType="keyboard")
            my_clock.reset()
            while my_clock.getTime() < deadline:
                keys = event.getKeys(keyList = ["f","j","t","b"])
                if len(keys) != 0:
                    break
            
            ## Escape function to get out of the trial loop
            if "t" in keys or "b" in keys:
                break
            
            ## determine the RT and ACC
            if len(keys) != 0:
                CONG.append(int(trial_col == trial_pos))
                if CONG[-1] == 1:
                    RTcong.append(my_clock.getTime())
                    deadline_cong   = np.mean(RTcong) + deadlineplus
                else:
                    RTincong.append(my_clock.getTime())
                    deadline_incong = np.mean(RTincong) + deadlineplus
                if keys[0] == "f" and (trial_col == 0 or trial_col == 1):
                    ACC.append(1)
                elif keys[0] == "j" and (trial_col == 2 or trial_col == 3):
                    ACC.append(1)
                else:
                    ACC.append(0)
                feedbackTrial.text  = FB_options[ACC[-1]]
            else:
                feedbackTrial.text  = FB_options[2]
            
            ## display the feedback text
            feedbackTrial.draw()
            win.flip()
            core.wait(FB_time)
            
            # end of the trial loop
    
        ## Escape function to get out of the block loop
        if "b" in keys:
            break
        if "t"in keys:
            continue
        
        ## calculate average RT and ACC
        RT = RTcong + RTincong
        if len(RT) > 0:
            averageRT = np.mean(RT)
        else:
            averageRT = 0
        if len(ACC) > 0:
            averageACC  = np.sum(ACC)/n_trials*100
        else:
            averageACC = 0
        
        ## provide feedback for the current block
        if averageACC < 80:
            retake_counter = 1
            if retake_counter < 5:
                feedbackBlock.text =   ("In this block, your average accuracy was {0:.0f}%.\n"+
                                        "This is too low, so we'll retake this block.\n\n"+
                                        "Push the space bar to proceed.").format(averageACC)
            else:
                feedbackBlock.text =   ("In this block, your average accuracy was {0:.0f}%.\n"+
                                        "This is still too low, but we won't retake the block again.\n\n"+
                                        "Push the space bar to proceed.").format(averageACC)
        else:
            block_OK = 1
            feedbackBlock.text =   ("In this block, your average accuracy was {0:.0f}%.\n"+
                                    "Your average RT was {1:.3f} seconds.\n\n"+
                                    "Push the space bar to proceed.").format(averageACC,averageRT)
        feedbackBlock.draw()
        win.flip()
        event.waitKeys(keyList = "space")
    
        # end of the block loop
        
    # end of the block retake block
    
## say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()