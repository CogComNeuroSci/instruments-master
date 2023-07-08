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
## Below we say to PsychoPy that 'The number is ..' should be printed, and a number should be inserted where {number} is situated
## Which number is inserted depends on the variable defined
## So, here we insert what is defined as 'number'
## Number was 10, so the sentence that will be printed is:
## "The number is 10"
## Try replacing the 10 with another numerical value to see what will happen!

print(f"The number is {number}")

## The f-string formatting allows a great deal of flexibility for writing to the screen. Here is another example:
number1 = 1
number2 = 3
total = number1 + number2
print(f"The total of {number1} and {number2} equals {total}")
## Can you make sense of this code?

## Another way to use f-string formatting is for control over nice floating point representations
print(f"nice number {number1/number2:.2f}")
##This :.2f code says that the formatting should be such that there are two decimal-value digits

## We can also use f-string formatting to represent percentages. We do it as follows:
print(f"percentage is {number1/number2:%}")

#########
## END ##
#########