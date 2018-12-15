# Importing modules
import numpy, time
from psychopy import visual, gui, core

# create a dialog box
### ESther: hier heb je meteen al een syntax error
info = {"Participant name":"Unknown", "Participant number":0, "Age":0, "Gender":["male", "female", "", "Handpreference":["left", "right", "ambidexter"]}
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# initializing
nblocks = 3
ntrials = 8
participant = info["Participant name"]
key_list = ["f","j"]
### Esther: pas op, deze aanbiedingstijden zijn 
Stimulus_presentation  = numpy.array([0.16, 0.33, 0.50])
my_clock = core.Clock()

# initialize the window
win = visual.Window(size=[600,500], units = 'norm')

# initialize instructions
Instructions = ("In dit experiment krijgen jullie Gabor stimuli te zien.\n" +
                "Druk op de f toets wanneer de Gabor stimulus naar links gedraaid is\n" +
                "en druk op de j toets wanneer de Gabor stimulus naar rechts gedraaid is.\n" +
                "Druk op de spatiebalk om door te gaan.")

### Esther: waarom staat er hier een waitKeys()?
                event.waitKeys(keyList = ["space"])


# add a default RT that will be overwritten during the trial loop
RT = numpy.repeat(-99.9,n_trials)

### Esther: CorResp bestaat nog niet
# allow to store the accuracy
Accuracy = numpy.repeat(-99.9,len(CorResp))

# add a default response that will be overwritten during the trial loop
Resp = numpy.repeat(0,len(CorResp))

### Esther: Gaborright, Gaborleft, CorResp, Resp bestaan nog niet
# combine arrays in trial matrix
trials = numpy.column_stack([Gaborright, Gaborleft, Stimulus_presentation, CorResp, Resp, Accuracy, RT])

### Esther: waarom uitbreiden in de 2de dimensie?
# repeat the trial matrix for the three blocks
trials = numpy.tile(trials, (nblocks, 2))

# initialize graphical elements
Gaborvertical = psychopy.visual.GratingStim(win, pos=(0.0, 0.0), ori=0.0))
Gaborright = psychopy.visual.GratingStim(win, pos=(0.0, 0.0, ori=30)
Gaborleft = psychopy.Visual.GratingStim(win, pos=(0.0, 0.0, ori = 330)

### Esther: deze logische vergelijking bevat heel wat fouten zoals = versus ==
# make a function to deduce the correct response
def determine_CorResp(target = "Gaborright"):
    if target = "Gaborright":
        CorResp = "j"
     else target = "Gaborleft":
        CorResp = "f"
    
    return CorResp

### Esther: duration?
#define feedback message
def feedback_message():
    if int(trials[i,2]) == 1:
        feedback_text= ("Correct!", duration = 1)
    else int (trials [i,2]) == 0:
        feedback_text= ("Verkeerd antwoord!", duration = 1)
    return feedback_message()

# display the welcome message
message(message_text = "Welkom " + info["Participant name"] + "!\n\nDruk op de spatiebalk om door te gaan.", response_key = "space")

# display the Gabor stimuli in 3 blocks
for b in range(nblocks): 
    # announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    ### Esther: "space" hoeft niet tot een lijst omgevormd te worden 
    event.waitKeys(keyList = ["space"])

### Esther: waarom staat de trial loop niet in de blok loop?
# 8 trials
for i in range(b*ntrials,(b+1)*ntrials):
    Gaborright = trials [i,0]
    Gaborleft = trials [i, 1]
    Stimulus_presentation = [i, 2]
    
    ### Esther: heel wat problemen met flip en wait
    Gaborvertical.draw()
    core.wait (1)
    Gaborright.draw()
    ### Esther: trial bestaat niet
    core.wait(Stimulus_presentation[trial])
    Gaborvertical.draw()
    core.wait(1)
    
    ## clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    
    ## display the Go message on the screen
    win.flip()
    
    ## reset the clock to measure the RT
    my_clock.reset() 
    
    ## wait for the key press and register it
    keys = event.waitKeys(keyList = ["f","j"])
    
    ## register the time
    RT[trial] = my_clock.getTime()
    
    ## display the accuracy feedback:
    feedback_message()
     
     # escape from the trial loop
        if keys[0] == "escape":
            break

### Esther: goodbye?

# close the experiment window
win.close()
print (trials)