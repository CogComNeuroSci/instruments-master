# displaying Stroop stimuli

# import modules
import numpy

# we start with adding the values for the words and the colors
ColorWord   = numpy.array([ "red", "red", "red", "red",
                            "blue", "blue", "blue", "blue",
                            "green", "green", "green", "green",
                            "yellow", "yellow", "yellow", "yellow"])
FontColor   = numpy.array([ "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow"])

# deduce the congruence
## I start by assuming that all trials are incongruent.
Congruence = numpy.repeat('Incongruent', len(ColorWord))
## ColorWord == FontColor creates a boolean mask. Each position in Congruence where the mask is True will be replaced by 'Congruent' 
Congruence[ColorWord == FontColor] = 'Congruent'

# deduce the correct response
## I'll now use the same strategy of using True and False values to determine the correct response.
## For instance to detect on which trials the d key is the correct answers because the font color is red
print(FontColor == "red")
## I can now use these True and False values to determine of each element in the array FontColor whether I want to use it (True) of not (False)
## For instance, here I only print the value of the items in FontColor that equal red
print(FontColor[FontColor == "red"])
## and here I only print the value of the items in FontColor that are NOT equal to red
print(FontColor[FontColor != "red"])

## Basically, I want to make a copy of the FontColor array and replace all the red values with d, all the blue values with f and so on.
## Unfortunately, what I can't do is this:
#CorResp = FontColor
#CorResp[CorResp == "red"] = "d"
#print(CorResp)
#print(FontColor)
## Why? Because CorResp and FontColor are both pointing towards the same array of values 
## so changing values in CorResp will also change the values in FontColor.
## The solution is to use numpy.copy() to make a copy of FontColor that is independent from the original FontColor array
## (at least that is what google suggested me)
CorResp = numpy.copy(FontColor)
print(CorResp)

## Now I can proceed with my plan of selecting all the items that are equal to red, and replacing them by the value d
CorResp[CorResp == "red"] = "d"
print(CorResp)
print(FontColor)
## As you can see, the red values are replaced by d in the CorResp array, but the FontColor array stays unaltered
## We can now do the same for the other values
CorResp[CorResp == "blue"]    = "f"
CorResp[CorResp == "green"]   = "j"
CorResp[CorResp == "yellow"]  = "k"

## last but not least, we clean up all the print statements and end up with these five elegant lines of code:
#CorResp = numpy.copy(FontColor)
#CorResp[CorResp == "red"]     = "d"
#CorResp[CorResp == "blue"]    = "f"
#CorResp[CorResp == "green"]   = "j"
#CorResp[CorResp == "yellow"]  = "k"

# combine arrays in trial matrix
#trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp])
#print(trials)