# displaying Stroop stimuli

# import modules
from psychopy import visual
import time, numpy

# initialize the window
win = visual.Window(fullscr = True, units = "norm")

# initialize the variables
duration = 1

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

# deduce the correct response
CorResp = numpy.copy(FontColor)
CorResp[CorResp == "red"]     = "d"
CorResp[CorResp == "blue"]    = "f"
CorResp[CorResp == "green"]   = "j"
CorResp[CorResp == "yellow"]  = "k"

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp])
print(trials)

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome!")
Instructions    = visual.TextStim(win, text = "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
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
                                                "Any questions?", height = 0.05)
Stroop_stim     = visual.TextStim(win, text = "red", color = "blue")
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)
TheEndImage     = visual.ImageStim(win, image = "the_end.jpg")

# display the welcome message
Welcome.draw()
win.flip()
time.sleep(1)

# display the instructions
Instructions.draw()
win.flip()
time.sleep(1)

# display the Stroop stimulus
Stroop_stim.text    = trials[0,0]
Stroop_stim.color   = trials[0,1]
Stroop_stim.draw()
win.flip()
time.sleep(duration)

# display the Stroop stimulus
Stroop_stim.text    = trials[8,0]
Stroop_stim.color   = trials[8,1]
Stroop_stim.draw()
win.flip()
time.sleep(duration)

# display the Stroop stimulus
Stroop_stim.text    = trials[15,0]
Stroop_stim.color   = trials[15,1]
Stroop_stim.draw()
win.flip()
time.sleep(duration)

# display the goodbye message
TheEndImage.draw()
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()