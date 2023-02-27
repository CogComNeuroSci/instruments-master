import numpy

# declare all levels of the factor
ColorOptions    = numpy.array(["red","blue","green","yellow"])
TypeOptions     = numpy.array(["typical","atypical"])
DurationOptions = numpy.array([250,500,750])

# determine the number of levels for the factor
Ncolors     = len(ColorOptions)
Ntypes      = len(TypeOptions)
Nduration   = len(DurationOptions)
Nunique     = Ncolors * Ncolors * Ntypes * Nduration

# determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

# make the factorial design
Duration    = numpy.floor(UniqueTrials / (Ncolors*Ncolors*Ntypes))
Type        = numpy.floor(UniqueTrials / (Ncolors*Ncolors)) % Ntypes
ColorWord   = numpy.floor(UniqueTrials / Ncolors) % Ncolors
FontColor   = numpy.floor(UniqueTrials / 1) % Ncolors

# combine arrays in trial matrix
trials = numpy.column_stack([Duration, Type, ColorWord, FontColor])

# export as a tab separated file
numpy.savetxt("Stroop_FactorialDesign_5.txt", trials, delimiter = "\t", fmt = "%.0d") 
