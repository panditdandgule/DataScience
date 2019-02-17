#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 07:04:51 2019

@author: pandit
"""

import random 
import nltk

text="""Global warming or climate change has become a worldwide concern.It is gradually developing into an unprecedented environment"""

#Order of the grams
n=2

#Our N-Grams
ngrams={}

#Building the model
words=nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram=' '.join(words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram]=[]
    ngrams[gram].append(words[i+n])
    
#Testing the model
currentGram=' '.join(words[0:n])
result=currentGram
for i in range(30):
    if currentGram not in ngrams.keys():
        break
    possibilities=ngrams[currentGram]
    nextItem=possibilities[random.randrange(len(possibilities))]
    result +=' '+nextItem
    rWords=nltk.word_tokenize(result)
    currentGram=' '.join(rWords[len(rWords)-n:len(rWords)])
    
print(result)