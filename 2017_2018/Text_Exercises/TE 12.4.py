# Text exercise 12.4. Does not work in PsychoPy (does work in Spyder)
import os
directory_to_write = "/Users/tom/Documents/pythonfiles/psychopy/lesson12/"
already_exists = True
while already_exists:
    name = input("What is your name? ")
    file_name = directory_to_write + "experimental_data_" + name + ".csv"
    if not os.path.isfile(file_name):
        already_exists = False
print("OK let's get started!")