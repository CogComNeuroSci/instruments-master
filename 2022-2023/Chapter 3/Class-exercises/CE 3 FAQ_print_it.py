import numpy

# make an array
b = numpy.array([[1,2,3],[4,5,6]])
# look at it
print(b)

# test whether this indeed results in second row, third column = 6
print(b[1,2])
# it does

# now let's change its value to 7
b[1,2] = 7

# the 7 should now appear on the second row, third column
print(b)
# it does