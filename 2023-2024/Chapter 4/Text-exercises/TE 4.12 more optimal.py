#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:07:38 2018

@author: tom verguts
"""
import numpy as np

for number in range(2,100):
    for i in range(2,int(np.floor(np.sqrt(number)))+1):
        if (number % i) == 0:
            # calculate the second factor
            j = int(number/i)
            print(f"{number} equals {i} * {j}")
            break
    else:
        print(f"{number} is a prime number")