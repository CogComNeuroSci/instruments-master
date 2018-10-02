###########
## Lists ##
###########

## Lists are combinations of variables
## The most important thing we need to keep in mind is that lists can contain different types of variables

number_list = [1, 2, 3, 4, 5]
letter_list = ["a", "b", "c", "d"]
print(number_list)
print(letter_list)

## Now we will focus on some functions that are available for lists
## We only describe a few of the functions we can use to change lists
## Keep in mind that there is plenty more to discover

## Slicing: select certain items from a list
    ## Select the first item of a list
    ## Select the second, third and fourth item of the list, the fourth included
    ## Selecting the second item, counting from right to left
    ## Selecting all items, from the second until the end (end included) 

print(number_list[0])
print(letter_list[1:5])
print(letter_list[-2])
print(number_list[1:])

## We can select certain values in lists, and replace them 

number_list[0] = 20
print(number_list)

## Delete certain items

del(number_list[0])
print(number_list)

## Concatenation
subset1 = [1, 2, 3]
subset2 = [4, 5, 6]
set = subset1 + subset2
print(set)

## Repeat a list
## In this particular example, the list is repeated 4 times
    ## Mind that this is no mathematical computation: we do not multiply every item with 4
    ## We just repeat the list n amount of times

rep = subset1 * 4
print(rep)


########################
## Logical statements ##
########################

## Returns True if the statement is correct, returns False if the statement is wrong
## For example, we have a '3' in subset1, therefore the statement will return a True here

logical1 = 3 in subset1
print(logical1)

## However, we have no '5' in subset1, therefore the statement will return a False here

logical2 = 5 in subset1
print(logical2)


#################
## Neat tricks ##
#################

## Get the maximum and the minimum value of a list

print(max(subset2))
print(min(subset2))

## Return how many times an object is seen in a certain list
## Here, we see that the item '1' is located one time in the list subset1

print(subset1.count(1))

## Again, we have a lot of functions that can be used to alter lists
## We refer to the Python documentation for further information on lists
    ## https://docs.python.org/2/tutorial/datastructures.html

## In the following, we will provide some functions that are available for lists
## Of course, we will only provide a short overview of some of the most important/handy functions

## An object can be added at the end of a list
## This is called 'append()', but is basically a synonym for 'add this element at the end'

element = 6
list = [1, 2, 3, 4, 5]

print(list)

list.append(element)
print(list)

## Similar to the function 'append()' we also have the function 'extend()'
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
    ## Again, remove() is very handy when we want to delete an item and we do not know the index
        ## e.g. we want to delete the '100', but we don't know where it is situated
    ## However, we will be unable to delete all the '100' items in the list using one single command

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
## Note that when we order a list with words in it, it will of course be ordered alphabetically

list = [200, 500, 200, 100, 200, 500, 400, 300, 200, 300, 300, 100, 400, 100, 500]
list.sort()
print(list)

list = ["wild feverfew","hummingbird sage flower","desert sage","butterfly weed","violet snowdrop","blue wooly curls","red sage","golden currant"]
list.sort()
print(list)

## These are (in our opinion), the most relevant functions that are available for lists in Python
## We encourage that you explore further functionalities for yourself
    # You never explore too much about programming!
    # Learning extra information on how you can accomplish something will only make things easier in the future when a problem pops up!

#########
## END ##
#########