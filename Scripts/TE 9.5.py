# loading modules

def q_search(string):
    string_count = 0 ## this is a case where initialization is necessary
    for i in string: ## using the fact that string is an iterable type
        if i=="q":
            string_count +=1
    return string_count

# test the functions
a_string = "qQqA"
print(q_search(a_string))            ## counts the number of q's