#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 09:13:37 2019

@author: pandit
"""

import nltk

paragraph="""The Taj Mahal was built by Emperor Shah Jahan"""

#POS Tagging
words=nltk.word_tokenize(paragraph)
words

tagged_words=nltk.pos_tag(words)
tagged_words

#Named Entity Recognition
namedEnt=nltk.ne_chunk(tagged_words)
namedEnt.draw()