import numpy

# generate 12 participant numbers (starting from 1 instead of 0)
ppnrs = numpy.array(range(1,13))
 
# divide 12 participants across two conditions
print(ppnrs % 2)
# divide 12 participants across four conditions
print(ppnrs % 4)
