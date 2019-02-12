import numpy

# declare all levels of the factor
ColorOptions = numpy.array(["red","blue","green","yellow"])

# determine the number of levels for the factor
Ncolors = len(ColorOptions)

# make the factorial design
ColorWord = numpy.repeat(range(Ncolors), Ncolors)
FontColor = numpy.tile(range(Ncolors), Ncolors)

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor])

# export as a tab separated file
numpy.savetxt("Stroop_FactorialDesign_2.txt", trials, delimiter = "\t", fmt = "%.0d") 
