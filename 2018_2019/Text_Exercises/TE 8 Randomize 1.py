from psychopy import data

# make the 4-by-4 factorial design
ColorOptions = ["red","blue","green","yellow"]
trial_list = data.createFactorialTrialList({"ColorWord": ColorOptions, "FontColor": ColorOptions})

# repeat the 4-by-4 design two times
trials = data.TrialHandler(trial_list, nReps = 2, method = "fullRandom")
print(trials)
