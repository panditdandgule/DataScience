#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 08:04:18 2019

@author: pandit
"""

import pickle
import string
import os
from nltk import ngrams,FreqDist,word_tokenize
from numpy import arange
import matplotlib.pyplot as plt
%matplotlib inline

def ultimate_tokenize(sentence):
    sentence=sentence.translate(str.maketrans('','',string.punctuation+string.digits))
    return word_tokenize(sentence.lower())

#Understanding the Process
simple_example_text='Oh,then,I see Queen Mab hath been with you.'

simple_example_tokens_words=ultimate_tokenize(simple_example_text)

simple_example_tokens_words

simple_example_tokens_chars=list(simple_example_tokens_words[0])
simple_example_tokens_chars


simple_example_tokens_words_unigrams=list(ngrams(simple_example_token_words[1]))
simple_example_tokens_words_unigrams

fdist=FreqDist(simple_example_tokens_words_unigrams)
fdist

unigram_dict=dict()
for k,v in fdist.items():
    unigram_dict[' '.join(k)]=v
unigram_dict


