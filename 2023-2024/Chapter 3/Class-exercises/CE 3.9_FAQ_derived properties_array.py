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
CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean   = numpy.array(ColorWord == FontColor)
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]

# deduce the correct response
CorResp = numpy.copy(FontColor)
CorResp[CorResp == "red"]     = "d"
CorResp[CorResp == "blue"]    = "f"
CorResp[CorResp == "green"]   = "j"
CorResp[CorResp == "yellow"]  = "k"

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp])
print(trials)