#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 09:27:42 2022

You want to set a particular goal, e.g. to be able to afford the down payment in three years. How much should you save each month to achieve this? In this problem, you are going to write a program to answer that question. To simplify things, assume:
    
1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)
3. The down payment is 0.25 (25%) of the cost of the house
4. The cost of the house that you are saving for is $1M.

You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of the required down payment.

You should use ​bisection search​ to help you do this efficiently. You should keep track of the number of steps it takes your bisections search to finish.

@author: Matt Wells
"""

starting_salary = int(input("Enter annual salary: "))
semi_annual_raise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
months = 36

#set bisectional search bounds
min_rate = 0        # 0%
max_rate = 10000    # 100%
steps = 0

portion_saved = int((max_rate + min_rate) / 2)
found = False

while abs(min_rate - max_rate) > 1:
    steps += 1
    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)
    current_savings = 0.0

    for i in range(1, months + 1):
        monthly_return = current_savings * (annual_return / 12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - portion_down_payment) < 100:
            min_rate = max_rate
            found = True
            break
        elif current_savings > portion_down_payment + 100:
            break
        
        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)

    if current_savings < portion_down_payment - 100:
        min_rate = portion_saved
    elif current_savings > portion_down_payment + 100:
        max_rate = portion_saved
    
    portion_saved = int((max_rate + min_rate) / 2)
    
if found:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search", steps)
else:
    print("Is is not possible to pay the down payment in three years")