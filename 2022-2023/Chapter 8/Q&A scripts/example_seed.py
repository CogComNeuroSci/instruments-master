# seed example
# by Tom Verguts, March 2023

import numpy

trials = numpy.array([0, 1, 2, 3, 4])

#numpy.random.seed(seed = 1999)
numpy.random.shuffle(trials)
print(trials)