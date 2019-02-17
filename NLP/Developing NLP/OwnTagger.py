#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 22:23:34 2019

@author: pandit
"""

import nltk

def learnDefaultTagger(simpleSentence):
    wordsInSentence=nltk.word_tokenize(simpleSentence)
    tagger=nltk.DefaultTagger("NN")
    posEnabledTags=tagger.tag(wordsInSentence)
    print(posEnabledTags)
    
def learnRETagger(simpleSentence):
    customPatterns=[
            (r'.*ing$', 'ADJECTIVE'),             # running
        (r'.*ly$', 'ADVERB'),                 # willingly
        (r'.*ion$', 'NOUN'),                  # intimation
        (r'(.*ate|.*en|is)$', 'VERB'),        # terminate, darken, lighten
        (r'^an$', 'INDEFINITE-ARTICLE'),      # terminate
        (r'^(with|on|at)$', 'PREPOSITION'),   # on
        (r'^\-?[0-9]+(\.[0-9]+)$', 'NUMBER'), # -1.0, 12345.123
(r'.*$', None),]
def learnLookupTagger(simpleSentence):
    mapping = {
        '.': '.', 'place': 'NN', 'on': 'IN',
        'earth': 'NN', 'Mysore' : 'NNP', 'is': 'VBZ',
        'an': 'DT', 'amazing': 'JJ'
    }
    tagger = nltk.UnigramTagger(model=mapping)
    wordsInSentence = nltk.word_tokenize(simpleSentence)
    posEnabledTags = tagger.tag(wordsInSentence)
    print(posEnabledTags)
    
if __name__ == '__main__':
    testSentence="Mysore is an amazing place on earth. I have visited mysore 10 times"
    learnDefaultTagger(testSentence)
    learnRETagger(testSentence)
    learnLookupTagger(testSentence)