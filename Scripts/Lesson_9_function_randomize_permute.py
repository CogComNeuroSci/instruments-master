############
## import ##
############

import itertools
import pandas as pd

#######################
## Create a function ##
#######################

def permutate(list):

    newList = ([x for x in itertools.permutations(list)])

    title = ''

    raw_data = {title: newList}
    data = pd.DataFrame(raw_data, columns = [title])

    return data

#######################
## examples of usage ##
#######################

list_2 = (1,2)
list_3 = (1,2,3)
list_4 = (1,2,3,4)

print (permutate(list_2))
print (permutate(list_3))
print (permutate(list_4))

list_abc = ('a','b','c')

print (permutate(list_abc))

#########
## END ##
#########
