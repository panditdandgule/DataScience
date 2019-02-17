#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 08:16:00 2018

@author: pandit
"""

import nltk
import  random
from nltk.corpus import  movie_reviews
import pickle
from sklearn.naive_bayes import  MultinomialNB,GaussianNB,BernoulliNB

documents=[(list(movie_reviews.words(fileid)),category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]

#documents=[]

#for category in movie_reviews.categories():
#    for fileid in movie_reviews.fileids(category):
#        documents.append(list(movie_reviews.words(fileid)),category)

random.shuffle(documents)

#print(documents[1])

all_words=[]
for w in movie_reviews.words():
    all_words.append(w.lower())
    
all_words=nltk.FreqDist(all_words)
#print(all_words.most_common(15))

#print(all_words("stupid"))

word_features=list(all_words.keys())[:3000]

def find_features(document):
    words=set(document)
    features={}
    for w in word_features:
        features[w]=(w in words)
        
    return features

print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets=[(find_features(rev),category) for (rev,category) in documents]

training_set=featuresets[:1900]
testing_set=featuresets[1900:]

#posterior=prior


#classifier=nltk.NaiveBayesClassifier.train(training_set)

classifier_f=open("naivebayes.pickle","rb")
classifier=pickle.load(classifier_f)
classifier_f.close()

print("Naive Bayes Algo accuracy:",(nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)
      
#save_classifier=open("naivebayes.pickle","wb")
#pickle.dump(classifier,save_classifier)
#save_classifier.close()

MNB_classifier=SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:",(nltk.classify.accuracy(MNB_classifier,testing_set))*100)

GaussianNB_classifier=SklearnClassifier(GaussianNB())
GaussianNB_classifier.train(training_set)
print("GaussianNB_classifier accuracy percent:",(nltk.classify.accuracy(GaussianNB_classifier,testing_set))*100)
