import os
from psychopy import gui

# create a dialog box
info = {"What is your name?": ""}

# determine the current working directory
directory_to_write = os.getcwd()

# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Demo")
    name = info["What is your name?"]
    
    # determine the file name
    file_name = directory_to_write + "/subject_" + name + "_data.txt"
    print(file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False

# we have found a new file name, ready to start
print("OK, let's get started!")
