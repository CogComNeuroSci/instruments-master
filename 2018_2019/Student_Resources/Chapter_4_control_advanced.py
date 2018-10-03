#####################
##      break      ##
#####################

print("# break #")

## If-statements can also be used to control the ending of a loop
## The command used to escape from a loop is called 'break'
## We illustrate this example by using a while-loop that would be endless without the break in it

number = 0
while True:
    print(number)
    number += 1
    if number == 20:
        break


####################
##    continue    ##
####################

print("# continue #")

## Another statement that can manipulate the flow of the loop is the 'continue'-statement
## The role of continue is to skip all the other commands in the loop, and to skip to the next iteration of the loop
## The continue function can be easily explained by the following code:
    ## The if-statement checks whether the number can be divided by 2 without having a remainder
    ## If this statements evaluates as True, a continue-statement is encountered, and the print just below will be skipped
    ## Thus, all even numbers will NOT be printed, while the odd numbers will be printed

for number in range(10):
    if number%2 == 0:
        continue
    print(number)


####################
##      pass      ##
####################

print("# pass #")

## Another command sometimes used in loops is the 'pass' command
## In essence, this command is a NULL operation, or in other words: it has no outcome
## It can be used to indicate that code has to come there (to remind the programmer where to look when altering the code)
## It can also be used when you need code to make the syntax work, but you don't want to write working code
## As you can see in the output, the pass has no output, and can be commented out without any problems

for letter in "Spell this": 
   if letter != " ":
      pass
   else:
      print("The space came right after this letter!")
   print("Letter :" + letter)


#########
## END ##
#########