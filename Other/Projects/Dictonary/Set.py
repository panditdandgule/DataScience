#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:03:23 2019

@author: pandit
"""

#Creating a Set
set1=set()
print("Intial blank Set: ")
print(set1)

#Creating a Set with the use of a string
set1=set("GeeksForGeeks")
print("\nSet with the use of String: ")
print(set1)

#Creating a Set with the use of Constructor
#(using object to Store String)
String='GeeksForGeeks'
set1=set(String)
print("\nSet with the use of an Object: ")
print(set1)

#Creating a set with the use of a List
set1=set(['Geeks','For','Geeks'])
print("\n Set with the use of List: ")
print(set1)

#Creating a Set with the a List of Numbers
set1=set([1,2,3,4,4,3,3,3,6,5])
print("\nSet with the use of Numbers: ")
print(set1)