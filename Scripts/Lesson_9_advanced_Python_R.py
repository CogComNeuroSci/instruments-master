############
## import ##
############

import subprocess
import os

## In the following, we define where the Rscript.exe is situated on your computer
## Basically, what we need to understand is that the Python program we created does a couple of things:
    ## It locates the executable script file of R (the file that makes sure that you can run R scripts on your computer
        ## You probably already know .exe files (executable files), as they, for instance, are often used to install downloaded programs on your computer
    ## This Python program uses the Rscript.exe file to run a specific R file, the file we want to control using this program, in this case it is a program called 'max_number'
        ## Note that 'max_number' is an R script, so the extension (right behind the file name) of the program is '.R', instead of the '.py' we are used to
    ## Finally, this program provides the arguments that are used in the R script to do a computation (here: determine the largest number is a series of numbers)
        ## The result of the computation is fed back to Python, and displayed in our output
        ## Thus: 
            ## Python calls an Rscript to be run 
            ## Python provides the numbers that are processed by R
            ## The solution calculated by R is fed back to Python
            ## This solution is then displayed in our Python output

## Below, we first define where the 'Rscript.exe' is located
## To do so, we let Python search on our C drive, in the folder 'Program Files'
    ## In these folders, we will find subdirectories to the programs located in your computer, such as Java, R, Rstudio etc.
    ## Here, we specifically select the folder R, from here on, Python will do our work, but for those who are interested, we will walk through the steps below
        ## In the map 'R', we will find a folder that signifies the version of R you are working on (in my case 3.3.2)
        ## In this map, we will find several subdirectories, with the first one 'bin'
        ## In 'bin', we will find two folders, two R files, and a Shell file (which we ignore here)
        ## One of the two R files is 'Rscript.exe', the other one is 'R.exe'
            ## R.exe is actually a command prompt which opens a black window that has the same properties as R itself (try it for yourself if you want to)
                ## In essence, R.exe opens R, just in a different version than we are used to
            ## Rscript.exe cannot be opened on its own, but it is used to run scripts written in R, as we explained earlier
## The code below searches for a file called 'Rscript.exe', and returns the path to this file
## More than one 'Rscript.exe' can be found in the folder 'R', so we take the first one (located in 'bin', the others are located in the folders in 'bin' itself)
## We would like to point out an anomaly in the definition of the path name:
    ## When the path to 'Rscript.exe' is returned, we see that the path name contains the character '\'
    ## When we would define the path without changing the '\' into '\\', the program would yield errors
    ## Therefore, we want to change all the '\' into '\\'
    ## However, when we type in '\\' in Python (try it!), we see something weird happens
        ## This happens because the backslash ('\') can be seen as an escape character
        ## This means that two backslashes are actually seen as one backslash, while four backslashes are read as two backslashes
        ## So, to replace the '\' by '\\', we write that we want to replace '\\' by '\\\\'
        ## This may look inconvenient, but we do not mind, as the code runs without further issues

path = []
for r,d,f in os.walk("C:\\Program Files\\R"):
    for files in f:
         if files == "Rscript.exe":
              path.append(os.path.join(r,files))

print path[0]
R_path = path[0].replace("\\", r"\\\\")
print R_path 

## The 'command' code refers to the location of the 'Rscript.exe' on your computer
    ## Keep in mind that this file is used to execute the R script we define below

command = R_path 

## 'path2script'defines the path to the R script we want to run from Python
## Here, we located somewhere in the 'documents' folder, but if you downloaded it, it will problably be situated in the 'downloads' folder
    ## In that case, the code would be something like 'Downloads\\max_number.R'

path2script = 'C:\\Users\\Pieter\\Documents\\Vakantiejob code\\scripts lessen\\max_number.R'

## Here, we specify the arguments that are used in R to do a calculation/computation
## More specifically, we provide a list of numbers, and R will find the largest number from that list
## The process of finding the largest number is done entirely by R, Python plays no role in this!
## The result yielded by R is fed back to Python, where it will be printed in the output

args = ['11', '3', '9', '215']

## Below, we build the subprocess command
## Actually, this is just a list which contains the three needed elements: 
    ## the path to 'Rscript.exe'
    ## the path to the R file you want to run
    ## the arguments used in that R script
## The '+' only means that you add the args with a list that contains command and path2script
## We do this because args is a list (note the square brackets), and we want to combine two lists to one new list
    ## Note that you cannot just add command, path2script and args together, as args is a list, and the others are just strings
    ## This is the reason we define the combination of command and path2script as a list first

cmd = [command, path2script] + args

## In the following, we use 'subprocess.check_output' to check the result provided by the R script
## This result is then returned to Python and stored in the variable 'R_result'
    ## Please not that 'R_result' is a string, and not an integer!
        ## We can check this by printing the type of the variable
    ## Although for this tutorial, this is not really a problem, it could be a potential problem
        ## Data type conversion provides the solution, therefore we change the string into an integer by using int()
## Note: the 'universal_newlines=True' is a command that requires deeper knowledge of data storage
    ## We only need to know that 'universal_newlines=True' makes sure that the returned characters are 'decoded bytes'
    ## This makes sure that the returned solution from R is of the same encoding as the encoding used in our Python program
    ## Analogy: to communicate effectively, Python and R have to use the same language, and the info they exchange should be written in the same language
    ## 'universal_newlines=True' makes sure this is the case, so Python understands what R returns
## This is specific knowledge, and is merely an extension of what you already know, for those who are interested, we refer to stackoverflow:
    ## https://stackoverflow.com/questions/38181494/what-is-the-difference-between-using-universal-newlines-true-with-bufsize-1-an

R_result = subprocess.check_output(cmd, universal_newlines=True)
print type(R_result)

number = int(R_result)
print type(number)

print('The maximum of the numbers is %d') %number

#########
## END ##
#########
