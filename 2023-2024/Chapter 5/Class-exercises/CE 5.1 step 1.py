# displaying Stroop stimuli

# import modules
from psychopy import visual, event
import time, numpy

# initialize the window
win = visual.Window(fullscr = True, units = "norm")

# initialize the variables
nblocks     = 2
ntrials     = 16
participant = 2

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
Congruence = numpy.repeat('Incongruent', len(ColorWord))
Congruence[ColorWord == FontColor] = 'Congruent'

#Alternative:
#CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
#CongruenceBoolean   = numpy.array(ColorWord == FontColor)
#Congruence          = CongruenceLevels[CongruenceBoolean*1]

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

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp, Accuracy])

# repeat the trial matrix for the two blocks
trials = numpy.tile(trials, (nblocks, 1))

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome!\n\nPress the space bar to continue.")
Instructions    = visual.TextStim(win, text = "OK", height = 0.05)
Block_start     = visual.TextStim(win, text = "OK")
Stroop_stim     = visual.TextStim(win, text = "red", color = "blue")
Feedback        = visual.TextStim(win, text = "OK")
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)
TheEndImage     = visual.ImageStim(win, image = "the_end.jpg")

# deduce the task instruction
if participant%2 == 0:
    # participants with an even number have to respond to the color word
    Instructions.text = (   "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
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
    Instructions.text = (   "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
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

# display the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the instructions
Instructions.draw()
win.flip()
event.waitKeys(keyList = "space")

# display the Stroop stimuli
# in two blocks
for b in range(nblocks):
    
    # announce what block is about to start
    Block_start.text = "Block " + str(b+1) + " will start when you press the space bar."
    Block_start.draw()
    win.flip()
    event.waitKeys(keyList = "space")
    
    # in 16 trials
    for i in range(b*ntrials,(b+1)*ntrials):
        
        # set the color word and the font color for this trial
        Stroop_stim.text    = trials[i,0]
        Stroop_stim.color   = trials[i,1]
        
        # draw the stimulus on the back buffer
        Stroop_stim.draw()
        
        # clear the keyboard input
        event.clearEvents(eventType = "keyboard") #This is optional for event.WaitKeys()
        
        # display the stimulus on the screen
        win.flip()
        
        # Wait for the response
        keys = event.waitKeys(keyList = ["d","f","j","k"])
        
        # determine accuracy
        trials[i,4] = int(trials[i,3] == keys[0])
        
        # determine the feedback message
        if int(trials[i,4]) == 1:
            Feedback.text = "Correct!"
        else:
            Feedback.text = "Wrong answer!"
        
        # display the feedback message
        Feedback.draw()
        win.flip()
        time.sleep(0.25)

# display the goodbye message
TheEndImage.draw()
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()

print(trials)
