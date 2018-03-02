"""
Some deconstruction of the list comprehension used in CE 12.5 (solution of Esther)

"""

# import modules
from psychopy import data
import pandas

# initializing
numbers     = range(1,8)
colors      = ["red","green","green"]

# make the basic design and convert to a data frame
Design = data.createFactorialTrialList({"Number": numbers, "Color": colors})
dataFrame = pandas.DataFrame.from_dict(Design)

# add the stimulus type via list comprehension
dataFrame["StimType"] = [int(dataFrame["Color"][i] == "green")*10+dataFrame["Number"][i] for i in range(dataFrame.shape[0])]

print(dataFrame)

# and now the deconstruction of what happens on line 19

## make an empty list
list = []

## determine the number of rows in the data frame
nrows = dataFrame.shape[0]

## loop over the rows
for i in range(nrows):
    
    ## what is the number on this trial
    currentNumber = dataFrame["Number"][i]
    
    ## what is the color on this trial
    currentColor = dataFrame["Color"][i]
    
    ## is the current color equal to "green"
    IsGreenBoolean = currentColor == "green"
    
    ## return 0 when the color is not green and 1 when the color is green (so turn the boolean into an integer)
    IsGreenInteger = int(IsGreenBoolean)
    
    ## for the green stimuli, we will add 10 to the number (1 to 7) to end up with a unique stimulus number
    ## for the red stimuli, we will add 0 to the number (so it stays 1 to 7)
    stimtype = IsGreenInteger*10 + currentNumber
    
    ## add this information to the list
    list.append(stimtype)

## last, we add this to the dataFrame

dataFrame["StimTypeDeconstructed"] = list

print(dataFrame)