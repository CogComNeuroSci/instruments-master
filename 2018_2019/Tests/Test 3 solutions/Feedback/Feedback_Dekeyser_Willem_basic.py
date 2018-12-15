# import modules
from psychopy import visual, event, core, gui
import time, numpy



# create a dialog box
info = {"Participant number":0, "Participant name":"Unknown", "Gender":["male", "female", "other"], "hand preference":["left", "right", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Experiment")

if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# initialize the window
### Esther: breedte en hoogte omgewisseld
win = visual.Window(size = (500, 600), units = "norm", allowGUI = True)

# initialize the variables
ntrials     = 8
duration    = numpy.array([0.016, 0.033, 0.050])
orientation = numpy.array([30,-30])
##orientation = numpy.array([30,30,30,30,-30,-30,-30,-30]) -> ik wou in mijn trialloop doorheen deze waarden loopen. Dit wou niet werken.
##                                                             Deze waarden stellen de orientatie van gabor1 en gabor 2 stimulus aan.

# initialize gabor stimuli
gabor = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor1')

# initialize instructions text
instructions_text   = "The instructions are: \n\nPress f when the Gabor is turned to the left \n\nPress j when the Gabor is turned to the right. \n\nGoodluck!"

# initialize graphical elements
MessageOnSCreen     = visual.TextStim(win, text = "OK")

# store correct response
CorResp = numpy.repeat('t',len(orientation))

# deduce the correct response
CorResp[orientation == orientation[0]]     = "f"
CorResp[orientation == orientation[1]]     = "j"

# allow to store the accuracy, key and reaction time
key = numpy.repeat(-99.9,len(CorResp))
RT = numpy.repeat(-99.9,len(CorResp))
orientation = numpy.repeat(-99.9,len(CorResp))

# combine arrays in trial matrix
##trials = numpy.column_stack([duration, orientation, CorResp, key, RT])                -> Ik slaagde er maar niet in om deze trial in orde te krijgen.
##print(trials)

# repeat the trial matrix for the 3 blocks
##trials = numpy.tile(trials, (nblocks, 2))

# modules

## function for displaying messages
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

## function for displaying the feedback
def feedback_message(correct = -99):
    if correct == 1:
        message(message_text = "Correct!", duration = 1)
    else:
        message(message_text = "Wrong answer!", duration = 1)


# Initialize a clock to measure the reaction time
my_clock = core.Clock()

# display the welcome message
message(message_text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# display instructions
message(message_text = instructions_text + "!\n\nPress the space bar to continue.", height = 0.05, response_key = "space")


# displey the gabor in 3 blocks
for j in range(len(duration)):
    
    #display block message
    block_text          = "Block {0} will now start.\n\nPress the space bar to continue.".format(str(j+1))
    message(message_text = block_text, height = None, response_key = "space")
    
    for trials in range (ntrials):
        ## escape from the trial loop  -> in for-loop
        if key[0] == "escape" or key[0] == "tab":
            break
    
        ### Esther: waarom deze while loop waar je in vast geraakt?
        while trials <= 4:
            # initialize right gabor
            gabor1 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
                        size=[1.0, 1.0], sf=[4, 0], ori = 30, name='gabor1')
            
            #display gabor
            gabor.draw()
            win.flip()
            core.wait(1)
            
            ### Esther: er kan in elk geval heel wat gedupliceerde code verwijderd worden
            ### Esther: en nog eenvoudiger is core.wait(duration[j])
            # right gabor draw
            if j == 0:
                ##gabor.ori = int(orientation[trials])
                gabor1.draw()
                win.flip
                
                ### Esther: hier moet de clock gereset worden
                
                ## present the horizontal gabor stimuli for 16 ms
                core.wait(duration[0])
            if j == 1:
                gabor1.draw()
                win.flip
                ## present the horizontal gabor stimuli for 33 ms
                core.wait(duration[1])
            elif j == 2:
                gabor1.draw()
                win.flip
                ## present the horizontal gabor stimuli for 50 ms
                core.wait(duration[2])
            
            # display standard gabor
            gabor.draw()
            event.clearEvents(eventType = "keyboard")
            win.flip()
        
            # reset the clock
            my_clock.reset()
            
            # register response     
            key = event.waitKeys(keyList = ["f","j", "escape"])
            print(key) 
            
            ### Esther: ik zou hier meteen de RT meten
            
            if key == None:
                key = ['']
        
            # register Reaction Time
            RT = my_clock.getTime()*1000
            print("Your reaction time was {0} ms.!".format(round(RT,1)))
            
            correct = 0
            
            if key[0] == "f":
                correct == 1
            
            # determine keyboard response                              -> Ik was nog op zoek om de responsetijd, enz. op te slaan in een array, maar ben hier niet in geslaagd. 
            #                                                          -> Mijn reactietijd kan je wel geprint zien.
            ##trials[i,3] = key[0]
            
            # determine ReactionTime
            ##trials[i,4] = (round(RT,1))
            
            # determine correct response
            ##if key[0] == trials[i,1]:
            ##    correct == 1
            
            # present feedback message
            feedback_message()
            
        else:
            # initialize left gabor
            gabor2 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
                        size=[1.0, 1.0], sf=[4, 0], ori = -30, name='gabor1')
            
            #display gabor
            gabor.draw()
            win.flip()
            core.wait(1)
            
            #left gabor draw
            if j == 0:
                ##gabor.ori = int(orientation[trials])
                gabor2.draw()
                win.flip
                ## present the horizontal gabor stimuli for 16 ms
                core.wait(duration[i])
            if j == 1:
                gabor2.draw()
                win.flip
                ## present the horizontal gabor stimuli for 33 ms
                core.wait(duration[i])
            elif j == 2:
                gabor2.draw()
                win.flip
                ## present the horizontal gabor stimuli for 50 ms
                core.wait(duration[i])
                
            # display standard gabor
            gabor.draw()
            event.clearEvents(eventType = "keyboard")
            win.flip()
        
            # reset the clock
            my_clock.reset()
            
            # register response     
            key = event.waitKeys(keyList = ["f","j", "escape"])
            print(key) 
            
            if key == None:
                key = ['']
            
            # register Reaction Time
            RT = my_clock.getTime()*1000
            print("Your reaction time was {0} ms.!".format(round(RT,1)))
            
            correct = 0
            
            if key[0] == "j":
                correct == 1
            
            # determine keyboard response                              -> ik was nog op zoek om de responsetijd, enz. op te slaan in een array, maar ben hier niet in geslaagd.
            #                                                          -> Mijn reactietijd kan je wel geprint zien.
            ##trials[i,3] = key[0]
            
            # determine ReactionTime
            ##trials[i,4] = (round(RT,1))
            
            # determine correct response
            ##if key[0] == trials[i,1]:
            ##    correct == 1
            
            # present feedback message
            feedback_message()


# This is the end
message(message_text = "Goodbye " + info["Participant name"] + "!\n\nPress the space bar to end the experiment.", pos = (0,0), height = None)

# close the experiment window
win.close()







