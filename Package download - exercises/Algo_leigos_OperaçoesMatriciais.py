# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:37:38 2023

@author: Thiago
"""
import numpy as np

changeIt = np.array([1,2,3,4,5,6,7,8])

a=changeIt.reshape(2,4)
print('\n', a)

b=changeIt.reshape(2,2,2)
print('\n', b)

# Transposição de uma matriz é quando uma matriz M x N fica N x M

changeIt = ([[1,2,3,4], [5,6,7,8]]) 

c= np.transpose(changeIt)
print('\n', c)

# Inversão matricial é aplicada a matriz M x M (que tem o mesmo nº de linhas e colunas)

d= np.identity(4)
print('\n', d)

# O inverso da matriz A é A elevado a -1, podendo ser obtido com a função 'linalg.inv'

e= np.array([[1,2], [3,4]])
f= np.linalg.inv(e)
g= np.allclose(np.dot(e,f), np.identity(2))
print(g)




