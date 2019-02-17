#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:11:39 2019

@author: pandit
"""

#Loop control  statements

i=1

while i<=10:
    print(i)
    i+=1
    
#Break statement
i=1
while i<=10:
    if i>5:
        #come out of this loop
        break
    print(i)
    i+=1
    
    
#continue
i=1
while i<=10:
    if i>=4 and i<=7:
        i+=1
        continue
    print(i)
    i+=1
    
for i in range(1,11):
    if i>=4 and i<=7:
        continue
    print(i)
    
#Pass

i=1
if i==1:
    pass
else:
    pass


    