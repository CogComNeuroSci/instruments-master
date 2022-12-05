#Loading in modules
from psychopy import visual, core
import numpy as np

#participant variables
participant_number = 10
participant_name = "Fien Goetmaeckers"
participant_title = "Mrs"

#Design variables
Nblocktrials = 8
Nblocks = 2

#Making window
win = visual.Window([500, 500], color = (1,1,-1), units ='norm')

#Making welcome message
lastname = participant_name.split()[1]
welcometext = "Welcome {0} {1}!".format(participant_title, lastname)
welcome = visual.TextStim(win, text = welcometext, color = (-1,-1, -1))

#Making instructions
Instrtxt1 = "A colored shape will appear which increases in size.\n\n Your task is to indicate the shape of the target.\n\n If it's a circle press F,\n if it's a square press J."
Instrtxt2 = "A colored shape will appear which increases in size.\n\n Your task is to indicate the color of the target.\n\n If it's red press F,\n if it's green press J."
Instructions = visual.TextStim(win, text = "", alignText = 'center', color = (-1,-1, -1))
#Counterbalancing order
if participant_number%2:
    Instrtxt = [Instrtxt2, Instrtxt1]
else:
    Instrtxt = [Instrtxt1, Instrtxt2]    

#Final message
Thankmsg = visual.TextStim(win, text = "Thank you for participating", color = (-1,-1, -1))

#4 stimuli
Circle_red = visual.Circle(win, size = .1, fillColor = (1, -1, -1))
Square_red = visual.rect.Rect(win, size = .1, fillColor = (1, -1, -1))

Circle_green = visual.Circle(win, size = .1, fillColor = (-1, 1, -1))
Square_green = visual.rect.Rect(win, size = .1, fillColor = (-1, 1, -1))

#Feedback stimulus
Feedback = visual.TextStim(win, text = "Too late!", color = (-1,-1, -1))

#Gather all design variables in list
sizes = 2*np.arange(.005, .21, .015)
stimuli = [Circle_red, Square_red, Circle_green, Square_green]
all_stimuli = np.tile(stimuli, int(Nblocktrials/len(stimuli)))

#Display welcome message
welcome.draw()
win.flip()
core.wait(5)

#block loop
for b in range(Nblocks):
    #Display instructions depending on block
    Instructions.text = Instrtxt[b%2]
    Instructions.draw()
    win.flip()
    core.wait(5)
    #trial loop
    for t in range(Nblocktrials):
        #stimulus loop
        for s in sizes:
            #Select stimuli from list (all_stimuli), adjust it's size and draw it on the screen
            all_stimuli[t].size = s
            all_stimuli[t].draw()
            win.flip()
            core.wait(.2)

        #Blank screen
        win.flip()
        core.wait(.5)
        
        #Adjust feedback position depending on trial
        if t%2:
            Feedback.pos = (0,-.5)
        else:
            Feedback.pos = (0,.5)
            
        #Display feedback
        Feedback.draw()
        win.flip()
        core.wait(.5)

#Display thank you message
Thankmsg.draw()
win.flip()
core.wait(5)

#Close window
win.close()
