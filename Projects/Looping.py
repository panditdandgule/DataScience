#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 07:08:51 2019

@author: pandit
"""

#import module
import xlrd
import json

#file path
path="/home/pandit/Downloads/Projects/2019-excel-calendar-holidays-landscape.xls"

#open workbook
wb=xlrd.open_workbook(path,'r')

wb_sheet=wb.sheet_by_index(0)

values=[]

for col_idx in range(1,wb_sheet.ncols):
    values.append(wb_sheet.cell_value(0,col_idx))
    
    for row_idx in range(1,wb_sheet.nrows):
        values.append(wb_sheet.cell_value(row_idx,0))
print(values)

for col_idx in range(wb_sheet.ncols):
    values.append(wb_sheet.cell_value(1,col_idx))
    for row_idx in range(wb_sheet.nrows):
        values.append(wb_sheet.cell_value(row_idx,1))
print(values)