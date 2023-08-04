import numpy

# declare all levels of the factor
ColorOptions = numpy.array(["red","blue","green","yellow"])

# determine the number of levels for the factor
Ncolors = len(ColorOptions)
Nunique = Ncolors * Ncolors

# determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

# make the factorial design
ColorWord = numpy.floor(UniqueTrials / Ncolors)
FontColor = numpy.floor(UniqueTrials / 1) %  Ncolors

# deduce the congruence
Congruence = numpy.array(ColorWord == FontColor)

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor, Congruence])

# export as a tab separated file
numpy.savetxt("Stroop_FactorialDesign_5.txt", trials, delimiter = "\t", fmt = "%.0d") 

# all congruency levels
CongruenceLevels = numpy.array(["Incongruent", "Congruent"])

# all response options (in the right order)
ResponseOptions = numpy.array(["d","f","j","k"])

# loop over the trials
for trial in trials:
    print("New trial!")
    print(str("Color Word: " + ColorOptions[int(trial[0])]))
    print(str("Font Color: " + ColorOptions[int(trial[1])]))
    print(str("Congruence: " + CongruenceLevels[int(trial[2])]))
    print(str("Correct response: " + ResponseOptions[int(trial[1])]))
