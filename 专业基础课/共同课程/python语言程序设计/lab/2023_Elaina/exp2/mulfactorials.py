"""
mulfactorials.py
author:Elaina
date:2023/10/30
description:calculate multiple factorials
"""

def factorial(n):
    ans = 1
    while(n != 1):
        ans *= n
        n -= 1
    return ans

num = int(input())
for n in range(num, 0, -1):
    print(factorial(n))
