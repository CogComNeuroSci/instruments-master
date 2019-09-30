import numpy as np
import pandas as pd
import time
import math

from datetime import datetime

#######################
## manipulate data 1 ##
#######################

print('# manipulate data 1 #')

## To create a matrix in Python in an easy fashion, we can use 'list comprehension'
## To illustrate what this means, we look at an example adopted from 'http://www.python-course.eu/list_comprehension.php'
## In this simple example, we see that we can create a new list by easily altering the values in an already existing list
## The list Fahrenheit is created by multiplying the values in the list Celsius and adding a constant
## In this way, we can efficiently manipulate values in a list without having to type every single calculation
## Note that this operation is in essence a For loop, although it doesn't look like one syntactically 
## Also note that the result of this computation is a list, and not a matrix
    ## We will want to convert it to a needed type if we want to do certain computations on the data 

Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)

#######################
## manipulate data 2 ##
#######################

print ('# manipulate data 2 #')

## In the following, we will create a matrix (so, no list here) which is completely filled with all numbers from 0 to 7 (7 included)
## We can create a list filled with collections of the numbers, and use the command 'np.matrix()' to convert the list to a matrix
## Please note the difference between the types before and after conversion, and the difference in output between 'a' and 'matrix'

a = []
for x in range(8):
    row = []
    for y in range(8):
        row.append(y)
    a.append(row)

print(type(a)), (a)

matrix = np.matrix(a)
print(type(matrix)), (matrix)

#######################
## manipulate data 3 ##
#######################

print('# manipulate data 3 #')

## Do note that there are two major ways to represent data: matrices and arrays
    ## Both have their advantages and disadvantages, but usually it is recommended to use arrays
    ## The short answer on this matter (adopted for the SciPy documentation, explanation on why to use arrays):
        ## They are the standard vector/matrix/tensor type of numpy. Many numpy function return arrays, not matrices.
        ## There is a clear distinction between element-wise operations and linear algebra operations.
        ## You can have standard vectors or row/column vectors if you like.
    ## Additionally:
        ## Matrices are strictly 2-dimensional, while numpy arrays (ndarrays) are N-dimensional
    ## As we can see, these points all try to show us that arrays are superior to matrices

    ## However, keep in mind that matrices also have some advantages:
        ## Matrices provide a convenient notation for matrix multiplication: if a and b are matrices, then a*b is their matrix product
        ## Both matrices and arrays can be transposed using .T , but matrix objects also have .H for the conjugate transpose, and .I for the inverse

   ## For the interested reader: for the long answer on this matter, we refer to the SciPy documentation:
        ## https://docs.scipy.org/doc/numpy-dev/user/numpy-for-matlab-users.html#head-e9a492daa18afcd86e84e07cd2824a9b1b651935
    ## Also, on Stackoverflow, they talked about the difference between arrays and matrices:
        ## https://stackoverflow.com/questions/4151128/what-are-the-differences-between-numpy-arrays-and-matrices-which-one-should-i-u
        
    ## The text written above adopted some of the explanations from both stackoverflow and the SciPy doc
    
## For convenience, we will work with arrays from now on, as these are easier to manipulate 

#######################
## manipulate data 4 ##
#######################

print('# manipulate data 4 #')

## We will use the matrix we defined earlier, and convert it to an array
## Below, we first convert the matrix to an array
## Secondly, we select the rows and columns of the array and print them out
    ## Keep in mind that in Python, the first element is depicted by a 0, and not a 1
    ## Note that the column of the array is also printed as a row
    ## Also note that the select data is still an array, so if we want to make a list/matrix of it, we should convert it
## Additionally, we also identify the length of the rows and columns (how many elements do we have in them) by using the function 'len()'

array = np.array(matrix)
print(type(array)), (array)

print('---')

FirstRow = array[0,:]
ThirdRow = array[2,:]

print(type(FirstRow)), (FirstRow)
print(type(ThirdRow)), (ThirdRow)

print('---')

FirstColumn = array[:,0]
ThirdColumn = array[:,2]

print(type(FirstColumn)), (FirstColumn)
print(type(ThirdColumn)), (ThirdColumn)

print(len(FirstColumn))
print(len(FirstRow))

#######################
## manipulate data 5 ##
#######################

print('# manipulate data 5 #')

## Individual number elements in arrays (keep in mind that arrays can also hold complex numbers and strings AND that arrays can contain mixed data types) are integers
## This is a very useful characteristic, as it allows us to do mathematical computations on specific elements
## In the first example, we see that the value on the first row and in the second column is replaced by an integer
## In the second example, we see that some mathematical operations are performed on this integer
## The third example shows that we can directly change all values in an array at once by defining that every number with a specific value has to be replaced by another value
## The fourth example explains how we change the values of entire rows and columns, which depends on the same mechanism as selecting a row/column
## The last example shows how to transpose an array
    ## Transposing means that the columns become rows, and the rows become columns

array[0,1] = 18
print(array)

print('---')

array[0,1] = (array[0,1]*2)/6 - 10
print(array)

print('---')

array[array == 2] = 10
print(array)

print('---')

array[:,0] = 20
array[0,:] = 30

print(array)

print('---')

TransposedArray = np.transpose(array)
print (TransposedArray)

#######################
## manipulate data 6 ##
#######################

print('# manipulate data 6 #')

## When we want to delete a certain value from an NumPy array, we can use the function np.delete()
## You can do this by using the index
    ## The index can be returned by using the function .index
## In our first example, we delete items based on the position: we delete the items in the second, third and sixth position
## In the second example, we show that we can find the index of specific items, based on their value
    ## For convenience, we return to the old array we defined in the beginning of the code
    ## We can replace a value we want to ignore with a value of which we know that this value cannot happen (such as -1 for reaction times)
    ## In the later analysis, we can then filter this value out

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print (a)

index = [2, 3, 6]

new_a = np.delete(a, index)
print(new_a)

print('---')

a = []
for x in range(8):
    row = []
    for y in range(8):
        row.append(y)
    a.append(row)

matrix = np.matrix(a)
array = np.array(matrix)

array[array == 3] = -1
print(array)

#######################
## manipulate data 7 ##
#######################

print('# manipulate data 7 #')

## How to print a sequence of number
    ## Just printing a sequence
    ## Just a sequence from 0 to 8 appended to a list
        ## Remember that 8 is not included here
    ## A sequence ranging from 20 to 25 (again, 25 not included) appended to a list
    ## A sequence that ranges from 0 to 25 with steps of 5 appended to a list
    ## Going backwards/counting down appended to a list

for i in range(10):
    print(i)

numberSeq = []
for i in range(8):
    numberSeq.append(i)

print(numberSeq)

numberSeq = []
for i in range(20,25):
    numberSeq.append(i)

print(numberSeq)

numberSeq = []
for i in range(0,25,5):
    numberSeq.append(i)

print(numberSeq)

numberSeq = []
for i in range(100,0,-5):
    numberSeq.append(i)

print(numberSeq)

## Repeat a certain value a number of times
## Note that repeating an action a couple of times requires a loop

list = [1]
RepList = list*62
print(RepList)

list = ['Why repeat?']
RepList = list*62
print(RepList)

## Bind lists together
## This also works with integers
    ## Why isn't the first code working? Don't think too much about it!
        ## Hint: determine the type of the variables by using print type()
## Keep in mind that a list cannot contain both integers and strings at the same time
        ## A dictionary could be used for this 

firstname = 'John'
lastname = ' Shepard'

name = firstname + lastname
name.split
print(name)

Birthday = 11
Birthmonth = 4
Birthyear = 2154

fullBirth = Birthday+Birthmonth+Birthyear
print(fullBirth)

Birthday = [11]
Birthmonth = [4]
Birthyear = [2154]

fullBirth = Birthday+Birthmonth+Birthyear
print(fullBirth)

## You can also concatenate rows and columns of a vector using np.column_stack()
## An example of column concatenation can be seen below
    ## https://stackoverflow.com/questions/14314501/bind-columns-from-vectors-for-numpy
## We see that we bind a and b together in a column-like fashion, meaning that we will have two columns with (0,1) in it
## For row binding, we can use np.concatenate()
    ## https://docs.scipy.org/doc/numpy/reference/generated/numpy.concatenate.html

a = np.array([[1, 2]])
b = np.array([[3, 4]])
array = np.column_stack((a,b))
print(array)

a = np.array([[1, 2]])
b = np.array([[3, 4]])
array = np.concatenate((a, b), axis=0)
print(array)

## Check whether a number is 'NaN'
    ## Note: this function requires the import of 'math'
## A decent explanation for NaN is offered on wikipedia (https://en.wikipedia.org/wiki/NaN)
    ## "In computing, NaN, standing for not a number, is a numeric data type value representing an undefined or unrepresentable value, especially in floating-point calculations
    ##  Systematic use of NaNs was introduced by the IEEE 754 floating-point standard in 1985, along with the representation of other non-finite quantities like infinities"

number = float('NaN')
print(math.isnan(number))

#######################
## manipulate data 8 ##
#######################

print('# manipulate data 8 #')

## Logical operations
    ## prints 'True' if the statement is logically true, prints 'False' if not true 
        ## '<' and '>' are known signs
        ## '==' means that the code checks whether the values left and right from this sign are the same
        ## '!=' means that the code checks whether the values left and right from this sign are different
    ## Boolean values can also be converted to integers, with True equal to 1, and False equal to 0
## Remainder
    ## Check whether there is a remainder after a division or not
    ## Can be used as an integer, or as a Boolean statement
## Rounding of numbers and truncation
    ## round, ceil, floor and trunc
    ## Some examples can be found on: https://www.tutorialspoint.com/python/number_round.htm

print(6 > 5)
print(5 > 6)
print(6 == 6)
print(5 == 6)
print(5!= 6)

statement1 = 6 > 5
statement2 = 5 > 6

print(int(statement1))
print(int(statement2))

remainder = (10%4)
print(remainder)
print(remainder == 0)

int = 80.23456

print(round(int, 2))
print(round(int, 4))

print(math.ceil(int))
print(math.floor(int))

print(math.trunc(int))

#######################
## manipulate data 9 ##
#######################

print('# manipulate data 9 #')

## Using loops to alter data 
## The first approach may seem as the most intuitive way to replace values, however keep in mind that other approaches (such as using indexation, or list comprehension) are equally effective
## Below, we illustrate how to replace some values in a list by using a for loop with if statements, and by using list comprehension
## We also time both processes, and see that there are some differences in execution time between the two:
    ## The for loop is slower than the list comprehension
    ## Although this delay is not really a problem, it might be a problem when you want to measure time really precisely
    ## It also might be a problem when you have a lot of processes that require processing, and the time needed to compile the entire program piles up
    ## Because of this, we encourage to use code that is 'efficient' in the sense that it doesn't take long to execute

sentence = 'A master has failed more times than a beginner has tried'.split()
print(sentence)

t1 = datetime.now()
time1 = t1.microsecond

for words in sentence:
    a = words.upper()
    b = words.lower()
    c = len(words)
    d = [a,b,c]
    print(d)
    
t2 = datetime.now()
time2 = t2.microsecond

print('Time to execute in microseconds: %d')%(time2-time1)

print('---')

t1 = datetime.now()
time1 = t1.microsecond

new = [[words.upper(), words.lower(), len(words)] for words in sentence]
for i in new:
     print(i)

t2 = datetime.now()
time2 = t2.microsecond

print('Time to execute in microseconds: %d') %(time2-time1)

#########
## END ##
#########
