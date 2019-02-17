#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:53:11 2018

@author: pandit
"""

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps=PorterStemmer()

example_words=["Python","pythoner","pythoning","pythoned","pythonly"]

#for w in example_words:
 #   print(ps.stem(w))
 
new_text="It is very important to be pythonly whil you are pythoning with python"
 
words=word_tokenize(new_text)
 
for w in words:
     print(ps.stem(w))
    