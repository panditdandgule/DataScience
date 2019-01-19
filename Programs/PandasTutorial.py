#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 14:38:30 2019

@author: pandit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.DataFrame({'Country':['Russia','Austrolia','Columbia','Nigeria','US','UK'],'Rank':[101,111,112,115,118,120]})

data

data.describe()

data.head()

data.tail()

data.info()

data1=pd.DataFrame({'group':['a','a','a','b','b','b','c','c','c'],'ounces':[4,3,12,6,7,5,8,3,5]})

data1

data1.sort_values(by=['ounces'],ascending=True,inplace=False)

data1.sort_values(by=['group','ounces'],ascending=[True,False],inplace=False)

data2=pd.DataFrame({'K1':['One']*3+['two']*4,'K2':[3,2,1,3,3,4,4]})

data2

data2.sort_values(by='K2')

data2.drop_duplicates()

data2.drop_duplicates(subset='K1')

data3=pd.DataFrame({'Food':['bacon','pulled pork','bacon','pastrmi'],'ounces':[4,3,1,6]})

data3

meat_to_animal={
        'bacon':'pig',
        'pulled pork':'pig',
        'pastrami':'cow'}
def meat_2_animal(series):
    if series['Food']=='bacon':
        return 'pig'
    elif series['Food']=='pulled pork':
        return 'pig'
    elif series['Food']=='pastrami':
        return 'cow'
    else:
        return 'pig'

data3['animal']=data3['Food'].map(str.lower).map(meat_to_animal)

data3

lower=lambda x:x.lower()

data3['Food']=data['Food'].apply(lower)

data3['animal2']=data3.apply(meat_2_animal,axis='columns')

data3

data3.rename(index=str.upper,inplace=True)

df=pd.DataFrame({"a":[4,5,6],
                 "b":[7,8,9],
                 "c":[10,11,12]},index=[1,2,3])
    
df
