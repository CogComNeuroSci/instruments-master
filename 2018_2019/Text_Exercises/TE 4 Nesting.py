age = 0
while age <= 100:
    if age == 18:
        print("Your age is {0}! You can drink alcohol and drive a car!".format(age))
    elif age == 21:
        print("Your age is {0}! You can drink alcohol in the US!".format(age))
    elif age == 65:
        print("Your age is {0}! From now on, you can retire!".format(age))
    elif age == 100:
        print("Your age is {0}! You are living on Earth for a century!".format(age))
    else:
        print("Your age is {0}.".format(age))
        
    age += 1
