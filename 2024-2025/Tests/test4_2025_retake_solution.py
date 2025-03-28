# Test 4
# by Tom Verguts, March 2023
# This is a solution to the yellow/green apple/banana experiment.
# It's obviously not the only possible solution...

# import modules
from psychopy import visual, event, core, gui, data
import pandas, numpy, os, time

# timing
max_waiting_time = 1.5
feedback_time = 0.4

# set to 1 if you want to execute the code in speedy mode (not required for the test though)
speedy = 0

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
directory_to_write_to      = my_directory # no subdirs

## initialize the participant information dialog box
info = {"First name":"Incognito", "Last name":"Incognito", "Participant number":0, "Age":0, "Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"]}

## make sure the data file has a novel name
already_exists = True
while already_exists:
    
    ## present the dialog box (I fix the order to make sure that first name is before last name; not needed for test)
    my_dlg = gui.DlgFromDict(dictionary = info, 
             order = ["First name", "Last name", "Participant number", "Age", "Gender", "Handedness"], title = "Test 4")
    
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

## extract the name of the participant and some info from the dialog box information
subject_nr = info["Participant number"]
instruction_mapping = int(subject_nr%2)
subject_name = info["First name"]

## remove the name of the participant from the dialog box information (anonimity!) and add the instruction mapping
info.pop("First name")
info.pop("Last name")
info[" instruction mapping"] = instruction_mapping

## start the ExperimentHandler, add the output file name and store the dialog box info (without the participant name!)
this_exp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)


## constants
#############

n_blocks = 4
accuracy_total = 0 # for feedback at the end

## make the design based on the core trial characteristics
##########################################################

## declare all levels of the factors
color_options    = numpy.array(["yellow", "green"])
fruit_options    = numpy.array(["apple", "banana"])
location_options = numpy.array(["center", "lateral"])

## determine the number of levels for the factors
n_colors   = len(color_options)   #  = 2 
n_fruits   = len(fruit_options)   #  = 2
n_locations= len(location_options) # = 2

## number of repetitions of the stimuli per block
n_reps = 2

## determine the number of unique trials and the number of trials in a block
n_unique        = n_colors * n_fruits * n_locations # = 8
n_block_trials  = n_unique * n_reps
unique_trials    = numpy.array(range(n_unique)) # 0, 1, 2, ..., 7

## make the 3-by-3-by-2 factorial design
colors    = numpy.floor(unique_trials / (n_fruits*n_locations))  % n_colors
fruits    = numpy.floor(unique_trials / (n_locations))           % n_fruits 
locations = numpy.floor(unique_trials / 1)                       % n_locations

## possible responses
response_options = numpy.array(["f", "j", "q"])

## make the block structure
############################

## combine arrays in trial matrix
design          = numpy.column_stack([colors, fruits, locations, unique_trials])

## repeat the unique trials to form a block
block_trials     = numpy.tile(design, (n_reps, 1))
n_columns_block = block_trials.shape[1]

## make the trial stucture for the entire experiment
#####################################################

## number of trials in the experiment
n_trials         = n_blocks * n_block_trials

## make empty trial matrix; the 3 is for "Block", "Block type", and "CorResp"
trials          = numpy.ones((n_trials,n_columns_block + 3)) * numpy.nan

## determine the block types
block_type = numpy.array([0, 0, 1, 1]) # 0 = use left location
numpy.random.shuffle(block_type)

## fill in the random trial order per block
############################################

## loop over the nBlocks blocks to randomize each block separately
for block_i in range(n_blocks):
    
    ## trial number for this block
    current_trials = numpy.array(range(n_block_trials)) + block_i*n_block_trials
     
    stop_criterion = 0
    while not stop_criterion:
        
        ## suggest a shuffle
        numpy.random.shuffle(block_trials)
        
        ## check whether the first stimulus is a yellow apple
        if not ((block_trials[0, 0] == 0) and (block_trials[0, 1] == 0)):
            stop_criterion = 1

## store the trials for this block in the experiment array
    trials[current_trials, 0:n_columns_block] = block_trials
    
    ## fill in the block number (starting from 1 instead of from 0)
    trials[current_trials, n_columns_block] = block_i + 1 

    ## fill in the block type (0 or 1)
    trials[current_trials, n_columns_block + 1] = block_type[block_i]
        
    ## determine the correct response (based on color and instruction_mapping)
    trials[current_trials, n_columns_block + 2] = instruction_mapping + (1-2*instruction_mapping)*trials[current_trials, 0]

# validation and export

## creating pandas dataframe from numpy array
trials_DF = pandas.DataFrame.from_records(trials)

## add the column names
trials_DF.columns = ["colors", "fruits", "locations", "unique_trials", "block", "block_type", "cor_resp"]

## cross table validation
print(pandas.crosstab(trials_DF.fruits, trials_DF.colors))

# insert randomization in TrialHandler

## convert dataframe to list of dictionaries
trial_list = pandas.DataFrame.to_dict(trials_DF, orient = "records") #C: trial_list is list of dicts

## initialize the window
win_width       = 800
win_height      = 800
win             = visual.Window([win_width,win_height], units =  "norm", color = "pink")

## initialize clock
my_clock        = core.Clock()

## graphical elements
stimulus        = visual.ImageStim(win, size = 0.2, image= None)
welcome = ("Hi {},\n"+ "Welcome to this experiment!\n\n"+
                                                "Push the space bar to proceed.").format(subject_name)
instructions = [("Push " + response_options[0] + " when the fruit is green, or\n"+
                                                "Push " + response_options[1] + " when the fruit is yellow. \n\n"+
                                                "Push the space bar to start the experiment."),
                     ("Push " + response_options[1] + " when the fruit is green, or\n"+
                                                "Push " + response_options[0] + " when the fruit is yellow. \n\n"+
                                                "Push the space bar to start the experiment.")]
instructions_real = "Ok, that was practice.. we start after you hit the space button!"

# execute experiment

## welcome and instructions
message(message_text = welcome)
message(message_text = instructions[instruction_mapping])

for experiment_phase in range(2):
    if not experiment_phase: # practice phase
        practice_list = trial_list[4:10:2] # same list, randomly ordered
        trials = data.TrialHandler(trialList = practice_list, nReps = 1, method = "random")
    else:
        trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "sequential")  
    this_exp.addLoop(trials)
    if experiment_phase:
        message(message_text = instructions_real)
    for trial in trials:
        ## display the number on the screen
        horizontal_location = 0.5*int(trial["locations"])*(1-2*int(trial["block_type"]))
        stimulus.pos    = [horizontal_location, 0]
        if int(trial["colors"])==0 and int(trial["fruits"])==0:
            stimulus.image  = "yellow_apple.jpg"
        elif int(trial["colors"])==0 and int(trial["fruits"])==1:
            stimulus.image  = "yellow_banana.jpg"
        elif int(trial["colors"])==1 and int(trial["fruits"])==0:
            stimulus.image  = "green_apple.jpg"
        else:
            stimulus.image = "green_banana.jpg"
        
        stimulus.draw()
        win.flip()
        
        ## wait for the response
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
        if experiment_phase:
            accuracy_total += accuracy
        
        ## store the response information in the ExperimentHandler
        trials.addData("response", keys[0])
        trials.addData("Acc", accuracy)
        trials.addData("RT", RT)
        trials.addData("Training", experiment_phase)
        ## provide feedback
        # determine the feedback message
        if keys[0] == "t":
            feedback_text = "Too slow!"
        elif accuracy == 1:
            feedback_text = "Correct!"
        else:
            feedback_text = "Wrong!"
        if speedy and experiment_phase:
            feedback_duration = 0.01 # lightning fast feedback in speedy mode
        else:
            feedback_duration = feedback_time  
        message(message_text = feedback_text, duration = feedback_duration)
        ## let the ExperimentHandler proceed to the next trial
        this_exp.nextEntry()
    if keys[0] == "q": # second break needed to escape from while loop
        break
        
## let the experimentHandler know its job is done
this_exp.close()

## say goodbye to the participant
goodbye           = ("This is the end of the experiment.\n\n"+
                                                "You had {:.0f}% correct.\n\n".format(100*accuracy_total/n_trials) + 
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!")
message(message_text = goodbye, duration = 0)

win.close()