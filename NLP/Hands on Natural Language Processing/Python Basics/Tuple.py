#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:25:41 2019

@author: pandit
"""

#Same as list but immutable
tuple1=(12,)

tuple1=('This is string',14.5,0.9,500,'Another string')
tuple2=('Next tuple',14.5,0.9,500)

#Printing elements of tuples

print(tuple1)
print(tuple1[1])
print(tuple1[2])
print(tuple1[3])

#Adding two tuples
tuple3=tuple1+tuple2

#Length of a tuple
print(len(tuple3))

#Looping through a tuple
#Method1

for  i in range(0,len(tuple1)):
    print(tuple1[i])
    

    
    