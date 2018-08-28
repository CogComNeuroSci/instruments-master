"""
Test 5: a flanker task implementation
Esther De Loof and Tom Verguts, August 2018

"""

# loading modules
from psychopy import visual, event, core, gui, data
import os, random, pandas, math

# test mode (1) versus real experiment (0)
test = 1

# data file
info            = {"Participant number": 0, "Age": 0}
already_exists  = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Flanker Task")
    file_name = os.getcwd() + "/data_flanker_" + str(info["Participant number"])
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
dur_fix         = 0.5
dur_stim        = 3
dur_fb          = 1
text_width      = 0.9
win_width       = 1100
win_height      = 800
n_blocks        = 3
cues_pos        = [-0.5,0.5]
ESC             = "escape"
answers         = ["f","j",ESC]
left_stim       = ["<<<", "<<>", "><<", "><>"]
right_stim      = ["<><", "<>>", ">><", ">>>"]
all_stim        = left_stim + right_stim
ntrialsPerBlock = 24
n_rep           = ntrialsPerBlock/len(all_stim)
my_clock        = core.Clock()

# prepare graphic elements
win             = visual.Window([win_width,win_height], color = "black")

fixation        = visual.TextStim(win, text = "+")
central         = visual.TextStim(win, text = "")
cue_left        = visual.TextStim(win, text = "left",  color = "red")
cue_right       = visual.TextStim(win, text = "right", color = "red")
feedback        = visual.TextStim(win, text = "")

welcome         = visual.TextStim(win, text=(   "Hi {},\n"+
                                                "Welcome to the flanker task!\n"+
                                                "You'll have to judge whether a central arrow\n"+
                                                "is pointing left or right.\n\n"+
                                                "Push the space bar to proceed.").format(infoName["Name"]),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win, text=(   "The response options ''left'' and ''right'' \n"+ 
                                                "will be displayed at different sides of the screen on each trial. \n\n"+
                                                "Push left (letter 'f') when the central stimulus belongs \n to the category presented on the left.\n\n"+
                                                "Push right (letter 'j') when the central stimulus belongs \n to the category presented on the right.\n\n"+
                                                "For example, if the arrow points left, \n and the word ''left'' is on the left, you must push left."+
                                                "Push the space bar to start the experiment."), height = 0.05,
                                    wrapWidth = win_width*text_width)

def disp_feedback(input):
    feedback.text = input
    if input == "Too slow!":
        feedback.color = "pink"
        feedback.height = 0.1
    else:
        feedback.color = "purple"
        feedback.height = 0.15
    feedback.draw()
    win.flip()
    core.wait(dur_fb)

def randomize():
    # create the basic design
    Design = data.createFactorialTrialList({"StimulusNumber": range(len(all_stim))})
    
    # convert to data frame
    dataFrame = pandas.DataFrame.from_dict(Design)
    
    # nrep-licate the number of trials
    Extended = pandas.concat([dataFrame]*int(n_rep), ignore_index = True)
    print(Extended)
    
    # additional information
    odd = bool(info["Participant number"] % 2 == 1)
    ## odd      0: left / right (33%)     1: right / left (66%)
    ## even     1: left / right (33%)     0: right / left (66%)
    Extended["ResponseMapping"] = [1-odd for number in range(len(all_stim)*1)] + [odd for number in range(len(all_stim)*2)]
    
    Extended["LeftPos"]     = [ cues_pos[number] for number in Extended["ResponseMapping"]] # the position of the word Left
    Extended["RightPos"]  =   [-cues_pos[number] for number in Extended["ResponseMapping"]] # the position of the word right
    ## 0 = word, 1 = non-word
    Extended["StimType"]    = Extended["StimulusNumber"] // math.floor(len(all_stim)/2)
    Extended["CorAns"]      = Extended["ResponseMapping"] * 10 + Extended["StimType"]
    Extended["CorAns"].replace([0,1],   answers[0:2],        inplace = True)
    Extended["CorAns"].replace([10,11], answers[0:2][::-1],  inplace = True)
    Extended["Stimulus"]    = [all_stim[number] for number in Extended["StimulusNumber"]]
    
    # extract the trial indices
    index = list(Extended.index)
    
    # loop over the randomization untill the criterion is met
    stopcriterium = 0
    while stopcriterium != 1:
    
        ## suggest a shuffle
        random.shuffle(index)
        Suggestion = Extended.iloc[index]
        
        ## check whether there are two consecutive trials with the same stimulus
        current     = Suggestion.iloc[range(Suggestion.shape[0]-1)].reset_index(drop=True)
        subsequent  = Suggestion.iloc[range(1,Suggestion.shape[0])].reset_index(drop=True)
        
        comparison  = current["StimulusNumber"] == subsequent["StimulusNumber"]
        
        ## adjust the stopcriterium when necessary
        if comparison.sum() == 0:
            stopcriterium = 1
    
    # insert the random trial order
    Random = Extended.iloc[index]
    
    #print(pandas.crosstab([Random.ResponseMapping, Random.StimType], Random.CorAns))
    
    # convert dataframe back to list of dictionaries
    trial_list = pandas.DataFrame.to_dict(Random, orient = "records")
    
    # execute test mode
    if test == 1:
        trial_list = trial_list[0:2]
    
    # implement the trial handler
    trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "sequential")
    thisExp.addLoop(trials)
    
    return trials

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
    trials = randomize()
    
    # start of the trial loop
    for trial in trials:
        
        ## implement properties of this trial
        central.text        = trial["Stimulus"]
        cue_left.pos        = (trial["LeftPos"], 0)
        cue_right.pos       = (trial["RightPos"], 0)
        
        ## display the fixation
        fixation.draw()
        win.flip()
        core.wait(dur_fix)
        
        ## display the stimulus
        cue_left.draw()
        cue_right.draw()
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
            if keys[0] == trial["CorAns"]:
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
        central.text = "Take a break!\n\n\nPush the space bar to proceed."
    else:
        central.text = "This is the end!\n\n\nPush the space bar to exit the experiment."
    central.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
# end of the block loop

#thisExp.saveAsWideText(file_name+".csv", appendFile = False)
#thisExp.abort()
#core.quit()