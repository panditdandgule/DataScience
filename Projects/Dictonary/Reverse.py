#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 07:53:21 2019

@author: pandit
"""

#New tuple is created
def Reverse(tuples):
    new_tup=tuples[::-1]
    #print(new_tup)
    return new_tup

#Driver code
tuples=('z','a','d','f','g','e','e','k')
print(Reverse(tuples))