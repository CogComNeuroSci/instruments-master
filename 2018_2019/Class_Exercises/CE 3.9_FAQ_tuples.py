'''
This FAQ script contains some explanation on the use of puples, lists or an array in the Stroop task exercise (CE 3.9).

'''

## import modules
import numpy

## generate a random sample of 2 trials
RandomIndexes = numpy.random.randint(low = 0, high = 16, size = 2)
print("These are the random indices")
print(RandomIndexes)

# let's examine the tuple solution

## make a tuple for the ColorWord and FontColor
ColorWord   = ( "red", "red", "red", "red",
                "blue", "blue", "blue", "blue",
                "green", "green", "green", "green",
                "yellow", "yellow", "yellow", "yellow")
FontColor   = ( "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow")

print("Tuples: two trials")
## first trial
trial = 0
print(ColorWord[trial])
print(FontColor[trial])

## second trial
trial = 1
print(ColorWord[trial])
print(FontColor[trial])

## or if you use a loop:
print("Tuples: two trials via a loop")
for trial in range(2):
    print(ColorWord[trial])
    print(FontColor[trial])


# if we later in the course want to show the trials in a random order:

print("Tuples: two random trials")
## first random trial
trial = 0
print(ColorWord[RandomIndexes[trial]])
print(FontColor[RandomIndexes[trial]])

## second random trial
trial = 1
print(ColorWord[RandomIndexes[trial]])
print(FontColor[RandomIndexes[trial]])

## or if you use a loop:
print("Tuples: two random trials via a loop (approach 1)")
for trial in range(2):
    print(ColorWord[RandomIndexes[trial]])
    print(FontColor[RandomIndexes[trial]])

## or alternatively:
print("Tuples: two random trials via a loop (approach 2)")
for trial in RandomIndexes:
    print(ColorWord[trial])
    print(FontColor[trial])

## note that we can determine the random indexes and use them in the loop,
## but we cannot reorder the tuples before we start looping
