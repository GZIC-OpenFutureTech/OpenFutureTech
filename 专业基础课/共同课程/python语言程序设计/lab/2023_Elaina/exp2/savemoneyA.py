"""
savemoneyA.py
author:Elaina
date:2023/10/30
description:calculate how long can we bug a house
"""
# init
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
monthly_salary = annual_salary / 12
annual_return_rate = 0.04
current_savings = 0
portion_down_payment = 0.25

cnt = 0
while(current_savings < total_cost*portion_down_payment):
    current_savings += current_savings*annual_return_rate/12
    current_savings += monthly_salary*portion_saved
    cnt += 1
print(cnt)