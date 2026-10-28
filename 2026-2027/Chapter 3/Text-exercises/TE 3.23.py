import numpy

my_array1 = numpy.array([[1, 2, 3], [4, 5, 6]])
my_array2 = numpy.copy(my_array1)

my_array2[0,1] = 99

print(my_array2)
print(my_array1)