# displaying Stroop stimuli

# import modules
import time, numpy, pandas

# initialize the variables
nblocks     = 2
ntrials     = 16
participant = 2

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
CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean   = numpy.array(ColorWord == FontColor)
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]

# deduce the task instruction
if participant%2 == 0:
    # participants with an even number have to respond to the color word
    CorResp = numpy.copy(ColorWord)
else:
    # participants with an odd number have to respond to the ink color
    CorResp = numpy.copy(FontColor)

# deduce the correct response
CorResp[CorResp == "red"]     = "d"
CorResp[CorResp == "blue"]    = "f"
CorResp[CorResp == "green"]   = "j"
CorResp[CorResp == "yellow"]  = "k"

# allow to store the accuracy
Accuracy = numpy.repeat(-99.9,len(CorResp))

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp, Accuracy])
print(trials)

# repeat the trial matrix for the two blocks
trials = numpy.tile(trials, (nblocks, 1))

# check some of the trial characteristics
print("participants with an even number have to respond to the word meaning")
print(pandas.crosstab(trials[:,0], trials[:,3]))
print("participants with an odd number have to respond to the ink color")
print(pandas.crosstab(trials[:,1], trials[:,3]))