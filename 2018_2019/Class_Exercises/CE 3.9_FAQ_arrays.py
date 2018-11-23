'''
This FAQ script contains some explanation on the use of puples, lists or an array in the Stroop task exercise (CE 3.9).

'''

## import modules
import numpy

## generate a random sample of 2 trials
RandomIndexes = numpy.random.randint(low = 0, high = 16, size = 2)
print("These are the random indices")
print(RandomIndexes)

# let's examine the array solution

## make an array for the ColorWord and FontColor
ColorWord   = numpy.array([ "red", "red", "red", "red",
                            "blue", "blue", "blue", "blue",
                            "green", "green", "green", "green",
                            "yellow", "yellow", "yellow", "yellow"])
FontColor   = numpy.array([ "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow",
                            "red", "blue", "green", "yellow"])

## combine arrays in trial matrix so we can inspect them like the Excel file
trials = numpy.column_stack([ColorWord, FontColor])
print(trials)
## each line is a trial
## the first column contains the information on the ColorWord
## the second column contains the information on the FontColor

print("Arrays: two trials")
## first trial
trial = 0
print(trials[trial,0])
print(trials[trial,1])

## second trial
trial = 1
print(trials[trial,0])
print(trials[trial,1])

## or if you use a loop:
print("Arrays: two trials via a loop")
for trial in range(2):
    print(trials[trial,0])
    print(trials[trial,1])


# if we later in the course want to show the trials in a random order:

print("Arrays: two random trials")
## first random trial
trial = 0
print(trials[RandomIndexes[trial],0])
print(trials[RandomIndexes[trial],1])

## second random trial
trial = 1
print(trials[RandomIndexes[trial],0])
print(trials[RandomIndexes[trial],1])

## or if you use a loop:
print("Arrays: two random trials via a loop (approach 1)")
for trial in range(2):
    print(trials[RandomIndexes[trial],0])
    print(trials[RandomIndexes[trial],1])

## or alternatively:
print("Arrays: two random trials via a loop (approach 2)")
for trial in RandomIndexes:
    print(trials[trial,0])
    print(trials[trial,1])

## again, we can randomise the trial order before we start presenting the trials
## this lowers the probability that errors will be made (e.g., you present the colorWord for trial 1 with the FontColor for trial 2)

numpy.random.shuffle(trials)
print(trials)

## with one simple line of code we have shuffled the order of the rows in the array.
## Note that this code is even less error prone: all columns are shuffled in the same command!
## Also, all of these functionalities are built-in to the numpy array data type, so no need for additional modules

print("Arrays: two random trials that we randomized by reordering the rows in the trial matrix before the loop started")
for trial in range(2):
    print(trials[trial,0])
    print(trials[trial,1])
