##################
## while loop 1 ##
##################

print("# While loop 1 #")

## The while loop greatly resembles the for loop in the sense that it performs a certain action until a certain condition is fulfilled
## The example while loop below shows that a certain string is printed until the value 5 is reached
## Translated in words, we could say that the while loop "prints the integer 'i', as long as i is smaller than 5"
## Going through the first iteration:
    ## i equals 0 (defined by the programmer)
    ## 'while i is smaller than 5' is true in this case, so the statements in the loop will be executed
    ## This means that i is printed, and we add 1 to i
    ## Adding a value is also called 'incrementing', so here i is 'incremented' with 1
## Consequently, at the start of the second iteration, i would equal 1
## The loop continues until the statement 'i<5' is not longer 'True' (hence it becomes 'False')
## 'True' and 'False' are actually 'Boolean' statements
## A more general definition of while loops could be that the loop repeats as long as a certain Boolean condition is met

i = 0
while i < 5:
    print(i)
    i = i + 1


##################
## while loop 2 ##
##################

print("# While loop 2 #")

## Another notation for the incrementation can be seen below
## The statement 'i = i+1' is exactly the same as 'i += 1' as we saw in Lesson 5

i = 0
while i < 5:
    print(i)
    i += 1


##################
## while loop 3 ##
##################

print("# While loop 3 #")

## We can set the start value at any value, and the while loop will do an action as long as a certain condition is fulfilled
## If we would replace 'i = 0' with 'i = 6', the while loop would not be executed, as the condition 'i < 5' is not met
## In the output, we would see nothing, except the title '# While loop 3 #'

i = 6
while i < 5:
    print(i)
    i = i + 1

## Please note that the while loop will also be neglected if we replace 'i = 6' by 'i = 5'
## This is the case because the while loop will only execute when i is SMALLER than 5, which is not the case here 

i = 5
while i < 5:
    print(i)
    i = i + 1

## if we now replace 'while i < 5:' with 'while i <= 5:', our while loop will execute once
## Why is this the case?
    ## Because now, the loop will execute when i is smaller than 5, but also when i EQUALS 5
## Thus, we will see '5' printed here

i = 5
while i <= 5:
    print(i)
    i = i + 1


##################
## while loop 4 ##
##################

## We can use more complex criteria, for example by requiring one of two criteria to be met to execute the commands in the while loop.
## To do this we insert "or" between the two criteria.

print("# While loop 4.1 #")

i = 0
j = 10
while i < 5 or j > 3:
    print("i is {0} and j is {1}".format(i,j))
    i = i + 1
    j = j - 2

## Alternatively we can require that both criteria are met to execute the commands in the while loop.
## This can be done by adding "and" between the two criteria.

print("# While loop 4.2 #")

i = 0
j = 10
while i < 5 and j > 3:
    print("i is {0} and j is {1}".format(i,j))
    i = i + 1
    j = j - 2


##################
## while loop 5 ##
##################

print("# While loop 5 #")

## To get more familiar with Boolean expressions, let's just print a Boolean answer in the output window.
## As i clearly equals i, the answer is of course 'True'

print(i == i)

## You can also look at it like this
## This block tries to explain the Boolean nature of the while loop using the loop illustrated in 'while loop 1'

## First iteration
Condition0 = 0<5
print(Condition0)

## Second iteration
Condition1 = 1<5
print(Condition1)

## As we can see, both conditions evaluate as 'True'
## The while loop will do everything that is stated in the loop as long as the condition check evaluates as 'True'

## Where the while loop stops
Condition5 = 5<5
print(Condition5)

## As we notice here, this condition check evaluates as 'False', therefore the loop will stop, and nothing will be printed
## This example can be seen as a deeper view into the mechanism of the while loop 


##################
## while loop 6 ##
##################

print("# While loop 6 #")

## A possible danger when working with while loops is that we can create infinite loops
## An example of this can be seen when the loop executes during a condition which is always met
## Below, we have included an example of a while loop that never ends
    # Please do not uncomment the loop below, as your computer will not be able to escape the loop
## Try to find out for yourself why the loop never stops

#j = 0
#while j < 5:
#    print(j)

## Answer:
    ## The condition is always met as there is no incrementation: j equals 0 in the first iteration, but nothing is added
    ## This causes j to always be 0, and thus to always be smaller than 5
    ## Therefore, the loop will never end
    ## This is why forgetting incrementation will lead to problems in your code


#########
## END ##
#########