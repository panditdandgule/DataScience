#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 20:42:55 2019

@author: pandit
"""

import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer

#instantiate the vectotizer
vectorizer=CountVectorizer()

#create 3 documents
document1='Hi How are you'
document2='today is a very very pleasant day and we can have some fun fun fun'
document3='This was an amazing experience'

#Put them together
listofdocuments=[document1,document2,document3]

#fit them as bag of words
bag_of_words=vectorizer.fit(listofdocuments)

print(bag_of_words)

#apply transform method
bag_of_words=vectorizer.transform(listofdocuments)

#print bag of words
print(bag_of_words)

print(vectorizer.vocabulary_.get('very'))
print(vectorizer.vocabulary_.get('fun'))
