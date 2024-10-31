import numpy

my_array = numpy.array([[1, 2, 3], [4, 5, 6]])
print(len(my_array))
print(my_array.shape)
print(my_array.size)

my_list = [[1, 2, 3], [4, 5, 6]]
print(len(my_list))
# some more advanced programming skills are needed to extract the total number of elements from nested lists (flatten the list and then apply len())