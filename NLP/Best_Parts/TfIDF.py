#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 11:29:28 2019

@author: pandit
"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

paragraph="""If a man wishes to become a great orator,he must first become a
            student of the great orators who have come before him. He must immerse
            himself in their texts, listening for the turns of phrases and textual
            symmetrics,  the pauses and crescendos, the metaphors and melodies that have
            enabled the greatest speeches to stand the test of time. There was 
            not currently a resource on the web to my liking that offered the man who 
            wished to study the greatest orations of all time-from ancient to modern-not
            only a list of the speeches but a link to the text and paragraph outlining the 
            context in which the speech was given."""

sentence=nltk.sent_tokenize(paragraph)
lemmatizer=WordNetLemmatizer()

new_sentence=[]

#Removing stopwords
for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[lemmatizer.lemmatize(word) for word in words if word not in stopwords.words('english')]
    new_sentence.append(' '.join(words))
    
#Creating the Bag of words model
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features=20)
X=cv.fit_transform(new_sentence).toarray()

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf=TfidfVectorizer(max_features=20)
X1=tfidf.fit_transform(new_sentence).toarray()

