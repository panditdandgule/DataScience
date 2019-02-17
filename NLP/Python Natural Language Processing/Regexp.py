#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:47:07 2019

@author: pandit
"""

import re
def searchvsmatch():
    line=" I love animals."
    
    matchobj=re.match(r'animals',line,re.M | re.I)
    if matchobj:
        print("match",matchobj.group())
    else:
        print("No match!!")
    
    searchObj=re.search(r'animals',line,re.M | re.I)
    if searchObj:
        print("search:",searchObj.group())
    else:
        print("Nothing found!!")
        
def basicregex():
    line = "This is test sentence and test sentence is also a sentence."
    contactInfo = 'Doe, John: 1111-1212'
    print("-----------Output of re.findall()--------")
    # re.findall() finds all occurences of sentence from line variable.
    findallobj=re.findall(r'sentence',line)
    
    print(findallobj)
    
#re.search() and group wise extraction
groupwiseobj=re.search(r'(\w+),(\w+):(\S+)',contractinfo)
print("\n")
print("____________________Output of Groups_______________")

print("1st group ____________"+groupwiseobj.group(1))

print("2nd group ____________"+groupwiseobj.group(2))    

print("3rd group ____________"+groupwiseobj.group(3))

# re.sub() replace string
phone = "1111-2222-3333 # This is Phone Number"

#Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print("\n")
print("-----------Output of re.sub()--------")
print("Phone Num : ", num)