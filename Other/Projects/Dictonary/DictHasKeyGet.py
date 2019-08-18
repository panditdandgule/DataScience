#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:00:20 2019

@author: pandit
"""

#has_key() -This function return true if specified key is present in the dictionary else return false

#get(key,def_val) -This function return the key value associated with the key mentioned in arguments.

#has_key() and get()
#Initializing dictionary
dict={'Name':'Nandini','Age':19}

#using has_key() to check if dic1 has a key
if dict.has_key('Name'):
    print("Name is a key")
else:
    print("Name is not a key")
    
#using get() to print a key value
print("The value associated with ID is: ")
print(dict.get('ID','Not Present'))

#printing dictionary values
print("The dictioanry values are: ")
print(str(dict))