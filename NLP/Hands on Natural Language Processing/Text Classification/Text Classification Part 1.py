#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 07:55:10 2019

@author: pandit
"""

import numpy as np
import  re
import pickle
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')

#Importing the dataset
reviews=load_files('/home/pandit/Downloads/NLP/Hands on Natural Language Processing/Text Classification/txt_sentoken')
X,y=reviews.data,reviews.target