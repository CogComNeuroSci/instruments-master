
# moving between data formats (by way of illustration)
# by Tom Verguts, March 2019

import numpy as np
import pandas as pd
import collections as cl

# example 1
# from array to list of dicts (via pandas dataframe)
n_levels_factor1 = 4
n_levels_factor2 = 4

Factor1 = np.array(range(n_levels_factor1))
Factor2 = np.array(range(n_levels_factor2))
Nunique= n_levels_factor1*n_levels_factor2
UniqueTrials = np.array(range(Nunique))
Condition1   = np.floor(UniqueTrials/ (len(Factor1)))
Condition2   = np.floor(UniqueTrials/1)% len(Factor2)
Conditions = np.column_stack((Condition1, Condition2))
print(Conditions)

Conditions_pd = pd.DataFrame(Conditions)
Conditions_pd.columns = ["Factor1", "Factor2"]
print(Conditions_pd)

Conditions_list = pd.DataFrame.to_dict(Conditions_pd, orient = "records")
print(Conditions_list)

# example 2
# from handmade list of dicts (i.e., not created via createFactorialTrialList) to pandas dataframe
positions = ["left", "right"]
ColorOptions = ["red","blue","green","yellow"]
Design = []
subject_nr = 3
handedness = "Left"
for loop_position in positions:
    for loop_word in ColorOptions:
        for loop_font in ColorOptions:
            #Design.append({"subject": subject_nr, "ColorWord": loop_word, "FontColor": loop_font, "position": loop_position, "Handedness": handedness}) # does not work
            Design.append(cl.OrderedDict({"subject": subject_nr, "ColorWord": loop_word, "FontColor": loop_font, "position": loop_position, "Handedness": handedness})) # does work

dataFrame = pd.DataFrame.from_dict(Design)
dataFrame.columns = ["subject", "ColorWord", "FontColor", "position", "Handedness"]
print(dataFrame)
print(pd.crosstab(dataFrame.ColorWord, dataFrame.FontColor))