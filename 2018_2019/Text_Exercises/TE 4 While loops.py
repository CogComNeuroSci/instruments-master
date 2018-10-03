i = 0
while i < 5:
    print(i)
    i = i + 1

i = 0
j = 10
while i < 5 or j > 3:
    print("i is {0} and j is {1}".format(i,j))
    i = i + 1
    j = j - 2

i = 0
j = 10
while i < 5 and j > 3:
    print("i is {0} and j is {1}".format(i,j))
    i = i + 1
    j = j - 2

print(i == i)

print((i  ==  i) == False)