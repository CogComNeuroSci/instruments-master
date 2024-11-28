"""
solution for Test 2: create a random dot color task
On each trial, participants decided whether a field contained more (static) blue or green dots. 
The total number of dots is always 80, with differing proportions of green or blue dots depending on the difficulty condition. 
The position of dots is randomly generated on each trial.
"""

# Importing modules
## random module for random sampling, time module for timing the updating of the display, numpy for creating numpy arrays
## and the visual module for drawing stimuli on the screen.
import random, time, numpy
from psychopy import visual

# Display preparation
## Initialize the screen to display the stimuli on.
win = visual.Window(fullscr = True, units = "norm")

# Initialize variables
## These arethe variables that stay the same across the entire assignment.
radius =  2 * 1/100 #1% of the screen's height
field_size = 1 * 50/100 #50% of the screen
fields_edges = (- field_size, field_size) 
number_of_dots = 80
portion_maj = [0.7, 0.6, 0.55] #portion of the majority color
colors = ["green", "blue"]

nr_trials = 5
nr_blocks = len(portion_maj) 
tot_trials = nr_trials*nr_blocks
duration = 1

###
#create the trial matrix
###
MajColor    = numpy.array([random.choice(colors) for i in range(tot_trials)])
MinColor    = MajColor.copy()
MinColor[MinColor == colors[0]] = "temp" #temporary chance this to temp, such that we can change all other colors first
MinColor[MinColor == colors[1] ] = colors[0]
MinColor[MinColor == "temp"] = colors[1]
PortionMaj  = numpy.array([[portion_maj[i] for j in range(nr_trials)] for i in range(nr_blocks)]).flatten()
CorResp     = MajColor.copy() #MajColor tells us which color is the correct answer
CorResp[CorResp == colors[0]] = "f" #the correct response is key 'f' if the correct response is the first color
CorResp[CorResp == colors[1]] = "j" #the correct response is key 'j' if the correct response is the second color

# combine arrays in trial matrix
Accuracy = numpy.repeat(-99.9, len(CorResp)) #to allow for space to save if the participant is correct, add already a column, fill it up later
trials = numpy.column_stack([MajColor, MinColor, PortionMaj, CorResp, Accuracy]) #warning! All becomes a string
print(trials)


# Initialize the graphical elements
Welcome         = visual.TextStim(win, text = "Welcome!", color = "black")
Instructions    = visual.TextStim(win, text = f"In this experiment you will see multiple dots in {colors[0]} and {colors[1]}.\n" +
                                                "You have to respond which color most dots are in." +
                                                f"If the majority color is {colors[0]}, press “f”.\n" +
                                                f"If it’s {colors[1]}, press “j”.\n" +
                                                "Answer as quickly as possible, but also try to avoid mistakes.\n", height = 0.05, color = "black")
Block_stim      = visual.TextStim(win, text = "", color = "black")
Feedback_stim   = visual.TextStim(win, text = "", color = "black") 
Goodbye         = visual.TextStim(win, text = "Goodbye!", color = "black")

fixation        = visual.TextStim(win, text = "+", height = field_size/2, color = "black")
dot             = visual.Circle(win, radius = radius)

# display the welcome message
Welcome.draw()
win.flip()
time.sleep(duration)

# display the instructions
Instructions.draw()
win.flip()
time.sleep(duration)

for j in range(nr_blocks):
    #Add a message at the start of each block, announcing the block that is about to start
    Block_stim.text     = f"Block {j+1} out of {nr_blocks} will start now"
    Block_stim.draw()
    win.flip()
    time.sleep(duration)
    
    for i in range(nr_trials):
        trial_nr = j*nr_trials + i #keep track of where we are in the trial matrix
                
        fixation.draw()
        win.flip()
        time.sleep(duration)
        
        ##we create a for loop to edit the color and position of each dot before drawing it
        for dot_i in range(number_of_dots):
            if (dot_i < float(trials[trial_nr, 2]) * number_of_dots): #the first dots are in the majority color
                dot.fillColor = trials[trial_nr, 0]
                
            else: #the other dots are in the minority color
                dot.fillColor = trials[trial_nr, 1] #the other color than the majority color
            
            #we randomly sample the position of the dot. We sample within the bounds of the invisible grid.
            dot.pos = (random.uniform(fields_edges[0], fields_edges[1]),  random.uniform(fields_edges[0], fields_edges[1]))
            dot.draw() #this dot is drawn before we edit and draw the other one
        
        win.flip() #we only flip the screen once all the dots are edited and drawn!
        time.sleep(duration)
        
        #assume they answered f, meaning they think the majority color is green (the first color)
        answer = "f"
        if answer == trials[trial_nr, 3]:
            Feedback_stim.text = "Correct"
            trials[trial_nr, 4] = True #save accuracy
        else:
            Feedback_stim.text = "False"
            trials[trial_nr, 4] = False #save accuracy
            
        Feedback_stim.draw()
        win.flip()
        time.sleep(duration)
            
# display the goodbye message
Goodbye.draw()
win.flip()
time.sleep(duration)

win.close()
print(trials)