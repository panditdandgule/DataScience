#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:57:47 2019

@author: pandit
"""

import re
p=re.compile('[a-e]')
print(p.findall("Are you working"))

p=re.compile('\d')
print(p.findall('i was born on 19th Feb 1991'))

p=re.compile('\d+')
print(p.findall('i was born on 19th Feb 1991'))

p=re.compile('\w')
print(p.findall('i was born on 19th Feb 1991'))

p=re.compile('\w+')
print(p.findall('i was born on 19th Feb 1991'))

p=re.compile('\W')
print(p.findall('i was born on 19th Feb 1991'))

p=re.compile('\W+')
print(p.findall('i was born on 19th Feb 1991'))

p=re.compile('ab*')
print(p.findall('i was born on 19th Feb 1991'))

from re import split
print(split('\W+','Words,words,'))

print(split('\W+','on 12th Jan 2019'))

print(split('\d+','on 12th Jan 2019'))

print(re.sub('ub','pan','Subject has been added'))

print(re.sub('ub','~!','Subject has been added'))

print(re.sub(r'\sAND\s','&','Baked beans and spans'))

regex=r"([a-zA-Z]+)(\d+)"

match=re.search(regex,"i was born in 1991")

print(match)

if match!=None:
    print("Match at index %s,%s"%(match.start(),match.end()))
    

string="hello my number is 9823438 and my friend's number  is 98774"

regex='\d+'

match=re.findall(regex,string)
print(match)

new_emails=set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+",text))

sentence='horses are fast'
regex=re.compile('(?P<animal>\w+)(?P<verb>\w+)(?P<adjective>\w+))

import re
pattern=re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
old='IPs :173.254.28.78 or 167.81.178.97'

new_ip='127.0.0.1'

replaced=re.sub(pattern,new_ip,old)

print('replaced=%s'%(replaced))


