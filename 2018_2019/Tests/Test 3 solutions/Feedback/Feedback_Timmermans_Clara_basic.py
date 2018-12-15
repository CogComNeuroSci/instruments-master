# This is the script for test 3
# 12/12/18 by Clara Timmermans

## Part 1: import modules ##
from psychopy import visual, event, gui, core
import time
import numpy as np 

## Part 2 : initalize window ##
win = visual.Window(size = (600,500), units = "norm")


## Part 3 : initialize variables ##
# create a dialog box
info = {"Participant name":"Unknown","Participant number":0,"Age":0, "Gender":["male", "female", "x"], "Hand preference" : ["left","right","ambidexter"] }
infoDlg = gui.DlgFromDict(dictionary=info, title="Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")
    
# initialize the variables
nblocks = 3
ntrials = 8
duration1 = 0.016
duration2 = 0.033
duration3 = 0.050

# initialize a clock to measure the RT
my_clock = core.Clock()
#my_clock2 = core.Clock()

# initialize graphical elements
gabor_vert = visual.GratingStim(win, tex="sin", mask="circle", texRes=256, 
           size=[0.4, 0.6], sf=2, ori = 0, name='gabor_vert')
gabor_target =  visual.GratingStim(win, tex="sin", mask="circle", texRes=256, 
           size=[0.4, 0.6], sf=20, ori = 30, name='gabor_target')
MessageOnSCreen = visual.TextStim(win, text = "OK")

# initalize orientation and spatial frequency 
Ori = np.array([-30,30,30,-30,30,-30,-30,30])
SF = np.array([2,20,2,20,2,2,20,20])

# deduce the correct response
Ori_str = np.array(["left","right","right","left","right","left","left","right"])
CorResp = np.copy(Ori_str)
for i in range(ntrials):
    CorResp[CorResp == "left"] = "f"
    CorResp[CorResp == "right"] = "j"
print(CorResp)

# default RT 
RT = np.repeat(-99.9,len(CorResp))

# default response key
Key = np.repeat("",len(CorResp))

# default accuracy
Accuracy = np.repeat("",len(CorResp))

# combine arrays in trial matrix
trials = np.column_stack([CorResp, Key,  RT, Accuracy,Ori, SF])

# repeat the trial matrix for the two blocks
trials = np.tile(trials, (nblocks, 1))
print(trials)

# function for presenting messages on screen
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    MessageOnSCreen.color   = color
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

# function for presenting feedback on screen
def feedback_message():
    if int(trials[i,3]) == 1:
        message(message_text = "Correct", duration = 1)
    else:
        message(message_text = "Wrong answer!", duration = 1)

# ik heb deze functie niet meer correct kunnen implementeren binnen de tijd.
# als ik verifier(duration1) ingaf dan kreeg ik de tijd van het eerste blok, maar printte hij de tijd van het tweede blok
# ik heb deze fout er niet meer kunnen uithalen
# function to verify presentation time
#def verifier(duration):
#    my_clock2 = core.Clock()
#    my_clock2.reset()
#    win.flip()
#    core.wait(duration)
#    Time = my_clock2.getTime() * 1000
#    print(Time)

# define task instruction
Instructions_text = ("In this experiment you will see a gabor stimulus presented on the screen.\n\n" +
                                            "You have to respond to the orientation of the stimulus.\n" +
                                            "You can use the two response buttons: “f” and“j”,\n" +
                                            "use the index and middle finger of your left and right hand.\n\n" +
                                            "If the stimulus is rotated to the left, press “f”\n" +
                                            "If the stimulus is rotated to the right, press “j”\n" +
                                            "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                            "Any questions?\n\nPress the space bar to continue.")
                                            

## Part 4 : display on the screen ##
# display the welcome message
message(message_text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# display the instructions
message(message_text = Instructions_text, response_key = "space", height = 0.05)

for b in range(nblocks):
    
    # display block message
    message(message_text = "Block " + str(b+1) + " will start when you press the space bar.", response_key = "space")
    
    # 10 trials
    for i in range(b*ntrials,(b+1)*ntrials):

        ### Esther: who, hier laat je heel wat redundante code terugkomen voor een klein probleem op te lossen
        if b == 0:
            # draw vertical gabor for 1 sec
            gabor_vert.draw()
            win.flip()
            core.wait(1)
            
            # draw rotated gabor 
            gabor_target.ori = int(trials[i,4])
            gabor_target.sf = int(trials[i,5])
            gabor_target.draw()
            win.flip()
            
            ### Esther: dit is de correcte plaats om de klok te resetten
            
            core.wait(duration1)
            
            # draw vertical gabor
            gabor_vert.draw()
            win.flip()
        
            # Now that the stimulus is on the screen, reset the clock
            my_clock.reset()
            
            # wait for response
            Keys = event.waitKeys(keyList = ["f","j","k","escape"], clearEvents = True)
           
            # Register the RT
            RT = my_clock.getTime() * 1000
            
            # Store the response key
            trials[i,1] = Keys[0]
            
            # quit loop
            if "escape" in Keys[0]:
                break
                
            # Store the RT
            trials[i,2] = RT
            
            # determine accuracy
            trials[i,3] = int(trials[i,0] == trials[i,1])
           
            # display feedback
            feedback_message()
            
        elif b == 1:
            # draw vertical gabor for 1 sec
            gabor_vert.draw()
            win.flip()
            core.wait(1)
            
            # draw rotated gabor 
            gabor_target.ori = int(trials[i,4])
            gabor_target.sf = int(trials[i,5])
            gabor_target.draw()
            win.flip()
            core.wait(duration2)
            
            # draw vertical gabor
            gabor_vert.draw()
            win.flip()
        
            # Now that the stimulus is on the screen, reset the clock
            my_clock.reset()
            
            # wait for response
            Keys = event.waitKeys(keyList = ["f","j","k","escape"],clearEvents = True)
           
            # Register the RT
            RT = my_clock.getTime() * 1000
            
            # Store the response information
            trials[i,1] = Keys[0]
            
            # quit loop
            if "escape" in Keys[0]:
                break
                
            # Store the RT
            trials[i,2] = RT
                
            # determine accuracy
            trials[i,3] = int(trials[i,0] == trials[i,1])
            
            # display feedback
            feedback_message()
            
        else:
            # draw vertical gabor for 1 sec
            gabor_vert.draw()
            win.flip()
            core.wait(1)
            
            # draw rotated gabor j
            gabor_target.ori = int(trials[i,4])
            gabor_target.sf = int(trials[i,5])
            gabor_target.draw()
            win.flip()
            core.wait(duration3)
            
            # draw vertical gabor
            gabor_vert.draw()
            win.flip()
        
            # Now that the stimulus is on the screen, reset the clock
            my_clock.reset()
            
            # wait for response
            Keys = event.waitKeys(keyList = ["f","j","k","escape"],clearEvents = True)
           
            # Register the RT
            RT = my_clock.getTime() * 1000
            
            # Store the response information
            trials[i,1] = Keys[0]
            
            # quit loop
            if "escape" in Keys[0]:
                break
            
            # Store the RT
            trials[i,2] = RT
            # determine accuracy
            trials[i,3] = int(trials[i,0] == trials[i,1])
            
            # display feedback
            feedback_message()
    
    ### Esther: hier moet je ook nog eens uit de block loop breken

print(trials)


## Part 5: finish the experiment ##
# display goodbye message
message(message_text = "Goodbye!", duration = 1, pos = (0,0.75), height = 0.2)

# close experiment window
win.close()
core.quit()










