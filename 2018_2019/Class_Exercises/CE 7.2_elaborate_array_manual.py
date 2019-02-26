"""
parity judgement task implementation with ExperimentHandler
Esther De Loof & Tom Verguts, february 2019

"""

# import modules
from psychopy import visual, event, core, gui, data
import numpy as np
import os

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height])

# initializing
colors      = ["red","green"]
RespOptions = ["f", "j"]
text_width  = 0.9
my_clock    = core.Clock()
info        = {"Participant number": 0, "Name": "", "Session": 0}

# make sure the data file has a novel name
already_exists = True
while already_exists:
    
    # present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Parity Judgement Task")
    
    # construct the name of the folder that will hold the data
    directory_to_write_to = my_directory + "/data_ParityJudgementTask"
    
    # if the folder doesn't exist yet, make it
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    # construct the name of the data file
    file_name = directory_to_write_to + "/ParityJudgementTask_subject_" + str(info["Participant number"]) + "_Session_" + str(info["Session"]) + "_data"
    
    # check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        
        # if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        # if the data file name has already been used, ask the participant to inser a different participant number or session number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number or session number")
        myDlg2.show()

print("OK, let's get started!")

# extract the name of the participant from the dialog box information
subject_name = info["Name"]

# remove the name of the participant from the dialog box information (anonimity!)
info.pop("Name")

# start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name!)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# graphical elements
stimulus        = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the parity judgement task!\n"+
                                                "Respond to the number\n"+
                                                "and ignore its color.\n\n"+
                                                "Push the space bar to proceed.").format(subject_name),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "Push left (letter 'f') or\n"+
                                                "Push right (letter 'j') \n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

# randomization step 1: Within-subjects design
Design = [{"Number": 1, "Color": "red"}, {"Number": 2, "Color": "red"}, {"Number": 3, "Color": "red"}, {"Number": 4, "Color": "red"},\
          {"Number": 1, "Color": "green"}, {"Number": 2, "Color": "green"}, {"Number": 3, "Color": "green"}, {"Number": 4, "Color": "green"} ]

# randomization step 2: deduce the correct response (even numbers, press f)
correct = [0,1,0,1,0,1,0,1]

# randomization step 3: create the trials for the entire experiment via the TrialHandler
trials = data.TrialHandler(trialList = Design, nReps = 1, name = "Exp", method = "random")
thisExp.addLoop(trials)

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the trial loop
for trial in trials:
    
    ## display the number on the screen
    stimulus.color = trial["Color"]
    stimulus.text = trial["Number"]
    stimulus.draw()
    win.flip()
    
    ## wait for the response
    event.clearEvents(eventType = "keyboard")
    my_clock.reset()
    keys = event.waitKeys(keyList = RespOptions)
    RT = my_clock.getTime()
    
    ## calculate the derived properties
    CorResp = correct[trial["Number"]-1]
    accuracy = (keys[0] == CorResp) * 1
    
    ## store the information in the ExperimentHandler
    trials.addData("response", keys[0])
    trials.addData("Acc", accuracy)
    trials.addData("RT", RT)
    
    ## let the ExperimentHandler proceed to the next trial
    thisExp.nextEntry()
# end of the trial loop

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()