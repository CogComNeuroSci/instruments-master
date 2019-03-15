#Geen idee wat ik aan het doen ben, heb een paar dingen probeert te copy/pasten maar is niet echt goed gelukt (voor de grote test ga ik beter het kunnen)

# import modules
import os
from psychopy import gui
from psychopy import visual, event, core, gui
import time, numpy


# create a dialog box
info = {"Name": "", "Participant number": 0, "Age": 0, "Gender": ['male', 'female', 'third gender'],'handedness':['left', 'right', 'ambidexter']}

# determine the current working directory
directory_to_write = os.getcwd()

# keep asking for a new name when the data file already exists 
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Demo")
    name    = info["Name"]
    number  = info["Participant number"]

    
    # determine the name of the subject directory
    subject_directory  = directory_to_write + "/nr_" + str(number)
    
    # if the directory doesn't exist yet, make it now
    if not os.path.isdir(subject_directory):
        os.mkdir(subject_directory)
    
    # determine the file name
    file_name = subject_directory + "/Test4_Subject_" + str(number) + ".csv"
    print(file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False

# we have found a new file name, ready to start
print("OK, let's get started!")


win = visual.Window(size = (1000, 700), units = "norm") 


#Welcome
HelloText=visual.TextStim(win, text = "Welkom {0}!, press space to get to the instructions".format(info['Name']))
HelloText.draw()
win.flip()
event.waitKeys(keyList=["space"])


#Instructions for PP
InstructiesRichting = visual.TextStim(win, text = "You have to react to the direction of the arrow, use the arrow button to do so. Use the spacebar to start.")
InstructiesPositie = visual.TextStim (win, text = "You have to react to the position of the arrow, use the arrow button to do so. Use the spacebar to start.")
Block_start     = visual.TextStim(win, text = "OK")

# declare all levels of the factor
PijlLinks    = visual.TextStim(win, text = "<")
PijlRechts   = visual.TextStim(win, text =">")

PositionTrials = [ -.5, .5] #geeen idee wat ik hier anders moet doen om de positie te veranderen
PijlTrials = ["<", ">"]
CorResp = ["left", "right"]

Resp = numpy.repeat("",len(CorResp))
Accuracy = numpy.repeat(numpy.nan,len(CorResp))

Subject     = numpy.repeat(info["Participant number"],len(CorResp))
Gender      = numpy.repeat("".join(info["Gender"]),len(CorResp))
Age         = numpy.repeat(info["Age"],len(CorResp))
Handedness  = numpy.repeat("".join(info["handedness"]),len(CorResp))
trials = numpy.column_stack([Subject, Gender, Age, Handedness, PositionTrials, Resp, CorResp, Accuracy])

#gewoon dat iets op het scherm staat...
nblocks= 6
ntrials = 2
for b in range(nblocks):
    
    # announce what block is about to start
    InstructiesRichting.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    # display the trials in this block
    for i in range(b*ntrials,(b+1)*ntrials):
        
        # set the color word and the font color for this trial
        PijlLinks.pos   = int(trials[i,4])
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        # draw the stimulus on the back buffer
        PijlLinks.draw()
        win.flip()
        
        # wait for the response
        keys = event.waitKeys(keyList = ["left","right"])
        
        # store the response information
        trials[i,5] = keys[0]
        
        # determine accuracy
        trials[i,7] = int(trials[i,5] == trials[i,6])
        




# display the goodbye message
Goodbye = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()





# combine arrays in trial matrix
#trials = numpy.column_stack([Resp, CorResp, Accuracy])
# export as a tab separated file
#numpy.savetxt("Test_4.txt", trials, delimiter = "\t", fmt = "%.0d") 