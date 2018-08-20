############
## import ##
############

import pandas as pd
import numpy as np

import random
from random import shuffle
from random import randint
import itertools

#######################
## Create a function ##
#######################

def simple_randomisation(number_of_subjects,number_of_conditions):
    subjects = []

    for i in range(1,(number_of_subjects+1)):
        subjects.append(i)

    shuffle(subjects)
    print (subjects)

    step = []
    conditions = []

    for i in range(1,number_of_conditions+1):
        step.append(i)

    conditions.extend([step for i in range(int(number_of_subjects/number_of_conditions))])

    cond = np.array(conditions)
    condit = np.ravel(cond)
    conditions = list(condit)

    shuffle(conditions)
    print (conditions)

    raw_data = {'Subjects': subjects, 'Conditions': conditions}
    data = pd.DataFrame(raw_data, columns = ['Subjects', 'Conditions'])

    return data 

print(simple_randomisation(20,2))
