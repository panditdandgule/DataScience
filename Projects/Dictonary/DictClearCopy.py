#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:47:26 2019

@author: pandit
"""

#Clear() and copy()

#Initializing dictionary
dic1={'Name':'Nandini','Age':19}

#Initializing dictionary
dic3={}

#using copy() to make shallow copy of dict
dic3=dic1.copy()

#Printing new dictionary
print("The new copied dictionary is: ")
print(dic3.items())

#clearning the dictionary
dic1.clear()

#printing cleared dictionary
print("The content of deleted dictionary is :",end=" ")
print(dic1.items())

