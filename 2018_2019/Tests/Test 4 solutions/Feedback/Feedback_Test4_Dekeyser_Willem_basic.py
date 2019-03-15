### Dit script is niet te runnen. Ik heb verschillende zaken door elkaar geslaan. Als je de GUI in een ander bestand opent, werkt die en zorgt die ervoor dat de naam niet wordt opgeslagen.
### Op het einde van mijn script kan je ook de code vinden die ik heb getypt voor de randomisatie en validatie van mijn trials in numpy. 
### In mijn script zitten ook verschillende errors waar ik geen tijd meer voor heb gehad om ze weg te werken.


from psychopy import visual, event, core, gui, data
import numpy
import pandas
import os

# set the directory
my_directory = os.getcwd()

# initialize the window
win = visual.Window(size = (1000, 700), units = "norm", allowGUI = True)

# initializing
RespOptions = []
text_width  = 1
my_clock    = core.Clock()
info        = {"Name": "", "Participant number": 0, "Age": 0, "Gender": ["male", "female", "other"], "hand preference":["left", "right", "ambidexter"]}


# make sure the data file has a novel name
already_exists = True
while already_exists:
    
    # present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Test 4")
    
    # construct the name of the folder that will hold the data
    directory_to_write_to = my_directory + "/data"
    
    # if the folder doesn't exist yet, make it
    if not os.path.isdir(directory_to_write_to):
        os.mkdir(directory_to_write_to)
    
    # construct the name of the data file
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"])
    
    # check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        
        # if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        # if the data file name has already been used, ask the participant to insert a different participant number or session number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another participant number")
        myDlg2.show()

# extract the name of the participant from the dialog box information
subject_name = info["Name"]

# remove the name of the participant from the dialog box information (anonimity!)
info.pop("Name")

# start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name!)
thisExp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


# declare all levels of the factor
##position = numpy.array(["<",">"])
##orientation = numpy.array([(-0.5,0),(0,0),(0.5,0)])

# Within-subjects design
Design = [{'StimulusPosition': '<', 'StimulusOrientation': array([-0.5,  0. ])}, \
           {'StimulusPosition': '>', 'StimulusOrientation': array([-0.5,  0. ])}, \
           {'StimulusPosition': '<', 'StimulusOrientation': array([0., 0.])}, \
           {'StimulusPosition': '>', 'StimulusOrientation': array([0., 0.])}, \
           {'StimulusPosition': '<', 'StimulusOrientation': array([0.5, 0. ])}, \
           {'StimulusPosition': '>', 'StimulusOrientation': array([0.5, 0. ])}]


## Esther: hier moest je 10 keer de 6 unieke trials herhalen om aan 60 trials te geraken per block
## Esther: deze code hoort eigenlijk ook thuis in de blokloop omdat je per block een nieuwe trialhandler met 60 trials zal willen toevoegen

# create the trials
trials = data.TrialHandler(trialList = Design, nReps = 1, name = "Experiment", method = "fullrandom")
thisExp.addLoop(trials)


# constants

## number of blocks
nBlocks = 12

## number of trials per block
nBlockTrials = 60

## number of design repetitions per block
##nReps = int(nBlockTrials/(4*4))

# initialize instructions text
instructions_text.text   = ("Depending on the block you're in, there will be two different instructions. \n\n" +
                      "It will be made clear before the start of the block which instructions you'll have to follow." +
                      "You'll encounter the following instructions througout the experiment:"
                      "1: Press the right arrow key when the arrow-stimulus is pointing to the right. \n\n" +
                      "Press the left arrow key when the arrow-stimulus is pointing to the left. \n\n" 
                      "Or 2: Press the right arrow key when the arrow-stimulus is positioned on the right side of the screen. \n\n" +
                      "Press the left arrow key when the arrow-stimulus is positioned on the left side of the screen. \n\n" +
                      "Press the down arrow key when the arrow-stimulus is positioned in the middle of the screen. \n\n" +
                      "Goodluck!")
                      
orientation_instructions_text.text   = ("This block, press the right arrow key when the arrow-stimulus is pointing to the right. \n\n" +
                                  "Press the left arrow key when the arrow-stimulus is pointing to the left. \n\n" +
                                  "Goodluck!")
                                  
position_instruction_text.text       = ("This block, press the right arrow key when the arrow-stimulus is positioned on the right side of the screen. \n\n" +
                                  "Press the left arrow key when the arrow-stimulus is positioned on the left side of the screen. \n\n" +
                                  "Press the down arrow key when the arrow-stimulus is positioned in the middle of the screen. \n\n" +
                                  "Goodluck!")


# initialize graphical elements
MessageOnSCreen     = visual.TextStim(win, text = "OK")


# modules

## function for displaying messages
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    
    MessageOnSCreen.text    = message_text
    MessageOnSCreen.height  = height
    MessageOnSCreen.pos     = pos
    MessageOnSCreen.color   = color
    
    MessageOnSCreen.draw()
    win.flip()
    if duration == 0:
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration)

## Esther: oei, je bent blijkbaar vergeten dat je de naam van de proefpersoon al uit de gui info hebt gegooid ;)

# display the welcome message
message(message_text = "Welcome " + info["Participant name"] + "!\n\nPress the space bar to continue.", response_key = "space")

# display the instructions
message(message_text = instructions_text + "!\n\nPress the space bar to continue.", height = 0.05, response_key = "space")


# fill in the random trial order per block

## loop over the 10 blocks to randomize each block separately
for blocki in range(nBlocks):
    
    ## Esther: de structuur hieronder had if-statements moeten gebruiken in plaats van while
    
    ## which instructions per block?
    while (blocki) <= 4:
        message(message_text = orientation_instructions_text + "!\n\nPress the space bar to continue.", height = 0.05, response_key = "space")
    while (blocki) >= 5 or <= 8:
        message(message_text = position_instructions_text + "!\n\nPress the space bar to continue.", height = 0.05, response_key = "space")
    else:
        message(message_text = orientation_instructions_text + "!\n\nPress the space bar to continue.", height = 0.05, response_key = "space")
        
    for trial in trials:
        
        ## display the number on the screen
        stimulus.pos = trial["StimulusPosition"]
        stimulus.text = trial["StimulusOrientation"]
        stimulus.draw()
        win.flip()
        
        ## wait for the response
        event.clearEvents(eventType="keyboard")
        my_clock.reset()
        keys = event.waitKeys(keyList = ["",""])
        
        trials.addData("response", keys[0])
        ##accuracy = 1*(keys[0]==correct[trial["Number"]-1])
        trials.addData("Acc", accuracy)
        trials.addData("RT", my_clock.getTime())


# This is the end
message(message_text = "Goodbye " + info["Participant name"] + "!\n\nPress the space bar to end the experiment.", pos = (0,0), height = None)

# close the experiment window
win.close()



# Validation -> This is the validation when I would have worked with arrays.


# make the design based on the core trial characteristics

## declare all levels of the factor
#position = numpy.array(["<",">"])
#orientation = numpy.array([(-0.5,0),(0,0),(0.5,0)])
#
## determine the number of levels for the factor
#Npos    = len(position)
#Nori    = len(orientation)
#print(Nori)
#Nunique = Npos * Nori
#
## determine the number of unique trials
#UniqueTrials = numpy.array(range(Nunique)) 
#print(UniqueTrials)
#
## make the 2-by-3 factorial design
#StimulusPosition     = numpy.floor(UniqueTrials / 1) %  Npos
#print(StimulusPosition)
#StimulusOrientation  = numpy.floor(UniqueTrials / Npos)
#print(StimulusOrientation)
#
## combine arrays in trial matrix
#Design = numpy.column_stack([StimulusPosition, StimulusOrientation])
#print(Design)
#
# make the design for one block
#
## number of design repetitions per block
#nReps = int(nBlockTrials/Nunique)
#print(nReps)
#

## Esther: hier heb je wel correct je 60 trials geimplementeerd

## repeat the 2-by-3 design 6 times
#blockTrials = numpy.tile(Design, (nReps, 1))
#print(blockTrials)
#
# make the trial stucture for the entire experiment
#
## number of trials in the experiment
#ntrials = nBlocks * nBlockTrials
#print(ntrials)
#
## make empty trial matrix
#trials = numpy.ones((ntrials,3)) * numpy.nan
#print(trials)

# Validation and export
#
## creating pandas dataframe from numpy array
#trials = pandas.DataFrame.from_records(trials)
#
## name the columns
#trials.columns = ["StimulusPosition", "StimulusOrientation", "Block"]
#
## cross table validation
#print(pandas.crosstab([trials.StimulusPosition, trials.StimulusOrientation], trials.Block))
#
## export
#trials.to_csv(path_or_buf = "Test4_output_arrays.csv", index = False)