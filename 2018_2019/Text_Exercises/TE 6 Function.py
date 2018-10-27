# just pick a number
my_number = 4
 
# square the number and print it
square = my_number*my_number
print(square)

# a homemade squaring function
def square_function(number):
    return number*number

# square the number via the homemade function and print it
square2 = square_function(my_number)
print(square2)

# a homemade greeting function
def greeting(name):
    male_names = ["Tom", "Pieter", "Wim", "Dimi"]
    female_names = ["Marianne", "Esther", "Lien", "Nathalie"]
    if name in male_names:
        salute = "mr. "
    else:
        salute = "ms. "
    greeting_string = "Good morning " + salute + name + "!"
    return greeting_string
 
# test the homemade greeting function
print(greeting("Dimi"))
