#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:22:31 2019

@author: pandit
"""

from collections import OrderedDict

def printDistinct(input):
    #convert list into ordered dictionary
    ordDict=OrderedDict.fromkeys(input)
    
    #iterate through dictionary and get list of keys
    #list of keys will be resultent distinct elements
    #in array
    result=[key for(key,value) in ordDict.items()]
    
    #concatenate list of elements with ','
    print(','.join(map(str,result)))
    
#Driver program
if __name__ == "__main__":
    input=[12,10,8,45,2,10,10,45]
    printDistinct(input)