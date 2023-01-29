#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 08:13:13 2023

Implement a function that meets the specification below. Use a try-except block.

@author: Matt Wells
"""

def sumDigits(s):
    """Assumes s is a string and returns the sum of the decimal digits in s. For example, if s is 'a2b3c' it returns 5."""
    
    sum = 0 
    
    try:
        for i in range(len(s)):
            if s[i].isdigit():
                sum += int(s[i])
        return sum
    except TypeError:
        print("Input is not of type string")
    