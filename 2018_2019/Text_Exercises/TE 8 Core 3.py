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

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor])

# export as a tab separated file
numpy.savetxt("Stroop_FactorialDesign_3.txt", trials, delimiter = "\t", fmt = "%.0d")