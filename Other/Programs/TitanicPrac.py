#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 07:16:54 2019

@author: pandit
"""

import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report
from sklearn import preprocessing
import matplotlib.pylab as pylab
import matplotlib as mpl
import warnings

#Setup
sns.set(style='white',context='notebook',palette='deep')
pylab.rcParams['figure.figsize']=12,8
warnings.filterwarnings('ignore')
mpl.style.use('ggplot')
sns.set_style('white')

#import train and test to play with it
df_train=pd.read_csv('/home/pandit/Downloads/Kaggle/all/train.csv')
df_test=pd.read_csv('/home/pandit/Downloads/Kaggle/all/test.csv')

g=sns.FacetGrid(data=df_train,hue='Survived',col='Pclass',margin_titles=True,
                palette={1:'seagreen',0:'grey'})
g=g.map(plt.scatter,'Fare','Age',edgecolor='w').add_legend();

ax=sns.boxplot(x='Pclass',y='Age',data=df_train)
ax=sns.stripplot(x='Pclass',y='Age',data=df_train,jitter=True,edgecolor='gray')
plt.show()

#histogram
df_train.hist(figsize=(15,20))
plt.figure()

df_train['Age'].hist()

f,ax=plt.subplots(1,2,figsize=(15,20))
df_train[df_train['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,edgecolor='black',
        color='red')
ax[0].set_title('Survived=0')
x1=list(range(0,85,5))
ax[0].set_xtricks(x1)
f,ax=plt.subplots(1,2,figsize=(15,20))
df_train[df_train['Survived']==1].Age.plot.hist(ax=ax[1],bins=20,edgecolor='blue',
        color='green')
ax[1].set_title('Survived=1')
x2=list(range(0,85,5))
ax[1].set_xtricks(x2)
plt.show()

#Pie chart
f,ax=plt.subplots(1,2,figsize=(18,8))
df_train['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',
        ax=ax[0],shadow=True)
ax[0].set_title('Survived')
ax[0].setylabel('')
sns.countplot('Survived',data=df_train,ax=ax[1])
ax[1].set_title('Survived')
plt.show()

# scatter plot matrix
pd.plotting.scatter_matrix(df_train,figsize=(10,10))
plt.show()

#violionplots
sns.violinplot(data=df_train,x='Sex',y='Age')

# Using seaborn pairplot to see the bivariate relation between each pair of features
sns.pairplot(df_train, hue="Sex")

# Seperating the data into dependent and independent variables
X=df_train.iloc[:,:-1]
y=df_train.iloc[:,-1]

df_train.columns