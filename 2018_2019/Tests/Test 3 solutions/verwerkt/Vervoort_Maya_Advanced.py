#Test 3 for the course IEP - Advanced part
#Date: 12 December 2018
#Author: Maya Vervoort

#Import modules
from psychopy import visual, gui, event, core
import time, numpy

#Initialize window
##Asked size: 600 wide, 500 high
##Units asked: normalized
win = visual.Window(size = (600,500), units = "norm")

#Creating dialogue box
info = {"Name": "Unknown", "Participant number": 0, "Age": 0, "Gender": ["male", "female", "other"], "Handedness": ["Right", "Left", "Ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary = info, title = "Experiment")
if infoDlg.OK:
    print(info)
else:
    print("User Cancelled")

#Initialize graphic elements
welcome = visual.TextStim(win, text = "Welcome, " +info["Name"])
Instr = visual.TextStim(win, text = "OK")
Cont = visual.TextStim(win, text = "OK", pos = (0,-0.75))
StartBlock = visual.TextStim(win, text = "Blabla")
End = visual.TextStim(win, text = "That's it! Thank you for participating! Press space to end the experiment.")
StartGabor = visual.GratingStim(win, tex="sin", mask="gauss", sf = 4)
StimGabor = visual.GratingStim(win, tex = "sin", mask = "gauss", ori = 20, sf = 4) 
Feedback = visual.TextStim(win, text = "Blabla")

#Important variables
time_stim = [0.016, 0.033, 0.050]
nblocks = 3
ntrials = 8

#Orientations
orientation = [30, 30, 30, 30, -30, -30, -30, -30]
spatF = [2, 20, 2, 20, 2, 20, 2, 20]

#Extracting PPs info out of dialogue box
PPnr = numpy.repeat(info["Participant number"], len(orientation))
PPAge = numpy.repeat(info["Age"], len(orientation))
PPGender = numpy.repeat("".join(info["Gender"]), len(orientation))
PPHand = numpy.repeat("".join(info["Handedness"]), len(orientation))

#Let Accuracy be stored
Accuracy = numpy.repeat(99, len(orientation))

#Deduce Correct Response
CorResp = numpy.copy(orientation)

#Store responses
Resp = numpy.repeat(99.9, len(orientation))

#Store RTs
RT = numpy.repeat("f", len(orientation))

#Store planned presentation time
PlanPres= numpy.repeat("f", len(orientation))

#Store actual presentation time
ActPres = numpy.repeat("f", len(orientation))

#Combine arrays into matrix
trials = numpy.column_stack([PPnr, PPAge, PPGender, PPHand, orientation, spatF, CorResp, Resp, RT, Accuracy, PlanPres, ActPres])

#Repeat this for 3 blocks
trials = numpy.tile(trials, (nblocks, 1))

#Initialize clock for RTs
MyClock = core.Clock()

#Initialize clock for Stimulus timing
ClockStim = core.Clock()

#Write info + instructions
Cont.text = ("Press space to continue")
Instr.text = ("You will see Gabor figures in this experiment.\n" + 
        "You need to respond to the orientation of this figure.\n"+
        "When the figure is turned to the left \n" +
        "(meaning the lines go from top left to bottom right) press 'f'. \n"+
        "When the figure is turned to the right \n"+
        "(meaning the lines go from top right to bottom left) press 'j'. \n"+
        "When you're ready to start, press the spacebar to begin the experiment.")

#Build definition for feedback
def feedback_message():
    if int(trials[i,9]) == 1:
        Fb = visual.TextStim(win, text = "Correct")
        Fb.draw()
        win.flip()
        time.sleep(1)
    else:
        Fb = visual.TextStim(win, text = "Verkeerd antwoord")
        Fb.draw()
        win.flip()
        time.sleep(1)

#Display Welcome message
welcome.draw()
Cont.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#Display instructions
Instr.draw()
win.flip()
event.waitKeys(keyList=["space"])

#Start experiment
for b in range(nblocks):
    #Announce the start of the block
    StartBlock.text = ("Start of block " + str(b+1) + " press space to begin.")
    StartBlock.draw()
    win.flip()
    StartKeys = event.waitKeys(keyList = ["space", "escape"])
    
    #To escape from the block
    if StartKeys[0] == "escape":
        break
    
    #In 8 trials
    for i in range(b*ntrials, (b+1)*ntrials):
        StartGabor.draw()
        win.flip()
        time.sleep(1)
        
        #Define properties of the Gabor Stimulus
        StimGabor.ori = int(trials[i,4])
        StimGabor.sf = int(trials[i,5])
        StimGabor.draw()
        
        #Define correct responses
        if StimGabor.ori == 30:
            trials[i, 6] = "j"
        else:
            trials[i,6] = "f"
        
        #Clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        #Clear clock for Stimulus check
        ClockStim.reset()
        
        #Display on the screen
        win.flip()
        #Time the actual stimulus should be presented
        if b == 1:
            core.wait(0.016)
            trials[i,10] = 0.016
        elif b == 2:
            core.wait(0.033)
            trials[i,10] = 0.033
        elif b == 3:
            core.wait(0.50)
            trials[i,10] = 0.050
        #Check if the Gabor Stimulus is actually presented the correct amount of time
        print(ClockStim.getTime())
        trials[i,11] = ClockStim.getTime()
        
        #Reset the clock for registering RTs now that the stimulus is presented
        MyClock.reset()
        
        #End stimulus as distractor, has to wait until a response is given
        StartGabor.draw()
        win.flip()
        keys = event.waitKeys(keyList = ["j", "f", "escape"])
        
        #Calculate RT
        RT = MyClock.getTime()
        
        #To escape from the trial loop
        if keys[0] == "escape":
            break
        
        #Store responses
        trials[i,7] = keys[0]
        
        #Determine Accuracy
        trials[i, 9] = int(trials[i,6] == trials[i,7])
        
        #Store RT
        trials[i, 8] = RT
        
        #Determine feedback
        feedback_message()


#End of experiment, say goodbye
End.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#To check
print(trials)

#Close window
win.close()
