# latin square
import numpy as np
a = ["a", "b", "c", "d"]
l = []
for loop in range(len(a)):
    l.append(list(np.roll(a,loop)))
print(l)