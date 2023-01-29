#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 07:35:56 2023

When the implementation of fib in Figure 4.7 is used to compute fib(5), how many times does it compute the value fib(2)?

@author: Matt Wells
"""

def fib(n):
    """Assumes n int >= 0
    Returns Fibonacci of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def testFib(n):
    for i in range(n+1):
        print('fib of', i, '=', fib(i))
        
testFib(5) 