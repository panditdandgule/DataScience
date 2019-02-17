#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 07:52:08 2019

@author: pandit
"""

# This script give you idea how stemming has been placed by using NLTK and Polyglot libraries.
# It is part of morphological analysis

import nltk
from nltk.stem import PorterStemmer

word="unexpected"
text="disagreement"
text1 = "disagree"
text2 = "agreement"
text3 = "quirkiness"
text4 = "historical"
text5 = "canonical"
text6 = "happiness"
text7 = "unkind"
text8 = "dogs"
text9 = "expected"
words_derv=["happiness","unkind"]
word_infle=["dogs","expected"]
words=["unexpected"."disagreement","disagree","agreement","quirkiness","canonical","historical"]

def stemmer_porter():
    port=PorterStemmer()
    print("\nDerivational Morphemes")
    print("".join([port.stem(i) for i in text6.split()]))
    print("".join([port.stem(i) for in text7.split()]))
    print("\n Inflectional Morphemes")
    print("".join([port.stem(i) for i in text8.split()]))
    print("".join([port.stem(i) for i in text9.split()]))
    print("\n Some examples")
    print("".join([port.stem(i) for i in word..split()]))
    print("".join([port.stem(i) for i in text.split()]))
    print("".join([port.stem(i) for i in text1.split()])
    print("".join([port.stem(i) for i in text2.split()]))
    print("".join([port.stem(i) for i in text3.split()]))
    print("".join([port.stem(i) for i in text4.split()]))
    print("".join([port.stem(i) for i in text5.split()]))
    
    
def polyglot_stem():
    print("\n Derivational Morphemes using polyglot library")
    for w in words_derv:
        w=Word(w,language="en")
        print("{:<20}{}".format(w,w.morphemes))
    print("\nInflectional Morphemes using polyglot library")
    for w in word_infle:
        w=Word(w,language="en")
        print("{:<20}{}".format(w,w.morphemes))
    print("\nSome Morphemes examples using polyglot library")
    for w in word_infle:
        w=Word(w,language="en")
        print("{:<20}{}".format(w,w.morphemes))
        
if __name__=="__main__":
    stemmer_porter()
    polyglot_stem()