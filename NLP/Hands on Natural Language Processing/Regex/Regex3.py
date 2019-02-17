#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:17:25 2019

@author: pandit
"""

import re

pattern1="I love Avengers"

print(re.sub(r"Avengers","Justice League",pattern1))

print(re.sub(r"[a-z]","0",pattern1,1,flags=re.I))