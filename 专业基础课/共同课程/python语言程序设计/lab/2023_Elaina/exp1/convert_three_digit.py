"""
convert_three_digit.py
author:Elaina
date:2023/10/23
description:ouput each digit of a three-bits number
"""

n = int(input())
d1 = n // 100
d2 = n // 10 % 10
d3 = n % 10
#print("The numbers in the hundreds, tens and ones digit are %d, %d, %d separately." %d1 %d2 %d3)
print(f'The numbers in the hundreds, tens and ones digit are {d1}, {d2}, {d3} separately.')