#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 12:59:31 2022

Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints the sum of the numbers in s.

@author: Matt Wells
"""

sum = 0

for s in ('1.23', '2.4', '3.123'):
    sum += float(s)
    
print(sum)

