#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 07:39:05 2018

@author: pandit
"""

from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample=gutenberg.raw("bible-kjv.txt")

print(sent_tokenize(sample))