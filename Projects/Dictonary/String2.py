#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 17:34:51 2019

@author: pandit
"""

#Intial String
String1='''I'm a Geek'''
print("Intial String with use of Triple Quotes: ")
print(String1)

#Escaping Single Quote
String1='I\'m a "Geek"'
print("\nEscaping Single Quote: ")
print(String1)

#Escaping Double Quotes
String1="I'm a \"Geek\""
print("\nEscaping Double Quotes: ")
print(String1)

#Printing Paths with the use of Escape sequences
String1="C:\\Python\\Geeks\\"
print("\n Escaping Backslashes: ")
print(String1)

#Default order
String1="{} {} {}".format('Geeks','For','Life')
print("Print String in default order: ")
print(String1)

#Positional Formatting
String1="{1}{0}{2}".format('Geeks','For','Life')
print("\n Print String in Positional order: ")
print(String1)

#Keyword  Formatting
String1="{l} {f} {g}".format(g='Geeks',f='For',l='Life')
print("\n Print String in order of keywords: ")
print(String1)

#Formattng of Integers
String1="{0:b}".format(16)
print("\nBinary representation of 16 is : ")
print(String1)


#Formatting of Floats
String1="{0:e}".format(165.6458)
print("\n Exponent representation of 145.6458 is")
print(String1)

#Rounding off Integers
String1="{0:.2f}".format(1/6)
print("\nOne-sixth is:")
print(String1)

#Python programs to demonstrate rfind and find
str="geeksforgeeks is for geeks"
str2="geeks"

#using find() to find first occurence of str2
print("The first occurence of str2 is at : ",end="")
print(str.find(str2,4))

#Using rfind
print("The last occurrence of str2 is at : ",end="")
print(str.rfind(str2,4))