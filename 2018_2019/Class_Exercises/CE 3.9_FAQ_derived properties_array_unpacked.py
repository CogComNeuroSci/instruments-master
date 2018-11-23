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
## let's start with comparing the color words and font colors one by one
## for each of the 16 comparisons this gives us a True or False answer (boolean answers)
print(ColorWord == FontColor)
## For each True answer, I want to call that 'Congruent' and each False answer needs to become 'Incongruent'
## I know that the True and False answers have the value 1 and 0, respectively
## I want to use those 0 and 1 values as indices to refer to Incongruent and Congruent in the following array:
CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
## For example for the first four trials:
print(CongruenceLevels[[1,0,0,0]])
## Let's try this with the boolean answers to see whether this works:
#print(CongruenceLevels[[True,False,False,False]])
## Damn, an error message: boolean index did not match indexed array along dimension 0; dimension is 2 but corresponding boolean dimension is 4
## Maybe I'll have to explicitly convert the True and False values to 1 and 0
## After some googling, I found this:
print(numpy.array([True,False,False,False])*1)
## Note that the True and False values need to be stored in an array!
## Only when they are stored in an array can you convert them to 0 and 1 by multiplying with 1
## When they are stored in a list, the *1 is interpreted as 'repeat this list once' (see Chapter 3 where we already discussed this!)
## So let's first store the True and False answers in an array
CongruenceBoolean   = numpy.array(ColorWord == FontColor)
print(CongruenceBoolean)
## Convert them to 0 and 1
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]
print(Congruence)

## last but not least, we clean up all the print statements and end up with these three elegant lines of code:
#CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
#CongruenceBoolean   = numpy.array(ColorWord == FontColor)
#Congruence          = CongruenceLevels[[CongruenceBoolean*1]]

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