#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 21:15:26 2018

@author: tom verguts
"""
import numpy as np

for number in range(2,500):
    sum = 1
    for x in range(2,int(np.floor(np.sqrt(number)))+1):
        if number % x == 0:
            sum += ( x + (number/x))
    if sum == number:
        print("{} is perfect-- that's very rare!".format(number))