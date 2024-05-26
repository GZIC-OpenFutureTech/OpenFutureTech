"""
test_operator.py
author:张辰旭
date:2023.03.21
description:检测浮点数之间运算的结果
"""
import math
#First set of questions to show
a = 3*4
b = 3.0 * 4
c = 4* 3.0
d = 3.0 *4.0
print("First set of questions to show")
print(a,b,c,d)
#Second set of questions to show
a = 12 / 3
b = 1/3
c = 12/3.0
d = 12.0/3
print("Second set of questions to show")
print(a,b,c,d)
#Third set of questions to show
a = 2**2
b = 2**2.0
c = 2.0*2
print("Third set of questions to show")
print("a.using **")
print(a , b,c)
a = math.pow(2,2)
b = math.pow(2,2.0)
c = math.pow(2.0,2.0)
print("b.using math.pow()")
print(a,b,c)
#forth set of questions to show
a = math.sqrt(7+9)
b = math.pow(100-19,1/4)
print("forth set of questions to show")
print(a,b)


