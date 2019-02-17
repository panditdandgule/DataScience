#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:08:25 2019

@author: pandit
"""

#Two types of loops in Python

#While loop
"""
whilte condition:
    Statements
"""

i=1
while i<=10:
    print(i)
    i+=1
    
#For loop
for i in range(1,11):
    print(i)
    
#Nested loops
"""
12345
12345
12345
12345
"""

for i in range(1,5):
    for j in range(1,6):
        print(j,end=" ")
    print()