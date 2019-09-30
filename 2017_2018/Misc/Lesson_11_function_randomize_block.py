############
## import ##
############

import pandas as pd

import random
from random import shuffle
from random import randint

#######################
## Create a function ##
#######################

def block_random(number_of_blocks,conditions):

    matrix = []

    def shuffle(list):
            copy = list[:]
            random.shuffle(copy)
            return copy

    for list in range(number_of_blocks):
        needed = shuffle(conditions)
        matrix.append(needed)

    title = ''

    raw_data = {title: matrix}
    data = pd.DataFrame(raw_data, columns = [title])

    return data

#######################
## examples of usage ##
#######################

digits = []

for i in range(1,11):
    digits.append(i)

print (block_random(4,digits))

print (block_random(5,['Celexa','Cipralex','Seroxat']))
print (block_random(6,[['Celexa'],['Cipralex'],['Seroxat']]))

print (block_random(7,['P','Sherman',42,'Wallaby Way','Sydney']))

#########
## END ##
#########
