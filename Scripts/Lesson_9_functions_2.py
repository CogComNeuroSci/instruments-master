# Illustration of functions
import numpy as np

def q_search(string):
    string_count = 0 ## this is a case where initialization is necessary
    for i in string: ## using the fact that string is an iterable type
        if i=="q":
            string_count +=1
    return string_count

def letter_search(string,letter):
    string_count = 0 ## this is a case where initialization is necessary
    for i in string: ## using the fact that string is an iterable type
        if i==letter:
            string_count +=1
    return string_count

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
a_string = "qQqA"
print(q_search(a_string))            ## counts the number of q's
print(letter_search(a_string,"q"))   ## same here
print(prime(1))
print(prime(16))
print(prime(17))