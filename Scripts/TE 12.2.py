# Add info from dialog box to the output

from psychopy import data, visual, event, core, gui
import random

# Dialog box
##dialog box: from demos
info = {"Participant number": 0, "Age": 0, "Handedness": ["left-handed", "right-handed"], "Gender": ["female", "male"]}
infoDlg = gui.DlgFromDict(dictionary = info)
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# Make data file with the experiment handler
data_file = "experimental_data_" + str(info["Participant number"])
thisExp = data.ExperimentHandler(dataFileName = data_file, extraInfo = info)

# Run a few trials (taken from the demos)
conds = data.createFactorialTrialList({"faceExpression": ["happy", "sad"], "presTime": [0.2, 0.3]})
training = data.TrialHandler(trialList = conds, nReps = 3, name = "train", method = "random", seed = 100)
thisExp.addLoop(training)

# run those trials
for trial in training:
    training.addData("training.rt", random.random() * 0.5 + 0.5)
    if random.random() > 0.5:
        training.addData("training.key", "left")
    else:
        training.addData("training.key", "right")
    thisExp.nextEntry()