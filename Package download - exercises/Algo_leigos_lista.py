# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 08:48:29 2023

@author: Thiago
"""

ListaA = [0,1,2,3]
print(ListaA)
ListaB = [4,5,6,7]

# A função 'extend' adiciona membros da lista a na lista b. Posso usar também
# 'append' e 'remove'.
ListaA.extend(ListaB)
ListaA.append(-5)
ListaB.remove(7) # Repare que aqui eu retirei o 7 da ListaB depois de tê-lo added na ListaA
print(ListaB)
ListaA
print(ListaA)
