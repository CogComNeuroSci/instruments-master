#This experiment is made by Nel Tavernier in purpose of Test 3 IEP on 12/12/2018

#Importing modules
from psychopy import visual, event, core, gui
from decimal import Decimal
import time, numpy
import matplotlib.pyplot as plt

#Making a window 
win = visual.Window([600,500], units = "norm")

#record dropped frames
win.recordFrameIntervals = True


# Making a dialog box
info = {'Participant number': 000, 'Participant name': 'Name', 'gender':['male', 'female', 'third gender'], 'age': 21, 'hand preference':['left', 'right', 'ambidexter']}
infoDlg = gui.DlgFromDict(dictionary=info, title='TestExperiment')
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print('User Cancelled')

# set response key before so we can use it as length
response_key = numpy.array(["left", "left", "right", "right", "left", "left", "right", "right"])
number = numpy.repeat(info['Participant number'], len(response_key))
gender = numpy.repeat("".join(info['gender']), len(response_key))
age = numpy.repeat(info['age'], len(response_key))
handpreference = numpy.repeat("".join(info['hand preference']), len(response_key))

#initialization
nblocks = 3
ntrials = 8
my_clock = core.Clock()
MessageOnSCreen = visual.TextStim(win, text = "OK")


# Making a gabor
myGabor = visual.GratingStim(win, mask = "gauss", ori = 0, sf = 4) 

# Correct response 
CorResp = numpy.copy(response_key)
CorResp[CorResp == "left"] = "f"
CorResp[CorResp == "right"] = "j"


# ori and sf

ori_Gauss = numpy.array([-30, -30, 30, 30, -30, -30, 30, 30])
sf_Gauss = numpy.array([2, 20, 2, 20, 2, 20, 2, 20])

# key acc and RT
Key = numpy.repeat("-99.9",len(ori_Gauss))
Accuracy = numpy.repeat("-99.9",len(CorResp))
RT = numpy.repeat("-99.9",len(CorResp))

# making the trialmatrix
trials = numpy.column_stack([ori_Gauss, sf_Gauss, Key, Accuracy, CorResp, RT, number, gender, age, handpreference])
trials = numpy.tile(trials, (nblocks, 1))


# Message function
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
        
#feedback function
def feedback_message():
    text_correct = visual.TextStim(win, text = "Correct!")
    text_wrong = visual.TextStim(win, text = "Wrong answer!")
    
    #determine accuracy
    trials[i, 3] = int(trials[i,4] == trials[i,2])
    #make feedback
    if int(trials[i,3]) == 1:
        text_correct.draw()
    else: 
        text_wrong.draw()
    win.flip()
    core.wait(1)


# instructions text
Instructions_text = ("This experiment contains 3 blocks. Each block will have 8 gausses that are shown."
                    "You will have to decide whether the stripes of the gauss are going from the left top to the right bottom"
                    "or from the right top to the left bottom. If the stripes from the gauss go from the left top you have to" 
                    "press the button 'f', if the stripes go from the right top you have to press the button 'j'. Good luck!"
                    "Press the space button to continue")

# Welcome message display
message(message_text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# Display Instructions 
message(message_text = Instructions_text, response_key = "space", height = 0.05)

#Make the blocks
for b in range (nblocks): 
    message(message_text = "Block " + str(b+1) + " will start when you press the space bar.", response_key = "space")
    
    ### Esther: pas op, deze aanbiedingstijden zijn 10 keer te lang
    if b == 0: 
        duration = 0.16
    if b == 1: 
        duration = 0.33
    if b == 2: 
        duration = 0.50
        
    #Make the trials
    for i in range(b*ntrials,(b+1)*ntrials):
        #show vertical gabor for 1 second
        myGabor.draw()
        win.flip()
        core.wait(1)
        
        #Showing the masking gabor
        gaborMask = visual.GratingStim(win, mask = "gauss", ori = trials[i,0], sf = trials[i,1]) 
        gaborMask.draw()
        win.flip()
        
        my_clock.reset()
        
        core.wait(duration)
        
        #show the vertical gabor
        myGabor.draw()
        event.clearEvents(eventType = "keyboard")
        win.flip()
        
        #wait until they answer with f or j
        Key = event.waitKeys(keyList = ["f", "j", "esc", "escape"], maxWait = 1.5)
        
        if Key == None: 
            Key = [""]
            
        trials[i, 2] = Key[0]
            
        #Get the reaction time after the key is pressed 
        RT = [my_clock.getTime()*1000]
        print(RT)
        trials[i, 5] = RT[0]
        
        #feedback message
        feedback_message()
        
        if Key[0] in ["esc", "escape"] : 
            break
    if Key[0] in ["esc", "escape"]: 
        break



#Present the goodbye message 
message(message_text = "Goodbye!", duration = 1, pos = (0,0.75), height = 0.2)

# print trial matrix 
print(trials)


#Close the window
win.close()

#showing whether there are dropped frames. 
plt.plot(win.frameIntervals)
plt.show()