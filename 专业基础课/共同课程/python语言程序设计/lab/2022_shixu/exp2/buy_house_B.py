'''
buy_house_B.py
author:张辰旭
date:2023.03.28
description:攒钱买房子，partB
'''
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percentage of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual salary raise, as a decimal: "))
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary / 12
months = 0
down_payment = total_cost * portion_down_payment
while current_savings < down_payment:
    if months > 0 and months % 6 == 0:
        monthly_salary *= (1 + semi_annual_raise)
    current_savings += current_savings * r / 12
    current_savings += monthly_salary * portion_saved
    months += 1
print("Number of months:", months)
