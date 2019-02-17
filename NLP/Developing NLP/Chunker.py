#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 07:14:35 2019

@author: pandit
"""

import nltk

text="Lalbagh Botanical Gardens is a well known botanical garden in Bengali"
sentences=nltk.sent_tokenize(text)
for sentence in sentences:
    words=nltk.word_tokenize(sentence)
    tags=nltk.pos_tag(words)
    chunks=nltk.ne_chunk(tags)
    print(chunks)