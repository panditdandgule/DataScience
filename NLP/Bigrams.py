#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:56:41 2019

@author: pandit
"""

import  nltk
from nltk.corpus import webtext

#bigrams means two words

from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

textWords=[w.lower() for w in webtext.words('pirates.txt')]

finder=BigramCollocationFinder.from_words(textWords)

finder.nbest(BigramAssocMeasures.likelihood_ratio,10)

from nltk.corpus import  stopwords
ignore_words=set(stopwords.words('english'))

ignore_words

filterStops=lambda w: len(w) < 3 or w in ignore_words

finder.apply_word_filter(filterStops)
finder.nbest(BigramAssocMeasures.likelihood_ratio,10)

