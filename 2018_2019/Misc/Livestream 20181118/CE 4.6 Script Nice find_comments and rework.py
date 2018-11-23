# displaying Stroop stimuli

# import modules
from psychopy import visual
import time, numpy as np

# initialize the window
win = visual.Window(size = [600,400], units = "norm")

# participant
ppnumber = 3
ppnumbereven = (ppnumber%2 == 0)

# initialize the variables
duration = 1

# blokken
aantalblokken = 2

# variabelen experiment
fontcolor = np.array(["red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "red", "blue", "green", "yellow", "red", "blue", "green", "yellow"])
colorword = np.array(["red", "red", "red", "red", "blue", "blue", "blue", "blue", "green", "green", "green", "green", "yellow", "yellow", "yellow", "yellow"])

# bepaal congruence
congrlevels = np.array(["Incongruent", "Congruent"])
congrboolean = np.array(fontcolor == colorword)
congruency = congrlevels[[congrboolean*1]]

# bepaal correcte respons
if ppnumbereven:
    corresp = np.copy(colorword)
else:
    corresp = np.copy(fontcolor)
corresp[corresp == "red"]   = "d"
corresp[corresp == "blue"]  = "f"
corresp[corresp == "green"] = "j"
corresp[corresp == "yellow"]= "k"

# trialmatrix
trialmatrix = np.column_stack([colorword, fontcolor, corresp, congruency])
print(trialmatrix)

# initialize graphical elements
Welcome         = visual.TextStim(win, text = "Welcome!")
## Esther: I would either work with one instructions text and update the instructions in the if-statement below
## Esther: or I would put the two instructions below immediately in a if-statement so only one is made
Instructions1   = visual.TextStim(win, text = "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
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
Instructions2   = visual.TextStim(win, text = "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
                                                "presented in a random ink color (red, blue, green and yellow color).\n\n" +
                                                "You have to respond to the meaning of the stimulus and\n" +
                                                "ignore the ink color of the written word.\n\n" +
                                                "You can use the following four response buttons (from left to right;\n" +
                                                "use the index and middle finger of your left and right hand):" +
                                                "“d”,“f”,“j” and “k”.\n\n" +
                                                "If the meaningr is red, press the leftmost button “d”.\n" +
                                                "If it’s blue, press “f”.\n" +
                                                "If it’s green, press “j”.\n" +
                                                "If it’s yellow, press “k”.\n\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                                "By all means ignore the ink color of the words, you should only respond to the meaning.\n\n" +
                                                "Any questions?", height = 0.05)
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)
## Esther: what if I don't have this image? Don't forget everything needed to execute the script!
TheEndImage     = visual.ImageStim(win, image = "the_end.jpg")

# display the welcome message
Welcome.draw()
win.flip()
time.sleep(1)

# display the instructions
## Esther: see comment above
## Esther: plus move the .flip and .sleep out of the if-structure
if ppnumbereven:
    Instructions2.draw()
else:
    Instructions1.draw()
win.flip()
time.sleep(1)

# display the Stroop stimulus
for block in range(aantalblokken):
    
    # announce the block number
    Instrtext= visual.TextStim(win, text= "Block {0} will start now".format(block+1), color="white")
    Instrtext.draw()
    win.flip()
    time.sleep(1)
    
    # loop over the trials
    ## Esther: very nice find to loop over the trial matrix like this, I'm going to steal that idea!
    for trial in trialmatrix:
        
        # display the stroop stimulus
        Stroop_stim = visual.TextStim(win, text = trial[0], color = trial[1])
        Stroop_stim.draw()
        win.flip()
        time.sleep(1)
        
        # display the feedback
        if trial[2] == "d":
            ## Esther: why not rename this so we can get rid of the .draw too?
            #cortext= visual.TextStim(win, text = "Correct!", color = "white")
            feedback = visual.TextStim(win, text = "Correct!", color = "white")
        else:
            #wrongtext= visual.TextStim(win, text = "Wrong answer!", color = "white")
            feedback = visual.TextStim(win, text = "Wrong answer!", color = "white")
        feedback.draw()
        win.flip()
        time.sleep(0.5)

# display the goodbye message
TheEndImage.draw()
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()
