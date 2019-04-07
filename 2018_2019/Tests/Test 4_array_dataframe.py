# Test 4, a solution

# import modules
from psychopy import visual, event, core, gui, data
import pandas, numpy, os

# set to 1 if you want to execute the code in speedy mode
speedy = 1


# file management and participant info

## set the directory
my_directory = os.getcwd()

## construct the name of the folder that will hold the data
directory_to_write_to = my_directory + "/data"
    
## if the folder doesn't exist yet, make it
if not os.path.isdir(directory_to_write_to):
    os.mkdir(directory_to_write_to)

## initialize the participant information dialog box
info = {"Participant name":"Incognito", "Participant number":0, "Age":0, "Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"]}

## make sure the data file has a novel name
already_exists = True
while already_exists:
    
    ## present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    ## construct the name of the data file
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"]) + ".csv"
    
    ## check whether the name of the data file has already been used
    if not os.path.isfile(file_name):
        
        ## if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        ## if the data file name has already been used, ask the participant to inser a different participant number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()


# randomization

## constants
#############

## number of blocks
nBlocks = 12

## number of trials per block
nBlockTrials = 60


## make the design based on the core trial characteristics
##########################################################

## declare all levels of the factors
ArrowOptions    = numpy.array(["<",">"])
PositionOptions = numpy.array([-0.5,0.5,0])
RespOptions     = numpy.array(["left","right","down"])

## determine the number of levels for the factors
Narrows         = len(ArrowOptions)
Npositions      = len(PositionOptions)

## determine the number of unique trials
Nunique         = Narrows * Npositions
UniqueTrials    = numpy.array(range(Nunique)) 

## make the 2-by-3 factorial design
Arrow           = numpy.floor(UniqueTrials / Npositions)
Position        = numpy.floor(UniqueTrials / 1) %  Npositions


## deduce characteristics
##########################

## determine the congruency
Congruence      = numpy.array(Arrow == Position) * 1

## overwrite the congruency of the neutral trials
Congruence[Position == 2] = -1


## make the block structure
############################

## combine arrays in trial matrix
Design          = numpy.column_stack([Arrow, Position, UniqueTrials, Congruence])

## how many times do we need to repeat these trials per block
nReps           = int(nBlockTrials / Nunique)

## repeat the unique trials to form a block
blockTrials     = numpy.tile(Design, (nReps, 1))


## make the trial stucture for the entire experiment
#####################################################

## number of trials in the experiment
ntrials         = nBlocks * nBlockTrials

## make empty trial matrix
trials          = numpy.ones((ntrials,15)) * numpy.nan


## randomize the block order
#############################

## basic version: use the block number to determine the mapping
print(numpy.array(range(nBlocks)) % 3 == 0)
print(numpy.array(range(nBlocks)) < int(nBlocks/3))

## make an array with all the block instuctions
BlockTypes      = numpy.concatenate([numpy.repeat(0,nBlocks*2/3),numpy.repeat(1,nBlocks*1/3)])

## advanced version: no repetitions of the position instructions (1)
stopcriterium = 0
while stopcriterium != 1:
    
    ## suggest a shuffle
    numpy.random.shuffle(BlockTypes)
    
    ## calculate the difference
    comparison = numpy.diff(BlockTypes) + 1
    
    ## check whether there was a repetition
    if numpy.sum(comparison * BlockTypes[:-1]) == 0:
        stopcriterium = 1


## fill in the random trial order per block
############################################

## loop over the 12 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:4] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 4] = blocki+1
    
    ## fill in the block type (respond to arrow direction or position)
    trials[currentTrials, 5] = BlockTypes[blocki]
    
    ## determine the correct response
    if BlockTypes[blocki] == 0:
        trials[currentTrials, 6] = trials[currentTrials, 0]
    else:
        trials[currentTrials, 6] = trials[currentTrials, 1]
    
    ## insert the trial number within the block
    trials[currentTrials, 7] = numpy.array(range(nBlockTrials))+1

## store the participant information
trials[:,11] = info["Participant number"]
trials[:,12] = info["Age"]
if info["Gender"] == "male":
    trials[:,13] = 0
elif info["Gender"] == "female":
    trials[:,13] = 1
else:
    trials[:,13] = 2
if info["Handedness"] == "right":
    trials[:,14] = 0
elif info["Handedness"] == "left":
    trials[:,14] = 1
else:
    trials[:,14] = 2


# validation and export

## creating pandas dataframe from numpy array
trialsDF = pandas.DataFrame.from_records(trials)

## add the column names
trialsDF.columns = ["Arrow", "Position", "UniqueStim", "Congruence", "Block", "Mapping", "CorResp", "TrialInBlock", 
                  "response", "Acc", "RT", "Participant number", "Age", "Gender", "Handedness"]

## cross table validation
print(pandas.crosstab([trialsDF.Arrow, trialsDF.Position], trialsDF.Congruence))
print(pandas.crosstab(trialsDF.Mapping, [trialsDF.Arrow, trialsDF.Position]))
print(pandas.crosstab(trialsDF.Block, trialsDF.Mapping))
print(pandas.crosstab([trialsDF.Arrow, trialsDF.Position], [trialsDF.Mapping, trialsDF.CorResp]))

## export (just to be able to check the randomization)
trialsDF.to_csv(path_or_buf = "Test4.csv", index = False)


# initializing

## initialize the window
win_width       = 1000
win_height      = 700
win             = visual.Window([win_width,win_height])

## initialize clock
my_clock        = core.Clock()

## graphical elements
text_width      = 0.5
stimulus        = visual.TextStim(win,text="")
welcome         = visual.TextStim(win,text=(    "Hi {},\n"+
                                                "Welcome to this experiment!\n\n"+
                                                "Push the space bar to proceed.").format(info["Participant name"]),
                                    wrapWidth = win_width*text_width)
instruct_dir    = visual.TextStim(win,text=(    "Push left when the arrow points to the left or\n"+
                                                "Push right when the arrow points to the right. \n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
instruct_pos    = visual.TextStim(win,text=(    "Push left when the arrow is positioned on the left,\n"+
                                                "Push the middle button when the arrow is in the center, \n"+
                                                "Push right when the arrow is positioned on the right. \n\n"+
                                                "Push the space bar to start the experiment."),
                                    wrapWidth = win_width*text_width)
goodbye         = visual.TextStim(win,text=(    "This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!"),
                                    wrapWidth = win_width*text_width)


# execute experiment

## welcome and instructions
welcome.draw()
win.flip()
event.waitKeys(keyList = "space")

## trial loop
trialcounter = 0
while trialcounter < trialsDF.shape[0]:
    
    ## present the instructions at the start of the block
    if trialsDF.TrialInBlock[trialcounter] == 1:
        if trialsDF.Mapping[trialcounter] == 0:
            instruct_dir.draw()
        else:
            instruct_pos.draw()
        win.flip()
        if speedy == 1:
            pass
        else:
            event.waitKeys(keyList = "space")
    
    ## display the number on the screen
    stimulus.pos = (PositionOptions[int(trialsDF.Position[trialcounter])],0)
    stimulus.text = ArrowOptions[int(trialsDF.Arrow[trialcounter]) ]
    stimulus.draw()
    win.flip()
    
    ## wait for the response
    event.clearEvents(eventType = "keyboard")
    my_clock.reset()
    if speedy == 1:
        keys = ["left"]
    else:
        keys = event.waitKeys(keyList = RespOptions)
    RT = my_clock.getTime()
    
    ## calculate the derived response properties
    CorResp = RespOptions[int(trialsDF.CorResp[trialcounter])]
    accuracy = (keys[0] == CorResp) * 1
    
    ## store the response information
    if keys[0] == "left":
        trialsDF.response[trialcounter] = 0
    elif keys[0] == "down":
        trialsDF.response[trialcounter] = 1
    else:
        trialsDF.response[trialcounter] = 2
    
    trialsDF.Acc[trialcounter]   = accuracy
    trialsDF.RT[trialcounter]    = RT
    
    trialcounter = trialcounter + 1

## export data
trialsDF.to_csv(path_or_buf = file_name, index = False)

## say goodbye to the participant
goodbye.draw()
win.flip()
event.waitKeys(keyList = "space")

win.close()
