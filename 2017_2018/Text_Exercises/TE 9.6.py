# loading modules

def letter_search(string,letter):
    string_count = 0 ## this is a case where initialization is necessary
    for i in string: ## using the fact that string is an iterable type
        if i==letter:
            string_count +=1
    return string_count

# test the functions
a_string = "qQqA"
print(letter_search(a_string,"q"))   ## same here