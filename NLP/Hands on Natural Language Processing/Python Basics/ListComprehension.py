#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 07:44:25 2019

@author: pandit
"""

#List Comprehension in python

numbers=[1,2,3,4,5,6,7,8,9,10]

#Copying using a loop
newNumbers=[]
for number in numbers:
    newNumbers.append(number)
    
#Copying using list comprehension
newNumbers=[number for number in numbers]

#copying using filtered based on condition
newNumbers=[number for number in numbers if number<=5]

#Copying and filtering based on another list
numbers2=[1,3,5,7,9]
newNumbers=[number for number in numbers if number not in numbers2]

print(newNumbers)

#some more examples
newNumbers=[number*2 for number in numbers]
newNumbers=[number for number in numbers if number%2==1]
print(newNumbers)

#Generator Comprehension
squareGen=(number**2 for number in numbers)
list(squareGen)

#Dictionary Comprehension
myDict={"apple":1,"orange":4,"banana":10}
newDict={key:myDict[key] for key in myDict.keys()}

newDict={key:myDict[key] for key in myDict.keys() if myDict[key]>5}

#Joining list of words
words=["I","love","Avengers","so","much"]
sentence=' '.join(words)
print(sentence)
sentence='.'.join(words)
print(sentence)
