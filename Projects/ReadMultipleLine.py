#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 08:35:25 2019

@author: pandit
"""


import time
import datetime
import os
import sys
# import the smtplib module. It should be included in Python by default
import smtplib
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

tm = time.strftime('%Y-%m')

#files location here
path="/home/pandit/Downloads/Projects/Months/"+tm

contacts="/home/pandit/Downloads/Projects/Months/mycontacts.text"
messages="/home/pandit/Downloads/Projects/Months/message.text"

def get_contacts(filename):
    names = []
    emails = []
    dt=[] #for today date
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        today=time.strftime('%m%d')
        
        for a_contact in contacts_file.read():
            
            if today in a_contact:
                dt.append(a_contact.split()[0])
                names.append(a_contact.split()[1])
                emails.append(a_contact.split()[2])
                #a_contact=a_contact+a_contact
                print(a_contact)
                
    return dt, names, emails

def main():
    dt, names, emails = get_contacts(contacts)  # read contacts
    print(dt,names,emails) 
    
if __name__ == "__main__":
    main()