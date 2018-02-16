# Code for arrow cueing experiment randomization
# by Esther De Loof & Tom Verguts, feb 2018

from psychopy import data
import random
import pandas as pd
import numpy as np


# make the 2-by-2-by-2 factorial design
left_right = ["left", "right"]
Design = data.createFactorialTrialList(
    {"Direction": left_right, "Position": left_right, "Word": left_right})
print(Design)


# convert the list of dictionaries to a dataframe for inspection
dataFrame = pd.DataFrame.from_dict(Design)
print(dataFrame)


# repeat the 2-by-2-by-2 design ten times
Extended = pd.concat([dataFrame]*10, ignore_index = True)
print(Extended)


# randomize the trial order
index = list(Extended.index)
random.shuffle(index)
Random = Extended.iloc[index]
print(Random)


# cross table validation (approach 1)
print(pd.crosstab(Random.Direction, [Random.Position, Random.Word]))
print(pd.crosstab([Random.Direction, Random.Position], Random.Word))


# cross table validation (approach 2)
print(pd.pivot_table(Random, index=["Direction"], columns=["Position", "Word"], aggfunc=len))
print(pd.pivot_table(Random, index=["Direction", "Position"], columns=["Word"], aggfunc=len))


# Add additional information
Random["Congruence_DP"] = Random["Direction"] == Random["Position"]
Random["Congruence_DW"] = Random["Direction"] == Random["Word"]
Random["Congruence_PW"] = Random["Position"] == Random["Word"]
Random["FullCongruence"] = (Random["Direction"] == Random["Position"]) & (Random["Direction"] == Random["Word"])
Random["TrialNumber"] = range(len(Random.index))
Random["CorAns"] = Random["Word"]
Random["CorAns"].replace(["left", "right"], ["f","j"], inplace = True)
print(Random)