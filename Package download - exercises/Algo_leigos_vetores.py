# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 21:07:06 2023

@author: Thiago
"""

import numpy as np

a= np.array([1,2,3,4])
b= np.array([2,2,4,4])

A=a==b

B=a<b

print(A,B)