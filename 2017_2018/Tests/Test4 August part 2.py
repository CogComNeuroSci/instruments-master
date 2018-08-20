"""
Test 4: a flanker task implementation
Esther De Loof and Tom Verguts, August 2018
The mapping is made variable here; even subject numbers receive the reversed mapping
(not recommended in real experiments...)
"""

# import modules
from psychopy import visual, event, core, gui, data
import os, platform, math

# set the directory
#my_directory = "/Users/tom/Documents/EP_IEP/instruments-master/Scripts"
my_directory = "/Users/esther/Documents/GitHub/instruments-master/2017_2018/Tests"
if platform.system() == "Windows":
    my_directory = "C:" + my_directory
os.chdir(my_directory) 

# initialize the window
win_width   = 1000
win_height  = 700
win         = visual.Window([win_width, win_height])

# initializing
stimuli     = ["<<<", "<<>", "><<", "><>", "<><", "<>>", ">><", ">>>"]
my_clock    = core.Clock()
info        = {"Participant number": 0, "Name": ""}
n_blocks    = 3
text_width  = 0.9

# data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Flanker Task")
    file_name = my_directory + "/data_flanker_task_" + info["Name"]
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This name was already used. Please ask the experimenter to help you to enter a unique name.")
        myDlg2.show()
print("OK, let's get started!")
mapping = info["Participant number"] % 2
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# graphical elements
text_info = ["left (letter 'f')", "right (letter 'j')"]
if mapping == 1:
    text_info = list(reversed(text_info))
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the flanker task!\n"+
                                                "You'll have to judge whether a central arrow\n"+
                                                "points left or right.\n\n"+
                                                "Push the space bar to proceed.").format(info["Name"]),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push {} for a left arrow\n"+
                                                "Push {} for a right arrow\n\n"+
                                                "Push the space bar to start the experiment.").format(text_info[0], text_info[1]),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

def announce_blockstart():
    if fail:
        blockstart.text = ("You must do this block again...\n\n"+
                            "Push the space bar to start")
    else:
        blockstart.text = ( "Welcome to part {} of {}!\n\n"+
                            "Push the space bar to start.").format(block + 1, n_blocks)
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")

def randomize():
    Design = data.createFactorialTrialList({"StimulusNumber": range(len(stimuli))})
    Design = [ dict(item, Stimulus  = stimuli[     item["StimulusNumber"]])                                        for item in Design]
    Design = [ dict(item, Response  = math.floor(  item["StimulusNumber"]/(len(stimuli)/2)))                      for item in Design]
    Design = [(dict(item, CorAns    = "f") if (    item["Response"] == mapping) else dict(item, CorAns = "j"))   for item in Design]
    print(Design)
    # create the trials
    trials = data.TrialHandler(trialList = Design, nReps = 1, method = "random")
    thisExp.addLoop(trials)
    
    return trials

def output():
    global acc
    trials.addData("response", keys[0])
    trials.addData("RT", my_clock.getTime())
    if keys[0] == trial["CorAns"]:
        trials.addData("ACC", 1)
        acc += 1
    else:
        trials.addData("ACC", 0)
    thisExp.nextEntry()

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
block = 0
fail = False
while block < n_blocks:
    
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
    fail = bool((acc < len(stimuli))*(block == n_blocks - 1))
    if (block == n_blocks - 1 and acc == len(stimuli)) or block < n_blocks - 1:
        block += 1
# end of the block loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

thisExp.saveAsWideText(file_name+".csv", appendFile = False)
thisExp.abort()
core.quit()