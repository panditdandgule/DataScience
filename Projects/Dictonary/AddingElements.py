#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:50:33 2019

@author: pandit
"""

#Creating an empty dictionary
Dict={}
print("Empty Dictionary: ")
print(Dict)

#Adding elements one at a time
Dict[0]='Geeks'
Dict[1]='For'
Dict[2]=1
print("\n dictionary after adding 3 elements : ")
print(Dict)

#Adding set of values to a single key
Dict['Value_set']=2,3,4
print("\n Dictionary after adding 3 elements")
print(Dict)

#Updating existing keys values
Dict[2]='Welcome'
print("\nUpdated key value:")
print(Dict)

#Adding Nested Key value to Dictionary
Dict[5]={'Nested':{'1':'Life','2':'Geeks'}}
print(Dict)