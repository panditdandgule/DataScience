#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 22:23:08 2019

@author: pandit
"""

import os
import nltk
import nltk.corpus

print(os.listdir(nltk.data.find("corpora")))

from nltk.corpus import brown
brown.words()

nltk.corpus.gutenberg.fileids()

hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
hamlet

for word in hamlet[:500]:
    print(word,sep=' ',end=' ')
    
type(AI)

from nltk.tokenize import word_tokenize

AI_tokens=word_tokenize(AI)

len(AI_tokens)

from nltk.tokenize import blankline_tokenize
AI_blank=blankline_tokenize(AI)
len(AI_blank)

from nltk.util import bigrams,trigrams,ngrams

string="The best and  most beautiful things in the world cannot be seen or even touched,  they must felt with the heart"
quotes_tokens=nltk.word_tokenize(string)
quotes_tokens

quotes_bigrams=list(nltk.bigrams(quotes_tokens))
quotes_bigrams

quotes_trigrams=list(nltk.trigrams(quotes_tokens))
quotes_trigrams

quotes_ngrams=list(nltk.ngrams(quotes_tokens,5))
quotes_ngrams

from nltk.stem import PorterStemmer
pst=PorterStemmer()
pst.stem("having")


words_to_stem=['give','giving','given','gave']
for words in words_to_stem:
    print(words+":"+pst.stem(words))
    
from nltk.stem import LancasterStemmer
lst=LancasterStemmer()
for words in words_to_stem:
    print(words+":"+lst.stem(words))
    
from  nltk.stem import SnowballStemmer
sbst=SnowballStemmer('english')

for words in words_to_stem:
    print(words+":"+sbst.stem(words))
    
from nltk.stem import wordnet
from nltk.stem import WordNetLemmatizer
word_len=WordNetLemmatizer()

word_len.lemmatize('corpora')