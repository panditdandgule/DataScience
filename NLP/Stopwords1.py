#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:31:14 2019

@author: pandit
"""

import nltk
from nltk.corpus import stopwords

ensw=stopwords.words('english')
ensw

from nltk.tokenize import word_tokenize

parag1='What are you doing exactly right now? i want to  go my office'

parag1

paragArray=word_tokenize(parag1)

paragArray

filterArr=[item for item in paragArray if item not in ensw]
filterArr

ensw

paragArray

filterArr