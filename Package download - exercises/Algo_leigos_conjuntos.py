# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 22:27:05 2023

@author: Thiago
"""

SetA= set(['red', 'blue', 'green', 'black'])
SetB= set(['black', 'green', 'yellow', 'orange'])
SetX= SetA.union(SetB)
SetY= SetA.intersection(SetB)
SetZ= SetA.difference(SetB)
print(SetX, SetY, SetZ)

print('{0}\n{1}\n{2}'.format(SetX,SetY,SetZ))

# A é superconjunto de Y
Plus= SetA.issuperset(SetY)
print(Plus)

# SetA é subconjunto de SetX
Minus= SetA.issubset(SetX)
print(Minus)

# Adicionando um elemento:
SetA.add('white')
print(SetA)

result=SetA.issubset(-SetX)
print(result)