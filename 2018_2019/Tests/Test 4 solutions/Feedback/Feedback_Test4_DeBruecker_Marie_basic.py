import os
import numpy
from psychopy import gui, visual, core, data

# constants
# number of blocks
nBlocks = 12

# number of trials
nBlockTrials = 60


# make the design based on the core trial characteristics

pijltjes = ("<", ">")
RespOptions = ["<", ">"]

# Esther: het was niet de bedoeling om de proefpersonen te laten antwoorden met deze pijltjes < >, dit zijn de stimuli

PositionArrowOptions= ["stimulus", "stimulusleft", "stimulusright"]
DirectionArrowOptions = ["<", ">"]

# Esther: het was een heel goed idee om het factorieel design zo te maken, maar hierna gebruik je dit niet meer
trial_list = data.createFactorialTrialList({"PositionArrow": PositionArrowOptions, "DirectionArrow": DirectionArrowOptions})

# convert the list of dictionaries to a dataframe for inspection
dataFrame = pandas.DataFrame.from_dict(trial_list)

# we can also quickly convert the dataframe to a numpy array
array = dataFrame.values

# congruency
CongruencyLevels = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean = numpy.array([PositionArrow == DirectionArrow)
Congruence = CongruenceLevels [[CongruenceBoolean * 1]]

# Esther: pas op, je hebt hierboven een syntaxfout en er is geen rekening gehouden met de neutrale trials

## determine the number of levels for the factor
NPositionArrow = len(PositionArrowOptions)
NDirectionArrowOptions = len(DirectionArrowOptions)
Nunique = NPositionArrowOptions * NDirectionArrowOptions

## determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

# Esther: de arrays hieronder hebben allemaal een andere lengte, dus het is niet mogelijk om ze aan elkaar te zetten.
# Esther: je hebt het factorieel design ook al gemaakt, dus niet nodig om dit nog eens opnieuw te doen

## combine arrays in trial matrix
Design = numpy.column_stack([PositionArrow, DirectionArrow, UniqueTrials])


# make the design for one block

## number of design repetitions per block
nReps = int(nBlockTrials/Nunique)

## repeat the 4-by-4 design five times
blockTrials = numpy.tile(Design, (nReps, 1))


# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width,win_height], units = "norm")

# create a dialog box
info = {"What is your name?": "", "What is your participant number?": 0, "What is your age?": 0, "What is your gender?": ["male", "female", "neutral"], "What is your hand preference?": ["right", "left", "ambidexter"]}

# determine the current working directory
directory_to_write = os.getcwd()

# keep asking for a new number when the data file already exists
already_exists = True
while already_exists:
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Demo")
    name    = info["What is your name?"]
    number  = info["What is your participant number?"]
    age     = info["What is your age?"]
    gender  = info["What is your gender?"]
    handpreference = info["What is your hand preference?"]
    
    # Esther: die extra slash op het einde van de lijn hieronder is niet nodig
    
    directory_to_write_to = os.getcwd() + "/data/"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    # Esther: "/Test4_" + "_subject_" mochten meteen aan elkaar geschreven worden en de _data op het einde is overbodig
    file_name = directory_to_write_to + "/Test4_" + "_subject_" + str(info["Participant number"]) + "_data"
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

# Esther: Name zit niet in je dictionary, enkel info["What is your name?"]

# extract the name of the participant from the dialog box information
subject_name = info["Name"]

# remove the name of the participant from the dialog box information (anonimity!)
info.pop("Name")

# start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name!)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# graphical elements
# Esther: het is veel eenvoudiger om slechts één stimulus aan te maken en daar dan de positie en inhoud van aan te passen tijdens de trial loop

pijltjes = visual.TextStim (win, text="<", ">")     # Esther: wat was hier de bedoeling met de dubbele pijlen?

stimulus        = visual.TextStim(win,text="",  pos=(0.0, 0.0))
stimulusleft        = visual.TextStim(win,text="",  pos=(-0.5, 0.0))
stimulusright        = visual.TextStim(win,text="",  pos=(0.5, 0.0))

welcome = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to the experiment!\n"+
                                                "Push the space bar to proceed.").format(name)
                                                
instructionsdirection = visual.TextStim(win,text=("Push the left arrow on your keyboard if you see < or\n"+
                                                "Push the right arrow on your keyboard if you see > \n\n"+
                                                "Push the space bar to start the experiment.")
instructsposition = visual.TextStim(win,text=("Push the left arrow on your keyboard if "<" or ">" is on the left side of the screen or\n"+
                                                "Push the right arrow on your keyboard if "<" or ">" is on the right side of the screen \n\n"+
                                                "Push the space bar to start the experiment.")
goodbye = visual.TextStim(win,text=("This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!")

## number of trials in the experiment
ntrials = nBlocks * nBlockTrials

## make empty trial matrix
trials = numpy.ones((ntrials,8)) * numpy.nan

# welcome
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")


# fill in the random trial order per block

## loop over the 12 blocks
for blocki in range(nBlocks):
    if blocki%3 == 0:
        instructionsdirection.draw()
        stimulus.draw()
        stimulusleft.draw()
        stimulusright.draw()
        win.flip()
    
    ## Esther: de voorwaarde van dit if-statement is dezelfde als hierboven
    elif blocki%3 == 0:
        instructsposition.draw()
        pijltjes.draw()
        win.flip()
    
    # Esther: waarom dit laatste else statement?
    else:
        numpy.random.shuffle(blockTrials)


# Esther: eens je met de trialhandler werkt is dit niet meer de manier om extra info toe te voegen op trialbasis

## trial number for this block
 currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials

## store the position of the arrow in the experiment array
    trials[currentTrials, 0] = PositionArrow

## store the direction of the arrow in the experiment array
trials[currentTrials, 1] = DirectionArrow

## store the congruency
trials[currentTrials, 2] = Congruence

## fill in the block number 
trials[currentTrials, 4] = blocki


# say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

core.quit()



 ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    