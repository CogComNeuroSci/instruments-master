""" TEST 4 """
""" MADE BY ALICE FLORIS """


# IMPORT
from psychopy import visual, event, core, gui, data
import time, numpy, os, pandas

# DIALOGUE BOX
info = { "Participant number":0, "Participant name": "Unknown", 
         "Gender": ["male", "female", "third gender"], 
         "Age":0, "Hand preferance": ["left", "right", "ambidexter"]}
         
# SET THE DIRECTORY
MyDirectory     = os.getcwd()

# INITIALIZE
nBlocks         = 12
nBlockTrials    = 60
MyClock         = core.Clock()
Respons         = numpy.repeat(0, ntrials)
Accuracy        = numpy.repeat(0, ntrials)
RT              = numpy.repeat(-99, ntrials)

# Esther: pas op, je hebt de gui nog niet gepresenteerd, dus heb je de info hieronder nog niet ter beschikking

# PARTICIPANT INFORMATION
Number          = numpy.repeat(info["Participant number"],len(CorResp))
Gender          = numpy.repeat(info["Gender"],len(CorResp))
Age             = numpy.repeat(info["Age"],len(CorResp))
Handpreferance  = numpy.repeat(info["Hand preferance"],len(CorResp))

# GRAPHICAL ELEMENTS
MyWindow        = visual.Window( [1000, 700], color = [-1, -1, -1], units = "norm" )
Stimulus        = visual.TextStim(win, text = "" )

# MAKING A FUNCTION FOR A MESSAGE
def message(text = "", color = "red", pos = (0.0, 0.0), response_key = "space", duration = 0):
    
    message.text    = text
    message.color   = color
    message.position= pos
    
    message.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

# DATA FILE
## KEEP ASKING FOR A NEW NUMBER WHEN THE DATA FILE ALREADY EXISTS
already_exists  = True
while already_exists:
    
    ## display the gui
    infoDLG     = gui.DlgFromDict(dictionary = info, title = "Experiment_test4" )
    number      = info["Participant number"]
    
    # Esther: er moet nog een slash komen voor Test4
    
    ## determine the file name
    file_name   = MyDirectory + "Test4_" + "/subject_" + number + "_data.csv"
    print(file_name)
    
    ## verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False
    else:
        infoDLG2       = gui.Dlg(title = "Error")
        infoDLG2.addText("Try another participant number")
        infoDLG2.show()
        
print("OK, let's get started!")

# TAKE THE NAME OF THE PARTICIPANT FROM THE DIALOG BOX INFORMATION
subject_name = info["Participant name"]

# & REMOVE THE NAME FROM THE DIALOG BOX INFORMATION FOR ANONIMITY
info.pop("Participant name")

# MAKE THE DESIGN BASED ON THE CORE TRIAL CHARACTERISTICS
## DECLARE ALL LEVELS OF THE FACTOR
DirectionOptions        = numpy.array(["left","right"])                 ## 50 % links als rechts
PositionOptions         = numpy.array([ [0.25, 0], [.50,0], [.75, 0]  ])      ## 1/3 links, midden als rechts

# Esther: let op, dit is niet rechts, midden en links op het scherm!

## DETERMINE THE NUMBER OF LEVELS FOR THE FACTOR
nDirection              = len(DirectionOptions)
nPosition               = len(PositionOptions)
nUnique                 = nPosition * nDirection 

## DETERMINE THE NUMBER OF UNIQUE TRIALS
UniqueTrials            = numpy.array(range(nUnique))

## MAKE THE FACTORIAL DESIGN
Direction               = numpy.floor(UniqueTrials / nDirection )
Position                = numpy.floor(UniqueTrials / 1 ) ‰ nDirection 

## Esther: let op, dit geeft niet het design dat we gevraagd hadden

## DEDUCE CONGRUENCE
CongruenceBoolean = numpy.array(Direction == Position)
Congruence = CongruenceBoolean*1

# Esther: ook de neutrale trials dienden zo benoemd te worden bij de congruentie

## COMBINE THE ARRAYS IN TRIAL MATRIX
DesignBalanced = numpy.column_stack([Number, Age, Gender, Handpreferance, Direction, Position, UniqueTrials, Congruence, Respons, RT, Accuracy, CorResp])


# MAKE THE DESIGN FOR ONE BLOCK
## NUMBER OF BALANCED DESIGN REPETITIONS PER BLOCK
nRepsBalanced           = int(nBlockTrials/nUnique)

## REPEAT THE FACTORIAL DESIGN
blockTrialsBalanced     = numpy.tile(DesignBalanced, (nRepsBalanced, 1))

## NUMBER OF UNBALANCED DESIGN REPETITIONS 
nRepsUnbalanced = int(nBlockTrials/DesignUnbalanced.shape[0])

## REPEAT THE UNBALANCED DESIGN 
blockTrialsUnbalanced = numpy.tile(DesignUnbalanced, (nRepsUnbalanced, 1))


# MAKE THE TRIAL STRUCTURE FOR THE ENTIRE EXPERIMENT
## NUMBR OF TRIALS IN THE EXPERIMENT
nTrials                 = nBlocks * nBlocksTrials

## MAKE EMPTY TRIAL MATRIX
trials                  = numpy.ones((ntrials,3)) * numpy.nan


# FILL IN THE RANDOM TRIAL ORDER PER BLOCK
## LOOP OVER THE 12 BLOCKS TO RANDOMIZE EACH BLOCK SEPARATELY
for blocki in range(nBlocks):
    
    # Esther: hier moest je delen door drie om 1/3 versus 2/3 te bekomen
    
    ## balanced or unbalanced block
    if (blocki)%2 == 0:
        blockTrials = blockTrialsBalanced
    else:
        blockTrials = blockTrialsUnbalanced
    
    ## randomize the trial order
    numpy.random.shuffle(blockTrials)
    
    ## trial number for this block
    currentTrials = numpy.array(range(nBlockTrials)) + blocki*nBlockTrials
    
    ## store the trials in the experiment array
    trials[currentTrials, 0:2] = blockTrials
    
    ## fill in the block number (starting from 1 instead of 0)
    trials[currentTrials, 2] = blocki+1


# VALIDATION
## CREATING PANDA DATAFRAME 
trials = pandas.DataFrame.from_records(trials)

## NAMING THE COLUMNS 
trials.columns = ["Position", "Direction", "UniqueTrials", "Congruence", "Block", "Balance", "CorAns" ]

## CROSS TABLE VALIDATION
print("Block randomization")
print(pandas.crosstab(trials.Congruence, trials.Balance))
print(pandas.crosstab(trials.Congruence, trials.Block))
print("Correct answers")
print(pandas.crosstab(trials.Position, trials.CorAns))
print(pandas.crosstab(trials.Block, trials.Direction))


# START EXPERIMENT 
## DISPLAY A WELCOME
message(text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# Esther: de info over de naam van de proefpersoon heb je ondertussen al verwijderd

## DISPLAY THE INSTRUCTIONS 
message(text = "Carefully read the instructions! \n\n" +
                    "In this block you will see arrows that change in position (left, middle or right of the screen) or direction (left or right)." +
                    "In some blocks it is the goal to react to the direction, sometimes to the position." + 
                    "Use the arrows on the keyboard to react." +
                    "When you are done with the instructions, press space to continue.", response_key = "space")


# TRIALS
## MAKE THE TRIAL LOOP
for trial in trials: 
    
    ## display the stimulus on the screen
    Stimulus.position   = trial["Position"]
    Stimulus.direction  = trial["Direction"]
    Stimulus.draw()
    win.flip
    
    ## wait for the response
    event.clearEvents(eventType="keyboard")
    my_clock.reset()
    keys = event.waitKeys(keyList = ["<",">"])  # Esther: dit zijn niet de response opties die we bedoelden
    
    trials.addData("response", keys[0])
    trials.addData("RT", my_clock.getTime())
    
    ## Storing data
        if keys[0] != 0:
            
            trials[i, 4] = keys[0]                                  ## store the response of the participant
            trials[i, 6] = int(trials[i, 5] == trials[i, 7 ] )       ## store the accuracy
            trials[i, 5] = RT                                       ## store the reactiontime


# END EXPERIMENT
message(text = "Thank you for partipating!", response_key = "space")



core.quit()





