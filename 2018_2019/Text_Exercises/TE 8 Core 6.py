from psychopy import data
import pandas, numpy

# make the 4-by-4 factorial design
ColorOptions = ["red","blue","green","yellow"]
trial_list = data.createFactorialTrialList({"ColorWord": ColorOptions, "FontColor": ColorOptions})

# convert the list of dictionaries to a dataframe for inspection
dataFrame = pandas.DataFrame.from_dict(trial_list)
print(dataFrame)

# we can also quickly convert the dataframe to a numpy array
array = dataFrame.values
print(array)
