# displaying Stroop stimuli

# import modules
from psychopy import visual
import time

# initialize the window
win = visual.Window(fullscr = True, units = "norm")

# we start with adding the values for the words and the colors
ColorWord = [   "red", "red", "red", "red",
                "blue", "blue", "blue", "blue",
                "green", "green", "green", "green",
                "yellow", "yellow", "yellow", "yellow"]
FontColor = [   "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow"]

# Loop over the ColorWords and FontColors
for i in range(len(ColorWord)):
    Stroop_stim = visual.TextStim(win, text = ColorWord[i])
    Stroop_stim.draw()

for i in range(len(FontColor)):
    Stroop_stim = visual.TextStim(win, color = FontColor[i])
    Stroop_stim.draw()
    win.flip()
    time.sleep(0.5)

# close the experiment window
win.close()