############
## String ##
############

## Strings represent a letter/word/sentence
## Again, we can determine the type of a variable by using type()

letter = "M"
print(type(letter))

word = "Monty"
print(type(word))

sentence = "The name 'Python' originates from Monty Python"
print(type(sentence))

## We can do some basic operations on the strings we define
## For your convenience, we have noted down some of these basic operations

## Changing between upper and lower case
    ## Keep in mind that these operations DO NOT change the original string: Sparta itself will stay unaltered after the .lower and .upper operations

Sparta = "ArE yOu NoT eNtErTaInEd?"
print(Sparta)
print(Sparta.lower())
print(Sparta.upper())
print(Sparta)

## Returning the length of a string

print(len(Sparta))

## Count how many times a specific letter/word is included in a string
    ## Note that this operation is case sensitive!
        ## If we would define 'e', the answer would be 1
        ## If we would define 'E', the answer would be 3

print(Sparta.count("e"))
print(Sparta.count("E"))

## Select a certain part of a string

print(Sparta[4:7])

## Check whether a string starts with a certain word or not
    ## Again, this is case sensitive

print(Sparta.startswith("Are"))
print(Sparta.startswith("ArE"))

## Splitting a sentence into words
## We can also return specific words using this operation

SpartaSplit = Sparta.split(" ")
print(SpartaSplit)
print(SpartaSplit[0])

## Formatting examples, showing another way to print variables
## Explanation of the code we see below:
    ## Print position 0, then 1, then 2
    ## Print position 2, then 1, then 0
    ## Print position 2, then 1, then 0 (other notation)
    ## Print 0, then 1, then 0, yielding 'abracadabra'

print("{0}, {1}, {2}".format("a", "b", "c"))
print("{2}, {1}, {0}".format("a", "b", "c"))
print("{2}, {1}, {0}".format(*"abc"))
print("{0}{1}{0}".format("abra", "cad"))

## This is only a subset of the operations we can perform on strings
## For more operations, we refer to the documentation on Python:
    ## https://docs.python.org/3.4/library/string.html
## If we want to do something using strings, we can of course google it
    ## Stackoverflow is a website which is often used when small problems are encountered during programming


#########
## END ##
#########