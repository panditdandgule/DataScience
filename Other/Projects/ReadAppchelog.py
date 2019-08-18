#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 09:29:54 2019

@author: pandit
"""

import re

path="/media/pandit/ECE41556E41523FC/PYTHON/Ethens/Project/Projects/access_log"
newipdata=[]

try:
    with open(path,'r') as f:
        for line in f.read().split():
            ip1=re.findall(r"\d{1,2}\.\d{1,3}\.\d{1,2}\.\d{1,2}",line)
            for ip in ip1:
                newipdata.append(ip)
       
except Exception as e:
    print("File not found",e)       
path1="/media/pandit/ECE41556E41523FC/PYTHON/Ethens/Project/Projects/"    
try:
    with open(path1+"writelog.text",'w+') as f:
        f.write("\n".join(newipdata))
        for line in f:
            count(line)
            
except Exception as e:
    print("Something wrong during write file",e)
    
else:
    print()
    print("*"*100)
    print("Successfully written below ip address in file")
    print("*"*100)
    print(newipdata)
    print()
    print("*"*100)
    print("Number of Address:",len(newipdata))