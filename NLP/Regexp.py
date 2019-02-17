#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:24:03 2019

@author: pandit
"""

import nltk
from nltk.tokenize import  regexp_tokenize
sent1="I can't do this. I wan't do that."

from nltk.tokenize import word_tokenize
word_tokenize(sent1)

regexp_tokenize(sent1,"[\w']+")

regexp_tokenize(sent1,"[\w]+")

from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[\w']+")

tokenizer.tokenize(sent1)

