#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:01:32 2022

Copy your solution to Part A (as we are going to reuse much of that machinery). Modify your program to include the following.

1. Have the user input a semi-annual salary raise ​semi_annual_raise​ (as a decimal percentage).
2. After the 6t​h​ month, increase your salary by that percentage. Do the same after the 12t​h month, the 18​th​ month, and so on.

Write a program to calculate how many months it will take you save up enough money for a down payment. LIke before, assume that your investments earn a return of ​r​ = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
    
1. The starting annual salary (annual_salary)
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semi­annual salary raise (semi_annual_raise)

@author: Matt Wells
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter semi-annual raise as decimal: "))

monthly_saved = (annual_salary / 12.0) * portion_saved

portion_down_payment = total_cost * 0.25

current_savings = 0.0
annual_return = 0.04

months = 0

while current_savings < portion_down_payment:
    months += 1
    monthly_return = (current_savings * annual_return) / 12
    current_savings += monthly_return + monthly_saved
    
    #new code to account for semi-annual raises
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_saved = (annual_salary / 12) * portion_saved

print("Number of months to save down payment:", months)

