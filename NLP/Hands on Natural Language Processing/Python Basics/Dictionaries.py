#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:36:13 2019

@author: pandit
"""

#Key -Value Pairs

dict1={}
#Adding elements of  the dictionary

dict1['Apple']='Apple is a fruit'
dict1['Orange']='Orange is a fruit'
dict1['Car']='Cars are fast'
dict1['Python']='Python is a snake'

#Printng dictionary elements

print(dict1)
print(dict1['Apple'])
print(dict1['car'])
print(dict1['python'])

print(dict1.get('jython','Does not exist'))

#Deleting elements

del dict1['Apple']

#Length of dictionary
print(len(dict1))

#List of keys and Values
listOfKeys=list(dict1.keys())
listOfValues=list(dict1.values())

#looping throug list
for key in dict1.keys():
    print(dict1[key])
    
    
