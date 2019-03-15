# import modules
from psychopy import visual, event, core, gui, data
import os, platform, math, numpy

# set the directory
my_directory = os.getcwd()

# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height], units = "norm")

# Initializing
info     = {"Participant number": 0, "Name": "unknown", "Age" :0, "Gender":["male", "female", "Other"], "Handedness": ["Left", "Right", "ambidexter"] }

# Esther: je bent hier nog niet klaar om naam en nummer van de proefpersoon vast te leggen want de gui is nog niet verschenen

p_number = info["Participant number"]
p_name   = info["Name"]
my_clock = core.Clock()
n_blocks = 12
n_trials = 6
text_width  = 0.9

# Initializing the arrow and making a facorial design
orientation_options = numpy.array(["<", ">"])
Norientation        = len(orientation_options)
position_options    = numpy.array([-0.75, 0, 0.75])
Nposition           = len(position_options)
arrow_orientation   = numpy.repeat(orientation_options, Nposition)
arrow_position      = numpy.tile(position_options, Norientation)

# Turning this factorial design in a trial matrix
trial_matrix = numpy.column_stack([arrow_orientation, arrow_position])
trials       = len(trial_matrix)
print(trial_matrix)

# data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    file_name = my_directory + "/data" + "/Test4_subject_" + str(info["Participant number"])
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This name was already used. Please ask the experimenter to help you to enter a unique name.")
        myDlg2.show()
print("OK, let's get started!")

## Esther: pas op, je slaat hier de naam van de proefpersoon mee op in de output file

thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

## Esther: pas op, p_name bevat nog niet de naam van je proefpersoon

# graphical elements
stimulus        = visual.TextStim(win,text="")
blockstart      = visual.TextStim(win,text="",wrapWidth = win_width*text_width)
welcome         = visual.TextStim(win,text=(    "Hello {},\n"+
                                                "Welcome to this experiment!\n"+
                                                "Push the space bar to proceed.").format(p_name),
                                    wrapWidth = win_width*text_width)
instruct        = visual.TextStim(win,text=(    "In block 1-8 you will respond to the orientation of the arrow\n"+
                                                "In block 8-12 you will respond to the position of the arrow\n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)

def announce_blockstart():
    if block <= 8:
        blockstart.text = ("Welcome to block {}!\n\n"+
                           "Respond to the orientation of the arrow.\n\n" + 
                           "If < push 'left'. \n\n" +
                           "If > push 'right'. \n\n" +
                           "Push the space bar to start.").format(block)
    else:
        blockstart.text = ( "Welcome to block {}!\n\n"+
                           "Respond to the position of the arrow.\n\n" + 
                           "If the arrow is on the left side of your screen, push 'left'. \n\n" +
                           "If the arrow is on the right side your screen, push 'right'. \n\n" +
                           "If the arrow is in the middle of your screen, push 'down'. \n\n" +
                            "Push the space bar to start.").format(block)
    blockstart.draw()
    win.flip()
    event.waitKeys(keyList = "space")

def randomize():
    Design = data.createFactorialTrialList({"arrow_orientation": orientation_options, "arrow_position": position_options})

    # create the trials
    if block <= 8:
        trials = data.TrialHandler(trialList = Design, nReps = 10, method = "random")
    else:
        trials = data.TrialHandler(trialList = Design, nReps = 10 , method = "random")
        thisExp.addLoop(trials)
    
    # Esther: pas op, hierboven staat addLoop enkel in de else statement, dus je zal enkel de data opslaan voor de laatste blokken
    # Esther: er is trouwens geen reden om de trialhandler in een if-statement te steken, het is twee keer hetzelfde
    # Esther: fullRandom was ook beter geweest dan random
    
    return trials

# welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

instruct.draw()
win.flip()
event.waitKeys(keyList = "space")

# start of the block loop
block = 0
while block < (n_blocks + 1):
    
    # announce the block start
    announce_blockstart()
    
    # randomization
    trials = randomize()
    
    # start of the trial loop
    for trial in range(n_trials):
        
        # Esther: hier maak je geen gebruik van de trialHandlers waarde gegevens in een random volgorde van 60 trials staan
        
        ## display the stimulus
        stimulus.text = arrow_orientation[trial]
        stimulus.pos  = (arrow_position[trial],0)
        stimulus.draw()
        win.flip()
        
        ## wait for the response
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["left","right", "down", "escape"])
        RT   = my_clock.getTime()
        resp = keys[0]
        
        #escape from the loop
        if keys[0] == 'escape':
            break
        
    # end of the trial loop
    
    # update the block number
    block += 1


# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()