## The if-statement can also be used in loops
## Below, we will highlight an example of an if-statement both in a while-loop and in a for-loop

###################
##   nesting 1   ##
###################

print("# nesting 1 #")

## While-loop
    ## Again, do not forget to increment or we will have an eternal loop!
## Use elif to make sure that the values are not printed twice
## Try and replace the 'elif'- by 'if'-statements to see what happens

age = 0
while age <= 100:
    if age == 18:
        print(f"Your age is {age}! You can drink alcohol and drive a car!")
    elif age == 21:
        print(f"Your age is {age}! You can drink alcohol in the US!")
    elif age == 65:
        print(f"Your age is {age}! From now on, you can retire!")
    elif age == 100:
        print(f"Your age is {age}! You are living on Earth for a century!")
    else:
        print(f"Your age is {age}.")
        
    age += 1


###################
##   nesting 2   ##
###################

print("# nesting 2 #")

## For-loop
## Here we write a loop where the numbers that can be divided by three are printed with a different sentence than the numbers that can't be divided by three
## The symbol '%' means that you look at the remainder of a division
    ## 9%3 == 0
    ## 5%3 != 0

for i in range(10):
    if i%3 == 0:
        print(f"The number {i} can be divided by three")
    else:
        print(f"The number {i} is not divisible by three")


#########
## END ##
#########