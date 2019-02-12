from psychopy import data, gui
import numpy, os

# determine the current working directory
directory_to_write = os.getcwd()

# create a dialog box for the participant name
info_name = {"What is your name?": ""}

# display the gui for the participant name
infoDlg = gui.DlgFromDict(dictionary=info_name, title="Name")

# create a dialog box for the participant details
info_details = {"Participant number":0, "Gender":["male", "female", "third gender"], "Age":0, "Handedness":["right", "left", "ambidextrous"]}

# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    # display the gui for the participant details
    infoDlg = gui.DlgFromDict(dictionary=info_details, title="Details")
    number  = info_details["Participant number"]
    
    # determine the file name
    output_file_name = directory_to_write + "/subject_" + str(number) + "_data"
    print(output_file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(output_file_name + ".csv"):
        already_exists = False

# we have found a new file name, ready to start
print("OK, let's get started!")

# Define the name of the file with the Stroop task characteristics
input_file_name = "ExperimentalDesign.xlsx"

# Import the trial list from the Excel file
trial_list = data.importConditions(input_file_name)
print(trial_list)

# Implement the trialHandler
trials = data.TrialHandler(trial_list, nReps = 1, method = "random")

# Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = output_file_name, extraInfo = info_details)

# Couple the TrialHandler to the ExperimentHandler
thisExp.addLoop(trials)

# Loop over the trials
for trial in trials:
    print(trial["ColorWord"])
    
    # Generate a random RT
    rt = numpy.random.normal(loc = 400, scale = 50)
    
    # Store the RT
    trials.addData("RT", rt)
    
    # Proceed to the next trial
    thisExp.nextEntry()

# Say goodbye to the participant
print("Goodbye " + info_name["What is your name?"] + "!")
