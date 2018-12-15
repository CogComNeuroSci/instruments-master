""" Test 3 """
""" Goal is to make an experiment where the participant need to estimate the oriëntation of the Gabor stimilus """

# Importing
from psychopy import visual, event, core, gui
import time, numpy 

# Initialize the clock
timing = core.Clock()

# Making a dialoge box
info = { "Participant number":0, "Participant name": "Unknown", 
         "Gender": ["male", "female", "Other gender"], "Age":0, 
         "Hand preference": ["left", "right", "both"] }
infoDLG = gui.DlgFromDict(dictionary = info, title = " Gabor experiment" )

if infoDLG.OK:
    print(info)
else:
    print("User Cancelled")

# Variables
nblock      = 3
ntrials     = 8
participant = info["Participant number"]

# Making values

## YOU HAVE THREE BLOCK WHICH EACH ANOTHER PRESENTATIONTIME
Presentation = numpy.array([ 0.16, 0.16, 0.16, 0.16, 0.16, 0.16, 0.16, 0.16,
                             0.33, 0.33, 0.33, 0.33, 0.33, 0.33, 0.33, 0.33,
                             0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50, 0.50 ])
                                    
## IN EACH BLOCK YOU HAVE AN ORIENTATION TO THE LEFT OR RIGHT
Orientation  = numpy.array([ -30, -30, -30, -30, 30, 30, 30, 30,
                             -30, -30, -30, -30, 30, 30, 30, 30,
                             -30, -30, -30, -30, 30, 30, 30, 30 ])
                                
## AND FOR EACH ORIENTATION YOU HAVE FREQUENCY 2 OR 20 HZ
Frecuency    = numpy.array([ 2, 2, 20, 20, 2, 2, 20, 20,
                             2, 2, 20, 20, 2, 2, 20, 20,
                             2, 2, 20, 20, 2, 2, 20, 20 ])
                             
## WHEN THE ORIENTATION IS TO THE LEFT, THE CORRECT RESPONE IS F
## WHEN THE ORIENTATION IS TO THE RIGHT, THE CORRECT RESPONE IS J
CorResp     = numpy.array([ "f", "f", "f", "f", "j", "j", "j", "j",
                            "f", "f", "f", "f", "j", "j", "j", "j",
                            "f", "f", "f", "f", "j", "j", "j", "j"]) 
                            
## OTHER STUFF
Resp        = numpy.repeat(0, ntrials)
Accuracy    = numpy.repeat(0, ntrials)
Congruency  = numpy.repeat("x", ntrials)
RT          = numpy.repeat(-99, ntrials)

## PARTICIPANT INFO
Number      = numpy.repeat(info["Participant number"],len(CorResp))
Gender      = numpy.repeat(info["Gender"],len(CorResp))
Age         = numpy.repeat(info["Age"],len(CorResp))

# COMBINE ALL ARRAYS IN ONE
trials      = numpy.column_stack([ Presentation, Orientation, Frecuency, CorResp, Accuracy, Congruency, RT, Resp, Number, Gender, Age])

# REPAT THIS TRIAL MATRIX FOR THE THREE BLOCKS
trials      = numpy.tile(trials, (nblocks, 1))

# Making a window
win             = visual.Window( [600, 500], color = [-1, -1, -1], units = "norm" )

# Making the graphics
gabor_stimulus   = visual.GratingStim(win, mask = "circle", size=[1.0, 1.0], ori = 30, sf = 2)
gabor_vertical  = visual.GratingStim(win, mask = "circle", size=[1.0, 1.0], ori = 180, sf = 2)

# Making a function for a message
def message(text = "", color = "red", pos = (0.0, 0.0), response_key = "space", duration = 0):
    
    message.text    = text
    message.color   = color
    message.position= pos
    
    message.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)
        
# Making a function performing a trial
def perform_trial():
    
    ## FIRST START WITH GABOR STIMILUS WITH VERTICAL ORIËNTATION
    gabor_vertical.draw()
    
    ## MAKING THE KEYBOARD INPUT CLEAR
    event.clearEvents(eventType = "keyboard")
    
    ## STIMILUS ON THE SCREEN
    win.flip()
    time.sleep(1.0)
    
    ## GABOR STIMILUS PRESENTS
    gabor_stimulus.draw()
    
    ## GABOR STIMILUS ON THE SCREEN
    win.flip()
    
    ## RESET THE CLOCK
    timing.reset()
    
    ## GABOR VERTICAL KEEPS ON THE SCREEN UNTIL THE PARTICIPANT RESPONDS
    gabor_vertical.draw()
    win.flip()
    
    ## WAITING FOR THE RESPONSE
    keys = event.waitKeys(keyList = ["f","j", "escape"])
    
    ## REGISTER THE REACTION TIME
    RT = timing.getTime()
    
    if keys == None:
        keys = [0]
        
    return keys, RT
    
# Making a feedback function
def feedback_message(correct = -99):
    if correct == 1:
        message(message_text = "Correct!", duration = 1)
    else:
        message(message_text = "Wrong answer!", duration = 1)
        
# Making a congruency function
def congruency_function(Orientation = 30, CorResp = "j"):
    if (Orientation = 30 and CorResp = "j") or (Orientation = -30 and CorResp = "f"):
        congr = "Congruent"
    else:
        congr = "Incongruent"
    return congr


# Display a welcome
message(text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# Display the gabor stimuli
##YOU HAVE THREE BLOCK WHICH EACH 8 TRIALS

for b in range(nblock):
    
    ## GIVE THE INSTRUCIONS
    message(text = "Carefully read the instructions! \n\n" +
                    "In this block you will see figures with another oriëntation: " +
                    "if you see a figures where the oriëntation is turned to the left, press F." +
                    "But if the oriëntation is turned to the right, you have to press J." +
                    "Any questions?\n\nPress the space bar to continue.", response_key = "space")
    
    ## MAKE PARTICIPANT CLEAR BLOCK IS GOING TO START
    message(text = "Press the space bar to continue to the block " + str(b+2) + ".", response_key = "space")
    
    ## YOU HAVE 8 TRIALS EACH BLOCK
    for i in range(b*ntrials,(b+1)*ntrials, (b+2)*ntrials):
        
        ## Set everything ready
        gabor_stimulus.duration = trials[i, 0] ## how long is it presented?
        gabor_stimulus.ori      = trials[i, 1] ## which oriëntation?
        gabor_stimulus.sf       = trials[i, 2] ## which frequency?
        
        ## Correct response
        trials[i, 3] = CorResp(trials[i, 3])
        
        ## Storing
        if keys[0] != 0:
            
            trials[i, 3] = keys[0]                                  ## store the response of the participant
            trials[i, 4] = int(trials[i, 3] == trials[i, 7 ] )       ## store the accuracy
            trials[i, 6] = RT                                       ## store the reactiontime
        
        ## Five feedback
        feedback_message(correct = trials[i, 4] ) 
        
        ## Escape from the trialloop
        if keys[0] == "escape":
            break
        
# Display the goodbye message
message(text = "Thank you for partipating!", duration = 1)

# Close experiment window
win.close()

print(trials)

