"""
svemoneyB.py
author:Elaina
date:2023/10/30
description:calculate how long can we bug a house
"""
# init
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))
monthly_salary = annual_salary / 12
annual_return_rate = 0.04
current_savings = 0
portion_down_payment = 0.25

cnt = 0
while(current_savings < total_cost*portion_down_payment):
    current_savings += current_savings*annual_return_rate/12
    current_savings += monthly_salary*portion_saved
    cnt += 1
    if(cnt%6 == 0): monthly_salary += monthly_salary*semi_annual_raise
print(cnt)