"""
calculatefloat.py
author:Elaina
date:2023/10/30
description:test float(high precision operations)
"""

import math
import decimal
from decimal import Decimal

def DecimalAdd(a, b):
    a = Decimal(a)
    b = Decimal(b)
    return a+b

def DecimalSub(a, b):
    a = Decimal(a)
    b = Decimal(b)
    return a-b

def GetDecimalLength(s:str):
    i = 0
    for i in range(0, len(s)-1, 1):
        if(s[i] == '.'): 
            break
    s2 = s[i:-1]
    return len(s2)

def FloatAdd(a:str, b:str):
    length = max(GetDecimalLength(a), GetDecimalLength(b))
    a = float(a)
    b = float(b)
    ans = round(a+b, length)
    if(ans == 0.0):
        return "0"
    return str(ans)

def FloatSub(a:str, b:str):
    length = max(GetDecimalLength(a), GetDecimalLength(b))
    a = float(a)
    b = float(b)
    ans = round(a-b, length)
    if(ans == 0.0):
        return "0"
    return str(ans)

# print(DecimalAdd("0.1", "0.2") == Decimal("0.3"))
# print(DecimalSub("0.4", "0.3") == Decimal("0.1"))
# print(DecimalSub("0.3", "0.2"))
# print(DecimalAdd("6.4", "6.2"))

print(FloatAdd("0.1", "0.2") == "0.3")
print(FloatAdd("6.4", "6.2"))
print(FloatAdd("0.7", "4.4"))

print(FloatSub("0.4", "0.3") == "0.1")
print(FloatSub("0.3", "0.2"))
print(FloatSub("6.4", "6.2"))