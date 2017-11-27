############
## Import ##
############

from os import listdir
from os.path import isfile, join
import platform
import pandas

## Define an input folder
## We want to have a list from all the files we have in this map

input_folder = r"/Users/Pieter/Dropbox/Academiejaar 2016-2017/EPO/Code en lijsten exp EPO/Experiment versie 3/Stimuli/Verzameling stimuli/Stimuli blauw"
if (platform.system() == "Windows"): 
    input_folder = "C:" + input_folder

## This example uses list comprehension
    ## Basically, the line of code below concatenates/joins (binds together) the filenames of all regular existing files in the input folder
    ## More specifically, we define the name of the entries in a specific directory (listdir) earlier defined in 'input_folder'
    ## If the entry is a file (isfile), we will join (join) it with the other names we (may have) already listed
    ## The result is a very long list which contains all the file names of the files in a specific folder

onlyfiles = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
print(onlyfiles)

## We want to give the file with all the names of our files the same name as the directory it originates from
## For example, we want to have a list of all the files we find in the folder 'Stimuli blauw'
    ## We will name this list 'Stimuli blauw.txt'
## We do this by searching for the last '/' in the path definition, as the folder name will appear immediately behind that
## Again, we use list comprehension to find all the places in the path string where '/' occurs
## We use the function max() to select the largest value
    ## Note: index[-1] would have worked as well of course
## In this particular case, we would see that the last '/' appears at place 122

c = "/"
index = [pos for pos, char in enumerate(input_folder) if char == c]
max_index = max(index)
print(max_index)

## We define the folder name (which will be the same as our file name) by defining everything behind the last '/' in the path definition

foldername = input_folder[max_index+1:]

## We redefine our major list of file names as a pandas.DataFrame with only one column

files = pandas.DataFrame(onlyfiles, columns = ["File name"])

## We can define a new folder where this new file is stored
## If no new folder is defined, the new document will be stored in map we were listing

output_folder = r"\Users\Pieter\Documents\Vakantiejob code\scripts lessen"
if (platform.system() == "Windows"): 
    output_folder = "C:" + output_folder

## Output the file to .txt

files.to_csv(output_folder + "/" + "%s.txt" %foldername, sep = "\t")

## Note that due to the numbering of the files in the directory, the files are ordered in an 'odd' fashion
## This is the case because the files that only have one integer (blauw_2) are seen differently as the files with two integers (blauw_36)
## To get rid of the odd numbering, we can number all the files with two integers (blauw_02 instead of blauw_2)

print(files)


#########
## END ##
#########