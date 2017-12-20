"""
CE 9.6: a Stroop task implementation
Esther De Loof and Tom Verguts, december 2017

"""

# import modules
from psychopy import visual, event, core, gui
import numpy as np
from numpy import random

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing
n_blocks    = 2
n_prac      = 4
n_trials    = 16
text_width  = 0.9
text_size   = 0.075
fix_time    = 0.5
deadline    = 1
FB_time     = 1
colWords    = ["red","blue","green","yellow"]
respOptions = ["d","f","j","k","e","b"]
FB_options  = ["Wrong answer!","Correct","Too slow! Try to respond faster."]
difficulty  = []
averageRT   = []
averageACC  = []
my_clock    = core.Clock()

info = {    "Participant number":   0,
            "Name":                 "",
            "Gender":               ["female", "male"],
            "Age":                  0,
            "Handedness":           ["left-handed", "right-handed"]}
gui.DlgFromDict(dictionary=info,title="Stroop task")

# probe the difficulty level
myRatingScale = visual.RatingScale(win, low=1, high=9, marker='slider',
    tickMarks=[1,5,9], stretch=1.5, tickHeight=1.5,  # singleClick=True,
    labels=["easy","average","hard"])
myItem = visual.TextStim(win, text="How difficult was this part?", height=.08, units='norm')

# graphical elements
fixation        = visual.TextStim(win,text="+",color="black")
stimulus        = visual.TextStim(win,text="",color="black")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the Stroop task!\n"+
                                                "Push the space bar to proceed.").format(info["Name"]),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
typical         = visual.TextStim(win,text=(    "In this experiment you will see color words (red, blue, green and yellow)\n"+
                                                "presented in a random ink color (red, blue, green and yellow color).\n"+
                                                "You have to respond to the ink color of the stimulus\n"+
                                                "and ignore the meaning of the written word.\n"+
                                                "You can use the following four response buttons\n"+
                                                "(from left to right; use the index and middle finger of your left and right hand):\n"+
                                                "d, f, j and k.\n"+
                                                "If the ink color is red, press the leftmost button d.\n\n"+
                                                "If it's blue, press f.\n"+
                                                "If it's green, press j.\n"+
                                                "If it's yellow, press k.\n\n"+
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n"+
                                                "By all means ignore the meaning of the words,\n"+
                                                "you should only respond to the ink color.\n\n"+
                                                "Push the space bar to start the experiment."),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
atypical        = visual.TextStim(win,text=(    "In this experiment you will see color words (red, blue, green and yellow)\n"+
                                                "presented in a random ink color (red, blue, green and yellow color).\n"+
                                                "You have to respond to the meaning of the color word\n"+
                                                "and ignore the ink color.\n"+
                                                "You can use the following four response buttons\n"+
                                                "(from left to right; use the index and middle finger of your left and right hand):\n"+
                                                "d, f, j and k.\n"+
                                                "If the color word is 'red', press the leftmost button d.\n\n"+
                                                "If it's 'blue', press f.\n"+
                                                "If it's 'green', press j.\n"+
                                                "If it's 'yellow', press k.\n\n"+
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n"+
                                                "By all means ignore the ink color,\n"+
                                                "you should only respond to the meaning of the words.\n\n"+
                                                "Push the space bar to start the experiment."),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
start_prac      = visual.TextStim(win,text=(    "This is the start of the practice phase.\n\n"+
                                                "Push the space bar to proceed."),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
start_exp       = visual.TextStim(win,text=(    "This is the start of the experiment.\n\n"+
                                                "Push the space bar to proceed."),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width, height = text_size, color = "black")
feedbackTrial   = visual.TextStim(win,text="",wrapWidth = win_width*text_width, height = text_size, color = "black")
feedbackBlock   = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "The is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")

# welcome
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
for block in range(n_blocks):

    RT  = []
    ACC = []

    ## instructions
    if info["Participant number"]%2 == 0:
        if block == 0:
            atypical.draw()
        else:
            typical.draw()
    else:
        if block == 0:
            typical.draw()
        else:
            atypical.draw()
    win.flip()
    event.waitKeys(keyList = "space")

    # start of the trial loop
    for trial in range(-n_prac,n_trials):
        
        ## announce the start of the practice phase or the start of the actual experiment
        if trial == -n_prac and block == 0:
            ## announce start of the practice phase
            start_prac.draw()
            win.flip()
            event.waitKeys(keyList = "space")
        elif trial == 0:
            ## announce start of the actual experiment
            start_exp.draw()
            win.flip()
            event.waitKeys(keyList = "space")
        
        ## determine the ink color and color word
        trial_col   = random.randint(0,len(colWords))
        trial_word  = random.randint(0,len(colWords))
        
        ## determine the correct answer
        if info["Participant number"]%2 == 0:
            if block == 0:
                COR = trial_word
            else:
                COR = trial_col
        else:
            if block == 0:
                COR = trial_col
            else:
                COR = trial_word
        
        ## display the fixation cross on the screen
        fixation.draw()
        win.flip()
        core.wait(fix_time)
        
        ## display the square on the screen
        stimulus.text   = colWords[trial_word]
        stimulus.color  = colWords[trial_col]
        stimulus.draw()
        win.flip()
        
        ## wait for the response or response deadline
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        while my_clock.getTime() < deadline:
            keys = event.getKeys(keyList = respOptions)
            if len(keys) != 0:
                break
        
        ## Escape function to get out of the trial loop
        if "e" in keys or "b" in keys:
            break
        
        ## determine the RT and ACC
        if len(keys) != 0:
            RT.append(my_clock.getTime())
            if COR == respOptions.index(keys[0]):
                ACC.append(1)
            else:
                ACC.append(0)
            feedbackTrial.text  = FB_options[ACC[-1]]
        else:
            feedbackTrial.text  = FB_options[2]
        
        ## feedback message
        feedbackTrial.draw()
        win.flip()
        core.wait(FB_time)
        
        # end of the trial loop
        
    ## Escape function to get out of the block loop
    if "e" in keys:
        break
    if "b"in keys:
        continue
    
    ## remove any remaining ratings
    myRatingScale.reset() 

    ## show & update until a response has been made
    while myRatingScale.noResponse:
        myItem.draw()
        myRatingScale.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()

    difficulty.append(myRatingScale.getRating())
    
    ## calculate average RT and ACC
    if len(RT) > 0:
        averageRT.append(np.mean(RT))
    else:
        averageRT.append(0)
    if len(ACC) > 0:
        averageACC.append(np.mean(ACC)*100)
    else:
        averageACC.append(0)
        
    feedbackBlock.text =   ("In this block, your average accuracy was {0:.0f}%.\n"+
                            "Your average RT was {1:.3f} seconds.\n\n"+
                            "Push the space bar to proceed.").format(averageACC[-1],averageRT[-1])
    feedbackBlock.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    # end of the block loop

if info["Participant number"]%2 == 0:
    which_type = ["atypical","typical"]
else:
    which_type = ["typical","atypical"]

most_diff = difficulty.index(max(difficulty))

# give feedback on the difficulty
summary = visual.TextStim(win,text=("You found the {0} block most difficult.\n\n"+
                                    "In the {1} task, your average RT was {2:.3f} seconds\n"+
                                    "and the accuracy was {3:.0f}%\n\n"+
                                    "In the {4} task, your average RT was {5:.3f} seconds\n"+
                                    "and the accuracy was {6:.0f}%\n\n"+
                                    "Push the space bar to proceed.").format(which_type[most_diff],which_type[0],averageRT[0],averageACC[0],which_type[1],averageRT[1],averageACC[1]),
                                   wrapWidth = win_width*text_width, height = text_size, color = "black")
summary.draw()
win.flip()
event.waitKeys(keyList = "space")

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()