############
## Import ##
############

from __future__ import division


#########################################
## Errors issued when printing strings ##
#########################################

## words, letters and sentences cannot be printed when they are not put between quotes
## print(Hi there)

## If we put a statements that consists of letters between '' or "", this can be printed without problems
print("Hi there")

## Note that in this case, the statement is put between '", which is bad, it should be '' or ""
## print('Hi there")

## This statement is not printed because the brackets are not closed
## print("Hi there"


#######################
## printing integers ##
#######################

## Printing numbers is more or less the same as printing text, although we do not need '' or "" to print our value
number = 10
print(number)

## We now discuss some formatting issues
## In the line of code below, we print a decimal number
## More specifically, we say to PsychoPy that 'The number is ..' should be printed, and a number should be inserted where the 0 is situated
## Which number is inserted depends on the variable defined at the back of the line of code, specified by format()
## So, here we insert what is defined as 'number'
## Number was 10, so the sentence that will be printed is:
## "The number is 10"
## Try replacing the 10 with another numerical value to see what will happen!

print("The number is {0}".format(number))

## The zero between {} indicates that this is the first number (Python starts counting at zero).
## Actually, because there is just one number, the explicit rank order 0 is not required and we can write

print("The number is {}".format(number))

## The formating of strings allows a great deal of flexibility for writing to the screen. Here is another example:
number1 = 1
number2 = 3
total = number1 + number2
print("The total of {0} and {1} equals {2}".format(number1, number2, total))
## Can you make sense of this code?

## Another way to use the format string is for control over nice floating point representations.
print("nice number {:.2f}".format(number1/number2))
##This :.2f code says that the format should be such that there are two decimal-value digits. 

## We can also use format() to represent percentages. We do it as follows:
print("percentage is {:%}".format(number1/number2))


#########
## END ##
#########