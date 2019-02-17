#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 08:00:59 2019

@author: pandit
"""

import nltk

def format_sentence(sent):
    return({word:True for  word in nltk.word_tokenize(sent)})
  
path='/home/pandit/Downloads/NLP/code1/data/pos_tweets.txt'
pos=[]
with open(path) as f:
    for i in f:
        pos.append([format_sentence(i),'pos'])

print(pos)

neg=[]
with open(path) as f:
    for i in f:
        neg.append([format_sentence(i),'neg'])

print(neg)

training = pos[:int((.9)*len(pos))] + neg[:int((.9)*len(neg))]

test = pos[int((.1)*len(pos)):] + neg[int((.1)*len(neg)):]

from nltk.classify import NaiveBayesClassifier
classifier=NaiveBayesClassifier.train(training)

classifier.show_most_informative_features()

example1="this workshop is awesome."
print(classifier.classify(format_sentence(example1)))

example2="this workshop is awful"
print(classifier.classify(format_sentence(example2)))

from nltk.classify.util import accuracy
print(accuracy(classifier,test))

import re
re1=re.compile('python')
print(bool(re1.match('Python')))

import nltk
text=nltk.word_tokenize("Python is an awesome language!")
nltk.pos_tag(text)

nltk.help.upenn_tagset('JJ')

from nltk.corpus import brown

brown_tagged_sents=brown.tagged_sents(categories='news')
brown_sets=brown.sents(categories='news')
unigram_tagger=nltk.UnigramTagger(brown_tagged_sents)
unigram_tagger.tag(brown_sents[2007])