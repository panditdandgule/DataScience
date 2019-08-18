#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 07:16:54 2019

@author: pandit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

orders=pd.read_table("http://bit.ly/chiporders")

orders.head()

pd.read_table("http://bit.ly/movieusers",sep='|',header=None)

user_cols=['user_id','age','gender','occupation','zip_code']

user_cols

users=pd.read_table("http://bit.ly/movieusers",sep='|',header=None,names=user_cols)

users.isnull().sum()

#+++++++++++++++++++====================++++++++++++++

ufo=pd.read_csv("http://bit.ly/uforeports")

ufo.head()

ufo['City']

ufo.City

ufo['Colors Reported']

ufo.shape

ufo.dtypes

ufo.columns

ufo.City + ufo.State

ufo['Location']=ufo.City + ufo.State

ufo.head()

ufo.columns

#+++++++++++++++++++++++++++++++
movies=pd.read_csv("http://bit.ly/imdbratings")

movies.head()

movies.describe(include=['object'])

movies.shape

movies.columns

type(movies)

#++++++++++++++++++++++++++++=====+++++++++++++++++++

ufo=pd.read_csv("http://bit.ly/uforeports")

ufo.head()

ufo.shape

ufo.size

ufo.dtypes

ufo.describe()

ufo.columns

ufo.rename(columns={'colors Reported':'colors_Reported',
                    'Shape Reported':'Shape_Reported'},inplace=True)

ufo.head()

ufo.columns

ufo_cols=['City','colors reported','shape reported','state','time']

ufo.columns=ufo_cols
ufo.head()

#+++++++++++++++++++++++++++++++=========================++++++++++++++++++++

ufo=pd.read_csv("http://bit.ly/uforeports")

ufo.head()

ufo.info()

ufo.shape

ufo.size

ufo.dtypes

ufo.drop('Colors Reported',axis=1,inplace=True)

ufo.head()

ufo.drop([0,1],axis=0,inplace=True)

ufo.head()

movies=pd.read_csv("http://bit.ly/imdbratings")

movies.head()

movies.shape

movies.size

movies.dtypes

movies['title']

movies.sort_values('duration',ascending=False)
movies.head()

movies.title.order()

movies.sort_values(['content_rating','duration'])

is_long=movies.duration>=200

is_long

movies[is_long]

movies[movies.duration>=200]

movies[movies.duration>=200]['genre']

movies.loc[movies.duration>=200,'genre']

movies.loc[movies.duration>=200, 'genre']

movies[movies.duration>=200]

movies[(movies.duration>=200) | (movies.genre=='Drama')]

movies[movies.genre.isin(['Crime','Drama','Action'])]

movies.head()

movies.dtypes

ufo=pd.read_csv("http://bit.ly/uforeports")

ufo.columns

ufo.City

ufo=pd.read_csv("http://bit.ly/uforeports",usecols=[0,4])

ufo.head()

for c in ufo.City:
    print(c)
    
drinks=pd.read_csv("http://bit.ly/drinksbycountry")

drinks.head()

drinks.shape

drinks.size

drinks.dtypes

drinks.select_dtypes(include=[np.number]).dtypes

drinks.describe()

drinks.describe(include='all')

drinks.describe(include=['object','float64'])


drinks.drop('continent',axis=1).head()

drinks.drop(2,axis=0).head()

drinks.mean()

drinks.mean(axis=1).shape

drinks.mean(axis=0)

drinks.head()

orders=pd.read_csv("http://bit.ly/chiporders")

orders.head()

drinks=pd.read_csv("http://bit.ly/drinksbycountry")

drinks.head()

drinks.beer_servings.mean()

drinks.groupby('continent').beer_servings.mean()

drinks.groupby('continent').beer_servings.mean()

drinks.groupby('continent').beer_servings.min()

drinks.groupby('continent').max()

drinks.groupby('continent').beer_servings.agg(['count','min','max','mean'])

drinks.groupby('continent').mean()

%matplotlib inline
drinks.groupby('continent').mean().plot(kind='hist')

movies=pd.read_csv("http://bit.ly/imdbratings")

movies.head()

movies.shape

movies.genre.unique()

movies.columns

movies.duration.describe()

movies.dtypes

movies.duration.describe(include=['object'])

movies.duration.mean()

movies.groupby('duration').mean().plot(kind='hist')

movies.columns

movies.groupby('content_rating').max().plot(kind='bar')

movies.groupby('genre').mean().plot(kind='bar')

movies.duration.value_counts().plot(kind='hist')

movies.duration.plot(kind='bar')

movies.genre.value_counts().plot(kind='bar')

ufo=pd.read_csv("http://bit.ly/uforeports")
ufo.head()

ufo.tail()

ufo.isnull().tail()

ufo.notnull().tail()

ufo[ufo.City.isnull()]

ufo.shape

ufo.dropna(how='any').shape

ufo.dropna(how='all').shape

ufo.dropna(how='any')

ufo.dropna(subset=['City','Shape Reported'],how='any')

ufo['Shape Reported'].value_counts()

ufo['City'].value_counts()

ufo['Shape Reported'].value_counts().plot(kind='bar')

ufo['Shape Reported'].fillna(value='VARIOUS')

ufo.VARIOUS


drinks=pd.read_csv("http://bit.ly/drinkscountry")

drinks.head()

drinks.index

drinks.index

drinks.columns

drinks.shape

drinks[drinks.continent=='South America']

drinks.loc[23,'beer_servings']

drinks.set_index('country')

drinks.head()

drinks.columns

drinks.loc['Brazil','beer_Servings']

drinks.index.name=None


drinks.head()

drinks.index.name='Country'

drinks.head()

drinks.head()

drinks.describe()

drinks.describe().loc['25%','beer_servings']


drinks.continent.head()

drinks.continent.head()

drinks.continent.value_counts().values

drinks.continent.value_counts()['Africa']

drinks.continent.value_counts().sort_index()


drinks.columns

drinks.country.value_counts()


ufo=pd.read_csv("http://bit.ly/uforeports")

ufo.head()

ufo.loc[0,:]

ufo.head()

ufo.loc[[0,1,2],:]

ufo.loc[0:2,:]

ufo.loc[:,['City','State']]

ufo.loc[0:2,'City':'State']


train=pd.read_csv("http://bit.ly/kaggletrain")

train.head()

train['Sex_male']=train.Sex.map({'female':0,'male':1})

train.head()

train.columns

train['Sex_female']=train.Sex.map({'female':1,'male':0})

train.columns

train.head()

pd.get_dummies(train.Sex)

pd.get_dummies(train.Sex).iloc[:,1:]

pd.get_dummies(train.Sex,prefix='Sex').iloc[:,1:]

train.Embarked.value_counts()

pd.get_dummies(train.Embarked,prefix='Embarked')

train.Embarked.value_counts()

pd.get_dummies(train.Embarked,prefix='Embarked')

train.head()

ufo=pd.read_csv("http://bit.ly/uforeports")

ufo.head()





