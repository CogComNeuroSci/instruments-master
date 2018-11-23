# displaying Stroop stimuli

# import modules
import numpy

# we start with adding the values for the words and the colors
ColorWord   = [ "red", "red", "red", "red",
                "blue", "blue", "blue", "blue",
                "green", "green", "green", "green",
                "yellow", "yellow", "yellow", "yellow"]
FontColor   = [ "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow"]

# deduce the congruence
CongruenceLevels = ["Incongruent", "Congruent"]
Congruence = []
for i in range(len(FontColor)):
    CongruenceBoolean = ColorWord[i] == FontColor[i]
    Congruence.append(CongruenceBoolean*1)

# deduce the correct response
CorResp = []
for i in range(len(FontColor)):
    if FontColor[i] == "red":
        CorResp.append("d")
    elif FontColor[i] == "blue":
        CorResp.append("f")
    elif FontColor[i] == "green":
        CorResp.append("j")
    elif FontColor[i] == "yellow":
        CorResp.append("k")

# easy way to see all combinations of trial properties?
# combine arrays in trial matrix anyway
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp])
print(trials)
