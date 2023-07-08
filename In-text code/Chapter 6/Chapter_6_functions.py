# to illustrate the use of selfmade and built-in functions in Python

def greeting(name):
    male_names = ["Tom", "Pieter", "Wim", "Dimi"]
    female_names = ["Marianne", "Esther", "Lien", "Nathalie"]
    if name in male_names:
        salute = "mr. "
    else:
        salute = "ms. "
    greeting_string = "Good morning " + salute + name + "!"
    return greeting_string

print(greeting("Lien"))

# illustration of two useful built-in functions, dir() and len();
# Google "built-in functions python" for more info on available functions
print(dir(str))                 # all attributes of class str; some of those attributes we already used in Chapter 3
print(len(greeting("Wim")))     # the length of the resultant string