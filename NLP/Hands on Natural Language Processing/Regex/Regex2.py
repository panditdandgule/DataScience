#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:11:41 2019

@author: pandit
"""

import re

pattern1="Apples are tasty"
pattern2="Today I feel like crying."

if re.match(r"^Apples",pattern1):
    print("Matches!")
else:
    print("No Match!")
if re.search(r"\.$",pattern2):
    print("Match!")
else:
    print("No Match!")