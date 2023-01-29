#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 07:53:59 2023

Finger Exercise: Implement a function that satisfies the specification.

@author: Matt Wells
"""

l = [1, 3, 6, 5] #test case
i = None

def findAnEven(l):
    """Assumes l is a list of integers
       Returns the first even number in l
       Raises ValueError if l does not contain an even number"""
    
    for i in l:
        if i % 2 == 0:
            return i
    raise ValueError("l does not contain an even number")

print(findAnEven(l))
        