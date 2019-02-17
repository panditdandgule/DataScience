#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 06:44:48 2019

@author: pandit
"""

'''
^ matches the beginning of a string
$ matches the end of a string
\b matches a word boundary
\d matches any numeric digit
\D matches any non-numeric character
(x|y|z) matches exactly one of x,y or z
x? matches an optional x charcter (in other words, it matches an x zero or one times)
x* matches zero or more times
x+ matches x one or more times
x{m,n} matches an x character at least m times, but not more than n times
?: matches an expression but do not capture it. Non capturing group
?= matches an suffix but exclude it from capture. Positive look ahead
?! matches if suffix is absent. Negative look ahead.
a(?!b) will match the "a" in "ac", but not the "a" in "ab"
?<= positive look behind
?<! negative look behind
'''

import re

pattern=re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
old='IPS:173.254.28.78 or 167.81.178.97'

new_ip='127.0.0.1'

replaced=re.sub(pattern,new_ip,old)

print('replaced=%s' %(replaced))

#re.sub() -The re.sub() function regular expression-based string sub

re.search('[abc]','space')

re.sub('[abc]','o','space')

re.sub('[aeu]','n',re.sub('[abc]','o','Space'))

#match phone number

re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')

re.compile(r'(\d{3})-(\d{3})-(\d{4})-(\d+)')

re.compile(r'(\d{3})\D+(\d{3})\D+(\d{4})$')

phone_re=re.compile(r'(\d{3})(\d{3})(\d{4})')

phone_re=re.compile(r'''(\d{3} |(\d{3}\))
                        (:?\s+|-|\.)?
                        (\d{3})
                        (:?\s+|-|\.)?
                        ''', re.VERBOSE)