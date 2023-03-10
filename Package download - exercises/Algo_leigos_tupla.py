# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 22:15:11 2023

@author: Thiago
"""

MyTuple = (1,2,3,(4,5,6,(7,8,9)))
MyNewTuple = MyTuple.__add__((10,11,12,(13,14,15)))
print(MyNewTuple)
print(MyTuple)

for Value1 in MyTuple:
    if type (Value1)==int:
        print(Value1)
    else:
        for Value2 in Value1:
            if type (Value2)==int:
                print('\t', Value2)
            else:
                for Value3 in Value2:
                    if type (Value3)==int:
                        print('\t\t', Value3)
for Value4 in MyNewTuple:
    if type (Value4)==int:
        print('\t\t\t', Value4)
    else:
        for Value5 in Value4:
            if type (Value5)==int:
                print('\t\t\t\t', Value5)

