# displaying Stroop stimuli

# Fixation cross is added before the target is presented (step 1)

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
ntrials     = 16
participant = info["Participant number"]

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

# deduce the task instruction
if participant%2 == 0:
    # participants with an even number have to respond to the color word
    CorResp = numpy.copy(ColorWord)
else:
    # participants with an odd number have to respond to the ink color
    CorResp = numpy.copy(FontColor)

# deduce the correct response
CorResp[CorResp == "red"]     = "d"
CorResp[CorResp == "blue"]    = "f"
CorResp[CorResp == "green"]   = "j"
CorResp[CorResp == "yellow"]  = "k"

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

# initialize graphical elements
MessageOnSCreen = visual.TextStim(win, text = "OK")
Stroop_stim     = visual.TextStim(win, text = "red", color = "blue")
TheEndImage     = visual.ImageStim(win, image = "the_end.jpg")

# make a function for presenting messages on screen
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

# deduce the task instruction
if participant%2 == 0:
    # participants with an even number have to respond to the color word
    Instructions_text = (   "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
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
else:
    # participants with an odd number have to respond to the ink color
    Instructions_text = (   "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
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

# Initialize a clock to measure the RT
my_clock = core.Clock()

# display the welcome message
message(message_text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# display the instructions
message(message_text = Instructions_text, response_key = "space", height = 0.05)

# display the Stroop stimuli
# in two blocks
for b in range(nblocks):
    
    # announce what block is about to start
    message(message_text = "Block " + str(b+1) + " will start when you press the space bar.", response_key = "space")
    
    # in 16 trials
    for i in range(b*ntrials,(b+1)*ntrials):
        
        # set the color word and the font color for this trial
        Stroop_stim.text    = trials[i,0]
        Stroop_stim.color   = trials[i,1]
        
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
        keys = event.waitKeys(keyList = ["d","f","j","k","escape"])
        
        # Register the RT
        RT = my_clock.getTime()
        
        # escape from the trial loop
        if keys[0] == "escape":
            break
        
        # Store the response information
        trials[i,4] = keys[0]
        
        # determine accuracy
        trials[i,5] = int(trials[i,3] == trials[i,4])
        
        # Store the RT
        trials[i,6] = RT
        
        # determine the feedback message
        if int(trials[i,5]) == 1:
            message(message_text = "Correct!", duration = 0.25)
        else:
            message(message_text = "Wrong answer!", duration = 0.25)
    
    # escape from the block loop
    if keys[0] == "escape":
        break

# display the goodbye message
TheEndImage.draw()
message(message_text = "Goodbye!", duration = 1, pos = (0,0.75), height = 0.2)

# close the experiment window
win.close()

print(trials)
