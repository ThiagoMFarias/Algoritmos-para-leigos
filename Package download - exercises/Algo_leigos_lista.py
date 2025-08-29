# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 08:48:29 2023

@author: Thiago
"""

ListaA = [0,1,2,3]
print(ListaA)
ListaB = [4,5,6,7]

# A função 'extend' adiciona membros da lista B na lista A. Posso usar também 'append' e 'remove'.
ListaA.extend(ListaB)
ListaA.append(-5)
ListaB.remove(7) # Repare que aqui eu retirei o 7 da ListaB depois de tê-lo added na ListaA
print(ListaB)
print(ListaA)

ListaX = ListaA + ListaB
print(set(ListaX))

ListaC = ['laranja', 'amarelo', 'vermelho', 'marron']
ListaD = [1,2,3,4]

for Value1, Value2 in zip(ListaC, ListaD):
    print(Value1, '.....', Value2)

'''
O que acontece passo a passo:
1 zip(ListaC, ListaD) → junta os elementos das duas listas posição a posição:

[('laranja', 1), ('amarelo', 2), ('vermelho', 3), ('marron', 4)]
Então você tem uma sequência de tuplas.

2. for Value1, Value2 in zip(...)

Aqui acontece o desempacotamento das tuplas.

Em cada iteração, o Python pega uma tupla (elemento_de_ListaC, elemento_de_ListaD)

Coloca o primeiro valor na variável Value1 e o segundo valor na variável Value2.

3. Iterações do loop

Primeira volta: Value1 = 'laranja', Value2 = 1
→ imprime: laranja ..... 1

Segunda volta: Value1 = 'amarelo', Value2 = 2
→ imprime: amarelo ..... 2

Terceira volta: Value1 = 'vermelho', Value2 = 3
→ imprime: vermelho ..... 3

Quarta volta: Value1 = 'marron', Value2 = 4
→ imprime: marron ..... 4

Tem outra forma de fazer com o range...

ListaC = ['laranja', 'amarelo', 'vermelho', 'marron']
ListaD = [1, 2, 3, 4]

for i in range(len(ListaC)):  # percorre os índices de 0 até 3
    Value1 = ListaC[i]        # pega o elemento da posição i em ListaC
    Value2 = ListaD[i]        # pega o elemento da posição i em ListaD
    print(Value1, '.....', Value2)

Com zip(), o código fica mais limpo e legível, pois não precisamos lidar com índices.
Com range() + índices, é mais verboso, mas faz a mesma coisa.
'''