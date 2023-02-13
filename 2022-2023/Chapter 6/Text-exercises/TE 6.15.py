# a homemade greeting function
def greeting(name):
    male_names = ["Tom", "Pieter", "Wim", "Dimi"]
    female_names = ["Marianne", "Esther", "Lien", "Nathalie"]
    if name in male_names:
        salute = "mr. "
    else:
        salute = "ms. "
    greeting_string = "Good morning " + salute + name + "!"
    
    # test whether we can access male_names (here it works)
    print(male_names)
    
    return greeting_string

# test whether we can access male_names (here it works)
greeting('Dimi')

# test whether we can access male_names (here it doesn't)
print(male_names)