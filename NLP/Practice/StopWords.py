#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 21:17:03 2019

@author: pandit
"""

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

example_sent='This is a sample sentence,showing off the stop words filtration.'

stop_words=set(stopwords.words('english'))

word_tokens=word_tokenize(example_sent)

filtered_sentence=[w for w in word_tokens if not w in stop_words] 

filtered_sentence=[]
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
        
print(word_tokens)
print(filtered_sentence)

#word_tokenize accepts a string as an input not a file
stop_words=set(stopwords.words('english'))
file1 = open("text.txt") 
line = file1.read()# Use this to read file content as a stream: 
words = line.split() 
for r in words: 
    if not r in stop_words: 
        appendFile = open('filteredtext.txt','a') 
        appendFile.write(" "+r) 
        appendFile.close() 