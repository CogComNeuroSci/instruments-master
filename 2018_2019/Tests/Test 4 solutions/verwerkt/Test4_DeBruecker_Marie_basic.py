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


PositionArrowOptions= ["stimulus", "stimulusleft", "stimulusright"]
DirectionArrowOptions = ["<", ">"]

trial_list = data.createFactorialTrialList({"PositionArrow": PositionArrowOptions, "DirectionArrow": DirectionArrowOptions})

# convert the list of dictionaries to a dataframe for inspection
dataFrame = pandas.DataFrame.from_dict(trial_list)

# we can also quickly convert the dataframe to a numpy array
array = dataFrame.values

# congruency
CongruencyLevels = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean = numpy.array([PositionArrow == DirectionArrow)
Congruence = CongruenceLevels [[CongruenceBoolean * 1]]

## determine the number of levels for the factor
NPositionArrow = len(PositionArrowOptions)
NDirectionArrowOptions = len(DirectionArrowOptions)
Nunique = NPositionArrowOptions * NDirectionArrowOptions

## determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

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
    
    directory_to_write_to = os.getcwd() + "/data/"
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    file_name = directory_to_write_to + "/Test4_" + "_subject_" + str(info["Participant number"]) + "_data"
    if not os.path.isfile(file_name+".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

# extract the name of the participant from the dialog box information
subject_name = info["Name"]

# remove the name of the participant from the dialog box information (anonimity!)
info.pop("Name")

# start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name!)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# graphical elements
pijltjes = visual.TextStim (win, text="<", ">")

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
    
    elif blocki%3 == 0:
        instructsposition.draw()
        pijltjes.draw()
        win.flip()
        
    else:
        numpy.random.shuffle(blockTrials)



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
    