############
## import ##
############

import sys
import csv
from random import shuffle

## One of the most common frustrations when learning how to program is the occurence of errors
## Probably, by now you are familiar with the 'SyntaxError'
## An example to refresh your mind
    ## print Hello world
    ##      ^
    ## SyntaxError: invalid syntax
## As this is a very common (but very special) error, we will return later in this code to this issue

## Luckily, there is a way around errors, a procedure which is called 'Handling Exceptions'
## An example to clarify
    ## The division 'x/0' is an undefined operation
        ## Without going into detail: there is no 'x' which will give 'x' when multiplied with 0
            ## Because of this, trying to define x/0 will result in an error issue 
        ## The error can also be seen on an ordinary calculator when you try to divide a number by 0
        ## Here in Python, the 'ZeroDivisionError' will appear
            ## 'ZeroDivisionError: integer division or modulo by zero' will be displayed in the output when you try to print e.g. '10/0'
## When we want to go around this error, we can use 'try except'
    ## The try function literally 'tries' to do a specific operation
        ## If the operation works out, then everything within the try clause will be executed, and everything is fine
            ## This try function can be conceptualized as an if statement
                ## The try function does everything within its clause (just as is the case with the if statement)
                ## However, when the clause yields an error, the except clause is evaluated
                    ## When the problem, and the solution to the problem is defined in the 'except'-clause, this will be executed
                    ## If there is no solution provided, an error will be displayed in the output, just as would be the cause without the try-except

## To explain, we look at the block of code below
    ## In the try function we define a division using two previously defined numbers
    ## In this try clause, we do the division and print the result of the division
        ## When the division is possible, the result is printed
        ## Here, z (the result of the division) is a normal integer, so z is printed without problems
        ## The except clause is neglected, as the try clause was compiled without issues

(x,y) = (5,5)

try:
    z = x/y
    print z
except ZeroDivisionError:
    print "divide by zero"

## Now, we look at the block of code below this explanation
    ## Here, we try the same thing as we did in the block above: we want to do a division between two previously defined numbers 
    ## Here, the problem is that we try to divide by zero
    ## The result of this is that the try function cannot be completed
    ## Therefore, Python will try to compile the except clause
        ## In this except clause, we defined that when the specific error 'ZeroDivisionError' is yielded, Python should print 'divide by zero' in the console
        ## However, when another error is issued, the except function will also not work out 
            ## For example: when a SyntaxError is the problem, this error issue will be printed in the console
            ## Only the specific error 'ZeroDivisionError' will result in the printing of 'divide by zero'

(x,y) = (5,0)

try:
    z = x/y
    print z
except ZeroDivisionError:
    print "divide by zero"

## Usually, what we want to do is catch a specific error
    ## For example, when we ask participants to press specific keys for answering in the experiment, we can expect that some participants use the wrong key
    ## To solve this problem, we can choose two paths:
        ## Use if statements to make sure that a message is displayed when the wrong key is pressed
            ## Think about 'if answer[0] not in ['d','j']:' ...
        ## Alternatively, we could use try except to do something specific when a 'KeyError' is generated
    ## Which approach to use depends on the specific situation
        # Remember: if it works, you are doing fine!
    ## Generally speaking, we encourage to think about possible flaws/misinterpretations in your experiment as much as possible
        ## Think what participants may do wrong, and try to make sure that participants do not have the possibility to make stupid mistakes
            ## For example, when they should only use 'd' and 'j' to answer, make sure that the other keyboard buttons are disabled during the experiment
        ## Try except should be used as an absolute exception, something you never thought of but still happened
            ## Most mistakes made by participants can be foreseen, and prevented
                # Try except could be implemented as the final 'safety net' of your code, to prevent your experiment from crashing due to some stupid error issue
## Returning to the main point, what we want to do is generate specific scenarios for specific problems:
    ## When the wrong key is pressed (KeyError), we want to display a message that says 'Only use the 'd'- and 'j'-keys
    ## When participants are asked to fill in their age in numbers, but they start using letters (TypeError), we want a message that says 'Only use number keys to fill in age'
## However, if we tried our very best to prevent errors from happening, and still and error occurs, we of course have no idea about the specific type of error that just occured
    ## Therefore, we could never prepare a specific message
## Luckily, we can catch every error that occurs, and display a specific message when an error occurs
    ## The good thing about this approach is that it will work for EVERY type of error that may occur
    ## The bad thing about it however is that you can only work with general messages ('Oops, and error occured!'), as the specific type of error is unknown to you
## This method can be used when you did your very best to avert error issues, but still something went wrong
## The block of code below shows us how the type of error, and the error message can be printed, although we did not predefine a specific error in the except statement
    ## Thus, not that no error (such as 'ZeroDivisionError') is defined here
    ## e1 and e2 can of course be written to an external file, if this would be needed

(x,y) = (5,0)

try:
    z = x/y
    print z
except:
    e1 = sys.exc_info()[0]
    e2 = sys.exc_info()[1]
    print("Error name: %s" % e1 )
    print("Error description: %s" % e2 )

## There is one major anomaly when it comes to errors: the SyntaxError
## First, we define what we mean with 'syntax'
    ## Syntax can be seen as the language itself, the 'grammatics' we use to create the code
    ## The dynamic of programming can be seen as communication between the programmer and the computer:
        ## The programmer tells the computer what is needed
        ## The computer provides the programmer with the solution
    ## By typing code, the programmer defines what is needed
        ## Similar to an everyday setting, we cannot understand the someone's needs when that person is talking nonsense
    ## The same happens when a programmers types code that contains errors: the computer does not understand what is needed
    ## This is what happens when a SyntaxError occurs: the computer interrupts the processing of the script and points out what is unclear
    ## Only when the script is fully understood, an output can be provided
    ## A SyntaxError is mainly a way to point out that the script contains errors, and only when these errors are gone, the script can be fully understood

## The SyntaxError occurs when the script is compiled, this means that Python checks the code before it is executed
    ## Thus, SyntaxErrors actually occur before the script is executed, and show that the 'spelling check' (is your command understandable) yields errors
## When there is a 'syntactical' problem (your code is not understood) in the code, the SyntaxError is issued
## Examples of code that would yield SyntaxErrors:
    ## print Hello world
    ## i = 0
    ## while i < 5
        ## print i
        ## i += 1
    ## print ('hello world'
## To understand why SyntaxError is special, we take a short look at computer history
    ## First, we define the term 'interpreted (programming) language'
        ## When a language is interpreted, it means that the instructions the programmer issues are executed directly
            ## When this does not happen, it means that the instructions are first translated into machine-language instructions (which are processed directly by the computers' CPU)
    ## In the beginning, interpreted languages were compiled line-by-line; that is, each line was compiled as it was about to be executed
    ## This practice has become less common, and today, it is very rare
    ## Nowadays, a lot of well-known programming languages combine 'compiling (checking for syntax errors)' and 'interpreting (executing the code)':
        ## JavaScript
        ## Ruby
        ## Also Python combines the two
    ## Thus, because Python first compiles a script, and then executes it, a SyntaxError may occur:
        ## The script is unreadable and cannot be executed before the 'grammar errors' are resolved
            ## print Hello world
            ##      ^
            ## SyntaxError: invalid syntax
            ## The '' should be added to resolve the SyntaxError
        ## Once the SyntaxErrors are taken care of, the script will be compiled succesfully, and executed

## Below, we show how the try except could be used in the setting of writing a file
## As we mentioned before, try except is a last safety net, you should not use it to solve multiple errors that occur
    # Try-except is succesfull when it is not used: if you need it, something in your code went wrong
    ## This situation (writing data) is different from situations where you depend on input from participants (usually at least one participant does something wrong
        ## Then again, this can be prevented by using if statements or other control mechanisms

## In the block of code below, we first define a set of variables by simply looping over a range of numbers
## The variable 'data' contains a list of five variables, ranging from zero to four (zero and four included)
## The variable x contains a list of six variables, ranging from zero to five (zero and five included)
    ## This list is shuffled (elements of list in random order)
## What we try to do is the following:
    ## The with statement is used to write the data away (seen in another lesson, if this is unclear, we refer to the provided code on writing data trial by trial)
    ## In the for loop, we first select the index we want
        ## We do this by selecting each consecutive element of 'index_list'
        ## Note that these values range from zero to five, and are ordered randomly
    ## Then, we select a certain element in 'data' based on 'index'
        ## Thus, if index = 4, we select the fifth item in 'data', which happens to be '4'
        ## If index = 2, we select the third item in 'data', which happens to be (indeed) '2'
        ## However, the fun starts when 'index = 5', as the element on place six in 'data' DOES NOT EXIST
            ## Obviously, this would lead to an error, more specifically, an IndexError
                ## ' IndexError: list index out of range '
                    ## This is the exact error that would appear if we wanted to write the (not existing) sixth element of 'data' to a file
    ## In other words: our code is faulty: an error will always occur
    ## To work around the index error, we use try-except
        ## Try-except will write all the 'good' data to an external file
        ## When an error occurs, this error is written to a 'logging file'
            ## Creating a new file for one line of code may seem pointless, but it makes sense when we write data in e.g. EEG experiments
                ## The main reason for this is that the amount of data written to external files is massive, therefore, multiple errors may occur
                ## By writing the actual data to another file than the error messages we create the opportunity to see really quick where in the data collection something went wrong
                ## Obviously, we write the trialnumber away with the error message, so we see which trials we want to check/throw away
                    ## Note that in this case, we know what type of error to expect, however, we can also write away general error messages as we have seen in the code above
                    ## Using that approach, we are shielded against possible occurences of error occurences, no matter the type
                # Creating a logging file is good practice, as it helps you to store relevant data in seperate files
                # In that way, we can easily find back information on for example error occurences, experiment timing etc. without having to search in one massive file
        ## Side notes
            ## Keep in mind that the error message will only be written when an IndexError appears, and not when other errors appear
            ## Also keep in mind, that with other errors, the program will crash
    ## Thus, the try-except handles the error pretty well and makes sure that, when an error occurs, the program does not crash, and the error is mentioned in our logging file
    # This type of error could obviously be prevented by checking and debugging your code upfront
    # Make a habit of saving your code often, and compiling it a lot to test for errors popping up
    # Comment out blocks of code to see on which point the error occurs
        # Remember that shortcuts to commenting and uncommenting exist, and are situated under the 'edit'-tab in the upperleft corner

data = []
for i in range(5):
    data.append(i)

print data

index_list = [i for i in range(len(data)+1)]
shuffle(index_list)

print index_list 

with open("WriteFile_Try_Except.txt", 'w') as f:
    try:
        for i in range(len(data)):

            index = index_list[i]

            number = data[index]
            print number 

            writer = csv.writer(f, delimiter='\t')
            writer.writerow([number])

    except IndexError:
        with open("LoggingFile_Try_Except.txt", 'w') as f:
            writer = csv.writer(f,delimiter=' ')
            writer.writerow([i+1,"IndexError"])

#########
## END ##
#########
