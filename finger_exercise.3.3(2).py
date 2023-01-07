#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 17:18:05 2023

What would have to be changed to make the code in Figure 3.4 work for finding an approximation to the cube root of both negative and positive numbers? (Hint: think about changing low to ensure that the answer lies within the region being searched.)

@author: Matt Wells
"""

number = int(input('Input a number: '))
x = abs(number)
epsilon = 0.01
numGuesses = 0

low = 0.0
high = max(1.0, x)

ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans 
    else:
        high = ans
    ans = (high + low) / 2.0
    
print('numGuesses =', numGuesses)

if number < 0:
    ans = -ans
    
print(ans, 'is close to square root of', x)
