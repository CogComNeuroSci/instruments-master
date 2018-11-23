import time
from psychopy import visual
import numpy
win = visual.Window([900, 800], color = "grey")
participantnr = 1
#welkom
welcome = visual.TextStim(win, text = "Welcome to the experiment")
welcome.draw()
win.flip()
time.sleep(2)


#instructie
if participantnr%2 ==0:
    instruction = visual.TextStim(win, text = "Respond to the color, not the meaning of the word")
    instruction.draw()
    win.flip()
    time.sleep(2)
else:
    instruction = visual.TextStim(win, text = "Respond to the word, not the meaning of the color")
    instruction.draw()
    win.flip()
    time.sleep(2)

#trials
Colorlist = ["red","red","red","red", "green","green","green","green","yellow","yellow","yellow","yellow","blue","blue","blue","blue","red","red","red","red", "green","green","green","green","yellow","yellow","yellow","yellow","blue","blue","blue","blue"]
Wordlist = ["red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue","red", "green", "yellow", "blue"]
trial = visual.TextStim(win, text = "text", color = "red")

Correct = visual.TextStim(win, text="Goe gedaan manneke")
NotCorrect = visual.TextStim(win, text = "Dikste loser ooit")

#block aanduiding
block1 = visual.TextStim(win, text = "we beginnen aan block 1")
block2 = visual.TextStim(win, text = "we beginnen aan block 2")


#in kolommen zetten
Stroop_array = numpy.column_stack([Colorlist, Wordlist])
for i in range(0,33):
    if participantnr%2 == 0:
        if i in range(0,17):
            if i == 0:
                block1.draw()
                win.flip()
                time.sleep(1)
        
            trial.setColor(Stroop_array[i][0])
            trial.setText(Stroop_array[i][1])
            trial.draw()
            win.flip()
            time.sleep(1)
            if Stroop_array[i][0] == "red":
                Correct.draw()
            else:
                NotCorrect.draw()
    
        if i in range(17,33):
            if i == 17:
                block2.draw()
                win.flip()
                time.sleep(1)
            
            trial.setColor(Stroop_array[i][0])
            trial.setText(Stroop_array[i][1])
            trial.draw()
            win.flip()
            time.sleep(1)
            if Stroop_array[i][0] == "red":
                Correct.draw()
            else:
                NotCorrect.draw()
    else:
        if i in range(0,17):
            if i == 0:
                block1.draw()
                win.flip()
                time.sleep(1)
        
            trial.setColor(Stroop_array[i][0])
            trial.setText(Stroop_array[i][1])
            trial.draw()
            win.flip()
            time.sleep(1)
            if Stroop_array[i][1] == "red":
                Correct.draw()
            else:
                NotCorrect.draw()
    
        if i in range(17,33):
            if i == 17:
                block2.draw()
                win.flip()
                time.sleep(1)
            
            trial.setColor(Stroop_array[i][0])
            trial.setText(Stroop_array[i][1])
            trial.draw()
            win.flip()
            time.sleep(1)
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
win.close()