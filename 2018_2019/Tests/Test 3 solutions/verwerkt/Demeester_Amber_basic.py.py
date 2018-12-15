# Test instrumenten - Amber Demeester
# Importing everything we need 
from psychopy import visual, event, core, gui
import time, numpy

#Create a dialog box
info = {"Participant number":0, "Participant name":"Unknown", "Gender":["male","female","other"], "Age": 0, "Hand preference": ["right", "left", "ambidexter"]}
infoDlg = gui.DlgFromDict(dictionary=info, title="Oriëntatie Gabor stimulus")

#intitialize the window
win = visual.Window([600,500], units = "norm")

# add the participant info
Subject = info["Participant number"]
Gender  = info["Gender"]
Age     = info["Age"]


# initialize graphical elements
welcome = visual.TextStim(win, text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.")
instructions = visual.TextStim(win, text = "In this experiment you'll see a Gabor stimulus a number of times.\nWe want you to press the F-key when the Gabor stimulus is turned to the left. When the Gabor stimulus is turned to the right, we want you to press the J-key \n\nPress Space to continue" ) 
Block_start     = visual.TextStim(win, text = "OK")
gabor1 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = -3, name='gabor1')
gabor2 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 3, name='gabor2')
gabor3 = visual.GratingStim(win, tex="sin", mask="gauss", texRes=256, 
           size=[1.0, 1.0], sf=[4, 0], ori = 0, name='gabor3')
Feedback = visual.TextStim(win, text= "OK")
goodbye_message = visual.TextStim(win, text = "Thank you for participating! \nPress Space to leave the experiment.")

# Initialize a clock to measure the RT
my_clock = core.Clock()

#drawing
welcome.draw()
win.flip()
event.waitKeys(keyList = ["space"])


instructions.draw()
win.flip()
event.waitKeys(keyList = ["space"])


#first block
Block_start.text = "The first bock will start \nPress Space to continue"
Block_start.draw()
win.flip()
event.waitKeys(keyList = ["space"])

for i in range(4): #We'll use a loop so we don't have to copy-paste this 4 times

    gabor3.draw()
    win.flip()
    core.wait(1)
    gabor1.draw()
    win.flip()
    # clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    core.wait(0.16)
    gabor3.draw()
    core.wait(1)
    event.waitKeys(keyList = ["j","f"])
    # Register the RT
    RT = my_clock.getTime()
    # determine the feedback message
    if event.getKeys() == "f":
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Wrong answer!"
        
    # display the feedback message
    Feedback.draw()
    win.flip()
    time.sleep(0.25)
    
    
    gabor3.draw()
    win.flip()
    core.wait(1)
    gabor2.draw()
    win.flip()
    # clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    core.wait(0.16)
    gabor3.draw()
    core.wait(1)
    event.waitKeys(keyList = ["j","f"])
    # Register the RT
    RT = my_clock.getTime()
    # determine the feedback message
    if event.getKeys() == "j":
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Wrong answer!"
    # display the feedback message
    Feedback.draw()
    win.flip()
    time.sleep(0.25)
    
    if keys[0] == "escape":
        break

#second block
Block_start.text = "The second bock will start \nPress Space to continue"
Block_start.draw()
win.flip()
event.waitKeys(keyList = ["space"])

for i in range(4): # we'll use a forloop so that we don't have to copy-paste this 4 times

    gabor3.draw()
    win.flip()
    core.wait(1)
    gabor1.draw()
    win.flip()
    # clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    core.wait(0.33)
    gabor3.draw()
    core.wait(1)
    event.waitKeys(keyList = ["j","f"])
    # Register the RT
    RT = my_clock.getTime()
    # determine the feedback message
    if event.getKeys() == "f":
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Wrong answer!"
    # display the feedback message
    Feedback.draw()
    win.flip()
    time.sleep(0.25)

    gabor3.draw()
    win.flip()
    core.wait(1)
    gabor2.draw()
    win.flip()
    # clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    core.wait(0.33)
    gabor3.draw()
    core.wait(1)
    event.waitKeys(keyList = ["j","f"])
    # Register the RT
    RT = my_clock.getTime()
    # determine the feedback message
    if evenet.getKeys() == "j":
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Wrong answer!"
    # display the feedback message
    Feedback.draw()
    win.flip()
    time.sleep(0.25)
    
    if keys[0] == "escape":
        break

#the thrid block
Block_start.text = "The third bock will start \nPress Space to continue"
Block_start.draw()
win.flip()
event.waitKeys(keyList = ["space"])

for i in range(4):   #we'll use a loop so that we don't have to copy-paste this 4 times
    gabor3.draw()
    win.flip()
    core.wait(1)
    gabor1.draw()
    win.flip()
    # clear the keyboard input
    event.clearEvents(eventType = "keyboard")
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    core.wait(0.50)
    gabor3.draw()
    core.wait(1)
    event.waitKeys(keyList = ["j","f"])
    # Register the RT
    RT = my_clock.getTime()
    # determine the feedback message
    if event.getKeys() == "f":
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Wrong answer!"
    # display the feedback message
    Feedback.draw()
    win.flip()
    time.sleep(0.25)

    gabor3.draw()
    win.flip()
    core.wait(1)
    gabor2.draw()
    win.flip()
    # clear the keyboard input
    jevent.clearEvents(eventType = "keyboard")
    # Now that the stimulus is on the screen, reset the clock
    my_clock.reset()
    core.wait(0.50)
    gabor3.draw()
    core.wait(1)
    event.waitKeys(keyList = ["j","f"])
    # Register the RT
    RT = my_clock.getTime()
    # determine the feedback message
    if event.getKeys[0] == "j":
        Feedback.text = "Correct!"
    else:
        Feedback.text = "Wrong answer!"
    # display the feedback message
    Feedback.draw()
    win.flip()
    time.sleep(0.25)
    
    if keys[0] == "escape":
        break

#Goodbye
goodbye_message.draw()
event.waitKeys(keyList = ["space"])

win.close()