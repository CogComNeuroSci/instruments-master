from psychopy import data

# make the 4-by-4 factorial design
ColorOptions = ["red","blue","green","yellow"]
trial_list = data.createFactorialTrialList({"ColorWord": ColorOptions, "FontColor": ColorOptions})
print(trial_list)
