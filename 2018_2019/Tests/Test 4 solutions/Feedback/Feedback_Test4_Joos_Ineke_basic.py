# Test 4 IEP Ineke Joos 6/03/2019

# import modules
from psychopy import visual, event, core, gui, data
import os, numpy, math, pandas

# set the directory
my_directory = os.getcwd()


# initialize the window
win_width = 1000
win_height = 700
win = visual.Window([win_width, win_height], units= "norm")

# initializing
stimuli = ["<", ">"]

# Esther: pas op, dit zijn geen punten links, midden en rechts op het scherm!

stimposition = [(0.25, 0), (0.5, 0), (0.75, 0)]
my_clock    = core.Clock()
info        = {"Participant number": 0, "Name": "", "Age": 0, "Gender": ["man", "vrouw", "derde gender"], "Handpreference": ["links", "rechts", "ambidexter"]}
nBlocks    = 12
nBlockTrials = 60
text_width = 0.9



# data file
already_exists = True
while already_exists:
    myDlg = gui.DlgFromDict(info, title = u"get subject info")
    number = str(info["Participant number"])
    subjectname = info["Name"]
    
    # Esther: je zal nog een slash moeten plaatsen voor Test_4 om deze code te laten werken.
    
    filename = my_directory + "Test_4" + "_subject_" + number
    if not os.path.isfile(filename + ".csv"):
        already_exists = False
    else:
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("This name was already used. Please ask the experimenter to help you to enter another name.")
        myDlg2.show()
print("OK, let's get started!")

# graphical elements
Welcome = visual.TextStim(win, text = "Hello {}! Today you will be participating in an experiment. Press space to continue.".format(subjectname))


InstrPosition = visual.TextStim(win,text=(    "In this experiment, you will get to see arrows on the screen. Your task is to react to the position of the arrows.\n"+
                                                "You can use the arrows on the keyboard to respond. If the arrow is presented to the left of the screen, \n\n"+
                                                "you need to press the arrow pointing to the left. \n"
                                                "If the arrow is presented to the right of the screen, you need to press the arrow pointing to the right. \n"
                                                "If it is shown in the middle of the screen, you are required to press the arrow pointing upwards. \n"
                                                "Push the space bar to start the experiment."),
                                    height = 0.05)




InstrDirection = visual.TextStim(win,text=(    "In this experiment, you will get to see arrows on the screen. Your task is to react to the direction of the arrows.\n"+
                                                "You can use the arrows on the keyboard to respond. If the arrow is pointing to the left, \n\n"+
                                                "you need to press the arrow on the keyboard that is pointing to the left. \n"
                                                "If the arrow is presented is pointing to the right, you need to press the arrow on the keyboard pointing to the right. \n"
                                                "Push the space bar to start the experiment."),
                                    height = 0.05)



TargetStim = visual.TextStim(win, text = "")
Goodbye = visual.TextStim(win, text = "The experiment has ended. Thank you for your participation. Tell the experimenter you're ready.")




# make the design based on the core trial characteristics

## declare all levels of the factor
StimOptions = numpy.array(stimuli)
StimPositions = numpy.array(stimposition)

## determine the number of levels for the factor
Nstimuli = len(StimOptions)
Npositions = len(StimPositions)
Nunique = Nstimuli * Npositions

## determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

## make the 4-by-4 factorial design
ArrowStimuli = numpy.floor(UniqueTrials / Npositions)
print(ArrowStimuli)
ArrowPositions = numpy.floor(UniqueTrials / 1) %  Npositions
print(ArrowPositions)

## deduce the congruence
CongruenceBoolean = numpy.array(ArrowStimuli == ArrowPositions)
Congruence = CongruenceBoolean*1

# Esther: close, maar we wilden ook graag de neutrale trials een apart label geven

## combine arrays in trial matrix
Design = numpy.column_stack([ArrowStimuli, ArrowPositions])
print(ArrowStimuli)

# Esther: hier moest de congruentie ook toegevoegd worden!

# make the design for one block

## number of design repetitions per block
nReps = int(nBlockTrials/Nunique)

## repeat the 4-by-4 design 
blockTrials = numpy.tile(Design, (nReps, 1))
print(blockTrials)

# make the trial stucture for the entire experiment

## number of trials in the experiment
ntrials = nBlocks * nBlockTrials

## make empty trial matrix
trials = numpy.ones((ntrials,11)) * numpy.nan

# present the welcome message
Welcome.draw()
win.flip()
event.waitKeys(keyList = "space")




# fill in the random trial order per block

## loop over the 12 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    # Esther: ik snap wat je in de code hieronder wil doen, maar deze vergelijking werkt niet
    
    ## first 8 blocks: instruction is to respond to direction of arrow, last 4 blocks: instruction is to respond to position of arrow
    if blocki == [0, 9]:
        Instr = InstrDirection
        
    else:
        Instr = InstrPosition
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)

    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    print(currentTrials)
    
    
    ## store the trials for this block in the experiment array
    trials[currentTrials, 0:2] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 4] = blocki+1
    
    
    
    ## store the correct response
    if blocki == [0, 9]:
        trials[currentTrials, 3] = trials[currentTrials, 1]     ## correct answer determined by position
    else:
        trials[currentTrials, 3] = trials[currentTrials, 0]     ## correct answer determined by direction
        
    # Esther: hier gaat het even mis omdat je meteen alle trials van het experiment overloopt in plaats van enkel die voor het eerste blok
        
    # start trial loop
    for i in trials:
        
        # Esther: de intructies hoefden niet op elke trial herhaald te worden
        
        # present instructions
        Instr.draw()
        win.flip()
        event.waitKeys(keyList = "space")
        
        # present TargetStim
        
#        TargetStim.text = stimuli(blockTrials[currentTrials, 0])
        print("ArrowStimuli")
        print(blockTrials[currentTrials[i], 0])
        
#        TargetStim.pos = stimposition(blockTrials[i, 1])
        TargetStim.draw()
        win.flip()
        
        # wait for response
        event.clearEvents(eventType = "keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["left", "right", "up"])
        
        # store reaction time
        trials[currentTrials, 8] = my_clock.getTime()
        
        # store response
        trials[currentTrials, 9] = keys[0]
        
        
        # store accuracy
        trials[currentTrials, 10] = (keys[0] == CorResp) *1
        if keys[0] == trials[currentTrials, 3]:
            trials[currentTrials, 10] == 1
        else:
            trials[currentTrials, 10] == 0


Goodbye.draw()
win.flip()
core.wait(3)


# Esther: goed dat je hier de kruistabellen uitvoert, maar het is wat vijgen na pasen gezien de trials al uitgevoerd zijn

# Validation and export

## creating pandas dataframe from numpy array
trials = pandas.DataFrame.from_records(trials)

## name the columns
trials.columns = ["Direction", "Position", "Congruency", "CorAns", "Block", "ResponseBlock", "TrialnumberBlock", "TrialnumberExp", "RT", "Response", "Accuracy"]

## cross table validation
print(pandas.crosstab([trials.Direction, trials.Position], trials.Block))


# export as a comma separated file
numpy.savetxt("Test_4.txt", trials, delimiter = ",", fmt = "%.0d")

# Esther: waarom hier de output naam gebruiken die je bovenaan bepaald hebt?

