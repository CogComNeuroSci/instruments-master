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

## Here, obviously, the order of the elements matters

a = 88
b = 4
c = a/b
print(c)

a = 88
c = a/4
print(c)

c = 88/4
print(c)


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
## When we do not import 'math', we create the square root of a number by exponentiating the number to the power (.5)
    ## The square root of a number can be seen as the inverse of exponentiating that number to the power of two
    ## Therefore,  taking the square root can be seen as exponentiating a number to the power "1/2" (which is the inverse of 2 (2**(-1)) )

c = 16**(.5)
print(c)

## NOTE: the type of this output will be 'float', which is a number that has a value after the comma
## a = 4
    ## print(a)
## The code above would yield '4' as output, and the type of 'a' would be 'int'
## b = float(a)
    ## print(b)
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


#########
## END ##
#########