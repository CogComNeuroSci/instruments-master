from psychopy import data

# make the 4-by-4-by-2-by-3 factorial design
ColorOptions    = ["red","blue","green","yellow"]
TypeOptions     = ["typical","atypical"]
DurationOptions = [250,500,750]
trial_list = data.createFactorialTrialList({"ColorWord": ColorOptions, "FontColor": ColorOptions, "Type" : TypeOptions, "Duration": DurationOptions})

# insert the design into the TrialHandler
trials = data.TrialHandler(trial_list, nReps = 10, method = "fullRandom")

# Loop over the trials
for trial in trials:
    print("New trial!")
    print(trial["ColorWord"])
    print(trial["FontColor"])
    print(trial["Type"])
    print(trial["Duration"])

