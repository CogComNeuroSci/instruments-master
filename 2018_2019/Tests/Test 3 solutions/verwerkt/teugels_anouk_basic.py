# import modules
from psychopy import visual, event, core, gui
import time, numpy as np

# create a dialog box
info = {"Voornaam":"Unknown", "Proefpersoonnummer":0, "Leeftijd":0, "Gender":["man", "vrouw","derde gender"], "Hand voorkeur":["links","rechts","ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Gabor Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")
    
# initialize window
win = visual.Window(size=[600,500],units="norm")

# initialize variables
naam = info["Voornaam"]
nblocks=3
ntrials=8
my_clock= core.Clock()

# adding values for orientation and spatial frequency
Orientation = np.array([30,-30,30,-30, 30,-30, 30,-30])
SpatialFreq = np.array([2,20,20,2,2,20,20,2])

# define visual stimuli
MessageOnScreen = visual.TextStim(win,text="OK")
Gabor=visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, size=[1.0, 1.0], sf=10, ori = 0)

# a funtion for presenting messages on screen
def message(message_text = "", response_key = "space", duration = 0):
    MessageOnScreen.text=message_text
    MessageOnScreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList=response_key)
    else:
        time.sleep(duration)

# determining the correct response
#def determineCorResp():
#    if Gabor.ori == 30:
#        CorResp = "j"
#    if Gabor.ori == -30:
#        CorResp = "f"
#    
#    return CorResp
#
# a function for giving feedback
#def feedback_message(CorResp):
#    if keys[0] == CorResp:
#        feedback = "Correct!"
#    else:
#        feedback = "Verkeerd antwoord!"
#    message(message_text=feedback, duration=1)

# welcome message
message(message_text="Welkom {0}! \n\nDruk op spatie om verder te gaan.".format(naam),response_key="space")

# instructions
message(message_text="Op het scherm verschijnt telkens een Gabor. \n\nDruk op 'f' indien de Gabor naar links is gedraaid (lijnen van linksboven naar rechtsonder)." +
        " \nDruk op 'j' wanneer deze naar rechts gedraaid is (lijnen van rechtsboven naar linksonder).\n\nDruk op spatie om verder te gaan.", response_key="space")

# response array
ResponseArray = np.array([])

# reactiontime array
RTArray = np.array([])

# blockloop
for block in range (nblocks):
    message(message_text="Block {0} start nu. Druk op spatie om verder te gaan.".format(block+1),response_key="space")

    for trial in range(ntrials):
        # set spatial frequency
        Gabor.sf = SpatialFreq[trial]
        
        # draw masking Gabor stimulus
        Gabor.draw()
        win.flip()
        core.wait(1)
        
        # change time per block
        if block == 0:
            seconds=0.16
        elif block == 1:
            seconds=0.33
        else:
            seconds=0.5
        
        # set orientation
        Gabor.ori = Orientation[trial]
        
        # draw Gabor stimuli
        Gabor.draw()
        
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard")
        
        # put Gabor on screen
        win.flip()
        
        # reset clocks 
        my_clock.reset()
        
        # define keys
        keys = event.waitKeys(keyList = ["f","j","escape"])
        
        # show Gabor for limited time
        core.wait(seconds)
        
        # reset orientation
        Gabor.ori = 0
        
        # vertical Gabor untill respons is given
        Gabor.draw()
        win.flip()
        
        # register RT
        RT=my_clock.getTime()
        
        #escape from trials
        if keys[0] == "escape":
            break
        
        # register response
        ResponseArray = np.append(ResponseArray, keys[0])
        
        # register RT
        RTArray = np.append(RTArray,RT)
        
#        # look if answer is correct
#        CorResp = determineCorResp()
#        
#        # give feedback
#        feedback(CorResp)
    
    #escape from block
    if keys[0] == "escape":
        break

print(ResponseArray)
print(RTArray)

# end message
message(message_text="Dit is het einde van het experiment. Bedankt voor je deelname!",response_key="space")

# close experiment
win.close()
core.quit()