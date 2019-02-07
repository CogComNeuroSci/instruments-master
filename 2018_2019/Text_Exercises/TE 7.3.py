import os
from psychopy import gui

# create a dialog box
info = {"What is your name?": "", "What is your participant number?": 0, "What is the session number?": 0}

# determine the current working directory
directory_to_write = os.getcwd()

# keep asking for a new name when the data file already exists
already_exists = True
while already_exists:
    
    # display the gui
    infoDlg = gui.DlgFromDict(dictionary=info, title="Demo")
    name    = info["What is your name?"]
    number  = info["What is your participant number?"]
    session = info["What is the session number?"]
    
    # determine the name of the subject directory
    subject_directory  = directory_to_write + "/nr_" + str(number)
    
    # if the directory doesn't exist yet, make it now
    if not os.path.isdir(subject_directory):
        os.mkdir(subject_directory)
    
    # determine the file name
    file_name = subject_directory + "/subject_nr_" + str(number) + "_session_" + str(session) + "_data.txt"
    print(file_name)
    
    # verify whether this file name already exists
    if not os.path.isfile(file_name):
        already_exists = False

# we have found a new file name, ready to start
print("OK, let's get started!")
