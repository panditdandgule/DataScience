#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 06:50:35 2019

@author: pandit
"""
#Corpus :Body of text singular. Corpora is the plural of this
#Lexicon : Words of their meanings
#Token : Each entity that is a part of whatever was split up based on this rule

import nltk
import sys
import sklearn

print("python:{}".format(sys.version))
print("sklearn:{}".format(sys.version))

from nltk.tokenize import word_tokenize,sent_tokenize

text="Hello students, how are you doing today? The olympics are inapiring and python is awesome"

print(sent_tokenize(text))

print(word_tokenize(text))

#Moving stopwords which is useless data

from nltk.corpus import stopwords
print(set(stopwords.words('english')))

example="This is some  sample text, showing off the stop words"

stop_words=set(stopwords.words('english'))

word_tokens=word_tokenize(example)

filtered_sentence=[w for w in word_tokens if not w in stop_words]

filtered_sentence

'''
filtered_sentence=[]
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
'''

print(word_tokens)
print(filtered_sentence)

#Stemming words with NLTK
from nltk.stem import PorterStemmer

ps=PorterStemmer()

example_words=['ride','riding','rider','riders']

for w in example_words:
    print(ps.stem(w))
    
#Stemming an entire sentence
new_text="When riders are riding their horses, they often think  of how coboys rode horses."

words=word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
    
#Parts of speech
nltk.download()
from nltk.corpus import udhr
print(udhr.raw('English-Latinl'))

from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
train_text=state_union.raw('2005-GWBush.txt')
sample_text=state_union.raw('2006-GWBush.txt')

print(train_text)

#Now that we have some text

custom_sent_tokenizer=PunktSentenceTokenizer(train_text)

#Now lets tokenize sample text
tokenized=custom_sent_tokenizer.tokenize(sample_text)

print(tokenized)

#Define a function that will tag each tokenized word with a pos

def process_content():
    try:
        for i in tokenized[:5]:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
    except Exception as e:
        print(str(e))
        
process_content()

nltk.download()

#chunking :group of clusters
train_text=state_union.raw('2005-GWBush.txt')
sample_text=state_union.raw('2006-GWBush.txt')

custom_sent_tokenizer=PunktSentenceTokenizer(train_text)
tokenized=custom_sent_tokenizer.tokenize(sample_text)

def process_content():
    try:
        for i in tokenized:
            words=nltk.word_tokenize(i)
            tagged=nltk.pos_tag(words)
            
            #combine the pos with regex
           
    except Exception as e:
        print(str(e))
        
process_content()
