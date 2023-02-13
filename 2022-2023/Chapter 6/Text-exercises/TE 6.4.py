# Would it be OK to define male_names = ("Tom", "Pieter", "Wim", "Dimi")? What’s the difference?

# a homemade greeting function
def greeting(name):
    male_names = ("Tom", "Pieter", "Wim", "Dimi")
    female_names = ("Marianne", "Esther", "Lien", "Nathalie")
    if name in male_names:
        salute = "mr. "
    else:
        salute = "ms. "
    greeting_string = "Good morning " + salute + name + "!"
    return greeting_string
 
# test the homemade greeting function
print(greeting("Dimi"))
