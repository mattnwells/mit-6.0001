#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 20:06:16 2023

Write a function isIn that accepts two strings as arguments and returns True if either string occurs anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operation in.

@author: Matt Wells
"""

def isIn(string1, string2):
    return bool((string1 in string2) or (string2 in string1))

x = input('Input string1: ')
y = input('Input string2: ')

print(isIn(x, y))