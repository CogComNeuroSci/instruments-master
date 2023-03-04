# Exercise similar to Test 4
# by Tom Verguts, March 2023
# note: I use underscore_notation for variables 
# I think this is easier to read and less error-prone than CamelBackNotation, but you are totally free to use either
# one additional advantage is that it's immediately clear which variables are mine and which are from psychopy
# (as the latter does use CamelBack, usually)

# import modules
from psychopy import visual, event, core, gui, data
import pandas, numpy, os, time

# timing
max_waiting_time = 2
feedback_time = 0.3

# set to 1 if you want to execute the code in speedy mode
speedy = 1

# make a function for presenting messages on screen
def message(message_text = "", response_key = "space", duration = 0, height = None, pos = (0.0, 0.0), color = "white"):
    message_on_screen = visual.TextStim(win, text = "OK")
    message_on_screen.text    = message_text
    message_on_screen.height  = height
    message_on_screen.pos     = pos
    message_on_screen.color   = color
    
    message_on_screen.draw()
    win.flip()
    if duration == 0: # for the welcome and goodbye
        event.waitKeys(keyList = response_key)
    else:
        time.sleep(duration) # for the feedback

# file management and participant info

## set the directory; no sub-dirs
my_directory = os.getcwd()

## construct the name of the folder that will hold the data
directory_to_write_to      = my_directory # C: no subdirs

## initialize the participant information dialog box
info = {"Participant name":"Incognito", "Participant number":0, "Age":0, "Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"]}

## make sure the data file has a novel name
already_exists = True
while already_exists:
    
    ## present the dialog box
    my_dlg = gui.DlgFromDict(dictionary = info, title = "Example for Test 4")
    
    ## construct the name of the data file
    file_name = directory_to_write_to + "/Test4_subject_" + str(info["Participant number"])
        
    ## check whether the name of the data file has already been used
    if not os.path.isfile(file_name + ".csv"):
        
        ## if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    else:
        
        ## if the data file name has already been used, ask the participant to inser a different participant number
        my_dlg2 = gui.Dlg(title = "Error")
        my_dlg2.addText("Try another participant number")
        my_dlg2.show()

## extract the name of the participant from the dialog box information
subject_name = info["Participant name"]
#subject_name = "tom verguts"
mapping = int(subject_name[0] in ["a", "b", "c", "A", "B", "C"])

## remove the name of the participant from the dialog box information (anonimity!)
info.pop("Participant name")
info["mapping"] = mapping

## start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name!)
this_exp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


# randomization

## constants
#############

## number of blocks
n_blocks = 2

## make the design based on the core trial characteristics
##########################################################

## declare all levels of the factors
letter_options   = numpy.array(["a", "b", "c"])
color_options    = numpy.array(["green", "black"])
location_options = numpy.array([-0.5, 0, 0.5])
#response_options = numpy.array(["f", "j", "q"])

    
## determine the number of levels for the factors
n_letters  = len(letter_options)  #  = 3
n_colors   = len(color_options)   #  = 2 
n_locations= len(location_options) # = 3


## number of repetitions of the stimuli per block
n_reps = 2

## determine the number of unique trials and the number of trials in a block
n_unique        = n_letters * n_colors * n_locations # = 18
n_block_trials  = n_unique * n_reps
unique_trials    = numpy.array(range(n_unique)) # 0, 1, 2, ..., 17 

## make the 3-by-3-by-2 factorial design
letters   = numpy.floor(unique_trials / (n_colors*n_locations))  % n_letters
colors    = numpy.floor(unique_trials / (n_locations))           % n_colors 
locations = numpy.floor(unique_trials / 1)                       % n_locations


## deduce characteristics
##########################

## determine the congruency
congruence      = numpy.array(letters == locations) * 1

## make the block structure
############################

## combine arrays in trial matrix
design          = numpy.column_stack([letters, colors, locations, unique_trials, congruence])
print(design)


## repeat the unique trials to form a block
block_trials     = numpy.tile(design, (n_reps, 1))
n_columns_block = block_trials.shape[1]

## make the trial stucture for the entire experiment
#####################################################

## number of trials in the experiment
n_trials         = n_blocks * n_block_trials

## make empty trial matrix; the 2 is for "Block" and "CorResp"
trials          = numpy.ones((n_trials,n_columns_block + 2)) * numpy.nan


## fill in the random trial order per block
############################################

## loop over the nBlocks blocks to randomize each block separately
for block_i in range(n_blocks):
    
    ## trial number for this block
    current_trials = numpy.array(range(n_block_trials)) + block_i*n_block_trials
     
    stop_criterium = 0
    while not stop_criterium:
        
        ## suggest a shuffle
        numpy.random.shuffle(block_trials)
        
        ## calculate the difference based on UniqueTrials
        comparison = numpy.diff(block_trials[:, 3])
        
        ## check whether there was a repetition
        if sum(comparison == 0) == 0:
            stop_criterium = 1
    ## store the trials for this block in the experiment array
    trials[current_trials, 0:n_columns_block] = block_trials
    
    ## fill in the block number (starting from 1 instead of from 0)
    trials[current_trials, n_columns_block] = block_i+1
    
    ## determine the correct response (based on color and mapping)
    trials[current_trials, n_columns_block+1] = mapping + (1-2*mapping)*trials[current_trials, 1]

# validation and export

## creating pandas dataframe from numpy array
trials_DF = pandas.DataFrame.from_records(trials)

## add the column names
trials_DF.columns = ["letters", "colors", "locations", "unique_trials", "congruence", "block", "cor_resp"]

## cross table validation
print(pandas.crosstab(trials_DF.locations, [trials_DF.letters, trials_DF.colors]))

# insert randomization in TrialHandler

## convert dataframe to list of dictionaries
trial_list = pandas.DataFrame.to_dict(trials_DF, orient = "records") #C: trial_list is list of dicts
print("**")
print(trial_list)

## initialize the window
win_width       = 1000
win_height      = 700
win             = visual.Window([win_width,win_height], color = "gray")

## initialize clock
my_clock        = core.Clock()

## graphical elements
stimulus        = visual.TextStim(win,text="")
welcome = ("Hi {},\n"+ "Welcome to this experiment!\n\n"+
                                                "Push the space bar to proceed.").format(subject_name)
instructions_list = [("Push " + response_options[0] + " when the color is green, or\n"+
                                                "Push " + response_options[1] + " when the color is black. \n\n"+
                                                "Push the space bar to start the experiment."),
                     ("Push " + response_options[1] + " when the color is green, or\n"+
                                                "Push " + response_options[0] + " when the color is black. \n\n"+
                                                "Push the space bar to start the experiment.")]
instructions = instructions_list[mapping]
goodbye           = ("This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!")

# execute experiment

## welcome and instructions
message(message_text = welcome)

experiment_phase = 0  #C: practice phase or experiment phase
practice_count = 0    #C: how many practice blocks have we tried 
while experiment_phase < 2:
    message(message_text = instructions)
    if experiment_phase == 0: # while we are still practicising
        practice_list = trial_list[2:6] # for simplicity, I always take the same practice list
        trials = data.TrialHandler(trialList = practice_list, nReps = 1, method = "random")
    else:
        trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "sequential")  
    this_exp.addLoop(trials)
    accuracy_phase = 0
    practice_count += (experiment_phase == 0) 
    for trial in trials:
        ## display the number on the screen
        stimulus.pos    = [0, location_options[int(trial["locations"])]]
        stimulus.text   = letter_options[int(trial["letters"])]
        stimulus.color  = color_options[int(trial["colors"])]
        stimulus.draw()
        win.flip()
        

        ## wait for the response
        event.clearEvents(eventType = "keyboard") # this is not strictly needed..
        my_clock.reset()
        if speedy and experiment_phase: # i don't want speedy in practice
            keys = ["f"]
        else:
            keys = event.waitKeys(keyList = response_options, maxWait = max_waiting_time)
        RT = my_clock.getTime()
        if keys == None:  # keys[0]
            keys = ["t"] # t for too late
        elif keys[0] == "q":
            break
        ## calculate the derived response properties
        cor_resp = response_options[int(trial["cor_resp"])]
        accuracy = (keys[0] == cor_resp) * 1
        accuracy_phase += accuracy
        ## provide feedback
        
        ## store the response information in the ExperimentHandler
        trials.addData("response", keys[0])
        trials.addData("Acc", accuracy)
        trials.addData("RT", RT)
        trials.addData("Training", experiment_phase)
        ## provide feedback
        # determine the feedback message
        if keys[0] == "t":
            feedback_text = "Too late!"
        elif accuracy == 1:
            feedback_text = "Correct!"
        else:
            feedback_text = "Wrong answer!"
        if speedy and experiment_phase:
            feedback_duration = 0.01 # lightning fast feedback in speedy mode
        else:
            feedback_duration = feedback_time  
        message(message_text = feedback_text, duration = feedback_duration)
        ## let the ExperimentHandler proceed to the next trial
        this_exp.nextEntry()
    if keys[0] == "q": # second break needed to escape from while loop
        break
    if (practice_count == 3) & (accuracy_phase < 2):
        break
    if (experiment_phase == 0) and (accuracy_phase > 2):
        experiment_phase = 1
    else:
        experiment_phase += int(experiment_phase == 1)
        
## let the experimentHandler know its job is done
this_exp.close()

## say goodbye to the participant
message(message_text = goodbye, duration = 0)

win.close()