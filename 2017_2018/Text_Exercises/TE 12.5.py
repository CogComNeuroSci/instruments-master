# some operating system (os) manipulations
# 
import os
from psychopy import gui
directory_to_write_to = "/Users/tom/Documents/pythonfiles/psychopy/lesson12/"
already_exists = True
myDlg = gui.Dlg(title=u"get subject info")
myDlg.addField("number? ")
while already_exists:
    myDlg.show()
    number = myDlg.data[0]
    filename = directory_to_write_to + "experimental_data_" + number + ".csv"
    if not os.path.isfile(filename):
        already_exists = False
print("OK let's get started!")