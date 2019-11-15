# Importing modules
import time
from psychopy import visual

# Display preparation
win = visual.Window(size = [800, 800], color = (-1,-1,-1), units = "norm")

# Prepare the graphical elements
message = visual.TextStim(win, text = "test")
    
# Display the welcome message
message.text = "Welcome!"
message.draw()
win.flip()
time.sleep(1)

# Display the goodbye message
message.text = "The end!"
message.draw()
win.flip()
time.sleep(1)

# Close the experiment window
win.close()
