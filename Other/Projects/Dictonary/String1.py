#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:18:46 2019

@author: pandit
"""

#Creating a string with single Quotes
String1='Welcome to the Geeks World'
print("String with the use of Single Quotes:")

#Access character of String
String1="GeeksForGeeks"
print("Initial String: ")
print(String1)

#Printing Last character
print("\n Last character of string is:")
print(String1[-1])

#Printing 3rd to 12th character
print("\nSlicing characters from 3-12")
print(String1[3:12])

#Printing characters between 3rd and 2nd last character
print("\nSlicing characters between"+"3rd and 2nd last character: ")
print(String1[3:-2])

#Update a character string
String1="Hello, I'm a Geek"
print("Initial String: ")
print(String1)

#Updating a character of the String
String1[2]='p'
print("\n Updating character at 2nd Index:")
print(String1)

#Update entire String
String1="Hello, I'm a Geek"
print("Initial String: ")
print(String1)

#Updating a string
String1="Welcome to the Geek World"
print("\nUpdated String: ")
print(String1)