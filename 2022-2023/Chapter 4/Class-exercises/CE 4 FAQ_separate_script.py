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
CongruenceLevels    = numpy.array(["Incongruent", "Congruent"])
CongruenceBoolean   = numpy.array(ColorWord == FontColor)
Congruence          = CongruenceLevels[[CongruenceBoolean*1]]

# deduce the correct response
CorResp = numpy.copy(FontColor)
CorResp[CorResp == "red"]     = "d"
CorResp[CorResp == "blue"]    = "f"
CorResp[CorResp == "green"]   = "j"
CorResp[CorResp == "yellow"]  = "k"

# allow to store the accuracy
Accuracy = numpy.repeat(-99.9,len(CorResp))

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence, CorResp, Accuracy])

# try for one trials
i = 0

# determine accuracy
trials[i,4] = int(trials[i,3] == "d")

# determine the feedback message
if int(trials[i,4]) == 1:
    Feedback_text = "Correct!"
else:
    Feedback_text = "Wrong answer!"

print(Feedback_text)


# try for a few trials
for i in range(3):

    # determine accuracy
    trials[i,4] = int(trials[i,3] == "d")
    
    # determine the feedback message
    if int(trials[i,4]) == 1:
        Feedback_text = "Correct!"
    else:
        Feedback_text = "Wrong answer!"
    
    print(Feedback_text)