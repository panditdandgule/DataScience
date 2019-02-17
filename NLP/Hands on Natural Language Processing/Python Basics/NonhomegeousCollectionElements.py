#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:18:47 2019

@author: pandit
"""

list1=[12,12.8,'This is a string']

#Printing the list

print(list1)
print(list1[0])
print(list1[1])
print(list1[2])

#Adding elements to the list

list1.append(50)
list1.insert(0,'Another String')

print(list1[3])

#Update list
list1[1]=20

#Deleting elements of the list

list1.pop()

del list1[2]

#Length of the list
print(len(list1))

#Looping through list
for i in range(0,len(list1)):
    print(list1[i])
    list1[i]=12
    
#Method2 :For each technique (Mainly for accessing)

for item in list1:
    print(item)
    
