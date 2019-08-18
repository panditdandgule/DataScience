#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:21:57 2019

@author: pandit

BAS Automatic Email for WeekEnd Support 
Ref :https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
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
def checkWeekendsupport():
    try:
        with open(path,'r',encoding='utf-8') as f:
            today=time.strftime('%m%d')
            flag=0
            for line in f:
                if today in line:
                    line=line.split(' ')
                    flag=1
                    #line[1] contains Name and line[2] contains surname
                    os.system('notify-send "BAS Offshore Support This Weekend :'+line[0] +' ' +line[1]+' ' +line[2]+'"')
            if flag==0:
                os.system('notify-send "No Support This Weekend!"')
    except FileNotFoundError:
        print("Could not read file:", path )
        #sys.exit()
     
# Function to read the contacts from a given contact file and return a
# list of names and email addresses
contacts="/home/pandit/Downloads/Projects/Months/mycontacts.text"
messages="/home/pandit/Downloads/Projects/Months/message.text"

def get_contacts(filename):
    names = []
    emails = []
    dt=[] #for today date
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        today=time.strftime('%m%d')
        for a_contact in contacts_file:
            if today in a_contact:
                dt.append(a_contact.split()[0])
                names.append(a_contact.split()[1])
                emails.append(a_contact.split()[2])
                a_contact=a_contact+a_contact
                
    return dt, names, emails

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    mydate = datetime.datetime.now()
    monthnm=mydate.strftime("%B")
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port='587')
    s.starttls()
    s.login("panditdandgule777@gmail.com", "password9623639868")

    dt, names, emails = get_contacts(contacts)  # read contacts
    message_template = read_template(messages)
    # For each contact, send the email:
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From']="panditdandgule777@gamil.com"
        msg['To']=email
        msg['Cc']="amols693@gmail.com"
        msg['Subject']="BAS Offshore Weekend Support "+monthnm+ ' '+"2019"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        s.send_message(msg)
    
        del msg
    s.quit()
    
if __name__ == '__main__':
    checkWeekendsupport()
    main()