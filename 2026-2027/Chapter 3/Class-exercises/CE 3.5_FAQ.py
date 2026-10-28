'''
This FAQ script contains some explanation on recursion.

Original question:
Ik snap niet zo goed waarom we voor deze oefening in de s.find() nog eens s.find moeten invoegen. Is het mogelijk om deze logica uit te leggen?
'''

## In CE 3.4 you were asked to find the index of the first occurrence of letter a in the word banana
## This should be the index 1 (python starts counting from 0) as the first 'a' occurs in the second letter of the word banana

## We solved this exercise by using the functionality .find() which is specifically made to search content in a string.
## This functionality can be found after some googling, for instance by searching for "python find index of letter in string"
## Googling might have lead you to this page: https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
## The explanation should already have enabled you to solve CE 3.4

s = "banana"
print(s.find("a"))


## In CE 3.5 you now want to find the index of the second occurrence of letter 'a' in the word banana
## To do this, you might first investigate whether the .find() function is capable of doing this.
## Usually, a function such as .find() has a number of properties that you can change.
## Maybe you'll be able to tell .find() to go search the second occurence of the letter that you are looking for.


## At this point, it might be a good idea to google around for some more information of the options that .find() offers you.
## A query such as "python string find" should lead you in the right direction.
## For instance, you may find this page: https://www.tutorialspoint.com/python/string_find.htm
## Or this one: https://docs.python.org/2/library/string.html
## Or this one: https://www.programiz.com/python-programming/methods/string/find
## And so on. It's always a good idea to consult some two or three pages. Reading the explanation in other words will deepen your understanding.
## Plus, it will also allow you to discover whether the sources agree or not (so you don't get stuck with a malfunctioning solution).

## All of these pages tell you that .find() accepts three pieces of information:
## sub = the substring that you are trying to find, which is 'a' in our case (note that it appears that we can search for more than one letter!)
## start = the start indicates where we need to start searching in the string, which is just the beginning of the word banana in our case
## end = the end indicates where we can stop searching in the string, which in our case in the end of theword banana

## The pages will also have informed you that the start and end values are optional.
## When no start and stop values are given, find() just searches the entire string that it is attached to (banana).

## OK, interesting, but how does this help us find the index for the second occurrence of 'a' in banana?
## Unfortunately there is no property that we can set that directly tells find() to go search for the second occurrence of the letter instead of the first.
## Our hopes didn't come true. However, all this googling might spark a light in your mind:
## "If I start searching after the first occurrence of the letter 'a', the .find() function will be forced to give me the index of the second occurrence!"

## You could quickly verify your idea by entering the index for the first string (that we found in CE 3.4) explicitly:

print(s.find("a", 1))

## Hm, this returns the index 1 again. Why?
## Of course, if we start searching at index 1, we again include the first a of banana in the search.
## So we should start at the index after the first occurrence of 'a'! Let's try:

print(s.find("a", 1+1))

## Yes, this tells us that the index 3 (the fourth letter in banana) holds an 'a', which is the correct answer.

# when you arrive here, you have essentially solved CE 3.5, from here on we make the code a bit smarter.

## In the solutions above we were just typing 1 as the index for the first occurrence of 'a'.
## This is a bit impractical as we will have to rewrite the code when we want to use a different word than banana (e.g., alarm).
## Can we write the code in a way that makes it useful for more words than just banana?

## After some thinking, you might come up with something like this:

position_first_a = s.find("a")
start_searching_at = position_first_a + 1
print(s.find("a", start_searching_at))

## This is a very good idea: you just store the index for the first occurrence of 'a' in position_first_a
## Next, you add 1 to start at the index right after the first occurrence of 'a'.
## And this value in entered as the second property of .find()

## If you combine the three steps above into one, dense line of code, you end up with our solution:

print(s.find("a",s.find("a")+1))

## Note that this dense formulation is by no means better than a formulation that is spread out across three lines.
## You'll just notice that as you get better at programming you will be inclined to write shorter code
## (partly because you will be able to think three steps ahead, and partly because you'll see the structure in a dense line of code more quickly)

# So why was the hint "recursion"?

## Recursion roughly means that you use the same functionality to solve both the big problem and a subproblem within that big problem.

## In our case, we used .find() to find the first index (the subproblem) 
## and then inserted that information in another .find() command to find the second index (the big problem).

## Googling for "programming recursion" will provide you with some more info to grasp this concept.
## This isn't a concept you need to fully understand for the tests, but it is an important strategy in programming and part of the vocabulary that you are building up.