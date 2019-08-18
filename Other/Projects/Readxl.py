#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:00:42 2019

@author: pandit
"""
#import module
import xlrd

#file path
path="/home/pandit/Downloads/Projects/2019-excel-calendar-holidays-landscape.xls"

#open workbook
xl_workbook=xlrd.open_workbook(path)

#list out sheet names
sheet_names=xl_workbook.sheet_names()
print('Sheet Names',sheet_names)

xl_sheet=xl_workbook.sheet_by_name(sheet_names[0])

xl_sheet=xl_workbook.sheet_by_index(0)
print ('Sheet name: %s' % xl_sheet.name)

#Pull the first row of index
row = xl_sheet.row(0)  # 1st row

print(row)
