# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:36:58 2019

@author: sulei
"""

a= [[1,2,3,4],
    [5,6,7,8], 
    [9,10,11,12]]
b = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

def t_3x4(x):
    for i in range(len(x)):
        for j in range(len(x[0])):
            b[j][i] = x[i][j]
    print(b)

print(t_3x4(a))   
c = map(t_3x4(a), a)

import numpy as np
f = np.transpose(a)