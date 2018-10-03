### basic while-loop
weight = "the weight of a duck"

if weight == "the weight of a duck":
    print("she's a witch!")
if weight != "the weight of a duck":
    print("burn her anyway")


### complex criterion
weight = "the weight of a duck"
made_out_of_wood = 1

if weight == "the weight of a duck" and made_out_of_wood == 1:
    print("she's a witch!")


### if...else
weight = "the weight of a duck"

if weight == "the weight of a duck":
    print("she's a witch!")
else:
    print("burn her anyway")


### if...elif...else
x = -2
if x < 0:
    print("Negative")
elif x == 0:
    print("Zero")
else:
    print("Positive")


### multiple elif statements
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


### order of importance
x = -2
if x < 0:
    print("Negative")
elif x <= 0:
    print("Smaller than or equal to zero")
else:
    print("Positive")


### execute all correct outcomes
x = -2
if x < 0:
    print("Negative")
if x <= 0:
    print("Smaller than or equal to zero")
if (x < 0) == False and (x <= 0) == False:
    print("Positive")