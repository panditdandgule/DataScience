#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 22:31:16 2019

@author: pandit
"""


# First, you're going to need to import wordnet: 
from nltk.corpus import wordnet 
  
# Then, we're going to use the term "program" to find synsets like so: 
syns = wordnet.synsets("program") 
  
# An example of a synset: 
print(syns[0].name()) 
  
# Just the word: 
print(syns[0].lemmas()[0].name()) 
  
# Definition of that first synset: 
print(syns[0].definition()) 
  
# Examples of the word in use in sentences: 
print(syns[0].examples()) 


import nltk 
from nltk.corpus import wordnet 
synonyms = [] 
antonyms = [] 
  
for syn in wordnet.synsets("good"): 
    for l in syn.lemmas(): 
        synonyms.append(l.name()) 
        if l.antonyms(): 
            antonyms.append(l.antonyms()[0].name()) 
  
print(set(synonyms)) 
print(set(antonyms)) 


import nltk 
from nltk.corpus import wordnet 
# Let's compare the noun of "ship" and "boat:" 
  
w1 = wordnet.synset('run.v.01') # v here denotes the tag verb 
w2 = wordnet.synset('sprint.v.01') 
print(w1.wup_similarity(w2)) 

