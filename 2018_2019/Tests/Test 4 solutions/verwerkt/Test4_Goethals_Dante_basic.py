##import modules

from psychopy import gui, visual, event, core, data
import numpy as np
import os

## set the directory

my_directory = os.getcwd()

##initialize window

win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height], units = 'norm')

##initializing
info = {"Participant number": str(0), "Name": "", "Age": 0, "Gender" : ["male", "female", "third gender"], "Handedness" : [ "left", "right", "ambidextrous"] }
my_clock = core.Clock()

##data file management

#novel name data file
already_exists = True
while already_exists:
    
    #dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    #data folder 
    directory_to_write_to = my_directory + "/data_Test4"
    
    #make folder if it isn't there
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
        
    #file name
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"])
    
    #name already used?
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        
        # give another number if used
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()
        
#get name pp        
subject_name = info["Name"]

#anonymous 
info.pop("Name")

#store info in handler
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

##graphical elements

stimulus = visual.Textstim(win, text="")
welcome = visual.TextStim(win, text= ( "Welcome {}, \n"+ 
                                      "Respond to the arrow < or > \n"+
                                      "presented either in the left/middle/right \n"+
                                      "of the screen. You will either give the \n"+
                                      "orientation of the arrow ( < or >) or give the location \n"+
                                      "on the screen (l/r/middle). Use the corresponding left arrow \n"+
                                      "downwards arrow (middle) or right arrow on your keyboard.\n"+
                                      "Push the spacebar to proceed.").format(subject_name),
                                      wrapWidth = win_width*text_width)
blockstart = visual.TextStim(win, text"")
instror = visual.TextStim(win, text=("Respond to the orientation.")
instrloc = visual.TextStim(win, text=("Respond to the location.")
goodbye = visual.TextStim(win, text=("It's done. \n\n"+
                                     "Thank you for your participation!")


## randomisatie

Design = [{"Arrow": ">", "Pos": "-0.5"}, {"Arrow": ">", "Pos": "0"}, {"Arrow": ">", "Pos": "0.5"},
         {"Arrow": "<", "Pos": "-0.5"}, {"Arrow": "<", "Pos": "0"}, {"Arrow": "<", "Pos": "0.5"}]

nBlocks = 12
nBlockTrials = 60
nReps = int(nBlocktrials / (3*2))

#welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

for blocki in range(nBlocks):
    
    blockTrials = data.TrialHandler(Design, nReps= nReps, method ="fullRandom")
    thisExp.addLoop(blockTrials)
    
    for trial in blockTrials:
        
        blockTrials.addData("Block", blocki+1)
        
        if (blocki+1) % 3 == 0:
            
            blockTrials.addData("instrloc")
            corAns = trial["Pos"]
            
        else:
            blockTrials.addData("instror")
            corAns = trial["Arrow"]
        corAns = CorAns.replace("-0.5", "left")
        corAns = CorAns.replace("0", "down")
        corAns = CorAns.replace("0.5", "right")
        corAns = CorAns.replace("<", "left")
        corAns = CorAns.replace(">", "right")
        blockTrials.addData("CorAns",CorAns)
        
        thisExp.nextEntry()
        
        # hier zit ik even vast, andere implementatieprobeersel
        
         for trial in blocktrials:
            
            stimulus.pos = trial["Pos"]
            stimulus.text = trial["Arrow"]
            stimulus.draw()
            win.flip()
            
            event.clearEvents(eventType="keyboard")
            my_clock.reset()
            keys = event.waitKeys(keyList = ["left", "down", "right"])
            
            trials.addData("response", keys[0])
            trials.addData("RT", my_clock.getTime())
            
            thisExp.nextEntry()
            
            if (block == 1) :
                block +=1

#say goodbye 

goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()
            




         
         

