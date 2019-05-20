#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:15:47 2019

@author: pandit
"""

#Intializing dictionary
dict={'Name':'Nandini','Age':19}

#using setdefault() to print a key value
print("The value associated with Age is :",end=" ")
print(dict.setdefault('ID','NO ID'))

#Printing dictionary values
print("The dictionary values are: ")
print(str(dict))