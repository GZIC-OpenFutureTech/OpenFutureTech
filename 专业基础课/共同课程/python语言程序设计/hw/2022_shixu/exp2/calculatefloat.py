'''
calculatefloat.py
author:张辰旭
date:2023.03.28
description:计算浮点数
'''
from decimal import Decimal
def DecimalAdd(num1, num2):
    sum = Decimal(num1) + Decimal(num2)
    return sum

def DecimalSub(num1, num2):
    diff = Decimal(num1) - Decimal(num2)
    return diff

def FloatAdd(num1, num2):
    int1, dec1 = map(int, num1.split('.'))
    int2, dec2 = map(int, num2.split('.'))
    int_sum = int1 + int2
    dec_sum = dec1 + dec2
    if dec_sum >= 10 ** len(str(dec1)):
        int_sum += 1
        dec_sum -= 10 ** len(str(dec1))
    total = f"{int_sum}.{dec_sum:0>{len(str(dec1))}}"
    return total

def FloatSub(num1, num2):
    x1,y1 = num1.split('.')
    x2, y2 = num2.split('.')
    dec_1 = max(len(y1),len(y2))
    int1, dec1 = map(int, num1.split('.'))
    int2, dec2 = map(int, num2.split('.'))
    if (int1 > int2) or ((int1 == int2)and(dec1 >dec2)):
        if(dec1 < dec2):
            int1 = int1 - 1
            dec_sub = 10**dec_1+dec1-dec2
            int_sub = int1 - int2
            total = f"{int_sub}.{dec_sub}"
            return total
        else:
            dec_sub = dec1 - dec2
            int_sub = int1 - int2
            total = f"{int_sub}.{dec_sub}"
            return total
    else:
        a = dec1
        dec1 = dec2
        dec2 = a
        b = int1
        int1 = int2
        int2 = b
        if (dec1 < dec2):
            int1 = int1 - 1
            dec_sub = 10 ** dec_1 + dec1 - dec2
            int_sub = int1 - int2
            total = f"-{int_sub}.{dec_sub}"
            return total
        else:
            dec_sub = dec1 - dec2
            int_sub = int1 - int2
            total = f"-{int_sub}.{dec_sub}"
            return total


if __name__ == '__main__':
    print(DecimalAdd("0.1","0.2")==Decimal("0.3"))
    print(DecimalSub("0.4", "0.3")==Decimal("0.1"))
    print(DecimalSub("0.3", "0.2"))
    print(DecimalAdd("6.4", "6.2"))
    print(FloatAdd("0.1", "0.2")=="0.3")
    print(FloatAdd("6.4", "6.2"))
    print(FloatAdd("0.7", "4.4"))
    print(FloatSub("0.4", "0.3") == "0.1")
    print(FloatSub("0.3", "0.2"))
    print(FloatSub("6.4", "6.2"))
    print(FloatAdd("2.3333333", "3.2222222") == "5.5555555")
    print(FloatSub("2022.23", "4038.09")=="-2015.86" )
    print(FloatSub("9999.989", "8888.999")=="1110.990" )
