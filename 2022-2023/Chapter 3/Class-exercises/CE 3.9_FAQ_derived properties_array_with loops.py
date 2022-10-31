# displaying Stroop stimuli

# import modules
import numpy, pandas

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
CongruenceLevels = numpy.array(["Incongruent", "Congruent"])
Congruence = numpy.array([])
for i in range(len(FontColor)):
    CongruenceBoolean = ColorWord[i] == FontColor[i]
    Congruence = numpy.append(Congruence, CongruenceBoolean*1)

# deduce the correct response
CorResp = numpy.copy(FontColor)
for i in range(len(FontColor)):
    if CorResp[i] == "red":
        CorResp[i] = "d"
    elif CorResp[i] == "blue":
        CorResp[i] = "f"
    elif CorResp[i] == "green":
        CorResp[i] = "j"
    elif CorResp[i] == "yellow":
        CorResp[i] = "k"

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp])
print(trials)
