### Solution 1: no title when the gender is unknown

# a homemade greeting function
def greeting(name):
    male_names = ["Tom", "Pieter", "Wim", "Dimi"]
    female_names = ["Marianne", "Esther", "Lien", "Nathalie"]
    if name in male_names:
        salute = "mr. "
    elif name in female_names:
        salute = "ms. "
    else: 
        salute = ""
    greeting_string = "Good morning " + salute + name + "!"
    return greeting_string
 
# test the homemade greeting function
print(greeting("Dimitri"))


### Solution 2: no title when the gender is unknown

# a homemade greeting function
def greeting(name):
    male_names = ["Tom", "Pieter", "Wim", "Dimi"]
    female_names = ["Marianne", "Esther", "Lien", "Nathalie"]
    salute = ""
    if name in male_names:
        salute = "mr. "
    elif name in female_names:
        salute = "ms. "
    greeting_string = "Good morning " + salute + name + "!"
    return greeting_string
 
# test the homemade greeting function
print(greeting("Dimitri"))


### Solution 3: get more information

# import modules
from psychopy import gui

# create a dialog box
info = {"Participant name":"Unknown", "Gender":["male", "female"]}
infoDlg = gui.DlgFromDict(dictionary = info, title = "Generic Experiment")

name = info["Participant name"]
gender = "".join(info["Gender"])

# a more informed homemade greeting function
def greeting(name, gender):
    if gender == "male":
        salute = "mr. "
    else:
        salute = "ms. "
    greeting_string = "Good morning " + salute + name + "!"
    return greeting_string
 
# test the homemade greeting function
print(greeting(name, gender))
