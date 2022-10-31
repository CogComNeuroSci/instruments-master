'''
This FAQ script contains some explanation on the use of tuples, lists or an array in the Stroop task exercise (CE 3.9).

'''

## import modules
import numpy

## generate a random sample of 2 trials
RandomIndexes = numpy.random.randint(low = 0, high = 16, size = 2)
print("These are the random indices")
print(RandomIndexes)

# let's examine the list solution

## make a list for the ColorWord and FontColor
ColorWord   = [ "red", "red", "red", "red",
                "blue", "blue", "blue", "blue",
                "green", "green", "green", "green",
                "yellow", "yellow", "yellow", "yellow"]
FontColor   = [ "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow",
                "red", "blue", "green", "yellow"]

print("Lists: two trials")
## first trial
trial = 0
print(ColorWord[trial])
print(FontColor[trial])

## second trial
trial = 1
print(ColorWord[trial])
print(FontColor[trial])

## or if you use a loop:
print("Lists: two trials via a loop")
for trial in range(2):
    print(ColorWord[trial])
    print(FontColor[trial])


# if we later in the course want to show the trials in a random order:

print("Lists: two random trials")
## first random trial
trial = 0
print(ColorWord[RandomIndexes[trial]])
print(FontColor[RandomIndexes[trial]])

## second random trial
trial = 1
print(ColorWord[RandomIndexes[trial]])
print(FontColor[RandomIndexes[trial]])

## or if you use a loop:
print("Lists: two random trials via a loop (approach 1)")
for trial in range(2):
    print(ColorWord[RandomIndexes[trial]])
    print(FontColor[RandomIndexes[trial]])

## or alternatively:
print("Lists: two random trials via a loop (approach 2)")
for trial in RandomIndexes:
    print(ColorWord[trial])
    print(FontColor[trial])

## interestingly, we can randomise the trial order before we start presenting the trials
## this lowers the probability that errors will be made (e.g., you present the colorWord for trial 1 with the FontColor for trial 2)

ColorWordRandom = [ColorWord[i] for i in RandomIndexes]
FontColorRandom = [FontColor[i] for i in RandomIndexes]

print("Lists: two random trials that we randomized before the loop started")
for trial in range(2):
    print(ColorWordRandom[trial])
    print(FontColorRandom[trial])

## Note that we had to use list comprehension as in CE 3.8
## We can avoid list comprehension, for instance by using the shuffle method
## This method shuffles the items in the list just like you would shuffle a deck of cards

## import modules
from random import shuffle

shuffle(ColorWord)
shuffle(FontColor)

print("Lists: two random trials that we randomized by shuffling the lists before the loop started")
for trial in range(2):
    print(ColorWord[trial])
    print(FontColor[trial])
