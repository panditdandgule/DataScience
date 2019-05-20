#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:39:12 2019

@author: pandit
"""

#Creating an empty dictionary
Dict={}
print("Empty Dictionary: ")
print(Dict)

#Creating a Dictionary with Integer keys
Dict={1:'Geeks',2:'For',3:'Geeks'}
print("\n Dictionary with the use of Integer Keys: ")
print(Dict)

#Creating dictionary with mixed keys
Dict={'Name':'Geeks',1:[1,2,3,4]}
print("\n Dictionary with the use of Mixed keys:")
print(Dict)

#creating a dictionary with dict() method
Dict=dict({1:'Geeks',2:'For',3:'Geeks'})
print(Dict)

#Creating a Dictionary with each item as a pair
Dict=dict([(1,'Geeks'),(2,'For')])
print("\n Dictionary with each item as a pair: ")
print(Dict)

