#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 07:56:25 2019

@author: pandit
"""
#Time module is must as reminder is set with the help of dates
import time

#os module is used to notify user using default "Ubuntu" notification bar
import os

'''
January text file is the one in which the actual support and
dates are present. This file can be manually edited or can be automated
For simplicity, we will edit it manually.
dates should be written in this file in the format:
    "MonthDay Name Surname" (Without Quotes)
'''

File='/home/pandit/Downloads/Projects/January_2019'

def checkWeekendSupport():
    fileName=open(File,'r')
    today=time.strftime('%m%d')
    flag=0
    for line in fileName:
        if today in line:
            line=line.split(' ')
            flag=1
            #line[1] contains Name and line[2] contains Surname
            os.system('notify-send "Support This Weekend:'+line[1]+' '+line[2]+'"')
    if flag==0:
        os.system('notify-send "No Support This weekend!"')
        
if __name__ =='__main__':
    checkWeekendSupport()
