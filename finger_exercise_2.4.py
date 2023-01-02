#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:57:29 2022

Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered. If no odd number was entered, it should print a message to that effect.

@author: Matt Wells
"""

maxOdd = None

for i in range(10):
    value = int(input("Input a number: "))
    
    if (value % 2 and (maxOdd is None or value > maxOdd)):
        maxOdd = value
    
    if maxOdd:
        print('The largest odd number entered was', maxOdd)
    else:
        print('No odd numbers were entered')
   