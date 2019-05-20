#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 12:02:22 2019

@author: pandit
"""

#Intial Dictionary
Dict={5:'Welcome',6:'To',7:'Geeks',
      'A':{1:'Geeks',2:'For',3:'Geeks'},
      'B':{1:'Geeks',2:'Life'}}

print("Initial Dictionary: ")
print(Dict)

#Deleting a key value
del Dict[6]
print("\n Deleting a specific key: ")
print(Dict)

#Deleting a key from Nested Dictionary
del Dict['A'][2]
print("\n Deleting a key from Nested Dictionary: ")
print(Dict)

#Deleting a key using pop()
Dict.pop(5)
print("\n Popping specific element")
print(Dict)

#Deleting a key using popitem
Dict.popitem()
print("\n Pops first element")
print(Dict)

#Deleting entire Dictionary
Dict.clear()
print("\n Deleting Entire Dictionary: ")
print(Dict)