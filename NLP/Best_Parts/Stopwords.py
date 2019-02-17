#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 08:49:24 2019

@author: pandit
"""

import nltk
from nltk.corpus import stopwords



paragraph="""If a man wishes to become a great orator,he must first become a
            student of the great orators who have come before him. He must immerse
            himself in their texts, listening for the turns of phrases and textual
            symmetrics,  the pauses and crescendos, the metaphors and melodies that have
            enabled the greatest speeches to stand the test of time. There was 
            not currently a resource on the web to my liking that offered the man who 
            wished to study the greatest orations of all time-from ancient to modern-not
            only a list of the speeches but a link to the text and paragraph outlining the 
            context in which the speech was given."""
            
sentences=nltk.sent_tokenize(paragraph)

new_sentence=[]

#Removing stopwords
for i in range(len(sentences)):
    words=nltk.word_tokenize(sentences[i])
    words=[word for word in words if word not in stopwords.words('english')]
    new_sentence.append(' '.join(words))