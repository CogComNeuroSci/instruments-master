##import modules
import numpy
import os
from psychopy import visual, event, core, gui, data

# create a dialog box
info = {"Name": "", "participant number": 0, "Age": 0, "Gender":["male", "female"], "handvoorkeur":["left", "right", "ambidexter"]}

# determine the current working directory
directory_to_write = os.getcwd()

# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Test 4")
    name    = info["Name"]
    number  = info["participant number"]
    
    # determine the directory
    directory  = directory_to_write + "/data"
    
    # if the directory doesn't exist yet, make it now
    if not os.path.isdir(directory):
        os.mkdir(directory)
    
    # determine the file name
    file_name = directory + "Test4_subject_"+ str(number) +".txt"
    print(file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Laat de proefleider je een ander participant number geven")
        myDlg2.show()

# we have found a new file name, ready to start
print("OK, let's get started!")

#verwijder naam uit info en voeg info toe aan output file
subject_name = info["Name"]
info.pop("Name")
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


# initialize the window
win_width = 1000
win_height = 700
win = visual.Window(size=[win_width, win_height], units="pix")

text_width  = 0.9

#initialize clock
rtclock= core.Clock()

# graphical elements
stimulus        = visual.TextStim(win,text="", pos=(0,0), units="norm")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the experiment!\n"+
                                                "You'll have to judge whether a stimulus\n"+
                                                "is an arrow to the left or to the right, or the position is left or right. This will be told before the block starts.\n\n"+
                                                "Push the space bar to proceed.").format(subject_name),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text="")
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)
                                    
                                    
#constants
nBlocks= 12
nReps= 10
nBlockTrials= 60
ntrials= nBlocks * nBlockTrials


#arrays met variabelen, voor xcoord normsysteem
pijloptions=numpy.array(["<", ">"])
coordoptions=numpy.array([(-0.5,0), (0,0), (0.5,0)])

Npijl=len(pijloptions)
Ncoord= len(coordoptions)
Nunique= Npijl * Ncoord 

UniqueTrials=numpy.array(range(Nunique))

#make factorial design 
Pijl= numpy.floor(UniqueTrials/Ncoord)
Coord= numpy.floor(UniqueTrials/1)% Npijl

#combine arrays in trial matrix
trials=numpy.column_stack([Pijl, Coord])
print(trials)

#repeat conditions 10 times
blockTrials= numpy.tile(trials, (nReps,1))
print(blockTrials)


## make empty trial matrix
trials = numpy.ones((ntrials,12)) * numpy.nan

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# fill in the random trial order per block

## loop over the 12 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ##bepaal instructies (ik vond niet hoe de pijltjestoetsen te doen, dus nam ik tijdelijk f en j)
    if (blocki)%3 == 0:
        instruct.text= "Reageer op de positie van het pijltje dmv de pijltjestoetsen, f is links, j is rechts. Druk spatie om verder te gaan"
    else:
        instruct.text= "Reageer op de richting van het pijltje dmv de pijltjestoetsen, f is links, j is rechts. Druk spatie om verder te gaan"
    instruct.draw()
    win.flip()
    event.waitKeys("space")
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)
    
#    loop over de geshuffelde trials voor dat block
    for trial in blockTrials:
        
        ##present the stimulus with its position
        stimulus.text= blockTrials[trial, 0]
        stimulus.pos = blockTrials[trial, 1]
        stimulus.draw()
        event.clearEvents(eventType= "Keyboard")
        win.flip()
        rtclock.reset()
        resp= event.waitKeys("f", "j")
        RT= clock.getTime()
        
#        ##store rt
#        trials[currentTrials, 9]=
    ## store thesubject nr
    trials[currentTrials, 0] = int(number)
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 1:3] = blockTrials
    
    ##store congruence 0 is neutraal, 1 is congrugent, 2 is incongurent
    if trials[currentTrials,1]== "<" and trials[currentTrials,2]== (-0.5, 0):
        trials[currentTrials,3]= 1
    elif trials[currentTrials,1]== ">" and trials[currentTrials, 2] == (0.5, 0):
        trials[currentTrials,3] = 1
    elif trials[currentTrials, 2] == (0,0):
        trials[currentTrials, 3] = 0
    else:
        trials[currentTrials, 3] = 2
    
    ##store correct response
    if blocki%3==0:  #reageer op positie, kolom 2
        if trials[currentTrials,2] == (-0.5,0):
            trials[currentTrials, 4] = "f"
        else: 
            trials[currentTrials, 4] = "j"
    else:
        if trials[currentTrials,1] == "<":
            trials[currentTrials, 4] = "f"
        else: 
            trials[currentTrials, 4] = "j"
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 5] = blocki+1
    
#    ## store the trailnr binnen het blok
#    trials[currentTrials, 5] = 
#    
    ## store the trailnr binnenn experiment
    trials[currentTrials, 6] = currentTrials     ## correct answer determined by font color

# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

print(trials)
core.quit()
win.close()