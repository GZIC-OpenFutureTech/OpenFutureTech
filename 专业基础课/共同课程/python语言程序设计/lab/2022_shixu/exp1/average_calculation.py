"""
average_calculation.py
author:张辰旭
date:2023.03.21
description:输入一个整数N求1-N的平均值
"""
n = int(input("input an interger"))
i = 0
m = 0
while i<=n:
    m += i
    i +=1
a = m / n
print(f"the average of the numble is :{a}")