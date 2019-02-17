#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:49:35 2019

@author: pandit
"""

from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer

def wordtokenization():
    content = """Stemming is funnier than a bummer says the sushi loving computer scientist.
    She really wants to buy cars. She told me angrily. It is better for you.
    Man is walking. We are meeting tomorrow. You really don't know..!"""
    print(word_tokenize(content))
    
def wordlemmatization():
    wordlemma=WordNetLemmatizer()
    print(wordlemma.lemmatize('cars'))
    print(wordlemma.lemmatize('walking',pos='v'))
    print(wordlemma.lemmatize('meeting',pos='n'))
    print(wordlemma.lemmatize('better',pos='a'))
    
    
def wordlowercase():
    text="I am a person"
    print(text.lower())
    
if __name__ == "__main__":
    wordtokenization()
    print("\n")
    wordlemmatization()
    wordlowercase()