#test 4 Remy Verdin
#import modules 
from psychopy import visual, event, core, gui, data
import os, platform, math

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing
nBlocks = 12
info        = {"Name": "", "Participant number": str(0), "Age": str(0), "Gender":["male", "female", "third gender"], "Handedness": ["right", "left", "ambidexter"] }
my_clock    = core.Clock()

data_file = "data"
directory_to_write_to = os.getcwd() 
file_name = directory_to_write_to + "Test4_subject_" + str(info["Participant number"])


#design
Design_block = [{"Stimulus": ">", "Position": [-0.5,0], "Congruency": "Incongruent" }, {"Stimulus": ">", "Position": [0,0], "Congruency": "Neutral" }, {"Stimulus": ">", "Position": [0.5,0], "Congruency": "Congruent" },{"Stimulus": "<", "Position": [-0.5,0], "Congruency": "Congruent" },{"Stimulus": "<", "Position": [0,0], "Congruency": "Neutral" },{"Stimulus": "<", "Position": [0.5,0], "Congruency": "Incongruent" }]

# data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Dialog box")
    file_name = directory_to_write_to + "Test4_subject_" + info["Participant number"]
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Please ask the experimenter to help you to enter a unique participant number.")
        myDlg2.show()
print("OK, let's get started!")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# graphical elements
stimulus        = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text = "Welcome to the experiment {0}. Press space to continue.".format(info["Name"]))
blocktext       = visual.TextStim(win, text = "")
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"))

info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

def announce_blockstart():
    if block < 4:
        blocktext.text = ("Welcome to block {0}. You should react to the POSITION of the position of the cues.  \n\n"+
                           "Press 'f' when the cue appears at the left side of the screen. \n"+
                           "Press 'j' when the cue appears at the right side of the screen. \n"+
                           "Press 'y' when the cue appears in the middle of the screen. \n"+
                           "Push the space bar to start.").format(block)
    else:
        blocktext.text = ( "Welcome to block {0}! You should react to the DIRECTION of the cues.\n\n"+
                           "Press 'f' when the cue is '<'. \n"
                           "Press 'j' when the cue is '>'.").format(block)
    blocktext.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
def AccurateResp():
    global acc
    if block < 4:
        if trial["Position"] == [-0.5,0]:
            CorAns = 'f'
        elif trial["Position"] == [0.5,0]:
            CorAns = 'j'
        elif trial["Position"] == [0,0]:
            CorAns = 'y'
    else:
        if trial["Stimulus"] == "<":
            CorAns = 'f'
        else:
            CorAns = 'j'
    return CorAns

def Accuracy():
    if keys[0] == CorAns:
        accuracy = 1
    else:
        accuracy = 0
    return accuracy

block = 1
while block < nBlocks+1:
    announce_blockstart()
    trials = data.TrialHandler(trialList = Design_block, nReps = 10, method = "random")  
    thisExp.addLoop(trials)
    
    acc_block = 0
    
    blocktext.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    for trial in trials:
        
        ## display the stimulus on the screen
        stimulus.text = trial["Stimulus"]
        stimulus.pos = trial["Position"]
        stimulus.draw()
        event.clearEvents(eventType="keyboard")
        
        win.flip()
        
        ## wait for the response
        my_clock.reset()
        keys = event.waitKeys(keyList = ["f","j","y"]) 
        RT = my_clock.getTime()
        CorAns = AccurateResp()
        accuracy = Accuracy()
        trials.addData("blocknr", block)
        trials.addData("trialnr in block", trial)
        trials.addData("response", keys[0])
        trials.addData("RT", RT)
        trials.addData("CorAns", CorAns)
        trials.addData("Accuracy", accuracy)
        thisExp.nextEntry()
    block += 1

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()