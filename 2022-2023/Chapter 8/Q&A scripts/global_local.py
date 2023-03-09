# illustration of global and local namespace

# these two variables are global
some_number = 10
some_other_number = 20

def adding_function(number1, number2):
    # result, number1, and number2 are local
    result = number1 + number2
    print("hello")
    
result = adding_function(number1 = some_number, number2 = some_other_number)
print(result)