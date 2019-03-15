# import modules
from __future__ import division
from psychopy import visual, event, core, gui, data
import numpy
from numpy import random
import os
import platform

# create a dialog box
info = {"Name": "", "Participant number": str(0), "age": 0, "gender":['male','female','third gender'], "dominant hand":['right','left','ambiodextrous']}

# determine the current working directory
my_directory = os.getcwd()

# Data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "test")
    directory_to_write_to = my_directory + "/data_test4"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/test4" +"_subject_" + str(info["Participant number"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
print("OK, let's get started!")
subject_name = info["Name"]
subject_number = info["Participant number"]
subject_age = info["age"]
subject_hand = info["dominant hand"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)
#visualvariables and text
win = visual.Window(size = (1000,700), units = "norm")
text_welcome      = visual.TextStim(win,text="Welcome to the experiment" + subject_name + "\n to continue, press spacebar")
text_instructies         = visual.TextStim(win,text="you will now see a few arrows presented on the screen. Press ")
text_goodbye    = visual.TextStim(win,text="thank you for participating \n\n goodbye")

#make variables
Nblock = 12
Nblocktrials = 60

#all levels of the factor
Arrowdirections = numpy.array(["left","right"])
Arrowplaces = numpy.array(["left", "middle", "right"])
Nplaces = len(Arrowplaces)
Ndirections = len(Arrowdirections)
Nunique = Ndirections * Nplaces
Nuniquetrials = numpy.array(range(Nunique))

#design
directions = numpy.floor(Nuniquetrials/Nplaces)
places = numpy.floor(Nuniquetrials/Ndirections)

#trialmatrix
trialmatrix = numpy.column_stack([directions, places])

#design for one block
Nreps = int(Nblocktrials/Nunique)
blocktrials = numpy.tile(trialmatrix,(Nreps,1))

#trialstructure for the entire experiment
Ntrials = Nblock * Nblocktrials

#emptytrialmatrix
empty = numpy.ones((ntrials

#experiment
for experiment in range(Nblock):
    numpy.random.shuffle(blocktrials)
    
    
    
#congruency
CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean   = numpy.array(Arrowdirections == Arrowplaces)
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]

# deduce the correct response
CorResp[CorResp == "<"]     = "left"
CorResp[CorResp == ">"]    = "right"


#adding the other data to the folder
thisExp.addData["Arrd",Arrowdirections]
thisExp.addData["Arrp",Arrowplaces]
thisExp.addData["congr",Congruence]
thisExp.addData["corrresp",CorResp]
thisExp.addData["blocknumber",ietsinzekerzin]
...