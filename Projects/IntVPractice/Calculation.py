#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:21:01 2019

@author: pandit
"""

class Calculation:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        self.a-self.b
    def mul(self):
        self.a*self.b
    def div(self):
        self.a/self.b
        
a=int(input("Enter a first number"))
b=int(input("Enter a second number"))

obj=Calculation(a,b)

choice=1
while(choice!=0):
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")
    
    choice=int(input("Enter a your choice"))
    if choice==1:
        print("Addition:",obj.add())
    elif choice==2:
        print("Substraction:",obj.sub())
    elif choice==3:
        print("Multiplication:",obj.mul())
    elif choice==4:
        print("Division:",obj.div())
    else:
        print("Invalid choice please try again")
        continue
print()