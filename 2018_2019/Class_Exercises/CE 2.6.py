# displaying Stroop stimuli

# import modules
from psychopy import visual
import time, numpy

# initialize the window
win = visual.Window(fullscr = True, units = "norm")

# initialize the variables
duration = 1

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
Stroop_stim.draw()
win.flip()
time.sleep(1)

# display the goodbye message
TheEndImage.draw()
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()