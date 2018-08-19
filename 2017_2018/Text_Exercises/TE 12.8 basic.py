# some operating system (os) manipulations
# Text exercise 12.8: basic version (i.e., no actual experiment is attached)
import os
from psychopy import gui
directory_to_write_to = "/Users/tom/Documents/pythonfiles/psychopy/lesson12/"
already_exists = True
myDlg = gui.Dlg(title=u"get subject info")
myDlg.addField("What is your last name? ")
myDlg.addField("What is your session number? ")
while already_exists:
    myDlg.show()
    name = myDlg.data[0]
    number = myDlg.data[1]
    filename = directory_to_write_to + "experimental_data_" + name + "_" + number + ".csv"
    if not os.path.isfile(filename):
        already_exists = False
    else:
        print("This file already exists! Choose another name.")
print("OK let's get started!")