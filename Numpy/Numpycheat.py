#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 10:52:37 2019

@author: pandit

The numpy library is the core library for scientific computing
in Python. It provides a high-perfomance multidimensional array
object, and tools for  working with these arrays.
"""

import numpy as np

#Creating Arrays
a=np.array([1,2,3])
print(a)
b=np.array([(1.5,2,3),(4,5,6)],dtype=float)
c=np.array([[(1.5,2,3),(4,5,6)],[(3,2,1),(4,5,6)]],dtype=float)

#Intial Placeholders
np.zeros((3,4)) #Create an array of zeros
np.ones((2,3,4),dtype=np.int16) #Create an array of ones
d=np.arange(10,25,5) #Create ana array of evenly spaced values
d
np.linspace(0,2,9)

#create a constant array
e=np.full((2,2),7)
e
#Create 2x2 identity matrix
f=np.eye(2)
f

#create an array with random variable
np.random.random((2,2))

#create an empty array
np.empty((3,2))

#Saving and Loading on Disk
np.save('my_array',a)

np.load('my_array.npy')

#Saving and Loading Text files
np.loadtxt("myfile.txt")
np.genfromtxt("my_file.csv",delimiter=',')
np.savetxt("myarray.txt",a,delimiter=" ")

#Inspecting Array
a.shape #Array dimensions
len(a) #length of array
b.ndim #Number of array dimensions
e.size #Number of array elements
b.dtype #Data type of array elements
b.dtype.name #Name of data type
b.astype(int)

#Asking for help
np.info(np.ndarray.dtype)

#Array mathematics
g=a-b #substraction
print(g)
np.subtract(a,b)

#addition
b+a
np.add(b,a)

np.divide(a,b)
np.multiply(a,b)

np.exp(b)
np.sqrt(b)
np.sin(a)
np.cos(b)
np.log(a)
e.dot(f)


#comparison
a==b  #Elementwise comparison

a<2 #Eelement wise comparison

#Aggregate functions
a.sum() #Arraywise sum

a.min() #Arraywise minimum values
b.max(axis=0) #maximum value of array rows
b.cumsum(axis=1) #comulative sum of the  elements
b.mean() #mean
b.median() #Median
a.corrcoef() #Correlation coefficient
np.std(b) #Standard deviation

#Copying arrays
h=a.view() #create view of the array with same data
np.copy(a) #create a copy of the array
h=a.copy() #create a deep copy the array

#Sorting Arrays
a.sort() #sort of the array
c.sort(axis=0)

#Subsetting,Slicing,Indexing
#subsetting
a[2] #Select the element of the second index
b[1,2] #select the element at row 1 column 2

a[0:2] #select items at index 0 and 1
b[0:2,1]#Select items at rows 0 and 1 in column 1

b[:1] #select all items at row 0(Equvivalent to b[0:1,:])

#Reverse array
a[::-1]

#Boolean indexing
a[a<2]

#Fancy Indexing
b[[1,0,1,0],[0,1,2,0]]
b[[1,0,1,0]][:,[0,1,2,0]]

#Array Manipulation
i=np.transpose(b) #permute array dimensions
i.T

##chage array shape
b.ravel() #Flatten the array
g.reshape(3,-2)  #Reshpae but dont change data

#Adding and removing elements

h.resize((2,6)) #Return new array with shape(2,6)
np.append(h,g)
np.insert(a,1,5)
np.delete(a,[1])

#Combining array
np.concatenate((a,d),axis=0) #concatenate arrays
np.vstack((a,b)) #Stack arrays vertically(row-wise)

np.r_(e,f) 
np.hstack #Stack arrays horizentally column wise

np.column_stack((a,d))

np.c_(a,d)

#splitting arrays
np.split(a,3)

np.vsplit(c,2)













