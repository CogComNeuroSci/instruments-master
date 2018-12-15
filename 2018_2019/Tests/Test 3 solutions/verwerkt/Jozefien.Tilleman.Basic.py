
#importing modules
from psychopy import visual, event, core, gui
import time, numpy as np


# create a dialog box
info = {"Participant number":0, "Participant name":"Unknown", "Gender":["male", "female","other"], "Age":0,"handpreference":["Left","Right"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="grating experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

#creating window
win = visual.Window([600, 500], units="norm", allowGUI=False)

##creating stimuli##

#creating gabor
gabor = visual.GratingStim(win, tex="sin", mask="circle", ori=0, size=[1.0, 1.0], sf=20, units="norm")

#creating informationtexts

Welcome=visual.TextStim(win,text="Welcome {0}\n Thank you for participating in this experiment.\n If you are ready to start, press 'space'".format(info["Participant name"]))

blocktext=visual.TextStim(win,text="")


goodbye=visual.TextStim(win, text="This is the end of the experiment.\n Thank you for participating.\n Press 'space' to quit the experiment.")

##creating variables##

#trialloop
gabor_Ori=np.array([-30,30,-30,30,-30,30,-30,30])
gabor_SF=np.array([2,20,20,2,2,20,20,2])
Res=np.repeat(0,len(gabor_Ori))
corr_Resp=gabor_Ori
RT=np.repeat(0,len(gabor_Ori))

trials=np.array([gabor_Ori,gabor_SF,Res,corr_Resp, RT])

#blockloop
text=np.array(["In the following trials you will be presented a 'gabor'.If the gabor is turned left, press f. If the gabor is turned right, press j.\n  The gabor stimulus will be masked with a vertical gabor stimulus. \n To go further, please press 'space'.","you ended the first block, press 'space' to continue to the next block.","you ended the second block, press 'space' to continue to the last block."])
PresTime=np.array([0.016,0.033,0.050])

Blocks=np.array([text,PresTime])


##putting stimuli on the window (flow)##

#Welcome
Welcome.draw()
win.flip()
event.waitKeys(keyList=["space"])

Clock=core.Clock

#blockloop
for b in range (3):
    
    blocktext.text=Blocks[0,b]
    PT=Blocks[1,b]
    print(PT)
    
    blocktext.draw()
    win.flip()
    event.waitKeys(keyList=['space'])

    #trialloop
    for i in range (8):
        #mask stimulus
        gabor.draw()
        win.flip()
        core.wait(1)
        
        #manipulated stimulus
        gabor.ori= trials[0,i]
        gabor.draw()
        event.clearEvents(eventType="keyboard",)
        win.waitBlanking
        win.flip()
        Clock.reset()
        key=event.getKeys(keyList=["f","j"], timeStamped=Clock)
        core.wait(0.016) #Dit moet core.wait(PT) zijn maar werkt niet
        
        #key and RT
        trials[2,i]=key[0]
        trials[4,i]=key[1
        
        #feedback
        if trials[2,i]==trials[3,i]:
            print("correct")
        else:
            print("incorrect")
        
        #mask stimulus
        gabor.ori=0
        gabor.draw()
        win.flip()
        
        #escaping from experiment
        if 'escape' in key:
            quit
    
    print(trials)

#goodbye
goodbye.draw()
win.flip()
event.waitKeys(keyList='space')


win.close()
core.quit()
