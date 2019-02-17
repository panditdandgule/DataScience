#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 16:49:27 2019

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
df=pd.read_table('/home/pandit/Downloads/NLP/Projects/smsspamcollection/SMSSpamCollection',header=None,encoding='utf-8')

df

df.info()
df.head()
df.tail()
df.shape
df.describe()
df.hist()

#class distribution
classes=df[0]

classes.value_counts()

#Preprocess the Data
from sklearn.preprocessing import LabelEncoder
encoder=LabelEncoder()
Y=encoder.fit_transform(classes)
print(Y[:10])

#store the SMS message data
text_messages=df[1]
print(text_messages[:10])

#Use Regular Expression


