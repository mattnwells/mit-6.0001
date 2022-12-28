#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:58:49 2022

Write a program that examines three variables—x, y, and z— and prints the largest odd number among them. If none of them are odd, it should print a message to that effect.

@author: Matt Wells
"""

x = int(input("Input a number x: "))
y = int(input("Input a number y: "))
z = int(input("Input a number z: "))

try:
    largest = max(val for val in (x,y,z) if val % 2)
    print(largest)
except ValueError:
    print('All numbers are even')
        