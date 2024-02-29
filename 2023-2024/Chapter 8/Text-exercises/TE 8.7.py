import numpy, pandas

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

# repeat the 4-by-4 design ten times
trials = numpy.tile(trials, (10, 1))

# completely random trial order
numpy.random.shuffle(trials)

# creating pandas dataframe from numpy array
dataFrame = pandas.DataFrame.from_records(trials)

# name the columns
dataFrame.columns = ["Duration", "Type", "ColorWord", "FontColor"]

# cross all thecore trial characteristics
print(pandas.crosstab([dataFrame.ColorWord, dataFrame.FontColor], [dataFrame.Type, dataFrame.Duration]))
