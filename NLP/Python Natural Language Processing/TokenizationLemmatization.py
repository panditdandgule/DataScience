#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 08:12:23 2019

@author: pandit
"""

# This script give you idea how tokenization and lemmatization has been placed by using NLTK.
# It is part of lexical analysis

from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def wordtokenization():
    content="""Stemming is funnier than a bummer says the sushi loving computer scientist"""
    print(word_tokenize(content))
    
def wordlemmatization():
    wordlemma=WordNetLemmatizer()
    print(wordlemma.lemmatize('cars'))
    print(wordlemma.lemmatize('walking',pos='v'))
    print(wordlemma.lemmatize('meeting',pos='n'))
    print(wordlemma.lemmatize('meeting',pos='v'))
    print(wordlemma.lemmatize('better',pos='a'))
    
if __name__=="__main__":
    wordtokenization()
    print("\n")
    print("______________Word Lemmatization__________")
    wordlemmatization()