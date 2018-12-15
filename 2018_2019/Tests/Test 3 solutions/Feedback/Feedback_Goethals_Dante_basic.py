#Test 3 : orientation detection of a Gabor patch

#import modules

from psychopy import visual, event, core, gui
import time, numpy



#create dialog box 
info = { "Participant name": Unknown, "Participant number": 0, "Age": 0, 
"Gender": ["male", "female", "third gender"],
"Hand preference": ["left", "right", "ambidextrous"]}
infoDlg = gui.DlgFromDict(dictionary=info, title ="Gabor experiment")
if infoDlg.OK: 
    print(info)
else:
    print("user cancelled")

#initialize window
win = visual.Window( size = [600,500], units = "norm")

#initialize the variables 
nblocks = 3
ntrials = 8

#adding values for orientation and spatial frequency
Orientation = numpy.array([30,30,30,30,-30,-30,-30,-30])
SpatialFrequency = numpy.array([2,2,20,20,2,2,20,20])

  
#deduce correct response
CorResp = numpy.copy(Orientation)
CorResp[CorResp == 30] = "j"
CorResp[CorResp == -30] = "f"

#add default response that will be overwritten during trial loop
Resp = numpy.repeat(0, len(CorResp))

#add default RT that will be overwritten during trail loop
RT = numpy.repeat(-99.9, len(CorResp))

#allow to store the accuracy
Accuracy = numpy.repeat(-99.9, len(CorResp))

#combine arrays in trial matrix
trials = numpy.column_stack([Orientation, SpatialFrequency, CorResp, Resp, Accuracy, RT])

### Esther: hierna moet de trials matrix nog drie keer herhaald worden om alle info te kunnen opslaan

#initialize graphical elements
Welcome = visual.Textstim(win, text = "Welcome " + info["Participant name"] + 
"! \n\nPress the space bar to continue.")
Instructions = visual.Textstim(win, 
text = "In a moment, you'll have to react to some specific figures that are briefly flashed. \n\n" + 
       "Press \"f\" when the orientation of the figure is leftwards.\n" +
       "That is when the lines go from the top left corner to the bottom right corner.\n\n" +
       "Press \"j\" when the orientation of the figure is rightwards. \n" + 
       "That is when the lines go from the top right corner to the bottom left corner. \n\n" +
       "Press the space bar to continue.") 
Block_start = visual.TextStim(win, text = "OK")
Goodbye = visual.TextStim(win, text ="Goodbye!")
Gabor_oriented = visual.GratingStim(win, mask = "circle", ori = 0, sf = 1)
Gabor_mask= visual.GratingStim(win, mask = "circle", ori = 0)
Feedback = visual.TextStim(win, text = "OK")

#make function for presenting message on screen
def message(message_text = "", duration = 0):
    Feedback.text = message_text
    
    Feedback.draw()
    win.flip()
    time.sleep(duration)
    
#make a function for displaying Feedback
def feedback_message(correct = -99):
    if correct == 1: 
        message(message_text = "Correct!", duration = 1)
    else:
        message(message_text = "Wrong answer!", duration = 1)

#initialize clock to measure RT
my_clock = core.Clock()

#display the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = ["space " ])

#display the instructions 
Instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])

#show Gabor patches
#three block

for b in range(nblocks):
    
    #announce what block is about to start
    Block_start.text = "Block" + str(b+1) + "will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    #with 8 trials
    ### Esther: dit is niet een correcte indexering
    for i in range(b*ntrials, (b+1)*ntrials, (b+2)*ntrials):
        
        #set orientation and spatial frequency for this trial
        Gabor_oriented.ori = trials[i, 0]
        Gabor_oriented.sf = trials[i, 1]
        
        #mask Gabor presentation
        Gabor_mask.draw()
        win.flip()
        core.wait(1)
        
        #oriented Gabor presentation
        Gabor_oriented.draw()
        
        ### Esther: dit is het moment om het keyboard te clearen
        
        win.flip()
        
        #reset clock
        my_clock.reset()
        
        # implementation 16, 33 or 50 ms per block
        ### Esther: je dient de waarden 0.016, 0.033 en 0.050 te genereren
        core.wait(((b+1)*(16)) + (1*b)) 
        
        #mask Gabor presentation on back buffer
        Gabor_mask.draw()
        
        #clear keyboard input
        event.clearEvents(eventType = "keyboard")
        
        #display on screen
        win.flip()
       
        #wait for response
        keys = event.waitKeys(keyList = ["f", "j", "escape"])
        
        #register RT 
        RT = my_clock.getTime()
        
        #escape from trial loop
        if keys[0] == "escape":
            break
        
        #store the response information
        trials[i,3] = keys[0]
        
        #store RT
        trials[i,5] = RT
        
        #determine accuracy
        ### Esther: het correcte antwoord is nog niet bepaald
        trials[i,4] = int(trials[i,2] == trials[i,3])
        
        #determine and display feedback message
        feedback_message(correct = int(trials[i,4))
        
    
    ### Esther: hier dien je nog uit de blokloop te breaken
    
    
### Esther: vaarwel?



