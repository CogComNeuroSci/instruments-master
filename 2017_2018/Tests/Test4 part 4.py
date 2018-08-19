"""
Test 4: a lexical decision task implementation
Esther De Loof and Tom Verguts, december 2017

"""

# import modules
from psychopy import visual, event, core, gui, data
import os, platform, math

# set the directory
my_directory = "/Users/esther/Documents/GitHub/instruments-master/2017_2018/Tests"
if platform.system() == "Windows":
    my_directory = "C:" + my_directory
os.chdir(my_directory) 

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height])

# initializing
stimuli     = ["aand", "baag", "cadaac", "dalran", "edwer", "ader", "badjas", "cadeau", "dakpan", "egel"]
my_clock    = core.Clock()
info        = {"Participant number": 0, "Name": ""}
n_blocks    = 2
text_width  = 0.9

# data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Lexical Decision Task")
    file_name = my_directory + "/data_lexical_decision_" + info["Name"]
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This name was already used. Please ask the experimenter to help you to enter a unique name.")
        myDlg2.show()
print("OK, let's get started!")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# graphical elements
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the lexical decision task!\n"+
                                                "You'll have to judge whether a stimulus\n"+
                                                "is a word or a non-word.\n\n"+
                                                "Push the space bar to proceed.").format(info["Name"]),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (letter 'f') for words\n"+
                                                "Push right (letter 'j') for non-words\n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

def announce_blockstart():
    if block == 0:
        blockstart.text = ("Welcome to the practice block!\n\n"+
                           "Push the space bar to start.")
    else:
        blockstart.text = ( "Welcome to part {} of 2!\n\n"+
                            "Push the space bar to start.").format(block)
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")

def randomize():
    Design = data.createFactorialTrialList({"StimulusNumber": range(len(stimuli))})
    Design = [dict(item, Stimulus = stimuli[item["StimulusNumber"]])                            for item in Design]
    Design = [dict(item, Word     = round(item["StimulusNumber"]/5))                            for item in Design]
    Design = [(dict(item, CorAns = "f") if (item["Word"] == 1) else dict(item, CorAns = "j"))  for item in Design]
    
    # create the trials
    if block == 0:
        Design = [Design[i] for i in [0,1,5,6]]
        trials = data.TrialHandler(trialList = Design, nReps = 1, method = "random")
    else:
        trials = data.TrialHandler(trialList = Design, nReps = 1, method = "random")
        thisExp.addLoop(trials)
    
    return trials

def output():
    global acc
    if block > 0:
        trials.addData("response", keys[0])
        trials.addData("RT", my_clock.getTime())
        
        if keys[0] == trial["CorAns"]:
            trials.addData("ACC", 1)
        else:
            trials.addData("ACC", 0)
            
        thisExp.nextEntry()
    else:
        if keys[0] == trial["CorAns"]:
            acc += 1

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
block = 0
while block < (n_blocks + 1):
    
    # announce the block start
    announce_blockstart()
    
    # randomization
    trials = randomize()
    
    # accuracy tracker
    acc = 0
    
    # start of the trial loop
    for trial in trials:
        
        ## display the stimulus
        stimulus.text = trial["Stimulus"]
        stimulus.draw()
        win.flip()
        
        ## wait for the response
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["f","j"])
        
        ## register the output
        output()
        
    # end of the trial loop
    
    # update the block number
    if (block == 0 and acc == 4) or block > 0:
        block += 1
# end of the block loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()