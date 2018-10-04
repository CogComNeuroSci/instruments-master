import numpy

my_array = numpy.array([1, "a", True])
print(my_array)
print(my_array[1])
print(type(my_array))

my_list = [1, "a", True]
print(my_list)
print(my_list[1])
print(type(my_list))


my_array = numpy.array([[1, 2, 3], [4, 5, 6]])
print(my_array)
print(my_array[1,2])

my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
#print(my_list[1,2]) # note that this syntax is not valid!
print(my_list[1])
print(my_list[1][2])

my_array = numpy.array([1, 2, 3, 4, 5])
print(my_array*3)

my_list = [1, 2, 3, 4, 5]
print(my_list*3)