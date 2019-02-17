#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 09:15:02 2019

@author: pandit
"""

import numpy as np
import  re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import  load_files

reviews=load_files('/home/pandit/Downloads/NLP/Hands on Natural Language Processing/Text Classification/txt_sentoken')
X,y=reviews.data,reviews.target

#Pickling the dataset
with open('X.open','wb') as f:
    pickle.dump(X,f)
    
with open('y.open','wb') as f:
    pickle.dump(y,f)
    
#Unpickling dataset
X_in=open('X.pickle','rb')
y_in=open('y.pickle','rb')

X=pickle.load(X_in)
y=pickle.load(y_in)

#Creating the corpus
corpus=[]
for i in range(0,2000):
    review=re.sub(r'\W','',str(X[i]))
    review=review.lower()
    review=re.sub(r'^br$','',review)
    review=re.sub(r'\s+br\s+','',review)
    review=re.sub(r'\s+[a-z]\s+','',review)
    review=re.sub(r'\^b\s+','',review)
    review=re.sub(r'\s+','',review)
    corpus.append(review)
    
#Creating the BOW model
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
vectorizer=CountVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english'))
transformer=TfidfTransformer()
X=transformer.fit_transform(X).toarray()

# Creating the Tf-Idf model directly
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(max_features = 2000, min_df = 3, max_df = 0.6, stop_words = stopwords.words('english'))
X = vectorizer.fit_transform(corpus).toarray()

#Creating the Tf-Idf model directly
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer=TfidfVectorizer(max_features=2000,min_df=3,max_df=0.6,stop_words=stopwords.words('english'))
X=vectorizer.fit_transform(corpus).toarray()

from sklearn.model_selection import train_test_split
text_train,text_test,sent_train,sent_test=train_test_split(X,y,test_size=0.20,random_state=0)

#Training the classifier
from sklearn.linear_model import LogisticRegression
classifier=LogisticRegression()
classifier.fit(text_train,sent_train)

#Testing model performance
sent_pred=classifier.predict(text_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(sent_test,sent_pred)

#Saving our classifier
with open('classifier.pickle','wb') as f:
    pickle.dump(classifier,f)

with open('tfidfmodel.pickle','wb') as f:
    pickle.dump(vectorizer,f)