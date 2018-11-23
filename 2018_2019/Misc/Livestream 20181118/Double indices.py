import numpy, time
from psychopy import visual

win = visual.Window(size = [600,500])

trials = numpy.column_stack([[  "red", "blue", "green", "yellow",
                                "red", "blue", "green", "yellow",
                                "red", "blue", "green", "yellow",
                                "red", "blue", "green", "yellow" ], 
                            [   "red", "red", "red", "red",
                                "blue", "blue", "blue", "blue",
                                "green", "green", "green", "green",
                                "yellow", "yellow", "yellow", "yellow"]])

for i, j in trials: 
    print(i)
    print(j)
    Stroop_stim1 = visual.TextStim(win, text = j, color = i)
    Stroop_stim1.draw()
    win.flip()
    time.sleep(0.5)