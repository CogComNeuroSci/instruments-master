# Test 3 IEP 12/12/18 Ineke Joos

# import modules
from psychopy import visual, event, core, gui
import time, numpy, random

# create a dialog box
info = {"Participantnummer":0, "Participant naam":"Unknown", "Gender":["man", "vrouw", "derde gender"], "leeftijd":0, "handvoorkeur": ["links", "rechts", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Stroop Experiment")


if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")
    
PartName = info["Participant naam"]

# initialize the window
win = visual.Window([600, 500], units = "norm")

# initialize variables
nblocks = 3
ntrials = 8
duration = 1

DurationList = [16/1000, 33/1000, 50/1000] # this is the planned presentation time 


# determine frequency
## screen: 60 Hz= 60 cycles/sec, needed: 2 Hz or 20 Hz. 
## units set to pix in gratingstim, stim is 150 pix. 
## 2 cycles: 2/150, 20 cycles: 20/150

FrequencyList = [2/150, 20/150, 2/150, 20/150, 2/150, 20/150, 2/150, 20/150]
FrequencyListMask = [20/150, 20/150, 2/150, 20/150, 2/150, 2/150, 2/150, 20/150]


OrientationList = [45, 45, 315, 45, 45, 315, 315, 315]
Keylist = ["j", "f"]


# initialize graphical elements
MaskStim = visual.GratingStim(win, tex="sin", size= 150, sf= None, ori = 0, name='gabor1', units = "pix")
TargetStim = visual.GratingStim(win, tex="sin", size= 150, sf= None , ori = 0, name='gabor2', units = "pix")
Correct = visual.TextStim(win, text = "Correct!")
Wrong = visual.TextStim(win, text = "Verkeerd antwoord!")
Goodbye = visual.TextStim(win, text= "Het experiment is afgelopen. Druk op spatie om af te sluiten.")

# initialize welcome message
Welcome = visual.TextStim(win, text = "Welcome {0}! Druk op spatie om verder te gaan.".format(PartName))
Welcome.draw()
win.flip()
event.waitKeys(keyList = ["space"])


# initialize instructions
Instr = visual.TextStim(win, text = "Tijdens dit experiment zal je enkele stimuli te zien krijgen. Druk op de f toets wanneer deze naar links is gedraaid (de lijnen lopen van linksboven naar rechtsonder) en de j toets wanneer deze naar rechts is gedraaid (de lijnen lopen van rechtsboven naar linksonder.\n\n Druk op spatie om aan het experiment te beginnen")
Instr.draw()
win.flip()
event.waitKeys(keyList = ["space"])


# initialize function for correct response
def correct_response():
    CR = "OK"
    if TargetStim.ori == 45:
        CR = Keylist[0]
    elif TargetStim.ori == 315:
        CR = Keylist[1]
        
    CorResp.append(CR)
        
    return CorResp



# initialize function for feedback
def feedback_message():
    if accuracy == 1:
        Correct.draw()
        win.flip()
        core.wait(1)
    else:
        Wrong.draw()
        win.flip()
        core.wait(1)




# allow to store the correct response
CorResp = numpy.repeat(-99.9,len(FrequencyList))

# allow to store the accuracy
Accuracy = numpy.repeat(-99.9,len(FrequencyList))

# add a default response that will be overwritten during the trial loop
Resp = numpy.repeat(-99.9,len(FrequencyList))

# add a default RT that will be overwritten during the trial loop
RT = numpy.repeat(-99.9,len(FrequencyList))

# add actual presentation time
ActualTime = numpy.repeat(-99.9,len(FrequencyList))

# add planned presentation time
PlannedTime = numpy.repeat(-99.9, len(FrequencyList))


# add the participant info
Subject = numpy.repeat(info["Participantnummer"],len(FrequencyList))
Gender  = numpy.repeat("".join(info["Gender"]),len(FrequencyList))
Age     = numpy.repeat(info["leeftijd"],len(FrequencyList))
Handpreference     = numpy.repeat(info["handvoorkeur"],len(FrequencyList))


# combine arrays in trial matrix
trials = numpy.column_stack([FrequencyList, OrientationList, CorResp, Resp, Accuracy, RT, Subject, Gender, Age, Handpreference, ActualTime, PlannedTime])


# repeat the trial matrix for the two blocks
trials = numpy.tile(trials, (nblocks, 1))

# set clock to measure RT
my_clock = core.Clock()

# set other clock to verify presentation time of gabor stimulus
verify_clock = core.Clock()


# initialize trials
for b in range(nblocks):
    
    # tell participant which block is about to start
    BlockStim = visual.TextStim(win, text = "Nu begint blok {}. Druk op spatie om te beginnen.".format(b+1))
    BlockStim.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    for i in range(ntrials):
        
        # begin trial with mask stimulus
        MaskStim.sf = FrequencyListMask[i]
        MaskStim.draw()
        win.flip()
        core.wait(duration)
        
        # show target stimulus
        TargetStim.ori = OrientationList[i]
        TargetStim.sf = FrequencyList[i]
       
        TargetStim.draw()
        win.flip()
        
        # reset clock to measure RT accurately 
        my_clock.reset()
        
        # reset clock and get time to measure onset of stimulus
        verify_clock.reset()
        T1 = verify_clock.getTime()
        
        # set delay time 
        if b == 0:
            core.wait(DurationList[0])
        elif b == 1:
            core.wait(DurationList[1])
        elif b == 2:
            core.wait(DurationList[2])
            
            
        
        # get time at ending of stimulus 
        T2 = verify_clock.getTime()
        
        # calculate presentation time
        PresentationT = T2-T1
        trials[i, 10] = PresentationT
        
        # show mask again
        MaskStim.sf = FrequencyListMask[i]
        MaskStim.draw()
        win.flip()
        
        # wait for and register answer
        keys = event.waitKeys(keyList = ["f", "j", "escape", "esc"])
        trials[i, 3] = keys[0]
        
        # determine reaction time 
        RT = my_clock.getTime()
        trials[i, 5] = RT
        
        # determine correct response
        CorrectResp = correct_response()
        trials[i, 2] = CorrectResp
        
        # determine accuracy
        accuracy = -1
        if CorResp[i] == keys[0]:
            accuracy = 1
        else:
            accuracy = 0
            
        trials[i, 4] = accuracy
        
        
        # display feedback message
        feedback_message()
        
        # escape from trialloop
        if keys[0] == "escape":
            break
            


print(trials)


# say goodbye
Goodbye.draw()
win.flip()
event.waitKeys(keyList = ["space"])

# close experiment window
win.close()

