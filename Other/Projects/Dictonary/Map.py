#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:31:52 2019

@author: pandit
"""

#Return double of n
def addition(n):
    return n+n

numbers=(1,2,3,4)
result=map(addition,numbers)
print(list(result))

numbers=(1,2,3,4)
result=map(lambda x:x+x, numbers)
print(list(result))

#Add two lists using map and lambda
numbers1=[1,2,3]
numbers2=[4,5,6]

result=map(lambda x,y:x+y, numbers1,numbers2)
print(list(result))