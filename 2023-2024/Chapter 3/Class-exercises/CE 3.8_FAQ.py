'''
This FAQ script contains some explanation on the use of a list versus an array in the Jasper Francken exercise (CE 3.8).

'''

## import modules
import numpy

# First, let's examine the list solution

## This is the list of scores that you were given:
scores = [12, 13, 9, 18]

## This is the solution you may have found on the Web:
tests_passed = [i for i in scores if i >= 10]
## Or alternatively (if we assume that the scores are integers and can't be decimals):
tests_passed = [i for i in scores if i > 9]

## total of correct items
tot_correct = len(tests_passed)
## total of items
l           = len(scores)

print(f"You passed {tot_correct/l:.0%} of your courses.")

# As an intermezzo, let's unpack that line of code from the Web (especially if you already understand the for-loops and if-statements from Chapter 4):
## this dense line of code uses list comprehension to solve your problem.
## it actually does the same as the following loop structure that is easier to understand.

## first, we start with an empty list where we will store all the scores of the tests that were passed.
tests_passed = []
## We then loop over all the values of scores to check for each of them whether Jasper passed the test
## The index i will consecutively take on the values 12, 13, 9 and 18
for i in scores:
    ## we print out the value of i in this iteration of the loop
    print(f"i = {i}")
    ## we check whether i is larger than 9
    if i > 9:
        ## if is is larger than 9 (Jasper passed the test), this score is added to our list tests_passed
        tests_passed.append(i)
    ## we check the current state of the list tests_passed
    print(tests_passed)
## We end up with the list tests_passed that only contains the scores on tests that were passed successfully


# Second, let's examen the array solution

## you'll first have to convert the list of scores to an array
scores = numpy.array([12, 13, 9, 18])

## 1) test whether the score is larger than 9
## Note that instead of having to loop over all the values in scores as we had to do with the list,
## numpy allows us to get the results for the entire array in one fell swoop
print(scores>9)
## 2) count the number of times that the answer to the above question is True 
## Hint: True = 1 and False = 0, so we can simply sum all the boolean answers that we got in the previous step
print(sum(scores>9))

## from here on, we do the same as in the list approach
## total of correct items (if we assume that the scores are integers and can't be decimals)
tot_correct = sum(scores>9)
## or equivalent:
tot_correct = sum(scores>=10)
## total of items
l           = len(scores)

print(f"You passed {tot_correct/l:.0%} of your courses.")