#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:11:33 2019

@author: pandit
"""

import pandas as pd

s=pd.Series([1,3,5,np.nan,6,8])

s

dates=pd.date_range('20180101',periods=10)

dates

df=pd.DataFrame(np.random.random((6,4)))

df

df.head()

df.tail()

df.describe()

df.T

df.sort_index(axis=1,ascending=False)

df[0:3]

df.loc[dates[0]]

df.iloc[dates[0]]

df.iloc[3]

df.iloc[3:5,0:2]

df.dropna(how='any')

df
df.fillna(value=5)

pd.isna(df)