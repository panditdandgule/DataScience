#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:57:29 2019

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
mydate.strftime("%B")

#files location here
path="/home/pandit/Downloads/Projects/Months"

#Read all data and store in list
#data=[]

listoffiles=os.listdir(path)
#print(listoffiles)


        
def checkWeekendsupport():
    print('Entry')
    try:
        with open(tm,'r') as f:
            print('Entry1')
            today=time.strftime('%m%d')
            flag=0
            for line in f:
                if today in line:
                    line=line.split(' ')
                    flag=1
                    #line[1] contains Name and line[2] contains surname
                    os.system('notify-send "BAS Offshore Support Tomorrow:'+line[1] +' ' +line[2]+'"')
            if flag==0:
                os.system('notify-send "No Support Today!"')
    except FileNotFoundError:
        print("Could not read file:", tm )
        #sys.exit()
        
if __name__ == '__main__':
    for filename in listoffiles:
        if tm in filename:
            checkWeekendsupport()
            break
        else:
            continue