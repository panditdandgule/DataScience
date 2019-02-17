#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:45:32 2019

@author: pandit
"""

#Block of meaningful code

def functionName(arg1,arg2):
    print(arg1,arg2)
    
functionName('The number is',12)

def sumOfTwo(num1,num2):
    return(num1+num2)
    
print(sumOfTwo(12,15))

#Our own length function

def length(l):
    count=0
    for item in l:
        count+=1
    return count

print(length([12,14,566]))

