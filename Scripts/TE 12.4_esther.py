# some operating system (os) manipulations
# 
import os
from psychopy import gui, data
import random

directory_to_write_to = "c:/Users/esther/Documents/Research/IEP/"

myDlg = gui.Dlg(title = "get subject info")
myDlg.addField("number?")

already_exists = True
while already_exists:
    myDlg.show()
    number = myDlg.data[0]
    filename = directory_to_write_to + "experimental_data_" + number
    if not os.path.isfile(filename + ".csv"):
        already_exists = False
print("OK let's get started!")

# Make data file with the experiment handler
thisExp = data.ExperimentHandler(dataFileName = filename)

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