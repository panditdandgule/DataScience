#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 08:26:37 2019

@author: pandit
"""

import numpy as np
import re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')

#importing the datasets
reviews=load_files('/home/pandit/Downloads/NLP/Hands on Natural Language Processing/Text Classification/txt_sentoken')
X,y=reviews.data,reviews.target

#Pickling the dataset
with open('X.pickle','wb') as f:
    pickle.dump(X,f)

with open('y.pickle','wb') as f:
    pickle.dump(y,f)
    
#Unpickling dataset
X_in=open('X.pickle','rb')
y_in=open('y.pickle','rb')
X=pickle.load(X_in)
y=pickle.load(y_in)