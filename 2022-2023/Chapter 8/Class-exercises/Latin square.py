# Here we have chosen to use a balanced Latin Square
# In this kind of balanced Latin Square, each option follows each option an equal number of times
# The code has been written by Paul Grau and he has added some insightfull explanation:
# https://medium.com/@graycoding/balanced-latin-squares-in-python-2c3aa6ec95b9

## Try out this code with the three conditions as mentioned in the exercise, you'll see
## that you need as much subject in the full permutation as in the latin square.
## However, do have a look at what happens with four conditions.

import itertools, numpy

nConditions = 4

# full permutation
perm = list(itertools.permutations(range(1,nConditions+1)))
print(perm)


def balanced_latin_squares(n):
    
    # deconstruction of the method
    ## for i in range(n): n sequences to be constructed
    ## for j in range(n): n items in each of the sequences
    ## j%2 (even): j/2+1
    ## j%2 (odd): n-j/2
    ## finally, either (j/2+1) and (n-j/2) 
    
    l = [[((numpy.floor(j/2)+1 if j%2 else numpy.floor(n-j/2)) + i) % n + 1 for j in range(n)] for i in range(n)]
    
    # Repeat reversed for odd n
    if n % 2:
        l += [seq[::-1] for seq in l]
    
    return l

latin = balanced_latin_squares(nConditions)
print(latin)