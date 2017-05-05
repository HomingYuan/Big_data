# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:19:20 2017

@author: user
"""

import  numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn
import pandas as pd

# create array

a =np.array([2,3,4]) # 1d array 注意array 必须是列表 np.array(2,3,4)会报错
#print(a)

# iteration item from array
'''
for i in a:
    print(i) 
'''
b = np.array([(1.5,2,3),(4,5,6)]) #2d array
# print(b)
'''
for k in range(len(b)):
    for j in range(len(b[k])):
        print(b[k][j])
'''

def print_in_order(b):
    for k in range(len(b)):
        for j in range(len(b[k])):
            print(b[k][j])
            # return [b[k][j] for k in range(len(b)) for j in range(len(b[k]))]
           
'''
c = np.array([(1.5,2,3),(4,5,6)])
print_in_order(c)
'''
def d_to_1d(d):
    return [b[k][j] for k in range(len(b)) for j in range(len(b[k]))]

# print(d_to_1d(c))

# print(b.min(),b.max(),b.sum(),b.mean())
'''
x1 = np.ones((2,2))
x2 = np.eye(2)
print(np.vstack((x1,x2)))  # merge on vertical direction
print(np.hstack((x1,x2)))
'''

# transpose

a = np.array([[1,0],[2,3]])
print(a)

print(a.transpose()) #transpose


     
print(np.trace(a)) #  trace

import numpy.linalg as nplg

print(nplg.eig(a)) # 特征值，特征向量

print(a.ravel())
print(a.reshape(1,4))
print(a.reshape(4,1))
     
     