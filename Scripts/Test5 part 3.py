"""
Test 5: a lexical decision task implementation
Esther De Loof and Tom Verguts, march 2018

"""

# loading modules
from psychopy import visual, event, core, gui, data
import os, platform, math, random

# test mode (1) versus real experiment (0)
test = 1

# data file
info            = {"Participant number": 0, "Age": 0}
already_exists  = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Lexical Decision Task")
    file_name = os.getcwd() + "/data_lexical_decision_" + str(info["Participant number"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This number was already used. Please ask the experimenter to help you to enter a unique number.")
        myDlg2.show()
print("OK, let's get started!")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# participant name
infoName        = {"Name": ""}
myDlgName       = gui.DlgFromDict(dictionary = infoName, title = "Please enter your name")

# initialization
dur_fix     = 0.5
dur_stim    = 2.5
dur_fb      = 1
text_width  = 0.9
win_width   = 1000
win_height  = 700
n_blocks    = 3
cues_pos    = [-0.5,0.5]
ESC         = "escape"
answers     = ["f","j",ESC]
words       = ["bloem", "kast", "schoen"]
nonwords    = ["bielo", "kang", "troen"]
allwords    = words + nonwords
n_rep       = 24/len(allwords)
my_clock    = core.Clock()

# prepare graphic elements
win = visual.Window([win_width,win_height], color = "black")

fixation        = visual.TextStim(win, text = "+")
central         = visual.TextStim(win, text = "")
cue_woord       = visual.TextStim(win, text = "word",       color = "red")
cue_nonwoord    = visual.TextStim(win, text = "non-word",   color = "red")
feedback        = visual.TextStim(win, text = "",           color = "pink")

welcome         = visual.TextStim(win, text=(   "Hi {},\n"+
                                                "Welcome to the lexical decision task!\n"+
                                                "You'll have to judge whether a stimulus\n"+
                                                "is a Dutch word or a non-word.\n\n"+
                                                "Push the space bar to proceed.").format(infoName["Name"]),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win, text=(   "The response options word (Dutch) and nonword \n"+ 
                                                "will be displayed at different sides of the screen on each trial. \n\n"+
                                                "Push left (letter 'f') when the central stimulus belongs \n to the category presented on the left.\n\n"+
                                                "Push right (letter 'j') when the central stimulus belongs \n to the category presented on the right.\n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)

def disp_feedback(input):
    feedback.text = input
    feedback.draw()
    win.flip()
    core.wait(dur_fb)

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
for block in range(n_blocks):
    
    # randomization
    Design = data.createFactorialTrialList({"StimulusNumber": range(len(allwords))})
    
    # execute test mode
    if test == 1:
        random.shuffle(Design)
        trials = data.TrialHandler(trialList = Design[0:2], nReps = 1, method = "sequential")
    else:
        trials = data.TrialHandler(trialList = Design, nReps = n_rep, method = "fullRandom")
    
    thisExp.addLoop(trials)
    
    # start of the trial loop
    for trial in trials:
        
        ## determine properties of this trial
        random.shuffle(cues_pos)
        central.text        = allwords[trial["StimulusNumber"]]
        cue_woord.pos       = (cues_pos[0], 0)
        cue_nonwoord.pos    = (cues_pos[1], 0)
        if cues_pos[0] < 0 and trial["StimulusNumber"] < len(words):    # word cue to the left  and word target
            CorAns = answers[0]
        if cues_pos[0] < 0 and trial["StimulusNumber"] >= len(words):   # word cue to the left  and nonword target
            CorAns = answers[1]
        if cues_pos[0] > 0 and trial["StimulusNumber"] < len(words):    # word cue to the right and word target
            CorAns = answers[1]
        if cues_pos[0] > 0 and trial["StimulusNumber"] >= len(words):   # word cue to the right and nonword target
            CorAns = answers[0]
        trials.addData("CorAns", CorAns)
        trials.addData("Stimulus", allwords[trial["StimulusNumber"]])
        
        ## display the fixation
        fixation.draw()
        win.flip()
        core.wait(dur_fix)
        
        ## display the stimulus
        cue_woord.draw()
        cue_nonwoord.draw()
        central.draw()
        win.flip()
        
        ## wait for the response
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = answers, maxWait = dur_stim)
        
        ## register the output
        if keys is not None:
            ## implement the escape function
            if keys[0] == ESC:
                break
            trials.addData("RT", my_clock.getTime())
            trials.addData("response", keys[0])
            if keys[0] == CorAns:
                trials.addData("ACC", 1)
            else:
                trials.addData("ACC", 0)
                disp_feedback("Error!")
        else:
            trials.addData("RT", "NA")
            trials.addData("response", "NA")
            trials.addData("ACC", "NA")
            disp_feedback("Too slow!")
        
        thisExp.nextEntry()
    # end of the trial loop
    
    # further execute the escape function
    if keys is not None:
        if keys[0] == ESC:
            break
    
    # end of block message
    if block < (n_blocks-1):
        central.text = "Pauze\n\n\nPush the space bar to proceed."
    else:
        central.text = "This is the end!\n\n\nPush the space bar to exit the experiment."
    central.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
# end of the block loop

core.quit()