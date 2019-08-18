#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 22:31:05 2019

@author: pandit
"""

#writing to excel sheets using python

import xlwt
from xlwt import Workbook

#Workbook is created
wb=Workbook()

#add_sheet is used to create sheet.
sheet1=wb.add_sheet('Sheet 1')

sheet1.write(1,0,'Pandit Dandgule')
sheet1.write(2,0,'Amol shinde')

wb.save('xlwt example.xls')


#Adding style sheet in excel

import xlwt

workbook=xlwt.Workbook()
sheet=workbook.add_sheet("Sheet Name")

#Specifying style
style=xlwt.easyxf('font:bold 1')

#Specifying column
sheet.write(0,0,'SAMPLE',style)
workbook.save("sample.xls")

