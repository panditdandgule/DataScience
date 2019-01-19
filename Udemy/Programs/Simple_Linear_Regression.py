import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset
dataset=pd.read_csv('/home/pandit/Downloads/Udemy/Simple_Linear_Regression/Salary.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,3].values

#splitting the dataset into the training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=0)

