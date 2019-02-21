#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 07:58:26 2018

@author: pandit
"""

from nltk.corpus import wordnet
syns=wordnet.synsets("program")

#synset
print(syns[0].name())

#just the word
print(syns[0].lemmas()[0].name())

#definition
print(syns[0].definition())

#examples
print(syns[0].examples())

synonyms=[]
antonyms=[]

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())
            
            
print(set(synonyms))
print(set(antonyms))