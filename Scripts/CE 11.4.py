# Code for arrow cueing experiment randomization
# by Esther De Loof & Tom Verguts, feb 2018

from psychopy import data
import random
import pandas as pd
import numpy as np


# make the 2-by-2 factorial design and convert to a dataframe
left_right = ["left", "right"]
Design = data.createFactorialTrialList(
    {"Word": left_right, "Position": left_right})
dataFrame = pd.DataFrame.from_dict(Design)


# repeat the basic 2-by-2 design 5 times (as 1/5 trials will be incongruent)
Extended = pd.concat([dataFrame]*5, ignore_index = True)


# extract the trial indices
index = list(Extended.index)


# add the colums with the word information
Extended["Direction"] = "m"
Extended["Congruence"] = [int(indexi / 4 != 0) for indexi in index]


# fill in the Direction based on the Congruence and Word information
Extended.loc[ Extended["Congruence"]==1, "Direction"] = Extended.loc[Extended["Congruence"]==1, "Word"]
Extended.loc[(Extended["Congruence"]==0) & (Extended["Word"] == "left" ), "Direction"] = "right"
Extended.loc[(Extended["Congruence"]==0) & (Extended["Word"] == "right"), "Direction"] = "left"


# randomize the trial order
index = list(Extended.index)
random.shuffle(index)
Random = Extended.iloc[index]


# add additional information
Random["Congruence_DP"] = Random["Direction"] == Random["Position"]
Random["Congruence_DW"] = Random["Direction"] == Random["Word"]
Random["Congruence_PW"] = Random["Position"] == Random["Word"]
Random["FullCongruence"] = (Random["Direction"] == Random["Position"]) & (Random["Direction"] == Random["Word"])
Random["TrialNumber"] = range(len(Random.index))
Random["CorAns"] = Random["Word"]
Random["CorAns"].replace(["left", "right"], ["f","j"], inplace = True)
print(Random)


# cross table validation
print("Balancing between position and word")
print(pd.crosstab(Random.Position, Random.Word))
print("Congruence and the mapping between Word and Direction")
print(pd.crosstab([Random.Direction, Random.Word], Random.Congruence))