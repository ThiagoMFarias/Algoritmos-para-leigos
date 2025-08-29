# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 20:33:50 2023

@author: Thiago
"""

def SecretNumber():
    GotIt = False
    while GotIt == False:
        One = int(input('Type a number between 1 and 10 :'))
        Two = int(input('Type a number between 1 and 10: '))
        
        if (One>=1) and (One<=10):
            if(Two>=1) and (Two<=10):
                print('Secret number is ' + str(One*Two))
                GotIt = True
                continue
            else:
                print('Incorrect second value.')
        else:
            print('Incorrect first value.')
        print('Try again!')

# Essa função não aceita nenhum argumento (fora self, se for um método de classe). Se você tentar passar argumentos ao chamá-la, causará um erro: