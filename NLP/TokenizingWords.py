#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:07:00 2018

Tokenizing words and sentance

@author: pandit
"""

from nltk.tokenize import sent_tokenize,word_tokenize

#tokenizing -words tokenizers... sentence tokenizers
#lexicon and corporas 
#corpora -body of text. ex: medical journals, presidential speeches, English language
#lexicon-words and their means

#investor speak 'bull' = someone who is positive about the market
#english-speak 'bull' -scary animal you dont want running @you

example_text="Hello Mr.Smith, how are you doing today? The wheater is great and python is awesome."

#print(sent_tokenize(example_text))

#print(word_tokenize(example_text))

for i in sent_tokenize(example_text):
    print(i)
    

for i in word_tokenize(example_text):
    print(i)