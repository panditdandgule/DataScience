#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 08:25:52 2019

@author: pandit
"""

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


text = """Stemming is funnier than a bummer says the sushi loving computer scientist.
She really wants to buy cars. She told me angrily.
It is better for you. Man is walking. We are meeting tomorrow."""

def stemmer_porter():
    port=PorterStemmer()
    print("\nStemmer")
    return "".join([port.stem(i) for i in text.split()])

def lemmatizer():
    wordnet_lemmatizer=WordNetLemmatizer()
    ADJ,ADJ_SAT,ADV,NOUN,VERB='a','s','r','n','v'
    print("\nVerb lemma")
    print(" ".join([wordnet_lemmatizer.lemmatize(i,pos="v") for i in text.split()]))
    print("\n Noun lemma")
    print(" ".join([wordnet_lemmatizer.lemmatize(i,pos='n') for i in text.split()]))
    print("\n Adjective lemma")
    print(" ".join([wordnet_lemmatizer.lemmatize(i,pos='a') for i in text.split()]))
    
if __name__=="__main__":
    print(stemmer_porter())
    lemmatizer()
