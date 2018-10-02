### Strings
my_first_string = "just any random string, basically"
print(my_first_string)
print(my_first_string[3])
print(my_first_string[9:15])

#print("We are the knights who say "Ni"!")
print("We are the knights who say \"Ni\"!")

name = "Brian"
say_hello_string = "Good morning, {0}!".format(name)
print(say_hello_string)

name1 = "Brian"
name2 = "Graham"
say_hello_string = "Good morning, {0} and {1}!".format(name1, name2)
print(say_hello_string)

name1 = "Brian"
and_string = " and "
name2 = "Graham"
together = name1 + and_string + name2
print(together)