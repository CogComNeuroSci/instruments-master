# displaying Stroop stimuli

# import modules
from psychopy import visual, event, core, gui
import time, numpy

# create a dialog box
info = {"Participant number":0, "Participant name":"Unknown", "Gender":["male", "female"], "Age":0}
infoDlg = gui.DlgFromDict(dictionary=info, title="Stroop Experiment")
if infoDlg.OK:  # this will be True (user hit OK) or False (cancelled)
    print(info)
else:
    print("User Cancelled")

# initialize the window
win = visual.Window(fullscr = True, units = "norm")

# initialize the variables
nblocks     = 2
nprac       = 3
ntrials     = 16
participant = info["Participant number"]

# initialize the typical versus atypical task Instructions
Atypical = (    "Carefully read the instructions, they will change across blocks!\n\n" +
                "In this block you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
                "presented in a random ink color (red, blue, green and yellow color).\n\n" +
                "You have to respond to the meaning of the written word and\n" +
                "ignore the ink color of the stimulus.\n\n" +
                "You can use the following four response buttons (from left to right;\n" +
                "use the index and middle finger of your left and right hand):" +
                "“d”,“f”,“j” and “k”.\n\n" +
                "If the written word is red, press the leftmost button “d”.\n" +
                "If it’s blue, press “f”.\n" +
                "If it’s green, press “j”.\n" +
                "If it’s yellow, press “k”.\n\n" +
                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                "By all means ignore the ink color, you should only respond to the meaning of the words.\n\n" +
                "Any questions?\n\nPress the space bar to continue.")

Typical = (     "Carefully read the instructions, they will change across blocks!\n\n" +
                "In this block you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
                "presented in a random ink color (red, blue, green and yellow color).\n\n" +
                "You have to respond to the ink color of the stimulus and\n" +
                "ignore the meaning of the written word.\n\n" +
                "You can use the following four response buttons (from left to right;\n" +
                "use the index and middle finger of your left and right hand):" +
                "“d”,“f”,“j” and “k”.\n\n" +
                "If the ink color is red, press the leftmost button “d”.\n" +
                "If it’s blue, press “f”.\n" +
                "If it’s green, press “j”.\n" +
                "If it’s yellow, press “k”.\n\n" +
                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                "By all means ignore the meaning of the words, you should only respond to the ink color.\n\n" +
                "Any questions?\n\nPress the space bar to continue.")

# we start with adding the values for the words and the colors
ColorWord   = numpy.array([ "red", "red", "red", "red",
                            "blue", "blue", "blue", "blue",
                            "green", "green", "green", "green",
                            "yellow", "yellow", "yellow", "yellow"])
FontColor   = numpy.array([ "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow"])

# deduce the congruence
CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean   = numpy.array(ColorWord == FontColor)
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]

# allow to store the correct response
CorResp = numpy.repeat("",len(Congruence))

# allow to store the accuracy
Accuracy = numpy.repeat(-99.9,len(CorResp))

# add a default response that will be overwritten during the trial loop
Resp = numpy.repeat(0,len(CorResp))

# add a default RT that will be overwritten during the trial loop
RT = numpy.repeat(-99.9,len(CorResp))

# add the participant info
Subject = numpy.repeat(info["Participant number"],len(CorResp))
Gender  = numpy.repeat("".join(info["Gender"]),len(CorResp))
Age     = numpy.repeat(info["Age"],len(CorResp))

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp, Resp, Accuracy, RT, Subject, Gender, Age])

# repeat the trial matrix for the two blocks
trials = numpy.tile(trials, (nblocks, 1))

# select three practice trials (twice because of the changing instructions)
practice = trials[[3,9,15,16,8,1],]

# initialize graphical elements
MessageOnSCreen = visual.TextStim(win, text = "OK")
Stroop_stim     = visual.TextStim(win, text = "red", color = "blue")
TheEndImage     = visual.ImageStim(win, image = "the_end.jpg")

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

# make a function for performing a trial
def perform_trial():
    
    # start with a fixation cross
    message(message_text = "+", duration = 0.25)
    
    # draw the stimulus on the back buffer
    Stroop_stim.draw()
    
    # clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    
    # display the stimulus on the screen
    win.flip()
    
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    
    # Wait for the response
    keys = event.waitKeys(keyList = ["d","f","j","k","escape"], maxWait = 1)
    
    # Register the RT
    RT = my_clock.getTime()
    
    if keys == None:
        keys = [0]
    
    return keys, RT

# make a function for displaying the feedback
def feedback(correct = -99):
    if correct == 1:
        message(message_text = "Correct!", duration = 0.25)
    else:
        message(message_text = "Wrong answer!", duration = 0.25)

# make a function to deduce the correct response
def determine_CorResp(target = "red"):
    if target == "red":
        CorResp = "d"
    elif target == "blue":
        CorResp = "f"
    elif target == "green":
        CorResp = "j"
    elif target == "yellow":
        CorResp = "k"
    
    return CorResp

# order the task instruction
if participant%2 != 0:
    # Participants with an odd number get the typical instruction first
    which_type = ["Typical","Atypical"]
else:
    # participants with an even number get the atypical instruction first
    which_type = ["Atypical","Typical"]

# Initialize a clock to measure the RT
my_clock = core.Clock()

# display the welcome message
message(message_text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# display the Stroop stimuli
# in two blocks
for b in range(nblocks):
    
    # reset the Instructions
    InstrType = "None"
    
    # deduce the task instruction
    InstrType = which_type[b]
    
    # display the instructions
    if InstrType == "Typical":
        Instructions_text = Typical
    elif InstrType == "Atypical":
        Instructions_text = Atypical
    message(message_text = Instructions_text, response_key = "space", height = 0.05)
    
    # announce that the practice phase is about to start
    message(message_text = "You'll first perform some practice trials.\n\nPress the space bar to start.", response_key = "space")
    
    # in 3 practice trials
    for i in range(b*nprac,(b+1)*nprac):
        
        # set the color word and the font color for this trial
        Stroop_stim.text    = practice[i,0]
        Stroop_stim.color   = practice[i,1]
        
        # deduce the correct answer for these task instructions
        if InstrType == "Typical":
            # typical Stroop instructions: FontColor
            practice[i,3] = determine_CorResp(practice[i,1])
        elif InstrType == "Atypical":
            # atypical Stroop instructions: ColorWord
            practice[i,3] = determine_CorResp(practice[i,0])
        
        keys, RT = perform_trial()
        
        # escape from the trial loop
        if keys[0] == "escape":
            break
        
        # check whether a response has been given
        if keys[0] != 0:
            
            # Store the RT and response information
            practice[i,4] = keys[0]
            practice[i,5] = int(practice[i,3] == practice[i,4])
            practice[i,6] = RT
            
            # determine and display the feedback message
            feedback(correct = int(practice[i,5]))
            
        else:
            
            # if no response has been given, encourage the participant to go faster
            message(message_text = "Too slow! Try to respond faster.", duration = 0.25)
    
    # announce that the actual block is about to start
    message(message_text = "That was the practice round.\n\nPress the space bar to start block " + str(b+1) + ".", response_key = "space")
    
    # in 16 trials
    for i in range(b*ntrials,(b+1)*ntrials):
        
        # set the color word and the font color for this trial
        Stroop_stim.text    = trials[i,0]
        Stroop_stim.color   = trials[i,1]
        
        # deduce the correct answer for these task instructions
        if InstrType == "Typical":
            # typical Stroop instructions: FontColor
            trials[i,3] = determine_CorResp(trials[i,1])
        elif InstrType == "Atypical":
            # atypical Stroop instructions: ColorWord
            trials[i,3] = determine_CorResp(trials[i,0])
        
        keys, RT = perform_trial()
        
        # escape from the trial loop
        if keys[0] == "escape":
            break
        
        # check whether a response has been given
        if keys[0] != 0:
            
            # Store the RT and response information
            trials[i,4] = keys[0]
            trials[i,5] = int(trials[i,3] == trials[i,4])
            trials[i,6] = RT
            
            # determine and display the feedback message
            feedback(correct = int(trials[i,5]))
            
        else:
            
            # if no response has been given, encourage the participant to go faster
            message(message_text = "Too slow! Try to respond faster.", duration = 0.25)
    
    # escape from the block loop
    if keys[0] == "escape":
        break

# display the goodbye message
TheEndImage.draw()
message(message_text = "Goodbye!", duration = 1, pos = (0,0.75), height = 0.2)

# close the experiment window
win.close()

print(practice)
print(trials)
