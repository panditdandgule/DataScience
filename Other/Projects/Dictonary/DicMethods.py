#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:37:30 2019

@author: pandit
"""

#Python code to demonstrate working of str() and items()

#Initializing dictionary
dic={'Name':'Nandini','Age':19}

#using str() to display dic as string
print("The constituents of dictionary as string are: ")
print(str(dic))

#Using str() to display dic as list
print("The constituents of dictionary as list are: ")
print(dic.items())

#Python code to demonstrate working of len() and type()
#Intializing dictionary
dic={'Name':'Nandini','Age':19,'ID':2541997}

#Initializing list
li=[1,3,5,6]

#using len() to display dic size
print("The size of dic is: ",end=" ")
print(len(dic))

#Using type() to display data type
print("The data type of li is: ",end=" ")
print(type(li))