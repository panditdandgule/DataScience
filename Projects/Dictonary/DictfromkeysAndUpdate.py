#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:54:08 2019

@author: pandit
"""

#fromkeys() and update()

#Intializing dictionary 1
dic1={'Name':'Nandini','Age':19}

#Initializing dictionary 2
dic2={'ID':2541997}

#Initizlizing sequance
sequ=('Name','Age','ID')

#Using update to add dic2 values in dic 1
dic1.update(dic2)

#printing the updated dictionary values
print("The updated dictionary is: ")
print(str(dic1))

#using fromkeys() to transform sequence into dictionary
dict=dict.fromkeys(sequ,5)

#printing new dictionary values
print("The new dictionary values are: ")
print(str(dict))