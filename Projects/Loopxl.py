#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:16:23 2019

@author: pandit
"""

#import module
import xlrd

#file path
path="/home/pandit/Downloads/Projects/2019-excel-calendar-holidays-landscape.xls"

#open workbook
book=xlrd.open_workbook(path)

sheet=book.sheet_by_index(1)

print(sheet)
#read header values into the list
keys=[sheet.cell(0,col_index).value for col_index in range(sheet.ncols)]

print(keys)

dict_list=[]
for row_index in range(1,sheet.nrows):
    print(sheet.nrows)
    d={keys[col_index]: sheet.cell(row_index,col_index).value
       for col_index in range(sheet.ncols)}
    dict_list.append(d)
    
print(dict_list)
print(" ".join(dict_list))

