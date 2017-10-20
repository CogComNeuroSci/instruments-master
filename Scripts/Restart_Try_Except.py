############
## import ##
############

import sys
import csv
from random import shuffle

## In the following, we will work with a slightly edited version of the code found in 'Try_Except.py'
## By using the code below, we want to solve a problem that occured in 'Try_Except'
## More specifically, we want to work around the occurence of an error, and we want to automatically restart a procedure when an error is encountered
    ## Because maybe you are thinking right now: 'Why on earth would I need that?', we provide a few situations where this knowlegde could be useful
        ## You want to initialise some variables (like we are doing below), but you made a mistake and now an error occurs
            ## It could be that you need these variables later on, so your code will be stuck if something happens
            ## Therefore, trying untill the variables are initialized the way they should be might be useful
        ## You are working with unstable code (sometimes it works, sometimes it does not) you received from a friend/colleague 
            ## Reading someone else's code might be difficult: unordered code, weird indentation, impractical operations etc.
            ## Because of this, retrying until it works might come in handy
                ## At least for a short instance, debugging will be needed later on of course
        ## You need to restart multiple blocks of code during your experiment/program
            ## The code below is obviously useful in program handling
                ## i.e. letting your code do what has to be done
                ## In addition, it makes your code cleaner, and thus easier to read (for friends & colleagues for example...)

## Below, we define the same variables as before:
    ## a list with five numbers in it, called 'data'
    ## another list with six numbers in it, which will be used to define the index which will be used to pull an element from 'data'
        ## Of course, pulling the element situated on index '5' will yield problems, as there is no index 5
            ## 'data' only has five elements, not six
    ## This was done to create an 'IndexError'
# If this sounds new to you, please take a look at 'Try_Except.py'
    # Also take a look at this code and the provided explanation if you forgot what the commands 'try' and 'except' actually do

data = []
for i in range(5):
    data.append(i)

index_list = [i for i in range(len(data)+1)]

## Below, we define a function called 'WriteData'
    ## Two arguments have to be defined to make the function work:
        ## InputList, which is the list with the numbers, we called it 'data' in the code above
            ## The numbers in this list are written away to an external file
        ## IndexList, which is the list which provides the index
            ## We write the numbers in InputList away line by line
            ## Which numbers are written depends on IndexList
                ## If IndexList consists of the following numbers:
                    ## [4, 2, 0, 5, 1, 3]
                ## This means that first the fifth (4+1) element of InputList is written away, then the third (2+1) element of InputList etc.
                ## An error will occur when the fourth element of IndexList is encountered
                    ## There are no six elements in InputList, so the 'IndexError' will be issued
## Note that we do not use 'Try' and 'Except' in the WriteData function (in contrast with the code in 'Try_Except.py')
## Also note that the shuffle occurs WITHIN WriteData, and not OUTSIDE WriteData (again, in contrast with the code in 'Try_Except.py')

## What we basically do by using WriteData is the following:
    ## We have an input list, and an index list
    ## We shuffle the index list
    ## We write each element in the input list to an external file (row by row, see 'Write_Data_Row.py' if this looks new to you) based on the elements in the index list 
    ## Sooner or later an 'IndexError' will occur, and the function will be broken down

## What we want to do is the following:
    ## We want to shuffle 'IndexList' until no error is issued
    # In other words, we want WriteData() to cycle until all elements in InputList can be written away, without an error issue ever occuring
        # Or from another perspective, WriteData() is repeated (and thus the shuffle() is repeated) until '5' is the last element in 'IndexList'
            # This of course also means that no error will occur

## So, the function below (WriteData()) is used to write the data to an external file

def WriteData(InputList,IndexList):
    shuffle(IndexList)
    with open("WriteFile_Restart_Try_Except.txt", 'w') as f:
        for i in range(len(data)):

            index = IndexList[i]

            number = InputList[index]
            print number 

            writer = csv.writer(f, delimiter='\t')
            writer.writerow([number])

## The function AttemptFunction() is used to repeat 'WriteData()' until no errors are issued
## Try (no pun intended) to understand the function, if you are stuck, feel free to read the explanation just below
    ## As we absolutely adore data analysis and data logging, we first define a logging file
        ## We use this logging file to keep track of how many times an error occured
            ## We do this by defining a variable called 'errorcount', which is incremented by 1 every time we use the code located within the 'except' clause
                ## Thus, errorcount goes up with 1 if an error is encountered
        ## Additionally, we can also use the loggingfile to write away the type of error, and the error message

## The function has to cycle until a solution is reached, thus, the best way to accomplish this is to use 'while True', as this condition is always met
        ## To stop cycling (i.e. we accomplished what we wanted), a simple 'break' can be used
    ## Next, we use 'try except'
        ## We try the WriteData function, if this works out from the first try, we skip to the 'else' statement, and we break from the while loop
            ## Note that this means that '5' is the last element in IndexList from the first try
            ## Chances are slim that this happens, but it is of course possible
        ## Chances are higher that an error occurs, so we have to execute the code within the 'except' clause
            ## The print statement is for the output, this gives us an idea how many times the except clause is ran, only by glancing at the output 
            ## The four statement below the print should be clear:
                ## We first define the name of the error
                    ## e.g. '<type 'exceptions.IndexError'>'
                ## Then, we define the error explanation given by Python
                    ## e.g. 'list index out of range'
                ## We write this data to the logging file, along with the errorcount
                ## At last, we increment errorcount with 1
    ## Finally, if the try is succesful (maybe after many trials), we can execute the code within the 'else' clause
        ## This 'break' (as aforementioned) breaks out of the 'while True' loop, and will end AttemptFunction

## We recommend looking at ""LoggingFile_Restart_Try_Except.txt" and "WriteFile_Restart_Try_Except.txt" to see for yourself what exactly happens
# We want to remember from this code that this approach makes sure that a certain procedure/code is repeated until a certain condition is met
    # The procedure to repeat here: shuffle(IndexList)
    # The condition that has to be met: the except clause that is skipped (no error occuring)
## Obviously, this some procedure can also be used in other contexts:
    ## Repeat a certain procedure a fixed number of times (using a for loop, instead of 'while True')
    ## Repeat until another condition is met
        ## e.g. more than 3 elements are written to the external file (you could use csv.reader() to read "WriteFile_Restart_Try_Except.txt", and then determine the length)
        ## Then, we could use an if clause to determine when to break the while True loop
# Just remember that we can use this method in a variety of settings

def AttemptFunction():
    with open("LoggingFile_Restart_Try_Except.txt", 'w') as f:
        errorcount = 1
        writer = csv.writer(f, delimiter='\t')
        while True:
            try:
                WriteData(data,index_list)
            except:
                print '---'
                e1 = sys.exc_info()[0]
                e2 = sys.exc_info()[1]
                writer.writerow([errorcount, e1, e2])
                errorcount += 1
            else:
                break

AttemptFunction()

## As a final remark, we note that this code may be a bit advanced
    # You should feel good if you completely understand everything/the majority of the explanation described above of course!
    ## However, we note that it might be difficult to implement this approach when creating an experiment
## We believe that showing this is beneficial, as it shows what can be accomplished using Python,, but then again, it is difficult to use 'in real life'
## If things are still a bit fuzzy, we refer to:
    ## the code on randomization (e.g. 'Lesson_8_function_randomize_latin.py'), as this focuses on functions
    ## Again, 'Try_Except.py' might also lend some useful insights
## Finally, for those who seek some challenge, we refer to
    ## https://stackoverflow.com/questions/17533104/restarting-a-program-after-exception
    ## This code is used to return exception values in general (outer) functions
        ## This would mean that AttemptFunction() is embedded in outer function, and the errors issued in AttemptFunction() are then used in this outer function
    # This is obviously more advanced material, but for those who want to suffer, there is always more

#########
## END ##
#########
