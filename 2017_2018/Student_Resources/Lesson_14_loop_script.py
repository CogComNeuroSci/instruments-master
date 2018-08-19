###############
## importing ##
###############

import os, os.path
import platform 
import csv

## We can use this method to run a certain Python file we created earlier multiple times
## The idea is that we create a loop that runs (executes, hence the name of the function: exec) a file a number of times
## We can use this technique to let an analysis (or randomisation) run multiple times, without us having to do it all ourselves
## First, we define the filepath, which means that we determine in which folder our to-be-edited files are situated
    ## This was already shown in the 'Read_and_Manipulate_Data.py' file
## Secondly, we determine how many files are located in this folder
    ## Keep in mind that all files are counted, so it is wise to only include the to-be-edited files in a certain folder!
## At last, we define the folder where the program that we want to repeat is situated
## Now, we wanted to analyze 10 raw data files using the program 'Read_and_Manipulate_Data.py'
    ## We can take a look at this program, and we see that the files are read and edited based on the subjectnumber (SubjectNr)
    ## The result is also written to a new folder, and the filename of that newly edited file also contains the subjectnumber
    ## 'Read_and_Manipulate_Data.py' only analyzes one file at the time, but now, we can create a loop that incorporates the subjectnumber, and does multiple edits at once!
## Using this approach, all files in a directory can be analyzed!
    ## Keep in mind that consistent naming of your files is needed to pull this off
    ## Also keep in mind that you start with subject number 1, therefore, the range function is altered
        ## It now explicitly starts at 1, instead of 0

filepath = '/Users/Pieter/Documents/Vakantiejob code/scripts lessen/RandomisationFiles assignment/'
if (platform.system() == 'Windows'): 
    filepath = 'C:' + filepath
os.chdir(filepath)

number = len([name for name in os.listdir('.')])
print (number)

programpath = '/Users/Pieter/Documents/Vakantiejob code/scripts lessen/'
if (platform.system() == 'Windows'): 
    programpath = 'C:' + programpath
os.chdir(programpath)

for SubjectNr in range(1,number):
    exec(open(programpath+"Read_and_Manipulate_Data.py").read())

## In essence, the program 'Read_and_Manipulate_Data.py' is ran multiple times, but everytime, the subjectnumber (and thus which raw data file is edited) is changed by the loop

#########
## END ##
#########
