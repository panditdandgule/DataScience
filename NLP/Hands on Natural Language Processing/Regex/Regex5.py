#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:34:38 2019

@author: pandit
"""

import re

X=["This is a wolf @scary",
   "Welcome to the jungle #missing",
   "111322 the number to know",
   "Remember the name s - John",
   "I  love you"]

for i in range(len(X)):
    X[i]=re.sub(r"\W"," ",X[i])
    X[i]=re.sub(r"\d"," ",X[i])
    X[i]=re.sub(r"\s+[a-z]\s+"," ",X[i],flags=re.I)
    X[i]=re.sub(r"\s+"," ",X[i])
    X[i]=re.sub(r"^\s","",X[i])
    X[i]=re.sub(r"\s$","",X[i])