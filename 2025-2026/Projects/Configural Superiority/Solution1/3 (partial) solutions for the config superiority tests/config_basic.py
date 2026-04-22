# The configural superiority task, basic version
# Stimulus is presented until key press here
# Tom Verguts, march 2023

# Import modules
from psychopy import visual, event, core, gui, data
import os, pandas, time, numpy

# Set to 1 if you want to execute the code in speedy mode
speedy = 0

# predefined variables
n_per_block      = 8
n_blocks         = 2
fixation_wait    = 0.5 # in seconds
max_waiting_time = 2 

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

def show_fixation():
    fixation.draw()
    win.flip()
    time.sleep(fixation_wait)

# File management, experiment handler, and participant info

my_directory = os.getcwd()
directory_to_read_from = os.path.join(my_directory, "stimuli")

directory_to_write_to = os.path.join(my_directory, "data")
if not os.path.isdir(directory_to_write_to):
    os.mkdir(directory_to_write_to)
    
info = {"Subject's name":"Name", "Subject number":0, "Age":0, "Gender":["male", "female", "third gender"], "Handedness":["right", "left", "ambidextrous"]}

already_exists = True
while already_exists or info["Subject's name"] == "Name":
    ## Note, I did an extra robustness check, namely to force subjects to change "name" to their actual name

    ## present the dialog box
    myDlg = gui.DlgFromDict(dictionary = info, title = "Configuration Superiority Effect")
    
    ## construct the name of the data file
    file_name = os.path.join(directory_to_write_to, "Config_Sup_subject_" + str(info["Subject number"]))

    ## check whether the name of the data file has already been used
    if (not os.path.isfile(file_name + ".csv")) and (not info["Subject's name"] == "Name"):
        
        ## if there isn't a data file with this name used yet, we're ready to start
        already_exists = False
        
    elif os.path.isfile(file_name + ".csv"):        
        ## if the data file name has already been used, ask the participant to inser a different participant number
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Try another subject number")
        myDlg2.show()
    else:
        ## if the subject has not provided his/her name, and the name field still contains "Name"
        myDlg2 = gui.Dlg(title = "Error")
        myDlg2.addText("Please fill in your actual name")
        myDlg2.show()

subject_name = info["Subject's name"]

info.pop("Subject's name")

this_exp = data.ExperimentHandler(dataFileName = file_name, extraInfo = info)

# Make the design based on the core trial characteristics

Stimulus_Options     = numpy.array([1, 2, 3, 4, 5, 6, 7, 8]) #Array of the names of the images

n_stimuli     = len(Stimulus_Options)   #  = 8
n_unique      = n_stimuli               # multiplication of just a single factor in this case..
unique_trials = numpy.array(range(n_unique)) # 0, 1, 2, ..., 7
design        = numpy.column_stack([unique_trials]) # no need to have anything else in case of a single factor

response_options = numpy.array(["e", "f", "j", "i", "q"])
correct_response_array = numpy.array([0, 3, 1, 2, 0, 3, 1, 2]) # got this from inspecting the stimuli

# make the trial stucture for the entire experiment

n_reps          = int(n_per_block/n_stimuli) # repetitions of the full design per block
block_trials    = numpy.tile(design, (n_reps, 1))
n_columns_block = block_trials.shape[1] # just 1 in this case

n_trials         = n_blocks * n_per_block

trials          = numpy.ones((n_trials, n_columns_block + 2)) * numpy.nan # We add Block (1) and Cor_resp (2)

for block_i in range(n_blocks):

    ## no restrictions in the assignment
    numpy.random.shuffle(block_trials)
    
    current_trials = numpy.array(range(n_per_block)) + block_i*n_per_block

    ## plug in the shuffled block
    print(block_trials.shape)
    trials[current_trials, 0:n_columns_block] = block_trials
    
    ## fill in the block number (starting from 1 instead of from 0)
    trials[current_trials, n_columns_block] = block_i + 1 

    ## fill in the correct response; note the left-hand wants something of shape (8*n_reps,), so we must squeeze the (8*n_reps, 1) shape 
    trials[current_trials, n_columns_block + 1] = numpy.squeeze(correct_response_array[block_trials])
    
# validation and export to trial_list

trials_DF = pandas.DataFrame.from_records(trials)

trials_DF.columns = ["stimuli", "block", "cor_resp"]

print("cross-table of stimuli and blocks looks like this for your design:")
print(pandas.crosstab(trials_DF.stimuli, trials_DF.block))

trial_list = pandas.DataFrame.to_dict(trials_DF, orient = "records") # trial_list is list of dicts

# initialize graphical elements, texts, the window, ... 
# for actual experiments, use full screen but I prefer partial screen while debugging
win_width       = 800
win_height      = 800
win             = visual.Window([win_width,win_height], units =  "norm", color = "black")

my_clock        = core.Clock()

stimulus        = visual.ImageStim(win, size = 0.5, image= None)
fixation        = visual.TextStim(win, text = "+")
welcome = ("Hi {},\n"+ "Welcome to this experiment!\n\n"+
                                                "Push the space bar to proceed.").format(subject_name)
instructions = ("Push " + response_options[0] + " when the upper left stimulus deviates;\n"+
                "Push " + response_options[1] + " when the lower left stimulus deviates;\n"+
                "Push " + response_options[2] + " when the lower right stimulus deviates;\n"+
                "Push "  + response_options[3] + " when the upper right stimulus deviates.\n\n"+
                "Push the space bar to start the experiment.")
                                                
instructions_real = "Ok, that was practice.. we start after you hit the space button!"

# welcome and instructions
message(message_text = welcome)
message(message_text = instructions)

trials = data.TrialHandler(trialList = trial_list, nReps = 1, method = "sequential")  
this_exp.addLoop(trials)

for trial in trials:
    show_fixation()
    stimulus.image = os.path.join(directory_to_read_from, str(Stimulus_Options[int(trial["stimuli"])]) + ".jpg")
    stimulus.draw()
    win.flip()

    my_clock.reset()
    if speedy:
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
    ## store the response information in the ExperimentHandler
    trials.addData("response", keys[0])
    trials.addData("Acc", accuracy)
    trials.addData("RT", RT)
    this_exp.nextEntry()
        
# let the experimentHandler know its job is done
this_exp.close()

# say goodbye to the participant
goodbye           = ("This is the end of the experiment.\n\n"+
                                                "Signal to the experimenter that you are ready.\n\n"+
                                                "Thank you for your participation!")
message(message_text = goodbye, duration = 0)

win.close()