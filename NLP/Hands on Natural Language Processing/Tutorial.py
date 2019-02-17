#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 07:11:52 2019

@author: pandit
"""

import nltk
import numpy as np
import matplotlib.pyplot as plt
import tweepy
import TwitterSearch
import unidecode
import langdetect
import langid
import gensim

from nltk.tokenize import word_tokenize
from nltk.text import Text



my_string = "Two plus two is four, minus one that's three — quick maths. Every day man's on the block. Smoke trees. See your girl in the park, that girl is an uckers. When the thing went quack quack quack, your men were ducking! Hold tight Asznee, my brother. He's got a pumpy. Hold tight my man, my guy. He's got a frisbee. I trap, trap, trap on the phone. Moving that cornflakes, rice crispies. Hold tight my girl Whitney."

tokens=word_tokenize(my_string)

tokens=[word.lower() for word in tokens]
tokens[:5]

t=Text(tokens)
t

t.collocations()

t.count('quack')

t.index('two')

t.similar('brother')

t.dispersion_plot(['man','thing','quack'])

t.plot

t.vocab()

from nltk.corpus import reuters
text=Text(reuters.words())

text.common_contexts(['August','June'])

#Tokenization
s="Le temps est un grand maitre, dit-on, le malheur est qu'il tue ses element"
s=s.lower()

from nltk.tokenize import RegexpTokenizer
tokenizer=RegexpTokenizer("[a-zA-Z'`eei]+")
s_tokenized=tokenizer.tokenize(s)
s_tokenized

from nltk.util import ngrams
generated_4grams=[]

for word in s_tokenized:
    generated_4grams.append(list(ngrams(word,4,pad_left=True,pad_right=True,left_pad_symbol='_',right_pad_symbol='_')))
    
generated_4grams

generated_4grams=[word for sublist in generated_4grams for word in sublist]
generated_4grams[:10]

#Obtaining n-grams(n=4)
ng_list_4grams=generated_4grams
for idx,val in enumerate(generated_4grams):
    ng_list_4grams[idx]=''.join(val)
    
ng_list_4grams

#Sorting n-grams by frequency (n = 4)
freq_4grams={}
for ngram in ng_list_4grams:
    if ngram not in freq_4grams:
        freq_4grams.update({ngram:1})
    else:
        ngram_occurrences=freq_4grams[ngram]
        freq_4grams.update({ngram:ngram_occurrences+1})
        
from operator import itemgetter
freq_4grams_sorted = sorted(freq_4grams.items(), key=itemgetter(1), reverse=True)[0:300] # We only keep the 300 most popular n-grams. This was suggested in the original paper written about n-grams.
freq_4grams_sorted

from nltk import everygrams
s_clean=' '.join(s_tokenized)
s_clean

def ngram_extractor(sent):
    return[''.join(ng) for ng in everygrams(sent.replace(' ','_ _'),1,4) if ' ' not in ng and '\n' not in ng and ng !=('_',)]
    
ngram_extractor(s_clean)

#Tokenizing
text="Yo man,its time for you to shut yo' mouth! I ain't even messing' dwag"

import sys

try:
    from nltk.tokenize import wordpunct_tokenize
    
except:
    print('[!] You need to install nltk')
    
test_tokens=wordpunct_tokenize(text)
test_tokens

from nltk.corpus import stopwords
stopwords.readme().replace('\n',' ')

stopwords.fileids()

stopwords.raw('greek')

stopwords.raw('greek').replace('\n',' ')

stopwords.words('english')[:10]

stopwords.sents('greek')

len(stopwords.words(['english','greek']))

##The classification
language_ratios={}
test_words=[word.lower() for word in test_tokens]
test_words_set=set(test_words)

for language in stopwords.fileids():
    stopwords_set=set(stopwords.words(language))
    
    common_elements=test_words_set.intersection(stopwords_set)
    language_ratios[language]=len(common_elements)
    
language_ratios

most_rated_language=max(language_ratios,key=language_ratios.get)
most_rated_language

test_words_set.intersection(set(stopwords.words(most_rated_language)))

