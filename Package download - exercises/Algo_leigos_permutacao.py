# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 22:14:33 2023

@author: Thiago
"""
# Permutação/reorganização de dados é possível de várias maneiras:

import numpy as np
from itertools import permutations

a = np.array([1,2,3])
b = np.random.permutation(a)
print(b)

# Obter todas as permutações de modo a testar uma de cada vez:

c = np.array([1,2,3])

for p in permutations(c):
    print(p)

# Reorganizando combinações: 

from itertools import combinations

d = np.array([1,2,3,4])

for comb in combinations(d,2):
    print('\n', comb)

# Você pode não precisar de todas as combinações, nesse caso a função random.sample funcione: nao entendi esse código e não consegui obter o resultado

""" pool = []

e = np.array([1,2,3,4])

for comb in combinations(e,2):
    pool.append(comb)

random.sample(pool,3)
 """

# Encerrando repetições: no python, uma base nunca têm dados repetidos. 
f = np.array([1,2,3,4,5,6,6,7,7,1,2,3])
g = np.array(list(set(f)))
print(g)