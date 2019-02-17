#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 08:03:25 2019

@author: pandit
"""

"""
if condition:
    statement
elif condition:
    statement
else:
    statements
    
"""

#Grade of student

marks=90

#No braces in python. Indectation does the job

if marks>90:
    print("Grade 0")
elif marks>80:
    print("Grade E")
elif marks>70:
    print("Grade A")
elif marks>60:
    print("Grade B")
elif marks>50:
    print("Grade C")
else:
    print("Better Luck next time")
    

#Divisible or not

number1=45
number2=5

if number1%number2==0:
    print("Divisible")
else:
    print("not divisible")
    
