# displaying Stroop stimuli

# import modules
from psychopy import visual
import time, numpy

# initialize the window
win = visual.Window(size = (800,400), units = "norm")

# initialize the variables
duration = 0.5

# we start with adding the values for the words and the colors
ColorWord   = numpy.array([ "red", "red", "red", "red",
                            "blue", "blue", "blue", "blue",
                            "green", "green", "green", "green",
                            "yellow", "yellow", "yellow", "yellow"])
FontColor   = numpy.array([ "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow"])

Stimulus = numpy.column_stack([ColorWord, FontColor])

student_nr = 1
response='d'

# deduce the congruence
CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
    ##array aanmaken met 2 waarden (congruent en incongruent)
    ##0 is False en incongruent staat op 0e plaats
CongruenceBoolean   = numpy.array(ColorWord == FontColor)
    ##bij moeiljke code eerst printen
        ##print (ColorWord == FontColor)
    ##snel in comment zetten met ctrl+'
    ##(CongruenceLevels[ColorWord==FontColor]) werkt niet om redenen
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]
    ## *1 om True en False om te zetten naar waarden van 1 en 0
    ##[]om plaats te geven van woord dat je nodig hebt

##geen for loop nodig
##


# deduce the correct response
    ##door dit stuk mag else display Stroop_stim weg
if student_nr%2==0:
    CorResp = numpy.copy(FontColor)
    ##CorResp = numpy.array(FontColor, copy = True)
    CorResp[CorResp == "red"]     = "d"
    CorResp[CorResp == "blue"]    = "f"
    CorResp[CorResp == "green"]   = "j"
    CorResp[CorResp == "yellow"]  = "k"
else:
    CorResp = numpy.copy(ColorWord)
    ##CorResp = numpy.array(FontColor, copy = True)
    CorResp[CorResp == "red"]     = "d"
    CorResp[CorResp == "blue"]    = "f"
    CorResp[CorResp == "green"]   = "j"
    CorResp[CorResp == "yellow"]  = "k"

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp])
    ##All of them must have the same first dimension
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

InstructionsOdd    = visual.TextStim(win, text = "In this experiment you will see color words (“red”, “blue”, “green” and “yellow”)\n" +
                                                "presented in a random ink color (red, blue, green and yellow color).\n\n" +
                                                "You have to respond to the meaning of the stimulus and\n" +
                                                "ignore the meaning of the written word.\n\n" +
                                                "You can use the following four response buttons (from left to right;\n" +
                                                "use the index and middle finger of your left and right hand):" +
                                                "“d”,“f”,“j” and “k”.\n\n" +
                                                "If the meaning is red, press the leftmost button “d”.\n" +
                                                "If it’s blue, press “f”.\n" +
                                                "If it’s green, press “j”.\n" +
                                                "If it’s yellow, press “k”.\n\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n" +
                                                "By all means ignore the meaning of the words, you should only respond to the ink color.\n\n" +
                                                "Any questions?", height = 0.05)


Stroop_stim     = visual.TextStim(win, text = "", color = 'red')
Goodbye         = visual.TextStim(win, text = "Goodbye!", pos = (0,0.75), height = 0.2)
TheEndImage     = visual.ImageStim(win, image = "the_end.jpg")
Cor             = visual.TextStim(win, text = 'Correct')
Incor           = visual.TextStim(win, text = 'Wrong answer!')
block           = visual.TextStim(win, text = '')
student         = visual.TextStim(win, text = '')

#display nummer
student.text =('Number is{}'.format(student_nr))
student.draw()
win.flip()
time.sleep(duration)


# display the welcome message
Welcome.draw()
win.flip()
time.sleep(1)

# display the instructions
if (student_nr % 2) ==0:
    Instructions.draw()
    win.flip()
    time.sleep(1)
else:
    InstructionsOdd.draw()
    win.flip()
    time.sleep(1)

# display the Stroop stimulus

#if (student_nr % 2) == 0:
for number in range(2):
    block.text= ('block{}'.format(number+1))
    block.draw()
    win.flip()
    time.sleep(duration)
    for i in range(len(ColorWord)):
        Stroop_stim.text=ColorWord[i]
        Stroop_stim.color=FontColor[i]
        ##kleine letter, met =, en geen ()
        Stroop_stim.draw()
        win.flip()
        time.sleep(duration)
        if response==CorResp[i]:        ##algemener dan die van bij else
            Cor.draw()
            win.flip()
            time.sleep(duration)
        else:
            Incor.draw()
            win.flip()
            time.sleep(duration)
#else:
#    for number in range(2):
#        block.text= ('block{}'.format(number+1))
#        block.draw()
#        win.flip()
#        time.sleep(duration)
#        for i in range(len(ColorWord)):
#            Stroop_stim.setText(ColorWord[i])
#            Stroop_stim.setColor(FontColor[i])
#                ##hoofdletter, zonder =, en wel ()
#            Stroop_stim.draw()
#            win.flip()
#            time.sleep(duration)
#            if ColorWord[i] == 'red':
#                Incor.draw()
#                win.flip()
#                time.sleep(duration)
#            else:
#                Cor.draw()
#                win.flip()
#                time.sleep(duration)


# display the goodbye message
TheEndImage.draw()
Goodbye.draw()
win.flip()
time.sleep(1)

# close the experiment window
win.close()
