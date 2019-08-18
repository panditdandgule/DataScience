#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 17:32:03 2019

@author: pandit
"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import make_scorer
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
from pandas import get_dummies
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib
import warnings
import sklearn
import scipy
import numpy
import json
import sys
import csv
import os

#setup
sns.set(style='white', context='notebook', palette='deep')
pylab.rcParams['figure.figsize'] = 12,8
warnings.filterwarnings('ignore')
mpl.style.use('ggplot')
sns.set_style('white')

#import train and test to play with it
df_train=pd.read_csv('/home/pandit/Downloads/Kaggle/all/train.csv')
df_test=pd.read_csv('/home/pandit/Downloads/Kaggle/all/test.csv')

df_train
df_test

df_train.isnull().sum()
df_test.isnull().sum()

df_train.describe()
df_test.describe()

df_train.head()
df_test.head()

type(df_train)
type(df_test)

total=df_train.isnull().sum().sort_values(ascending=False)
print(total)
percent_1=df_train.isnull().sum()/df_train.isnull().count()*100
print(percent_1)
percent_2=(round(percent_1,1)).sort_values(ascending=False)
print(percent_2)
missing_data=pd.concat([total,percent_2],axis=1,keys=['Total','%'])
missing_data.head(5)



#Scatter plot purpose is to identify the relationship between two quantitative variable
# Modify the graph above by assigning each species an individual color.
g=sns.FacetGrid(data=df_train,hue="Survived",col="Pclass",margin_titles=True,
                palette={1:"seagreen",0:"grey"})
g=g.map(plt.scatter,"Fare","Age",edgecolor="w").add_legend();

ax=sns.boxplot(x="Pclass",y="Age",data=df_train)
ax=sns.stripplot(x="Pclass",y="Age",data=df_train,jitter=True,edgecolor='gray')
plt.show()

df_train.hist(figsize=(15,20))
plt.figure()

df_train["Age"].hist();

f,ax=plt.subplots(1,2,figsize=(10,5))
df_train[df_train['Survived']==0].Age.plot.hist(ax=ax[0],bins=20,
        edgecolor='black',color='red')
ax[0].set_title('Survived=0')
x1=list(range(0,85,5))
ax[0].set_xticks(x1)
df_train[df_train['Survived']==1].Age.plot.hist(ax=ax[1],color='green',
        bins=20,edgecolor='black')
ax[1].set_title('Survived=1')
x2=list(range(0,85,5))
ax[1].set_xticks(x2)
plt.show()

f,ax=plt.subplots(1,2,figsize=(9,2))
df_train['Survived'].value_counts().plot.pie(explode=[0,0.1],
        autopct='%1.1f%%',ax=ax[0],shadow=True)
ax[0].set_title('Survived')
ax[0].set_ylabel('')
sns.countplot('Survived',data=df_train,ax=ax[1])
ax[1].set_title('Survived')
plt.show()

# scatter plot matrix
pd.plotting.scatter_matrix(df_train,figsize=(10,10))
plt.figure()

# violinplots on petal-length for each species
sns.violinplot(data=df_train,x='Sex',y='Age')

f,ax=plt.subplots(1,2,figsize=(18,8))
sns.violinplot("Pclass","Age",hue="Survived",data=df_train,
               split=True,ax=ax[0])
ax[0].set_title('Pclass and Age vs Survived')
ax[0].set_yticks(range(0,110,10))
sns.violinplot("Sex","Age",hue="Survived",data=df_train)
ax[1].set_title('Sex and Age vs Survived')
ax[1].set_yticks(range(0,110,10))
plt.show()

# Using seaborn pairplot to see the bivariate relation between each pair of features
sns.pairplot(df_train,hue='Sex')

# seaborn's kdeplot, plots univariate or bivariate density estimates.
#Size can be changed by tweeking the value used
sns.FacetGrid(df_train,hue='Survived',size=5).map(sns.kdeplot,'Fare').add_legend()
plt.show()

sns.jointplot(x='Fare',y='Age',data=df_train)

sns.jointplot(x='Fare',y='Age',data=df_train,kind='reg')

sns.swarmplot(x='Pclass',y='Age',data=df_train)

plt.figure(figsize=(7,4)) 
sns.heatmap(df_train.corr(),annot=True,cmap='cubehelix_r') #draws  heatmap with input as the correlation matrix calculted by(iris.corr())
plt.show()

df_train['Pclass'].value_counts().plot(kind='bar')

sns.factorplot('Pclass','Survived',hue='Survived',data=df_train)
plt.show()



f,ax=plt.subplots(1,3,figsize=(20,8))
sns.distplot(df_train[df_train['Pclass']==1].Fare,ax=ax[0])
ax[0].set_title('Fares in Pclass 1')
sns.distplot(df_train[df_train['Pclass']==2].Fare,ax=ax[1])
ax[1].set_title('Fares in Pclass 2')
sns.distplot(df_train[df_train['Pclass']==3].Fare,ax=ax[2])
ax[2].set_title('Fares in Pclass 3')
plt.show()

df_train.info()

df_train.size

df_train.shape

df_train.head()

df_train.isnull().sum()

df_train['Pclass'].value_counts()

df_train.head(5)

df_train.sample(5)

df_train.describe()

df_train.isnull().sum()

df_train.groupby('Pclass').count()

df_train.columns

df_train.where(df_train['Age']==30).head(2)

df_train[df_train['Age']<7.2].head(2)

# Seperating the data into dependent and independent variables
X=df_train.iloc[:,:-1].values
y=df_train.iloc[:,-1].values

def simplify_ages(df):
    df.Age = df.Age.fillna(-0.5)
    bins = (-1, 0, 5, 12, 18, 25, 35, 60, 120)
    group_names = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']
    categories = pd.cut(df.Age, bins, labels=group_names)
    df.Age = categories
    return df

def simplify_cabins(df):
    df.Cabin = df.Cabin.fillna('N')
    df.Cabin = df.Cabin.apply(lambda x: x[0])
    return df

def simplify_fares(df):
    df.Fare = df.Fare.fillna(-0.5)
    bins = (-1, 0, 8, 15, 31, 1000)
    group_names = ['Unknown', '1_quartile', '2_quartile', '3_quartile', '4_quartile']
    categories = pd.cut(df.Fare, bins, labels=group_names)
    df.Fare = categories
    return df

def format_name(df):
    df['Lname'] = df.Name.apply(lambda x: x.split(' ')[0])
    df['NamePrefix'] = df.Name.apply(lambda x: x.split(' ')[1])
    return df    
    
def drop_features(df):
    return df.drop(['Ticket', 'Name', 'Embarked'], axis=1)

def transform_features(df):
    df = simplify_ages(df)
    df = simplify_cabins(df)
    df = simplify_fares(df)
    df = format_name(df)
    df = drop_features(df)
    return df

df_train = transform_features(df_train)
df_test = transform_features(df_test)
df_train.head()

def cleanticket(ticket):
    ticket = ticket.replace('.', '')
    ticket = ticket.replace('/', '')
    ticket = ticket.split()
    ticket = map(lambda t : t.strip(), ticket)
    ticket = list(filter(lambda t : not t.isdigit(), ticket))
    if len(ticket) > 0:
        return ticket[0]
    else: 
        return 'XXX'
    
def encode_features(df_train, df_test):
    features = ['Fare', 'Cabin', 'Age', 'Sex', 'Lname', 'NamePrefix']
    df_combined = pd.concat([df_train[features], df_test[features]])
    
    for feature in features:
        le = preprocessing.LabelEncoder()
        le = le.fit(df_combined[feature])
        df_train[feature] = le.transform(df_train[feature])
        df_test[feature] = le.transform(df_test[feature])
    return df_train, df_test

df_train, df_test = encode_features(df_train, df_test)
df_train.head()

x_all = df_train.drop(['Survived', 'PassengerId'], axis=1)
y_all = df_train['Survived']

num_test = 0.3
X_train, X_test, y_train, y_test = train_test_split(x_all, y_all, test_size=num_test, random_state=100)

# Choose the type of classifier. 
rfc = RandomForestClassifier()

# Choose some parameter combinations to try
parameters = {'n_estimators': [4, 6, 9], 
              'max_features': ['log2', 'sqrt','auto'], 
              'criterion': ['entropy', 'gini'],
              'max_depth': [2, 3, 5, 10], 
              'min_samples_split': [2, 3, 5],
              'min_samples_leaf': [1,5,8]
             }

# Type of scoring used to compare parameter combinations
acc_scorer = make_scorer(accuracy_score)

# Run the grid search
grid_obj = GridSearchCV(rfc, parameters, scoring=acc_scorer)
grid_obj = grid_obj.fit(X_train, y_train)

# Set the clf to the best combination of parameters
rfc = grid_obj.best_estimator_

# Fit the best algorithm to the data. 
rfc.fit(X_train, y_train)

#Prediction
rfc_prediction = rfc.predict(X_test)
rfc_score=accuracy_score(y_test, rfc_prediction)
print(rfc_score)



xgboost = xgb.XGBClassifier(max_depth=3, n_estimators=300, learning_rate=0.05).fit(X_train, y_train)

xgb_prediction = xgboost.predict(X_test)
xgb_score=accuracy_score(y_test, xgb_prediction)
print(xgb_score)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)


logreg_prediction = logreg.predict(X_test)
logreg_score=accuracy_score(y_test, logreg_prediction)
print(logreg_score)


from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
dt = DecisionTreeRegressor(random_state=1)

# Fit model
dt.fit(X_train, y_train)
dt_prediction = dt.predict(X_test)
dt_score=accuracy_score(y_test, dt_prediction)
print(dt_score)

from sklearn.linear_model import HuberRegressor

# Fit model
huber.fit(X_train, y_train)
huber_prediction = huber.predict(X_test)
huber_score=accuracy_score(y_test, dt_prediction)
print(huber_score)
