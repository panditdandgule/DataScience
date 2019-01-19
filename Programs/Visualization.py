#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  5 15:35:18 2019

@author: pandit
"""

import pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt
import seaborn as sns

tips=sns.load_dataset("tips")

g=sns.lmplot(x='tip',
             y='total_bill',
             data=tips,aspect=2)

g=(g.set_axis_labels("Tip","Total bill(USD)")).set(xlim=(0,10),ylim=(0,100))

g

plt.title("Title")
plt.show(g)

uniform_data=np.random.rand(10,12)
data=pd.DataFrame({'x':np.arange(1,101),
                   'y':np.random.normal(0,4,100)})

data

#scatterplot
iris=sns.load_dataset("iris")
sns.stripplot(x='species',
              y='petal_length',
              data=iris)

sns.swarmplot(x='species',
              y='petal_length',
              data=iris)
titanic=sns.load_dataset("titanic")

#BarPlot
sns.barplot(x='species',
            y='petal_length',
            data=iris)

sns.barplot(x='sex',
            y='survived',
            hue='class',
            data=titanic)

sns.barplot(x='sex',
            y='survived',
            hue='class',
            data=titanic)

#Count plot
sns.countplot(x='deck',
              data=titanic,
              palette='Greens_d')

#Point plot
sns.pointplot(x='class',
              y='survived',
              hue='sex',
              data=titanic,
              palette={"male":"g",
                       "female":"m"})

#boxplot
sns.boxplot(x="alive",
            y="age",
            data=titanic)

#violinplot
sns.violinplot(x='age',
               y='sex',
               hue='survived',
               data=titanic)

