#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:21:57 2019

@author: pandit
"""

import time
import os
import sys
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

tm = time.strftime('%Y-%m')
now = datetime.now()

import datetime
mydate = datetime.datetime.now()
curmonth=mydate.strftime("%B")

#files location here
path="/home/pandit/Downloads/Projects/Months"

#Read all data and store in list
#data=[]

listoffiles=os.listdir(path)
print(listoffiles)

if tm in listoffiles:
    with open(tm,'r') as f:
        for line in f.split():
            print(line)

for filename in listoffiles:
    if tm in filename:
        func()
        continue
            
        
        
        
        
        
def func():
    pass
        
        
        
        
        
        
        
        
def SupportJan():
    return " "
 
def SupportFeb():
    return "Successfully February"
 
def SupportMar():
    return "March"

def numbers_to_months(argument):
    
    switcher = {tm:SupportJan,
                February:SupportFeb,
                tm:SupportMar
            }
    # Get the function from switcher dictionary
    func = switcher.get(tm, "Nothing")
    # Execute the function
    print(func())
    
if __name__ =='__main__':
    numbers_to_months(tm)
