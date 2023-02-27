from psychopy import data

# make the 4-by-4 factorial design
ColorOptions = ["red","blue","green","yellow"]
trial_list = data.createFactorialTrialList({"ColorWord": ColorOptions, "FontColor": ColorOptions})

# insert the design into the TrialHandler
trials = data.TrialHandler(trial_list, nReps = 1, method = "random")

# Loop over the trials
for trial in trials:
    print("New trial!")
    print(trial["ColorWord"])
    print(trial["FontColor"])

