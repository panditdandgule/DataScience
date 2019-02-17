#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 21:29:30 2019

@author: pandit
"""
#Reading an excel file using Python
import xlrd

#Give the location of the file
loc=("/home/pandit/Downloads/Projects/2019-excel-calendar-holidays-landscape.xls")

#To open workbook
wb=xlrd.open_workbook(loc)
sheet=wb.sheet_by_index(1)

#For row 0 and column 0
sheet.cell_value(0,0)

#Extracting number of rows
print(sheet.nrows)

print(sheet.ncols)

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))
    
for i in range(sheet.nrows):
    print(sheet.cell_value(i,0))
    
#Extract particular row value
sheet.cell_value(0,0)

print(sheet.row_values(i))

    