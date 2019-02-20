# Here we have chosen to use a balanced Latin Square
# In this kind of balanced Latin Square, each option follows each option an equal number of times
# The code has been written by Paul Grau and he has added some insightfull explanation:
# https://medium.com/@graycoding/balanced-latin-squares-in-python-2c3aa6ec95b9

## Here is the code deconstructed a bit more for your convenience.

import numpy

l = []
n = 4
for i in range(n):
    new = []
    for j in range(n):
        if j%2:
            new.append(((numpy.floor(j/2)+1) + i) % n + 1)
        else:
            new.append((numpy.floor(n-j/2) + i) % n + 1)
    l.append(new)

if n % 2:
    m = []
    for seq in l:
        m.append(seq[::-1])
    l.append(m)

print(l)