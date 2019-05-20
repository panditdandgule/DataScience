#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 08:10:58 2019

@author: pandit
"""

#Creating a set
set1=set()
print("Intial blank set: ")
print(set1)

#Adding element to set
set1.add(8)
set1.add(9)
set1.add(12)
print("\n Set after Addition of Three elements: ")
print(set1)

#Adding elements to the set using Iterator
for i in range(1,6):
    set1.add(i)
    
print("\n Set after Addition of elements from 1-5: ")
print(set1)

#Adding Tuples to the Set
set1.add((6,7))
print("\nAfter Addition of a Tuple: ")
print(set1)

#Using Update function
set1.update([10,11])
print("\nSet after Addition elements using update: ")
print(set1)

set1=set([1,2,3,4,5,6,7,8,9,10,11,12])
print("Intial  set: ")
print(set1)

#Removing elements from set
set1.remove(5)
set1.remove(6)

set1

#Removing elements form set
set1.discard(8)
set1.discard(9)

print("\n Set after Discarding two elements: ")
print(set1)

#Removing elements from set using iterator method
for i in range(1,5):
    set1.remove(i)
print(set1)

#Removing element from the set using the pop()
set1.pop()
print(set1)

set1.clear()

A={10,20,30,40,50}
B={110,30,80,40,60}

print(A.difference(B))
print(B.difference(A))

set1={2,4,5,6}
set2={4,6,7,8}
set3={4,6,7}

set1.intersection(set2)
set1.intersection(set3)



