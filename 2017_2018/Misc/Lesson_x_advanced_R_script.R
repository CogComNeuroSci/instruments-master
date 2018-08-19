###########
## max.R ##
###########

## The following line of code gets the arguments provided in the Python code
## The argument 'trailingOnly = TRUE' is a logical argument:
  ## A character vector of those arguments (if any) supplied after --args is provided and manipulated by the R script
  ## Thus, the R script manipulates the arguments inputted from python as if they were characters 

myArgs <- commandArgs(trailingOnly = TRUE)

## As we have noted before, we work with a character string (due to the 'trailingOnly = TRUE')
## Therefore, because we want to do an operation on numbers, we should convert the characters (letters) to numbers
## To do this, we convert myArgs to integers via the function 'as.numeric()'
  ## Note that we cannot show what is stored in myArgs or nums, as this of course depends on the input from Python
  ## In essence, myArgs or nums do not exist, they only exist when the Python script is compiled (executed)
  ## Running the R script on its own will only result in errors, as these variables are actually empty here
    ## They only represent numbers once these are provided through the arguments in the Python script

nums = as.numeric(myArgs)

## Now, we write away the result of the computation to the console
  ## Note that we use the function 'cat()' for this, but 'print()' would also work, as these do the same thing
## Before we write away the data, we first do the computation that we wanted to do: define the maximum value
## To do this, we use the function 'max()', which will determine which number in the provided list is the largest
  ## Note that this is the reason why we wanted to converted the strings to integers: finding the maximum will not work out on strings
## Here, what we actually do is writing the output of our computation to the 'standard output stream'
## The standard output stream (abbreviated as 'stdout') is actually the stream where the program writes its output
  ## This is done, for example, when the write() function is called
  ## Both the functions print() and cat() write output to the console
    ## Whenever output is written to the console, the data is transfered to the stdout
    ## UNnless we redirect the information, what is written to stdout can usually be seen in the console/output of your program
    ## If we would do print('Hello world') in Python, the 'Hello world' we see in the output is represented in the stdout
## What the Python script does, is capturing what is written in the stdout by the R script:
  ## The R script writes the largest value to the console
  ## The value is available in the stdout
  ## Python captures what is available in the stdout and may store it in a variable
  ## This variable is than altered and printed
## By retrieving what is available in the stdout, we can make sure that Python starts an R script, and retrieves the output of the computation
  ## This can be used to let R calculate (which is the main function of R), and when that is done, the result can be altered by Python

cat(max(nums))

#########
## END ##
#########
