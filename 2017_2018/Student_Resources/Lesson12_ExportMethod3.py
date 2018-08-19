"""
Export method 3: .csv files

"""

# import modules
from psychopy import visual, event, core, gui, data
import os

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# Stimuli
colors = ["red","green"]
stimulus = visual.TextStim(win,text="")

# Timing
my_clock = core.Clock()

# Data file
info = {"Participant number": 0, "Name": "Tom", "Session": 0}
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Export Test")
    directory_to_write_to = "/" + info["Name"]
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/ExportTest_subject_" + str(info["Participant number"]) + "_Session_" + str(info["Session"]) + "_data"
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, let's get started!")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# Within-subjects design
Design = data.createFactorialTrialList({"Word": colors, "Color": colors})
trials = data.TrialHandler(trialList = Design, nReps = 1, method = "random")
thisExp.addLoop(trials)

# start of the trial loop
for trial in trials:
    
    ## display the word on the screen
    stimulus.color = trial["Color"]
    stimulus.text = trial["Word"]
    stimulus.draw()
    win.flip()
    
    ## wait for the response
    event.clearEvents(eventType="keyboard")
    my_clock.reset()
    keys = event.waitKeys(keyList = ["f","j"])
    
    trials.addData("response", keys[0])
    trials.addData("RT", my_clock.getTime())
    
    thisExp.nextEntry()
# end of the trial loop

# export the data to Wide text and suppress other output
thisExp.saveAsWideText(file_name+".csv", appendFile = False)
thisExp.abort()