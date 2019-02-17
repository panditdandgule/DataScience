#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:10:34 2019

@author: pandit
"""

import nltk
from nltk.tokenize import sent_tokenize


sentences=sent_tokenize(parag)

print(sentences)

import nltk.data

tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
parag="My name is Pandit. I like python"
tokenizer.tokenize(parag)

from nltk.tokenize import word_tokenize
words=word_tokenize(parag)

print(words)

from nltk.tokenize import TreebankWordTokenizer()
tok2=TreebankWordTokenizer()
