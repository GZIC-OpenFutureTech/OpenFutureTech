'''
mulfactorials.py
author:张辰旭
date:2023.03.28
description:计算阶乘
'''
#计算阶乘
def factorial(n):
   if n==0 or n==1:
       return 1
   else:
       return n*factorial(n-1)

if __name__ == '__main__':
   m = int(input("input an interger:"))
   for i in range(m,0,-1):
       print(factorial(i))
