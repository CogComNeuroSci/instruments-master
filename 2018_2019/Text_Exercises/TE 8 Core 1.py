import numpy

# declare all levels of the factor
ColorOptions = numpy.array(["red","blue","green","yellow"])

# determine the number of levels for the factor
Ncolors = len(ColorOptions)

# make the factorial design
ColorWord = numpy.repeat(ColorOptions, Ncolors)
FontColor = numpy.tile(ColorOptions, Ncolors)

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor])

# export as a tab separated file
numpy.savetxt("Stroop_FactorialDesign_1.txt", trials, delimiter = "\t", fmt = "%.10s")
