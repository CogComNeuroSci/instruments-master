############
## Tuples ##
############

## Tuples are sequences, just like lists
## When declaring tuples, the only difference with lists is that tuples use parentheses, whereas lists use square brackets
    ## Note that the default is a tuple, so a = 'a','b','c' will be a tuple!
    ## When we want a list, we should explicitly use []
## A very important difference between tuples and lists is that the elements in tuples cannot be changed afterwards (in Python terms: tuples are immutable)
    ## Immutable means that the items in the collection cannot be altered after they are initialized
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
    ## When we try to change the tuple, we will see the following error:
            ## tuple[0] = 'e'
        ## TypeError: 'tuple' object does not support item assignment
    ## In other words: tuples do not support the replacement of one element by another value
    ## The fact that tuples are immutable makes them very handy if we want to make sure that values are not changed due to some error or anomaly when running the code
    ## On the other hand, mutable data types such as lists have as an advantage that you can change/replace values as you see fit
## Depending on your purpose, you might want to use tuples or lists

tup1 = ("Instruments of Experimental Psychology", "Cognitive Psychology I", 2017, 2018)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
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
print(type(tup1))

tup1 = (50)
print(tup1)
print(type(tup1))

## To select certain values in a tuple, we can use the same notations we used when manipulating lists
## The first one gives the following output:
    ## Instruments of Experimental Psychology
## The second one gives the following output:
    ## (2, 3)
## Keep in mind that the type of the output differs:
    ## If one item is selected, it will have the type you would expect ('Instruments of Experimental Psychology' is a string, '2017' is an integer)
    ## If we select multiple items, the type of the output will be a tuple!
        ## Remember that tuples are immutable, so replacing values in this output will be impossible!

tup1 = ("Instruments of Experimental Psychology", "Cognitive Psychology I", 2017, 2018)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

print(type(tup1[0]), (tup1[0]))
print(type(tup2[1:3]), (tup2[1:3]))

## We can alter tuples by gluing already existing tuples together
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

print("a" in tup3)
print("j" in tup3)

## To convert a list to a tuple, we can use tuple()
## This mechanism is the same as list(), where we convert something to a list


#########
## END ##
#########