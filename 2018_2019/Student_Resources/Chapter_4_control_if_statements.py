####################
## if-statement 1 ##
####################

print("# if-statement 1 #")

## If-statements can be used to select certain situations
## These statements can be used both in your ordinary code (as we will see shortly) and in loops (both in for- and while-loops)
## An if-statement has a specific form:
    ## if (defined statement) evaluates as True:
        ## do this
        ## do that
## In the following code, we define a variable called "name"
    ## We assign the value "Daenerys Targaryen" to "name"
## The if-statement will evaluate whether the value in name equals "Daenerys Targaryen" or not
    ## if name equals "Daenerys Targaryen", we see that the sentence "Welcome..." is printed
    ## if name does not equal (!=) "Daenerys Targaryen", we see that the sentence "This name..." is printed
## In our case, we defined name ourselves, so our if-statement is maybe a bit dull
## However, keep in mind that this can also be used in for example password checks, to see whether the saved password equals the inputted password!

name = "Daenerys Targaryen"

if name == "Daenerys Targaryen":
    print("Welcome, {0}, Mother of Dragons".format(name))
if name != "Daenerys Targaryen":
    print("'{0}', This name is unknown to me".format(name))

## We can also make the set of requirements more complex, for instance by requiring two conditions to be met

name = "Daenerys Targaryen"
door_open = 1

if name == "Daenerys Targaryen" and door_open == 1:
    print("Welcome, {0}, Mother of Dragons".format(name))

## In the code below, we define two specific conditions: we check the input for two specific strings
## Again, depending on the input, our output will be different
## Note that if the input string doesn't match with either of the defined strings, we have no output
## Try to type your own name between the "", and look at the output

name = "Viserys Targaryen"

if name == "Daenerys Targaryen":
    print("Welcome, {0}, Mother of Dragons".format(name))
if name == "Viserys Targaryen":
    print("Go away, you traitor!")

## Keep in mind that name == "Viserys Targaryen" evaluates here as True, and therefore the commands below this if-statement are executed


####################
## if-statement 2 ##
####################

print("# if-statement 2 #")

## Of course, we don't want to specify every condition that may occur, and luckily, we don't have to!
## We can use the "else"-statement to define what we want to happen if no condition is fulfilled
## In the case below, we see that we only have a specific response for "Daenerys Targaryen", for every other name there is the default "This name is unknown to me"

name = "Jorah Mormont"

if name == "Daenerys Targaryen":
    print("Welcome, {0}, Mother of Dragons".format(name))
else:
    print("'{0}', This name is unknown to me".format(name))


####################
## if-statement 3 ##
####################

## This is a first example of the use of an if...elif...else-statement. 
## We first verify whether x is smaller than zero. 
    ## If x is indeed smaller than zero the response "Negative" is printed and we exit the if...elif...else-statement. 
    ## If this condition is not met, we proceed to check whether the second condition is met: is x equal to zero. 
    ## Again, if this condition is met the action is executed ("Zero" is displayed in the output window) and we leave the loop. 
    ## Alternatively, when x is also not equal to zero we proceed to the else-statement and execute the remaining action (displaying "Positive" in the output window).

print("# if-statement 3.1 #")

x = -2
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")

## Note that as soon as a certain condition is met, the remaining options are not considered anymore and we leave the if...elif...else-statement. 
## Even if one of the following conditions would also be met, we wouldn’t consider it anymore. 

print("# if-statement 3.2 #")

x = -2
if x < 0:
    print("Negative")
elif x <= 0:
    print("Smaller than or equal to zero")
else:
    print("Positive")
    
## If however you would like to execute each action associated with a condition that is met, you’ll need to use multiple if-statements. 
## The example below shows how you can adjust the previous example to execute all the actions for which the conditions are met.

print("# if-statement 3.3 #")

x = -2
if x < 0:
    print("Negative")
if x <= 0:
    print("Smaller than or equal to zero")
if (x < 0) == False and (x <= 0) == False:
    print("Positive")


####################
## if-statement 4 ##
####################

print("# if-statement 4 #")

## If you want to define a series of subsequent conditions, we can also use the 'elif'-statement
## These elif-statements closely resemble the "switch case"-statements used in other programming languages (such as C++)
## Looking at the code below, we see that if- and elif-statements are very similar, however, there is one big difference:
    ## Using 'if'-statements, the code will check every condition you have defined
        ## This characteristic is especially useful if you have defined certain exceptions to a condition
    ## using 'elif'-statements, the code will check the conditions until one is met, and then the action is executed without checking the other conditions

age = 67

if age == 18:
    print("You can drink everything and drive a car now!")
elif age == 21:
    print("You can drink everything in the US from now on!")
elif age == 65:
    print("From now on, you can retire!")
elif age == 100:
    print("You are living on Earth for an entire century!")
else:
    print("Your age isn't very special...")


####################
## if-statement 5 ##
####################

print("# if-statement 5 #")

## If you want to check whether multiple conditions are met at the same time, you can use the 'and'-statement
## The and-statement will only execute the indented code (the code connected to the if-statement, proceeded by the .... indentation) if all statements/conditions connected by 'and' are true
## In the example below, we see that both the first name and the last name should have a specific value before the print command is executed
## Try to comment out 'Rickon Stark', and uncomment 'Arya Stark', and look at what is outputted next
    ## Tip: if you work on a Windows operating system (OS): select what you want to comment away, press 'ctrl' and then the '-key
    ## Another tip: quickly uncomment by selecting the desired code, press 'ctrl', then shift, and then the '-key
    ## For other OS: look in the 'Edit' tab, and below you will see the shortcut
    ## Shortcuts can be altered in the 'File' tab under 'Preferences'

FirstName = "Arya"
LastName = "Stark"

#FirstName = "Rickon"
#LastName = "Stark"

#FirstName = "Arya"
#LastName = "Lannister"

if (FirstName == "Arya") and (LastName == "Stark"):
    print("Nymeria is in the castle, {0} {1}".format(FirstName,LastName))
else:
    print("Something's off, Nymeria does not belong to {0} {1}!".format(FirstName,LastName))


####################
## if-statement 6 ##
####################

print("# if-statement 6 #")

## Similar to the and-statement, the or-statement also has influence on the output of an if-statement
## Here the idea is that the if-statement will execute if at least 1 condition is fulfilled
## This means that if we have 5 conditions connected by or-statements, and 1 of these conditions is fulfilled, then the indented code will be executed
## To make this more intuitive, let us look at the code below:
    ## We can uncomment each section, and we still will get the same result: in all cases the sentence 'Nymeria is in the castle' will be printed
    ## Looking at the first pair:
        ## First name is Arya, and last name is Stark, so at least 1 condition is fulfilled, meaning that the if-statement is executed
    ## Looking at the second pair:
        ## The first name is Rickon, but the second name is Stark, which means that 1 condition is met, enough to execute the if-statement
    ## Looking at the third pair:
        ## The first name is Arya, which fulfills one condition, thus the if-statement will be executed

#FirstName = "Arya"
#LastName = "Stark"

FirstName = "Rickon"
LastName = "Stark"

#FirstName = "Arya"
#LastName = "Lannister"

if(FirstName == "Arya") or (LastName == "Stark"):
    print("Nymeria is in the castle, {0} {1}!".format(FirstName,LastName))
else:
    print("Something's off!")


#########
## END ##
#########