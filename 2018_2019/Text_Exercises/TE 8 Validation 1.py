from psychopy import data
import pandas, numpy

# make the 4-by-4 factorial design
ColorOptions = ["red","blue","green","yellow"]
trial_list = data.createFactorialTrialList({"ColorWord": ColorOptions, "FontColor": ColorOptions})

# convert the list of dictionaries to a dataframe for inspection
dataFrame = pandas.DataFrame.from_dict(trial_list)

# repeat the 4-by-4 design two times
trials = pandas.concat([dataFrame]*2, ignore_index = True)

# completely random trial order
index = list(trials.index)
numpy.random.shuffle(index)
trials = trials.iloc[index]

dataFrame = trials

# cross the color words and font colors
print(pandas.crosstab(dataFrame.ColorWord, dataFrame.FontColor))
