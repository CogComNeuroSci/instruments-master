# import modules
import time, numpy
from psychopy import visual

# make experiment window
win = visual.Window([900, 800], color = "grey")

# initialize participant number
participantnr = 1

# trials (only 16 needed)
Colorlist = ["red","red","red","red", "green","green","green","green","yellow","yellow","yellow","yellow","blue","blue","blue","blue","red","red","red","red", "green","green","green","green","yellow","yellow","yellow","yellow","blue","blue","blue","blue"]
Wordlist = ["red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue"]

# in kolommen zetten
Stroop_array = numpy.column_stack([Colorlist, Wordlist])
print(Stroop_array)

# initialize graphical elements
trial = visual.TextStim(win, text = "text", color = "red")
Correct = visual.TextStim(win, text="Goe gedaan manneke")
NotCorrect = visual.TextStim(win, text = "Dikste loser ooit")
block1 = visual.TextStim(win, text = "we beginnen aan block 1")
block2 = visual.TextStim(win, text = "we beginnen aan block 2")

# welkom
welcome = visual.TextStim(win, text = "Welcome to the experiment")
welcome.draw()
win.flip()
time.sleep(2)

# instructie
if participantnr%2 == 0:
    instruction = visual.TextStim(win, text = "Respond to the color, not the meaning of the word")
else:
    instruction = visual.TextStim(win, text = "Respond to the word, not the meaning of the color")
instruction.draw()
win.flip()
time.sleep(2)

# loop over all the trials
for i in range(trials.shape[0]):
    
    # show the block number at the start of the block
    if i == 0:
        block1.draw()
        win.flip()
        time.sleep(1)
    if i == 17:
        block2.draw()
        win.flip()
        time.sleep(1)
    
    # show the stroop stimulus
    trial.setColor(Stroop_array[i][0])
    trial.setText(Stroop_array[i][1])
    trial.draw()
    win.flip()
    time.sleep(1)
    
    # provide feedback
    if participantnr%2 == 0:
        if Stroop_array[i][0] == "red":
            Correct.draw()
        else:
            NotCorrect.draw()
    else:
        if Stroop_array[i][1] == "red":
            Correct.draw()
        else:
            NotCorrect.draw()
    win.flip()
    time.sleep(1)

#DAG
goodbye = visual.TextStim(win, text = "Salu en de kost")
goodbye.draw()
win.flip()
time.sleep(2)

# end the experiment
win.close()