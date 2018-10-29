# Illustration of functions
import numpy as np

def prime(number):
    
    # number lower than 2 can't be primes
    if number <= 2:
        return "Sorry, I can only do numbers larger than 2"
    
    # now, we'll check whether the number can be divided between more numbers than itself and 1
    else:
        divisible = False
        
        # check all the integers between 2 and the number right before we arrive at the square root of the tested number
        # think about why this nicely lowers the range of numbers to check!
        for i in range(2,int(np.floor(np.sqrt(number))+1)+1):
            
            # we're only interested in divisions that result in an integer, not a decimal
            if number%i == 0:
                
                # as soon as a division results in an integer, the number can't be a prime!
                divisible = True
                break
        
        # after checking all the possible integers (of after we have found that the number can't be a prime),
        # we determine what message to return
        if divisible == False:
            return "Yes it's prime!"
        else:
            return "No, it's not prime!"

# test the functions
print(prime(1))
print(prime(16))
print(prime(17))