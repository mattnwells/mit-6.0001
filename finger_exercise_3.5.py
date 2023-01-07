#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  6 18:29:12 2023

Add some code to the implementation of Newton-Raphson that keeps track of the number of iterations used to find the root. Use that code as part of a program that compares the efficiency of Newton-Raphson and bisection search. (You should discover that Newton-Raphson is more efficient.)

@author: Matt Wells
"""

number = int(input('Input a number: '))

#Bisectional search

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
    
print('Number of guesses: ', numGuesses)

if number < 0:
    ans = -ans
    
print(ans, 'is close to square root of', x)


#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0 epsilon = 0.01

epsilon = 0.01

k = number

guess = k / 2.0
num_guess = 0

while abs(guess * guess - k) >= epsilon:
    num_guess += 1
    guess = guess - (((guess**2) - k)/(2*guess))
print('Number of guesses:', num_guess)
print('Square root of', k, 'is about', guess)
