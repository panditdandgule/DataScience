#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 09:10:41 2019

@author: pandit
#Birthday Reminder Application
"""

import time
#os module is used to notify user
#using default "Ubuntu" Notification bar
import os
#Birthday file is the one in which the actual birthdays
#and dates are present. This file can bem manually editied
#or can be automated.
#For simplicity, we will edit it manually.
#Birthdays should be written in this file in 
#the format: "MonthDay Name Surname"(without Quotes)

birthdayFile='/home/pandit/Downloads/NLP/Projects/BirthdayFile'

def checkTodayBirthdays():
    fileName=open(birthdayFile,'r')
    today=time.strftime('%m%d')
    flag=0
    for line in fileName:
        if today in line:
            line=line.split(' ')
            flag=1
            # line[1] contains Name and line[2] contains Surname 
            os.system('notify-send "Birthdays Today: ' + line[1] 
            + ' ' + line[2] + '"') 
    if flag==0:
        os.system('notify-send "No Birthday Today"')
            
if __name__=="__main__":
    checkTodayBirthdays()

