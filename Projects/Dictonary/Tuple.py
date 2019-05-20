#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 22:19:38 2019

@author: pandit
"""

#Creating an empty tuple
Tuple1=()
print("Initial empty tuple: ")
print(Tuple1)

#Creating a Tuple with use of Strings
Tuple1=('Geeks','For')
print("\n Tuple with the use of String: ")
print(Tuple1)

#Creating a Tuple with the use of list
list1=[1,2,3,4,5,6]
print("\nTuple using List: ")
print(tuple(list1))

#Creating a Tuple with the use of loop
Tuple1=('Geeks')
n=5
print("\nTuple with a loop")
for i in range(int(n)):
    Tuple1=(Tuple1,)
    print(Tuple1)
    
#Creating a Tuple with the use of built-in function
Tuple1=tuple('Geeks')
print("\nTuple with the use of function: ")
print(Tuple1)

#Creating a Tuple with Mixed Datatypes
Tuple1=(5,'Welcome',7,'Geeks')
print("\nTuple with mixed DataTypes: ")
print(Tuple1)

#Creating a Tuple with nested tuples
Tuple1=(0,1,2,3)
Tuple2=('python','geek')
Tuple3=(Tuple1,Tuple2)
print("\nTuple with nested tuples: ")
print(Tuple3)

#Concatenaton of tuples
Tuple1=(0,1,2,3)
Tuple2=('Geeks','For','Geeks')
print(Tuple1+Tuple2)

#Function to print unique rowss in a tuple

def uniqueRows(input):
    #Convert each row (list) into tuple
    input=map(tuple,input)
    
    #put all rows in set
    result=set(input)
    
    #print all unique rows
    for row in list(result):
        print(row)
        
#Driver program
if __name__ =="__main__":
    input=[[0,1,0,0,1],
           [1,0,1,1,0]]
    uniqueRows(input)