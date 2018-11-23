# displaying Stroop stimuli

# import modules
from psychopy import visual
import time, numpy

# initialize the window
win = visual.Window(size = (800,600), units = "norm")

# initialize the variables
duration = 1

# define stroop stimulus 
ColorWord = numpy.array(["red","red","red","red","blue","blue","blue","blue","green","green","green","green","yellow","yellow","yellow","yellow"])
FontColor = numpy.array(["red","blue","green","yellow","red","blue","green","yellow","red","blue","green","yellow","red","blue","green","yellow"])
Stimulus = numpy.column_stack([ColorWord, FontColor])

# deduce the congruence
## incongruent = index 0, congruent = index 1
CongruenceLevels = numpy.array(["Incongruent", "Congruent"]) 
CongruenceBoolean = numpy.array(ColorWord == FontColor)
## af en toe eens printen als je niet weet wat er gebeurt dus print(CongruenceBoolean)
## door * 1 te doen maakt hij van True = 1(congruent) False = 0 (incongruent)
Congruence = CongruenceLevels[[CongruenceBoolean *1]]

# define feedback
Feedback_correct_stim = visual.TextStim(win, text = "Correct")
Feedback_wrong_stim = visual.TextStim(win, text = "Wrong answer!")

# define block 1 and block 2
Block_1 = visual.TextStim(win, text = "Block 1 will start now")
Block_2 = visual.TextStim(win, text = "Block 2 will start now")


# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome!")
for participant_number in range(11):
    if participant_number % 2 == 0:
        Instructions    = visual.TextStim(win, text = "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
                                                "presented in a random ink color (red, blue, green and yellow color).\n\n" +
                                                "You have to respond to the meaning of the written word  and\n" +
                                                "ignore ink color of the stimulus.\n\n" +
                                                "You can use the following four response buttons (from left to right;\n" +
                                                "use the index and middle finger of your left and right hand):" +
                                                "“d”,“f”,“j” and “k”.\n\n" +
                                                "If the meaning of the word is red, press the leftmost button “d”.\n" +
                                                "If it’s blue, press “f”.\n" +
                                                "If it’s green, press “j”.\n" +
                                                "If it’s yellow, press “k”.\n\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                                "By all means ignore the ink color of the words, you should only respond to the meaning of the word.\n\n" +
                                                "Any questions?", height = 0.05)
    else:
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

Goodbye= visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)



# display the welcome message
Welcome.draw()
win.flip()
time.sleep(1)

# display the instructions
Instructions.draw()
win.flip()
time.sleep(2)

# display message block - stroop stimuli - feedback 
for x in range(2):
    if x == 0:
        Block_1.draw()
    else:
        Block_2.draw()
    win.flip()
    time.sleep(1)
    for i in range(len(ColorWord)):
        Stroop_stim =  visual.TextStim(win, text = ColorWord[i], color = FontColor[i])
        Stroop_stim.draw()
        win.flip()
        time.sleep(0.5)
        if participant_number % 2 == 0:
            if ColorWord[i] == "red":
                Feedback_correct_stim.draw()
            else:
                Feedback_wrong_stim.draw()
        else:
            if FontColor[i] == "red":
                Feedback_correct_stim.draw()
            else:
                Feedback_wrong_stim.draw()
        win.flip()
        time.sleep(0.5)
    


# display the goodbye message
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()
