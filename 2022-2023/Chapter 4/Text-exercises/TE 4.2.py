### Iterate over a list
my_list = ["a",1]

for i in my_list:
    print(i)

for i in range(len(my_list)):
    print(my_list[i])


### Iterate over a tuple
my_tuple = ("a",1)

for i in my_tuple:
    print(i)

for i in range(len(my_tuple)):
    print(my_tuple[i])


### Iterate over an array
import numpy
my_array = numpy.array(my_list)

for i in my_array:
    print(i)

for i in range(len(my_array)):
    print(my_array[i])