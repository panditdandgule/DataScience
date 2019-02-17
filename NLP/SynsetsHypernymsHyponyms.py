#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:39:01 2019

@author: pandit
"""

import nltk
from nltk.corpus import wordnet
word1="weapon"

synArray=wordnet.synsets(word1)
print(synArray)

woi=synArray[0]
woi

woi.definition()

woi.name()

woi.pos()
woi.hypernyms()

woi.hyponyms()
