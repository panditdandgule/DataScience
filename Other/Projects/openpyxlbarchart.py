#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:04:33 2019

@author: pandit
"""

#import openpyxl module
import openpyxl

#import Barchart class from openpyxl.chart sub_module

from openpyxl.chart import BarChart,Reference

#call a workbook() function of oepnpyxl
#to create a new blank workbook object
wb=openpyxl.Workbook()

#Get workbook active sheet from the active attribute
sheet=wb.active

#write 0 to 9 in 1st column of the active sheet
for i in range(10):
    sheet.append([i])
    
#Create data for plotting
values=Reference(sheet,min_col=1,min_row=1,max_col=1,max_row=10)


#Create object of BarChart class
chart=BarChart()

#Adding data to the Bar chart object
chart.add_data(values)

#set the title of the chart
chart.title="BAR-CHART"

#set the title of the x-axis
chart.x_axis.title="X_AXIS"

#set the title of the y-axis
chart.y_axis.title="Y_AXIS"

#add chart to the sheet
#the top-left corner of a chart
#is anchored to cell E2

sheet.add_chart(chart,"E2")

#save the file
wb.save("/home/pandit/Downloads/Projects/barChart.xlsx")
