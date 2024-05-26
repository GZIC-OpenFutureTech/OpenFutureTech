"""
playmath.py
author:Elaina
date:2023/10/30
description:play with some of the functions provided in the package math
"""

def MathTest(x):
    y = x*math.pow(math.e, -x) + math.sqrt(1-math.pow(math.e, -x))
    return y

import math
angletest = math.sin(math.pi/4) + math.cos(math.pi/4)/2
ceillingtest = math.ceil(276/19) + 2*math.log(12, 7)
print(angletest)
print(ceillingtest)
print(MathTest(5))
print(MathTest(0))