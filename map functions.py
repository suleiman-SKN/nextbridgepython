# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:12:06 2019

@author: sulei
"""

a = [i for i in range(50) if i%2==0]

a = float(a)
b = [2,5,4,7,9]

def squares(x):
    return x**2

list(squares(a))

print(a**2)

list(map(squares, a))
