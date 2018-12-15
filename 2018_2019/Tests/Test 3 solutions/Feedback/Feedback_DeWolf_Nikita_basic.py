#Import modules 
from __future__ import absolute_import, division, print_function
from psychopy import visual, core, event, gui
import time, numpy
import psychopy.core
import psychopy.event

# Create a DlgFromDict: we create a window in which name, age, hand preference and participant number will be asked
info = {'Name':'','Gender':['male', 'female', 'third gender'], 'Age':'', 'Participant Number': '0', 'Hand Preference': ['right', 'left', 'ambidextrous']}
infoDlg = gui.DlgFromDict(dictionary=info, title='TestExperiment')
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print('User Cancelled')

#Initialization of the window
win = visual.Window([600, 500], units = 'norm', color = (-1, -1, -1)) #Step 1: we'll work with a window with width =600 and height = 500. We also work with a normalized coordinate system

#Initialize variables
nblocks = 3
ntrials = 8
### Esther: vanwaar de -1 en 0?
orientation = (-1, 0) #if the orientation is to the left

#we add the values for the spatial frequencies (sf) and time
sf = numpy.array([2, 20])
time = numpy.array([16, 33, 50])

#deduce the task Instructions
if orientation == (-1, 0):
    #when the orientation is to the left, participants have to press the "f" keyList
    CorResp = "f"
else:
    #when the orientation is to the right, participant have to press the "j" keyList
    CorResp = "j"

#Deduce the correct response 
CorResp[CorResp == "left"] == "f"
CorResp[CorResp == "right"] == "j"

#Allow us to store the accuracy
Accuracy = numpy.repeat(-99.9, len(CorResp))

#Default response during the trial loop
Resp = numpy.repeat(0, len(CorResp))

#Initialization of the graphic elements
WelcomeText = visual.TextStim(win, text = "Welcome to the experiment, {0}!\nTo continue, please press the spacebar.".format(info['Name']))

Text = ("In this experiment you will be asked to estimate the orientation of a Gabor stimulus.\n" + 
       "More specifically, you need to determine whether the stimulus is oriented to the left or to the right.\n\n\n" + 
       "Press spacebar to continue.")
Instructions = visual.TextStim(win, text = Text, height = 0.08)

Text2 = ("When the stimulus is turned to the left (from the top left to bottom right), please press 'f' on your keyboard.\n"+
       "When the stimulus is turned to the right side (from the top right to the top left), pleasse press 'j' on your keyboard.\n"+
       "The entire experiment consists out of three blocks.\n\n"+
       "Answer as quickly as possible, but try to avoid mistakes.\n"+
       "When you have questions left, please contact the researcher.\n\n\n"+
       "When you're ready to start the experiment, you can press the space bar.")
Instructions2 = visual.TextStim(win, text = Text2, height = 0.08) # Ik kon de instructions in 1 venster doen, maar heb ervoor gekozen dit in twee delen te doen omdat het het overzichtelijker maakt voor de participant ook. 

Block_start = visual.TextStim(win, text = "OK")
Feedback = visual.TextStim(win, text = "OK")
Goodbye = visual.TextStim(win, text = "You've reached the end of the experiment.\nThank you for participating.\n\nHave a nice day!")

#Display the welcome message
WelcomeText.draw()
win.flip()
### Esther: "space" hoeft niet tot een lijst omgevormd te worden 
event.waitKeys(keyList=["space"])

#Display the instructions: pt.1
Instructions.draw()
win.flip()
event.waitKeys(keyList=["space"])

#Display the instructions: pt.2
Instructions2.draw()
win.flip()
event.waitKeys(keyList=["space"])

#Display the Gabor Stimuli
# in three blocks
for b in range(nblocks):
    #announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = ["space"])
    
    # In 8 trials 
    for i in range(b*ntrials, (b+1)*ntrials):
        #Present a Gabor stimulus with vertical orientation for 1 second
        ### Esther: het is nog beter om de stimulus al aan te maken voor de loops en hier dan enkel de cruciale eigenschappen aan te passen
        gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf= 5, ori = 0) # ori = 0 for vertical orientation
        gabor.draw()
        ### Esther: ola, eerst flippen en dan wachten!
        core.wait(1.0)
        win.flip() 
        
        #wait for the response
        ### Esther: dit moest waitKeys() zijn !
        keys = event.getKeys(keyList = ["f", "j", "escape"])
        
        #escape from the trial loop
        if keys == "escape":
            break
        
        #Determine the feedback message
         #If _______:
          #Feedback.text = "Correct!"
         #else:
          #Feedback.text = "Wrong answer!"
        
        
        ### Esther: waarom zo een moeilijke aanpak om je feedback message te laten staan voor een bepaalde tijd? core.wait(1.0) volstaat
        #display the feedback message 
        timer = core.Clock()
        timer.add(0.25)
        while timer.getTime() <0:
            Feedback.draw()
        win.flip()
    
    # escape from the block loop
    if keys== "escape":
        break

#Display the goodbye message 
Goodbye.draw()
win.flip()
core.wait(4.0)

#Close the experiment window
win.close()

print(trials)


"""Due to lack of time I couldn't find in time the answer to vary over the three timing 
options within the loop as well as the spatial frequention. As you can see, in every trial the same gabor stimulus is 
presented (with vertical orientation). The feedback couldn't be fixed in time as well. That's why
you see the hashtags with the not-filled-in-yet if statement. :( :( """