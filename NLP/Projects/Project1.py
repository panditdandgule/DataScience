#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  3 07:49:39 2019

@author: pandit
"""

import sys
import nltk
import sklearn
import pandas 
import numpy


print("Python :{}".format(sys.version))
print("NLTK:{}".format(nltk.__version__))
print("Scikit-learn:{}".format(sklearn.__version__))
print("Pandas:{}".format(pandas.__version__))
print("Numpy:{}".format(numpy.__version__))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Load the Dataset
df=pd.read_table('/home/pandit/Downloads/NLP/Projects/smsspamcollection/SMSSpamCollection',sep='\t',names=['label','body_text'],header=None,encoding='utf-8')

df

#Remove punctuation
import string
string.punctuation

#Function Remove punctuation
def remove_punct(text):
    text_nopunct="".join([char for char in text if char not in string.punctuation])
    return text_nopunct

df['body_text_clean']=df['body_text'].apply(lambda x:remove_punct(x))

df.head()

#Tokenization
import re

#Function to Tokenize words
def tokenize(text):
    tokens=re.split('\W+',text)
    return tokens

df['body_text_tokenized']=df['body_text_clean'].apply(lambda x: tokenize(x.lower()))

#we convert to Lower as Python is case-sensitive
df.head()

#Remove stopwords
import nltk
stopword=nltk.corpus.stopwords.words('english')

#Function to remove stopwords
def remove_stopwords(tokenized_list):
    text=[word for word in tokenized_list if word not in stopword]
    return text

df['body_text_nostop']=df['body_text_tokenized'].apply(lambda x:remove_stopwords(x))

df.head()

ps=nltk.PorterStemmer()

def stemming(tokenized_text):
    text=[ps.stem(word) for word in tokenized_text]
    return text

df['body_text_stemmed']=df['body_text_nostop'].apply(lambda x:stemming(x))

df.head()

wn=nltk.WordNetLemmatizer()

def lemmatizing(tokenized_text):
    text=[wn.lemmatize(word) for word in tokenized_text]
    return text

df['body_text_lemmatized']=df['body_text_nostop'].apply(lambda x:lemmatizing(x))
df.head(10)

#Apply CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
count_vect=CountVectorizer(analyzer=clean_text)
X_counts=count_vect.fit_transform(df['body_text'])
print(X_counts.shape)
print(count_vect.get_feature_names())

#N grams
from sklearn.feature_extraction.text import CountVectorizer
ngram_vect=CountVectorizer(ngram_range=(2,2),analyzer=clean_text)
X_counts=ngram_vect.fit_transform(df['body_text'])
print(X_counts.shape)
print(ngram_vect.get_feature_names())

#TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vect = TfidfVectorizer(analyzer=clean_text)
X_tfidf=tfidf_vect.fit_transform(df['body_text'])
print(X_tfidf.shape)
print(tfidf_vect.get_feature_names())

#Creat feature for text message length and % of punctuation in text

import string 
#Function to Caluculate Length of message excluding space
df['body_len']=df['body_text'].apply(lambda x:len(x)-x.count(" "))
df.head()

def count_punct(text):
    count=sum([1 for char in text if char in string.punctuation])
    return round(count/(len(text)-text.count(" ")),3)*100

df['punct%']=df['body_text'].apply(lambda x:count_punct(x))

df.head()

#check if features are good or not
bins=np.linspace(0,200,40)

plt.hist(df[df['label']=='spam']['body_len'],bins,alpha=0.5,normed=True,label='spam')
plt.hist(df[df['label']=='ham']['body_len'],bins,alpha=0.5,normed=True,label='ham')
plt.legend(loc='upper left')
plt.show()

bins=np.linspace(0,50,40)

plt.hist(df[df['label']=='spam']['punct%'],bins,alpha=0.5,normed=True,label='spam')
plt.hist(df[df['label']=='ham']['body_len'],bins,alpha=0.5,normed=True,label='ham')
plt.legend(loc='upper right')
plt.show()

#CountVectorizer
from sklearn.ensemble import  RandomForestClassifier
from sklearn.grid_search import GridSearchCV
rf=RandomForestClassifier()
param={'n_estimators':[10,150,300],
       'max_depth':[30,60,90,None]}

gs=GridSearchCV(rf,param,cv=5,n_jobs=-1)
gs_fit=gs.fit(X_count_feat,df['label'])
pd.DataFrame(gs_fit.cv_results_).sort_values('mean_test_score',ascending=False).head()

