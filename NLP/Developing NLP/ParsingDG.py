#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 07:27:52 2019

@author: pandit
"""

import nltk
grammar=nltk.grammar.DependencyGrammar.fromstring("""
                                                  'savings'->'small'
                                                  'yield'->'savings'
                                                  'gains'->'large'
                                                  'yield'->'gains'
                                                  """)
sentence='small savings yield large gains'
dp=nltk.parse.ProjectiveDependencyParser(grammar)
for t in sorted(dp.parse(sentence.split())):
    print(t)
    t.draw()