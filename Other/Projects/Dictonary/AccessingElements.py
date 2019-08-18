#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:57:43 2019

@author: pandit
"""

#Python program to demonstrate accessing a element form a dictionary

#Creating a Dictionary
Dict={1:'Geeks','name':'For',3:'Geeks'}

#accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

#accessing a element using key
print("Acessing a element using key:")
print(Dict[1])

#accessing a element using get() method
print("Accessing a element using get: ")
print(Dict.get(3))