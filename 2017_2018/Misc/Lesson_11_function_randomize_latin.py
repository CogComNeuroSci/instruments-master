############
## import ##
############

import pandas as pd

#######################
## Create a function ##
#######################

def latin_square(conditions):

    def shift(list, places):
        return list[-places:] + list[:-places]

    matrix = []

    for i in range(len(conditions)):
        matrix.append(shift(conditions, i))

    title = ''

    raw_data = {title: matrix}
    data = pd.DataFrame(raw_data, columns = [title])

    return data

#######################
## examples of usage ##
#######################

digits = []

for i in range(5):
    digits.append([i])

print (latin_square(digits))

print (latin_square(['SBIS-V','WAIS','Woodcock-Johnson III Tests']))
print (latin_square([['SBIS-V'],['WAIS'],['Woodcock-Johnson III Tests']]))

print (latin_square(['Python','aired','in','December',1989]))

#########
## END ##
#########
