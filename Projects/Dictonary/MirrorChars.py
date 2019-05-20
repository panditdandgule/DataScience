#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 07:46:47 2019

@author: pandit
"""

def mirrorChars(input,k):
    #create dictionary
    original='abcdefghijklmnopqrstuvwxyz
    reverse='zyxwvutsrqponmlkjihgfedcba'
    dictChars=dict(zip(original,reverse))
    
    #separate out string after length k to change
    prefix=input[0:k-1]
    suffix=input[k-1:]
    mirror=' '
    
    #change into mirror
    for i in range(0,len(suffix)):
        mirror=mirror+dictChars[suffix[i]]
        
    #concat prefix and mirrored part
    print(prefix+mirror)
    
#Driver program
if __name__=="__main__":
    input='paradox'
    k=3
    mirrorChars(input,k)