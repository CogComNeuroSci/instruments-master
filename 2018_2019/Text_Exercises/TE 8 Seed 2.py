import numpy

# seed for the numpy array
numpy.random.seed(seed = 4)

# declare all levels of the factor
ColorOptions = numpy.array(["red","blue","green","yellow"])

# determine the number of levels for the factor
Ncolors = len(ColorOptions)
Nunique = Ncolors * Ncolors

# determine the number of unique trials
UniqueTrials = numpy.array(range(Nunique)) 

# make the factorial design
ColorWord = numpy.floor(UniqueTrials / Ncolors)
FontColor = numpy.floor(UniqueTrials / 1) % Ncolors

# combine arrays in trial matrix
trials = numpy.column_stack([ColorWord, FontColor])

# repeat the 4-by-4 design two times
trials = numpy.tile(trials, (2, 1))

# completely random trial order
numpy.random.shuffle(trials)

# export as a tab separated file
numpy.savetxt("Stroop_Seed_1.txt", trials, delimiter = "\t", fmt = "%.0d")
