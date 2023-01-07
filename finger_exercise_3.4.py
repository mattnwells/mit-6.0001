#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:34:13 2023

What is the decimal equivalent of the binary number 10011?

@author: Matt Wells

Solution: 
    
10011

(1*2)**4 + (0x2)**3 + (0x2)**2 + (1x2)**1 + (1x2)**0 = 
16 + 0 + 0 + 2 + 1 =
19
"""

binNumber = '10011'
pwr = 0
number = 0

for i in reversed(binNumber):
    number = number + int(i)*2**pwr
    pwr += 1
    
print (number)