#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 07:19:17 2019

@author: pandit

Prog : iris Dataset
A machine learning project may not be linear, but it has a number of well known steps:

    Define Problem.
    Prepare Data.
    Evaluate Algorithms.
    Improve Results.
    Present Results.
Here is an overview of what we are going to cover:

    Installing the Python and SciPy platform.
    Loading the dataset.
    Summarizing the dataset.
    Visualizing the dataset.
    Evaluating some algorithms.
    Making some predictions.

"""
# Python version

import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

#Import Libraries
from pandas.plotting import scatter_matrix
import pandas
import matplotlib.pylab as pylab
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# Load dataset
url = "/home/pandit/Downloads/AnalyticsVidhya/iris.csv"
names=['sepal-length','sepal-width','petal-length','petal-width','class']
dataset=pandas.read_csv(url,names=names)

#shape
print(dataset.shape)

#head
print(dataset.head(20))

#descriptions
print(dataset.describe())

#class distribution
print(dataset.groupby('class').size())

'''
Data Visualization

We now have a basic idea about the data. We need to extend that with some visualizations.

We are going to look at two types of plots:

    Univariate plots to better understand each attribute.
    Multivariate plots to better understand the relationships between attributes.
'''
#box and whisker plots
dataset.plot(kind='box',subplots=True,layout=(2,2),sharex=False,sharey=False)
plt.show()

#histograms
dataset.hist()
plt.show()

#scatter plot matrix
scatter_matrix(dataset)
plt.show()

#Split out validation dataset
array=dataset.values
X=array[:,0:4]
Y=array[:,4]
validation_size=0.2
seed=7
X_train,X_test,y_train,y_test=model_selection.train_test_split(X,Y,test_size=validation_size,random_state=0)

'''
Test Harness

We will use 10-fold cross validation to estimate accuracy.

This will split our dataset into 10 parts, train on 9 and test on 1 and repeat for all combinations of train-test splits.'''

#test options and evaluation metric
seed=7
scoring='accuracy'

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))
# evaluate each model in turn
results = []
names = []
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)



# Compare Algorithms
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()

	
# Make predictions on validation dataset
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
print(accuracy_score(X_test, predictions))
print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))