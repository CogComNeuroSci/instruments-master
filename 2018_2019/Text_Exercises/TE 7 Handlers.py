from psychopy import data
import numpy

# Define the name of the file with the Stroop task characteristics
input_file_name = "ExperimentalDesign.xlsx"

# Import the trial list from the Excel file
trial_list = data.importConditions(input_file_name)
print(trial_list)

# Implement the trialHandler
trials = data.TrialHandler(trial_list, nReps = 1, method = "random")

# Define the name of the output file
output_file_name = "Output"

# Implement the ExperimentHandler
thisExp = data.ExperimentHandler(dataFileName = output_file_name)

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

