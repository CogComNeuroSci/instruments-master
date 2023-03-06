# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 12:48:14 2019

@author: pieter
"""

#%%

import numpy as np

#%%


# array of all zeros, n x n dimensions, with n the number of conditions
def latin_square(number_of_conditions):
    
    # create a start array
    start_array    = np.zeros((number_of_conditions, 
                               number_of_conditions))
    # first line, unshuffled conditions
    start_array[0] = np.arange(1, number_of_conditions+1)
    
    # loop over the rest of the array, and permute
    for i in range(1, number_of_conditions):
        begin = start_array[0,:i]      # the first i   elements
        end   = start_array[0,i:]      # the last  i+n elements
        
        # bind them together in the start array and store them
        start_array[i] = np.concatenate((end, begin), axis = None)
        
    # return array
    return start_array


#%%
    
result = latin_square(8)
print(result)
