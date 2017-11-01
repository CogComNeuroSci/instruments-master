#############
## Integer ##
#############

## A very basic variable is the integer, which represents natural numbers (e.g., 0, 1, 2, ...)
## Here, we defined an integer by assigning a number to a variable name
    ## We conveniently named our variable 'number'
## By printing the type of 'number', we can see that 'number' has the type 'int', which is short for 'integer'

number = 7
print(type(number))

## We can do basic computations on integers
## Below, we provide a few examples


##############
## Addition ##
##############

## NOTE: Every computation will yield the same result

## As is the case in normal arithmetic, the order of the elements does not matter when adding
    ## In other words: a+b and b+a will have the same outcome
        ## The correct term for this property is 'commutativity'

a = 6
b = 13
c = a+b
print(c)

a = 6
c = a+13
print(c)

c = 6+13
print(c)


#################
## Subtraction ##
#################

## NOTE: Every computation will yield the same result

## Here, obviously, the order of the elements does matter

a = 33
b = 13
c = a-b
print(c)

a = 33
c = a-13
print(c)

c = 33-13
print(c)


####################
## Multiplication ##
####################

## NOTE: Every computation will yield the same result

## As is the case in normal arithmetic, the order of the elements does not matter when multiplying

a = 7
b = 3
c = a*b
print(c)

a = 7
c = a*3
print(c)

c = 7*3
print(c)


##############
## Division ##
##############

## NOTE: Every computation will yield the same result

## Here, obviously, the order of the elements matter

a = 88
b = 4
c = a/b
print(c)

a = 88
c = a/4
print(c)

c = 88/4
print(c)

# Python interprets / on integers as long division (e.g., 7/2 = 3).
# If you don't like it, you can import a different definition of division as follows:
# (see the additional script named Lesson_5_data_types_division for an example)
# from __future__ import division
# print(7/2) # becomes standard division
# print(7//2.0) # remains long division


####################
## Exponentiation ##
####################

## NOTE: Every computation will yield the same result

## If we want an exponentiation, we first define the base number (5 in this case), then we write '**', and finally we write the exponent (2 in this case)
## We can remember this computations by imagining that we multiply the base number n times with itself
    ## 5**2 = 5*5
    ## 5**4 = 5*5*5*5

a = 5
b = 2
c = a**b

print(c)

a = 5
c = a**2

print(c)

c = 5**2

print(c)

#################
## Square root ##
#################

## Note that there is no specific function for square root (unless we import the package 'math', then we have 'math.sqrt()')
## When we did not import 'math', we create the square root of a number by doing the number to the power (.5)
    ## The square root of a number can be seen as the inverse of doing that number to the power of two
    ## Therefore,  taking the square root can be seen as doing a number to the power "1/2" (which is the inverse of 2 (2**(-1)) )

c = 16**(.5)

print(c)

## NOTE: the type of this output will be 'float', which is a number that has a value after the comma
## a = 4
    ## print a
## This above code would yield '4' as output, and the type of 'a' would be 'int'
## b = float(a)
    ## print b
## This code in turn would yield '4.0' as output, and the type of 'b' would be 'float'

###############
## Remainder ##
###############

## The remainder can be seen as what remains after a division
## Example: if we divide 18 by 5, the remainder is 3 (15/5 is possible, 3 remains)
## Example: if we divide 102 by 10, the remainder is 2 (100/10 is possible, 2 remains)

c = 18%5

print(c)

c = 102%10

print(c)

############
## String ##
############

## Strings represent a letter/word/sentence
## Again, we can determine the type of a variable by using type()

letter = 'M'
print(type(letter))

word = 'Monty'
print(type(word))

sentence = "The name 'Python' originates from Monty Python"
print(type(sentence))

## We can do some basic operations on the strings we define
## For convenience, we note down some of these basic operations

## Changing between upper and lower case
    ## Keep in mind that these operations DO NOT change the original string: Sparta itself will stay unaltered after the .lower and .upper operations

Sparta = 'ArE yOu NoT eNtErTaInEd?'
print(Sparta)

print(Sparta.lower())
print(Sparta.upper())

print(Sparta)

## Returning the length of a string
print(len(Sparta))

## Could how many times a specific letter/word is included in a string
    ## ! Mind that this operation is case sensitive !
        ## If we would define 'e', the answer would be 1
        ## If we would define 'E', the answer would be 3

print(Sparta.count("e"))
print(Sparta.count("E"))

## Select a certain part of a string
print(Sparta[4:7])

## Check whether a string starts with a certain word or not
    ## Again, this is case sensitive
    
print(Sparta.startswith("Are"))
print(Sparta.startswith("ArE"))

## Splitting a sentence into words
## We can also return specific words using this operation

SpartaSplit = Sparta.split(" ")
print(SpartaSplit)

print(SpartaSplit[0])

## Formatting examples, showing another way to print variables
## Explanation of the code we see below:
    ## Print position 0, then 1, then 2
    ## Print position 2, then 1, then 0
    ## Print position 2, then 1, then 0 (other notation)
    ## Print 0, then 1, then 0, yielding 'abracadabra'

print('{0}, {1}, {2}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format('a', 'b', 'c'))
print('{2}, {1}, {0}'.format(*'abc'))
print('{0}{1}{0}'.format('abra', 'cad'))

## This is only a subset of the operations we can perform on strings
## For more operations, we refer to the documentation on Python:
    ## https://docs.python.org/3.4/library/string.html
## If we want to do something using strings, we can of course google it
    ## Stackoverflow is a website which is often used when small problems are encountered during programming

###########
## Lists ##
###########

## Lists are combinations of variables
## The most important thing we need to keep in mind is that lists can contain different types of variables

number_list = [1, 2, 3, 4, 5 ]
letter_list = ["a", "b", "c", "d"]

print(number_list)
print(letter_list)

## Now we will focus on some functions that are available for lists
## We only describe a few of the functions we can use to change lists
## Keep in mind that there is plenty more to discover

## Slicing: select certain items for a list
    ## Select the first item of a list
    ## Select the second, third and fourth item of the list, the fourth included
    ## Selecting the second item, counting from right to left
    ## Selecting all items, from the second untill the end (end included) 

print(number_list[0])
print(letter_list[1:5])
print(letter_list[-2])
print(number_list[1:])

## We can select certain values in lists, and replace them 

number_list[0] = 20
print(number_list)

## Delete certain items

del number_list[0]
print(number_list)

## Concatenation
subset1 = [1, 2, 3]
subset2 = [4, 5, 6]
set = subset1 + subset2
print(set)

## Repeat a list
## In this particular example, the list is repeated repeated 4 times
    ## Mind that this is no mathematical computation: we do not multiply every item with 4
    ## We just repeat the list n amounts of times

rep = subset1 * 4
print(rep)

## Logical statements
## Returns True if the statement is correct, returns False if the statement is wrong
## Here, we have a 3 in subset1, therefore the statement will return a True here

logical1 = 3 in subset1
print(logical1)

## Here, we have no 5 in subset2, therefore the statement will return a False here

logical2 = 5 in subset1
print(logical2)

## Get the maximum and the minimum value of a list

print(max(subset2))
print(min(subset2))

## Returns how many times an object is seen in a certain list
## Here, we see that the item '1' is located one time in the list subset1

print(subset1.count(1))

## Again, we have a lot of functions that can be used in to alter lists
## We refer to the Python documentation for further information on lists
    ## https://docs.python.org/2/tutorial/datastructures.html

## In the following, we will provide some functions that are available for lists
## Of course, we will only provide a short overview of some of the most important/handy functions

## An object can be added at the end of a list
## This is called 'append', but is basically a synonym for 'add this element at the end'

element = 6
list = [1, 2, 3, 4, 5]

print(list)

list.append(element)
print(list)

## Similar to the function 'append()' we als have the function 'extend()'
    ## This function will also append elements to an already existing list 
## The major difference between the two is that:
    ## append will add elements at the end of the list
        ## Here, the element will be added just as it is: a list will remain a list
            ## Therefore, if a list is added at the end of list, we will still see the list in its original form, not just the elements of the list at the end
    ## extend will just add the elements
        ## If we extend a list with another list, only the elements will be added, not the list in its entirety

## To illustrate, we provide an example
    ## We see that the results of these two operations are different:
        ## append will add the entire list
            ## The result is
            ## [1, 2, 3, 4, 5, [6, 7]]
            ## Thus, the added element stays in its original form: a list
        ## extend will adds the elements of the list:
            ## The result is
            ## [1, 2, 3, 4, 5, 6, 7]
            ## Thus, the elements of the list are glued to the list, not the list itself
## We should keep this in mind when we use one of the two operations

list = [1, 2, 3, 4, 5]
list.append([6,7])

print(list)

list = [1, 2, 3, 4, 5]
list.extend([6,7])

print(list)

## We can easily find out how many times an element occurs in a certain list by using the function 'count()'
## For example, here we want to find out how many times a '0' occurs in the list
## Because counting this by hand would be a bit difficult (and prone to errors), we can use count()
    ## The result is '7'
        ## Meaning that we have seven zeros in the list 'long_list'

long_list = [0, 1, 2, 3, 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0, 20, 21, 22, 23, 0, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 0, 36, 0, 38, 39, 40, 41, 42, 43, 0, 45, 46, 47, 48, 49, 50, 51]

print(long_list.count(0))

## If we want to insert certain elements in a list, we can use the function 'insert()'
## In the function we have to define two parameters:
    ## The index where the element is added
    ## What is inserted in the list 
## To illustrate, we define an example:
    ## list.insert(2, 100)
        ## Here, we will insert '100' in the list, after index '2'
            ## In other words, the '100' will appear in the third (! zero-based indexing !) place of the list
            ## The other items will of course remain in the same order

list = [1, 2, 3, 4, 5]
list.insert(2,100)

print(list)

## If we want to delete certain items from a list, we can use the function pop()
## By default, the last item in the list is deleted
## By adding a parameter between the brackets, we can delete other elements
    ## Below, we delete the third element
## Note that we cannot use pop() to delete multiple items at the same time

list = [1, 2, 3, 4, 5]
list.pop()

print(list)

list = [10, 20, 30, 40, 50]
list.pop(2)

print(list)

## We can also use remove() to delete a certain item from a list
## Keep in mind that only one element is deleted
    ## So, in the first lines below, only the first '100' is deleted
    ## Again, remove is very handy when we want to delete an item and we do not know the index
        ## e.g. we want to delete the '100', but we don't know where it is situated
    ## However, we will be unable to delete all the '100' items in the list using one single command
## For deleting one element, remove() can be very useful
    ## Especially as we are not obliged to define the index, as is the case with pop()

list = [100, 200, 300, 100, 400, 100, 500]
list.remove(100)

print(list)

list = [100, 200, 300, 100, 400, 100, 500]
list.remove(200)

print(list)

## Maybe less interesting for us, but still worthy noting, we can also reverse the elements in a list

list = [100, 200, 300, 100, 400, 100, 500]
list.reverse()

print(list)

## The last function we mention can sort the elements in a list
## In the particular case, the items are ordered numerically, with the smallest item on the far left, and the largest on the far right
## Note that when we order a list with words in it, it will be of course order alphabetically

list = [200, 500, 200, 100, 200, 500, 400, 300, 200, 300, 300, 100, 400, 100, 500]
list.sort()

print(list)

list = ['wild feverfew','hummingbird sage flower','desert sage','butterfly weed','violet snowdrop','blue wooly curls','red sage','golden currant']
list.sort()

print(list)

## These are (in our opinion), the most relevant functions that are available for lists in Python
## We encourage that you explore further functionalities for yourself
    # You never explore too much about programming!
    # Learning extra information on how you can accomplish something will only make things easier in the future when a problem pops up!

############
## Tuples ##
############

## Tuples are sequences, just like lists
## When declaring tuples, the only difference with lists is that tuples use parentheses, whereas lists use square brackets
    ## Note that the default is a tuple, so a = 'a','b','c' will be a tuple!
    ## When we want a list, we should explicitly use []
## A very important difference between tuples and lists is that the elements in tuples cannot be changed afterwards (in Python terms: tuples are immutable)
    ## Immutable means that the items in the collection cannot be altered after they are initialised
    ## To explain, we create two collections of items: a list and a tuple:
        ## list = ['a','b','c','d']
        ## tuple = 'a', 'b', 'c', 'd'
    ## In the list, we can change individual items by assigning a new value to that place in the list:
        ## list[0] = 'e'
    ## print(list) will yield the following result:
        ## ['e', 'b', 'c', 'd']
            ## We see that the first item is changed, just as we wanted
            ## In Python terms: a list is mutable, as the items in the list can still be changed afterwards
    ## In the tuple, we can also try to change the first value:
        ## tuple[0] = 'e'
    ## When we try to print the tuple, we will see the following error:
            ## tuple[0] = 'e'
        ## TypeError: 'tuple' object does not support item assignment
    ## In other words: tuples do not support the replacement of one element by another value
    ## That tuples are immutable makes them very handy if we want to make sure that values are not changed due to some error or anomalie when running the code
    ## On the other hand, mutable data types such as lists have as an advantage that you can change/replace values as you see fit
## Depending on your purpose, you might want to use tuples or lists

tup1 = ('Instruments of Experimental Psychology', 'Cognitive Psychology I', 2017, 2018)
tup2 = (1, 2, 3, 4, 5 )
tup3 = 'a', 'b', 'c', 'd'

print(tup1)
print(tup2)
print(tup3)

## If we want to empty the tuple, we can just write the name of the tuple, and equate it with ()
## If we only want to assign one value to a tuple, we assign that value, and write a comma after it
    ## If we would neglect the comma, we would have assigned a string or integer to the variable name, not a tuple
    ## In other words, the type of the variable would be 'int' or 'string', not 'tuple'
        ## If this is not clear to you, try the following:
            ## tup1 = (50,)
            ## print type(tup1)
            
            ## tup1 = (50)
            ## print type(tup1)

tup1 = ()
print(tup1)

tup1 = (50,)
print(tup1)

tup1 = (50)
print(tup1)

## To select certain values in a tuple, we can use the same notations we used when manipulating lists
## The first one gives the following output:
    ## Instruments of Experimental Psychology
## The second one gives the following output:
    ## (2, 3)
## Keep in mind that the type of the output differs:
    ## If one item is select, it will have the type you would expect ('Instruments of Experimental Psychology' is a string, '2017' is an integer)
    ## If we select multiple items, the type of the output will be a tuple!
        ## Remember that tuples are immutable, so replacing values in this output will be impossible!

tup1 = ('Instruments of Experimental Psychology', 'Cognitive Psychology I', 2017, 2018)
tup2 = (1, 2, 3, 4, 5 )
tup3 = 'a', 'b', 'c', 'd'

print(type(tup1[0]), (tup1[0]))
print(type(tup2[1:3]), (tup2[1:3]))

## We can alter tuples by glueing already existing tuples together
## Keep in mind that this only works for tuples!
    ## Trying to concatenate (glue together) a string and a tuple will not work out
    ## Knowing this, we can also predict that the code 'tup4 = tup1[0]+tup2[1:3]' will not work
        ## This because 'tup1[0]' is a string, and combining strings (or integers) and tuples is a bad idea

tup4 = tup1[0:2]+tup2[1:3]
print(tup4)

## Deleting a tuple is pretty straightforward, as we can use a function we defined before: del
## We can delete an entire tuple, but not specific elements (again, because tuples are immutable)

del(tup4)

## Other basic operations already mentioned with lists can also be used on tuples
## Below, we define a few examples

print(len(tup1))

print('a' in tup3)
print('j' in tup3)

## To convert a list to a tuple, we can use tuple()
## This mechanism is the same as list(), where we convert something to a list

##################
## Dictionaries ##
##################

## Dictionaries have an easy setup
## They are contained using curly brackets ( {} )
## All items within the dictionary are seperated by commas. 
## An item consists of a key and a value
## These values can be called by their corresponding key.
## For example, we can define a key called 'Function', and when we print 'dictionary['Function']', we will see the value associated
## to that key.
## In this case, we will see 'Student', as the item 'Function': 'Student' was defined in the dictionary
## Of course, we cannot call items that are not defined in the dictionary
## To illustrate, we try to print what is stored in the key 'University'
## Uncomment to see what happens

dictionary = {'Function': 'Student', 'Age': 21, 'Bachelor': 3}

print(dictionary)

print("Function: ", dictionary['Function'])
print("Age: ", dictionary['Age'])
## print "University: ", dictionary['University']

## To update a dictionary, we simply link a new value with the key 

dictionary['Age'] = 22
dictionary['School'] = 'Ghent University'

print("Age: ", dictionary['Age'])
print("School: ", dictionary['School'])

## When you don't need the items in the dictionary anymore, you can do some operations to delete items in the dictionary
## Alternatively, you can also delete the entire dictionary  using a simple operation
    ## To remove a specific entry, we can use the del() function
    ## To remove all entries in a dictionary, we can use clear()
        ## The print will yield an empty dictionary, visualised by '{}'
    ## To remove the entire dictionary, we can also use del
        ## The final print statement will yield a NameError, as 'dictionary' will be seen as undefined
            ## This is of course the case because the dictionary was deleted 
## Specific examples of each implementations can be seen below

del(dictionary['School'])
print(dictionary)

dictionary.clear()
print(dictionary)

del(dictionary)
##print dictionary

## Dictionaries have some advantages, however, there are also some major disadvantages
## An example is the issue with the definition of the name of the keys
## To illustrate, we define a dictionary which has 'school' two times as a Key name in it
    ## When this is the case, the last definition wins
    ## In the code below for example, the value 'Stark' is the last variable assigned to the key 'Name'
    ## Therefore, this is the value that is printed when the key 'Name' is called

dictionary = {'Name': 'Bran', 'Name': 'Stark', 'Call': 'Winter is coming'}

print("Name: ", dictionary['Name'])

## A last remark is that the names of the keys must consist of immutable (unchangeable) objects
## Because of this property, the names of the keys must be a string, integer or a tuple
## When the key name is a list (which is mutable), an error will be issued
## We provide an example below to illustrate 
    ## As the name of the key is a list, the following error will occur
        ## TypeError: unhashable type: 'list'
        ## Uncomment to see for yourself

dictionary = {'First name': 'Bran', 'Last name': 'Stark', 'Call': 'Winter is coming'}
print(dictionary)

WrongKeyName = ['First name']
print(type(WrongKeyName), WrongKeyName)

## dictionary_error = {WrongKeyName: 'Bran', 'Last name': 'Stark', 'Call': 'Winter is coming'}
## print dictionary_error

## That were the main remarks on dictionaries
## We note that other functions still are available
## We provide a short rundown on some of the most eminent functions

## Returns whether a certain key is in your dictionary
    ## False if it not defined in the dictionary
    ## True if it is defined

print(dictionary.has_key('Name'))
print(dictionary.has_key('First name'))

## Get an overview of all the keys and what value is stored in the key
## Returns pairs of the keys and their associated value

print(dictionary.items())

## Get an idea about the keys you defined in your dictionary
## No associated values are printed here

print(dictionary.keys())

## To get an idea about the values we have in the dictionary, we can use the function values()

print(dictionary.values())

## Of course, other functions are available
    ## We encourage to discover these for yourself
## When in doubt about properties/functions of dictionaries
    # Google is your friend!

#########
## END ##
#########
