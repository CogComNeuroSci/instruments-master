import numpy

# declare all levels of the factor
ColorOptions    = numpy.array(["red","blue","green","yellow"])
TypeOptions     = numpy.array(["typical","atypical"])

# determine the number of levels for the factor
Ncolors     = len(ColorOptions)
Ntypes      = len(TypeOptions)
Nunique     = Ncolors * Ncolors * Ntypes

# determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

# make the factorial design
Type        = numpy.floor(UniqueTrials / (Ncolors*Ncolors))
ColorWord   = numpy.floor(UniqueTrials / Ncolors) % Ncolors
FontColor   = numpy.floor(UniqueTrials / 1) % Ncolors

# combine arrays in trial matrix
trials = numpy.column_stack([Type, ColorWord, FontColor])

# export as a tab separated file
numpy.savetxt("Stroop_FactorialDesign_4.txt", trials, delimiter = "\t", fmt = "%.0d")
