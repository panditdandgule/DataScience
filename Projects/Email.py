#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 20:32:06 2019

@author: pandit
"""

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr="panditdandgule777@gmail.com"
toaddr="dandgulepandit@gmail.com"

msg=MIMEMultipart()
msg['From']=fromaddr
msg['To']=toaddr
msg['Subject']='Prfessional Email Testing'

body="Welcome to first email"
msg.attach(MIMEText(body,'plain'))

server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(fromaddr,"password9623639868")
text=msg.as_string()
server.sendmail(fromaddr,toaddr,text)
server.quit()