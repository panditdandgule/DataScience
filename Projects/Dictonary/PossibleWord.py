#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:59:59 2019

@author: pandit
"""

#Function to print words which can be  created 
#using given set of characters

from collections import Counter

def possibleWords(input,charSet):
    
    #traverse words in list one by one
    for word in input:
        
        #convert word into dictionary
        dict=Counter(word)
        
        #now check if all keys of current word
        #are present in given character set
        flag=1
        for key in dict.keys():
            if key not in charSet:
                flag=0
                
        #if all keys are present (flag=1)
        #then print the word
        if flag==1:
            print(word)
            
#Driver program
if __name__ == "__main__":
    input=['go','bat','me','eat','goal','boy','run']
    charSet=['e','o','b','a','m','g','l']
    possibleWords(input,charSet)