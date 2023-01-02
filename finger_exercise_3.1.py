#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 20:58:59 2023

Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print a message to that effect.

Note: integer**1 always sufices - flawed question? 

@author: Matt Wells
"""

integer = int(input("Input an integer: "))

root = 0

#checks for negative integers
if integer < 0:
    neg = True
else:
    neg = False
    
for pwr in range (0, 6):
    if integer > 0:
        while root <= integer:
            root += 1
            if root**pwr == integer:
                print('The root is ', root, 'and power is ', pwr)
        root = 0
    elif integer < 0:
        while root >= integer:
            root -= 1
            if root**pwr == integer:
                print('The root is ', root, 'and power is ', pwr)
        root = 0
    elif integer == 0:
        print('No such pair exists')
        break