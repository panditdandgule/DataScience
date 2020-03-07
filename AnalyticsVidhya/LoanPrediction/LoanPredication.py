#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 16:22:20 2019

@author: pandit
Proj :LoanPredication
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

train_data_df=pd.read_csv('/home/pandit/Downloads/AnalyticsVidhya/LoanPrediction/train.csv')
test_data_df=pd.read_csv("/home/pandit/Downloads/AnalyticsVidhya/LoanPrediction/test.csv")

train_data_df.columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area','Loan_Status']
test_data_df.columns = ['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']

train_data_df.columns
test_data_df.head()

#Get summery of numerical variable
train_data_df.describe()
test_data_df.describe()

train_data_df['ApplicantIncome'].hist(bins=50)

train_data_df.boxplot(column='ApplicantIncome')

train_data_df.boxplot(column='ApplicantIncome',by='Education')

train_data_df['LoanAmount'].hist(bins=50)

train_data_df.boxplot(column='LoanAmount')

import matplotlib.pyplot as plt
fig=plt.figure(figsize=(8,4))
ax1=fig.add_subplot(121)
ax1.set_xlabel('Credit_History')
ax1.set_ylabel('Count of Applications')
ax1.set_title('Applicants by Credit_History')
temp1.plot(kind='bar')

ax2=fig.add_subplot(122)
temp2.plot(kind='bar')
ax2.set_xlabel('Credit_History')
ax2.set_ylabel('Probability of getting loan')
ax2.set_title('Probability of getting loan by credit history')

train_data_df.apply(lambda x: sum(x.isnull()),axis=0)

train_data_df['LoanAmount'].fillna(train_data_df['LoanAmount'].mean(),inplace=True)

train_data_df['LoanAmount']

train_data_df['Self_Employed'].value_counts()

train_data_df['TotalIncome']=train_data_df['ApplicantIncome']+train_data_df['CoapplicantIncome']

train_data_df['TotalIncome']

train_data_df['TotalIncome_log']=np.log(train_data_df['TotalIncome'])

train_data_df

train_data_df['TotalIncome_log'].hist(bins=20)

train_data_df['Gender'].fillna(train_data_df['Gender']mode()[0],inplace=True)
train_data_df['Married'].fillna(train_data_df['Married'].mode()[0],inplace=True)
train_data_df['Dependents'].fillna(train_data_df['Dependents'].mode()[0],inplace=True)
df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0], inplace=True)
df['Credit_History'].fillna(df['Credit_History'].mode()[0], inplace=True)

from sklearn.preprocessing import LabelEncoder
var_mod=['Gender','Married','Dependents','Education','Self_Employee','Property_Area','Loan_Status']
le=LabelEncoder()
for i in var_mod:
    train_data_df[i]=le.fit_transform(train_data_df[i])

train_data_df.dtypes


