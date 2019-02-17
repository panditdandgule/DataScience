#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 08:39:38 2019

@author: pandit
"""

#The glob module finds all the path names matching a specified pattern.
import time
import os
import sys
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

tm = time.strftime('%Y-%m')
now = datetime.now()

#files location here
path="/home/pandit/Downloads/Projects/Months"

#Read all data and store in list
#data=[]

#listoffiles=os.listdir(path)
#print(listoffiles)

path="/home/pandit/Downloads/Projects/Months/2019-02"


def checkWeekendsupport():
    try:
        with open(path,'r') as f:
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
        print("Could not read file:", path )
        #sys.exit()
        
      


def sendemail():
    fromaddr="panditdandgule777@gmail.com"
    toaddr="dandgule@gmail.com,panditdandgule777@gmail.com"

    msg=MIMEMultipart()
    msg['From']=fromaddr
    msg['To']=toaddr
    msg['Subject']='BAS Offshore Weekend Support'
    
    body="This is remainder email for you..!\n"+"\n\n"+"Please reach out to Jambeer if any issue.\n\n"+"Thank You..!"
    msg.attach(MIMEText(body,'plain'))

    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(fromaddr,"password9623639868")
    text=msg.as_string()
    server.sendmail(fromaddr,toaddr,text)
    server.quit()
    
if __name__ == '__main__':
    checkWeekendsupport()
    sendemail()
    
    
'''
if tm in listoffiles:
    filename=open(tm,'r')
    print("pandit")
    with open(filename,'r') as f:
        for line in f.split():
            data.append(line)
print(data)
'''