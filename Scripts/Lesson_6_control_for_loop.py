################
## for loop 1 ##
################

print("# For loop 1.1 #")

## The sentence "We like Python!" will be printed 10 times in the output
## In essence, the for loop we see below can be translated as follows: "for every number we have between 0 and 10 (0 included, 10 not included), print "We like Python!" in the output
## So, when we compile this loop, we will see that the sentence is printed 10 times, as there are 10 numbers between 0 and 10

for i in range(10):
    print("We like Python!")

## Now let"s check what effect the indentations have on the code.
## Here we have added another print statement "print("Yes we do!")" and we indented it so it becomes part of the for loop.

print("# For loop 1.2 #")

for i in range(10):
    print("We like Python!")
    print("Yes we do!")

## Let"s compare that to what happens when we fail to indent the second print statement.

print("# For loop 1.3 #")

for i in range(10):
    print("We like Python!")
print("Yes we do!")


################
## for loop 2 ##
################

print("# For loop 2 #")

## We can also add varying values in a loop
## Here we will print the index, which means that you print i in the output
## i is, as explained before, each number between 0 and 10
## Of course i can take different values based on the characteristics of the loop
## "%d" means that a decimal number has to be inserted
## What number is inserted is specified at the end of the statement, in our case this number is the index, called "i"

for i in range(10):
    print("%d. We like Python!") %i


################
## for loop 3 ##
################

print("# For loop 3 #")

## Global variables which were defined earlier can also be used in a loop
## Here we define a name, and this name is then printed using a for loop
## Similar with the numbers, we also have to specify that a string has to be inputted, that"s why we type "%s"
## What the string exactly is, is again specified at the end of the statement
## Changing the name variable will alter the output
## Try this by writing your own name between the "", and look at the output!

name = "Jon Snow"

for i in range(10):
    print("You know nothing, %s...") %name


################
## for loop 4 ##
################

print("# For loop 4 #")

## Keep in mind that both strings (letters/words/sentences) and integers (numbers) can be manipulated in a loop
## To illustrate this, we will number the printed sentences using the index (as we have done previously), and we print the "name" variable at the same time!
## Also notice that "name" was defined earlier, and this definition will still be used here

for i in range(10):
    print("%d. You know nothing, %s...") %(i, name)


################
## for loop 5 ##
################

print("# For loop 5 #")

## Notice that the term "i" is arbitrary, we can replace it by anything, and the loop will still work
## To illustrate this, we change "i" by "numbers"
## Keep in mind that if you want to print the index, you should use the name you defined earlier
## Here, we will have to specify that the number we print is actually the index, which we called "numbers"

name = "the King in the North"

for numbers in range(10):
    print("%d. All hail %s!") % (numbers, name)


################
## for loop 6 ##
################

print("# For loop 6 #")

## Time now to use another description of the vallues that the index has to take on. 
## In the example below we drop range(10) and simply replace it by pointing to a vector with three items.
## The loop will go through each of the three position of the vector and print its contents.

v = ("one", "two", "three")
for i in v:
    print(i)


################
## for loop 7 ##
################

print("# For loop 7 #")

## By now you should be sufficiently familiar with for loops so we can use them to display stimuli on the screen.
## In this example we will draw a circle on the window, and let the circle size increase with each pass through the loop.

from psychopy import visual
import time
from time import sleep

win = visual.Window(size=(500, 400), units="height", color = "white")

sizes = [.05, .10, .15]
print(sizes)
for i in sizes:
    circle = visual.Circle(win, radius = i, pos=(0,0), fillColor = "black")
    circle.draw()
    win.flip()
    time.sleep(2)


#########
## END ##
#########