#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:42:24 2019

@author: pandit
"""

#console i/o

inp=('Enter a number:')
number1=int(inp)

inp=input('Enter a number:')
number2=int(inp)

#Writing to a file
inp=input=('Enter some text')
with open('textFile.txt','a') as f:
    f.write(inp)
    
#Reading from a file

with open('textFile.txt','r') as f:
    string=f.read()
    print(string)
    
