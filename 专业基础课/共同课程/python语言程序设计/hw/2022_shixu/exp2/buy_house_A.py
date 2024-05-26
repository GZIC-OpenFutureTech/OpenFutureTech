'''
buy_house_A.py
author:张辰旭
date:2023.03.28
description:攒钱买房子，partA
'''
annual_salary = float(input("Enter your starting annual salary: "))
part_saved = float(input("Enter the portion of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment
months = 0
while current_savings < down_payment:
    monthly_saved = monthly_salary * part_saved
    current_savings += current_savings * r / 12
    current_savings += monthly_saved
    months += 1
print("Number of months:", months)
