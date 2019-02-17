#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 08:16:54 2019

@author: pandit
"""

#Bigrams,  Stemming and Lemmatizing

from nltk.corpus import reuters

reuters.readme().replace('\n',' ')

reuters.fileids()

reuters.fileids()[-1]

len(reuters.fileids())

reuters.categories()

reuters.sents('test/14826')

#Bigrams
trade_words=reuters.words(categories='trade')
len(trade_words)
trade_words

trade_words_condensed=trade_words[:100]
trade_words_condensed

from nltk.corpus import stopwords
trade_words_condensed=[w.lower() for w in trade_words_condensed if w.lower() not in stopwords.words('english')]

trade_words_condensed[:10]

import string

punct_combo=[c + "\"" for c in string.punctuation] + ["\"" + c for c in string.punctuation] + [".-", ":-", "..", "..."]
trade_words_condensed = [w for w in trade_words_condensed if w not in string.punctuation and w not in punct_combo]
trade_words_condensed

from nltk import bigrams
bi_trade_words_condensed=list(bigrams(trade_words_condensed))
bi_trade_words_condensed[:5]

from nltk import FreqDist
bi_fdist=FreqDist(bi_trade_words_condensed)

for word, frequency in bi_fdist.most_common(3):
    print(word,frequency)
    
bi_fdist.plot(3,cumulative=False)

#Stemming
from  nltk.stem import (PorterStemmer,LancasterStemmer)
from nltk.stem.snowball import SnowballStemmer

porter=PorterStemmer()
lancaster=LancasterStemmer()

snowball=SnowballStemmer("english")

print(porter.stem('Re-testing'),lancaster.stem('Re-testing'),snowball.stem('Re-testing'))

SnowballStemmer.languages


from nltk import word_tokenize
sentence="So, we'll go no more a-roving. So late into the night, Though the heart be still as loving, And the moon be still as bright."

translator=str.maketrans('','',string.punctuation)

translator

tokens=word_tokenize(sentence.translate(translator))
tokens[:3]

for stemmer in [porter, lancaster,snowball]:
    print([stemmer.stem(t) for t in tokens])
    
#Lemmatizing
from  nltk import WordNetLemmatizer

wnl=WordNetLemmatizer()

print(wnl.lemmatize('brightening'),wnl.lemmatize('boxes'))

wnl.lemmatize('brightening',pos='v')

text = "Truly Kryptic is the best puzzle game. It's browser-based and free. Google it."

from nltk import word_tokenize
text_tokenized=word_tokenize(text.lower())
text_tokenized

from nltk.corpus import words
words.readme().replace('\n',' ')

words

words.fileids()

words.words('en')[:10]

words.words('en-basic')[:10]

len(words.words('en'))

len(words.words('en-basic'))

#Finding unusal words
english_vocab = set(w.lower() for w in words.words())
text_vocab = set(w.lower() for w in text_tokenized if w.isalpha()) # Note .isalpha() removes punctuation tokens. However, tokens with a hyphen like 'browser-based' are totally skipped over because .isalpha() would be false.
unusual = text_vocab.difference(english_vocab)
unusual