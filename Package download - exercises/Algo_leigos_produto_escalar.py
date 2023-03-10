# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 21:04:39 2023

@author: Thiago
"""

import numpy as np

a= np.array([[1,2,3],[4,5,6]])
b= np.array([[1,2,3],[4,5,6],[7,8,9]])
c=a.dot(b)
print(c)

# Note que num prduto escalar o número de linhas em "a" tem que ser igual ao
# número de colunas de "b". 

d= np.mat([[1,2,3],[4,5,6]])
e= np.mat([[1,2,3],[4,5,6],[7,8,9]])
f= d*e
print(f)