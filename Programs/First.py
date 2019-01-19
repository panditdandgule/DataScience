#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 07:11:41 2018

@author: pandit
"""

import pandas as pd
melbourne_file_path =('/home/pandit/Downloads/Kaggle/melb_data.csv')
melbourne_data=pd.read_csv(melbourne_file_path)
melbourne_data.describe()

iowa_file_path=('/home/pandit/Downloads/Kaggle/train.csv')
home_data=pd.read_csv(iowa_file_path)
home_data.describe()

import datetime
now=datetime.datetime.now()
avg_lot_size=int(round(home_data['LotArea'].mean()))

newest_home_age=now.year-home_data['YearBuilt'].max()

home_data.describe()