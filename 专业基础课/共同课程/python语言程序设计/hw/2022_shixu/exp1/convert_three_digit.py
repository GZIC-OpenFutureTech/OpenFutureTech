"""
convert_three_digit.py
author:张辰旭
date:2023.03.21
description:将三位数的个十百位分开
"""
n = int(input("inputs a three-digit natural number"))
a = n // 100
b = n //10 % 10
c = n % 10
print("The numbers in the hundreds,tens and ones digit are:",a,",",b,",",c,"separately" )