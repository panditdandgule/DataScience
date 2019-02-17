#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:08:33 2019

@author: pandit
"""

import nltk
simplesentence="Bangalore is the capital of Karnataka"
wordsSentence=nltk.word_tokenize(simplesentence)
print(wordsSentence)

partsOfSpeechTags=nltk.pos_tag(wordsSentence)
print(partsOfSpeechTags)


