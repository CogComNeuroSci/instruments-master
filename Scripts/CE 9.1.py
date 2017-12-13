# Illustration of functions
import numpy as np

def prime(number):
    if number <= 2:
        return "Sorry, I can only do numbers larger than 2"
    else:
        divisible = False
        for i in range(2,int(np.floor(np.sqrt(number))+1)+1):
            if number%i == 0:
                divisible = True
                break
        if divisible == False:
            return "Yes it's prime!"
        else:
            return "No, it's not prime!"

# test the functions
print(prime(1))
print(prime(16))
print(prime(17))