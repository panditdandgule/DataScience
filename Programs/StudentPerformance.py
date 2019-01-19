#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 17:32:58 2019

@author: pandit
"""

import numpy as np
import pandas  as pd
import seaborn as sns
import matplotlib.pyplot as plt

passmark=40

df=pd.read_csv('/home/pandit/Downloads/Kaggle/students-performance-in-exams/StudentsPerformance.csv')

df.head()

print(df.shape)
df.describe()

#Let us check for any missing values
df.isnull().sum()

p=sns.countplot(x='math score',data=df,palette='muted')
_=plt.setp(p.get_xticklabels(),rotation=90)

#How many students pass in math exams
df['Math_PassStatus']=np.where(df['math score']<passmark,'F','P')
df.Math_PassStatus.value_counts()

p=sns.countplot(x='parental level of education',data=df,hue='Math_PassStatus',palette='bright')
_=plt.setp(p.get_xticklabels(),rotation=90)

sns.countplot(x="reading score",data=df,palette="muted")
plt.show()

#How many students passed in reading?
df['Reading_PassStatus']=np.where(df['reading score']<passmark,'F','P')
df.Reading_PassStatus.value_counts()

p=sns.countplot(x='parental level of education',data=df,hue='Reading_PassStatus',palette='bright')
_=plt.setp(p.get_xticklabels(),rotation=90)

#Let us explore writing score
p=sns.countplot(x='writing score',data=df,palette="muted")
_=plt.setp(p.get_xticklabels(),rotation=90)

#How many students passed writing?
df['Writing_PassStatus']=np.where(df['writing score']<passmark,'F','P')
df.Writing_PassStatus.value_counts()

p=sns.countplot(x='parental level of education',data=df,hue='Writing_PassStatus',palette='bright')
_=plt.setp(p.get_xticklabels(),rotation=90)

#Let us check how many students passed in all the subjects
df["OverAll_PassStatus"]=df.apply(lambda x : 'F' if x['Math_PassStatus']=='F' or x['Reading_PassStatus']=='F' or x['Writing_PassStatus']=='F' else 'P',axis=1)
df.OverAll_PassStatus.value_counts()

p=sns.countplot(x='parental level of education',data=df,hue='OverAll_PassStatus',palette='bright')
_=plt.setp(p.get_xticklabels(),rotation=90)

#Find the percentage of marks
df['Total_Marks']=df['math score']+df['reading score']+df['writing score']
df['Percentage']=df['Total_Marks']/3

p=sns.countplot(x="Percentage",data=df,palette="muted")
_=plt.setp(p.get_xticklabels(),rotation=0)

def GetGrade(Percentage, OverAll_PassStatus):
    if ( OverAll_PassStatus == 'F'):
        return 'F'    
    if ( Percentage >= 80 ):
        return 'A'
    if ( Percentage >= 70):
        return 'B'
    if ( Percentage >= 60):
        return 'C'
    if ( Percentage >= 50):
        return 'D'
    if ( Percentage >= 40):
        return 'E'
    else: 
        return 'F'

df['Grade'] = df.apply(lambda x : GetGrade(x['Percentage'], x['OverAll_PassStatus']), axis=1)

df.Grade.value_counts()

sns.countplot(x="Grade", data = df, order=['A','B','C','D','E','F'],  palette="muted")
plt.show()



p = sns.countplot(x='parental level of education', data = df, hue='Grade', palette='bright')
_ = plt.setp(p.get_xticklabels(), rotation=90) 


