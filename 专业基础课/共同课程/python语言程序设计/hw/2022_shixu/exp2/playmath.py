'''
playmath.py
author:张辰旭
date:2023.03.28
description:math库的使用
'''
import math
def MathTest(x):
    e = math.e
    y = x*math.pow(e,-x)+math.sqrt(1-math.pow(e,-x))
    return y

if __name__ == '__main__':
    pi = math.pi
    ans_1 = math.sin(pi/4)+math.cos(pi/4)/2
    ans_2 = math.ceil(276/19)+2*math.log(12,7)
    x = float(input("input a numble"))
    ans_3 = MathTest(x)
    print("answer1:",ans_1)
    print("answer2:", ans_2)
    print("answer3:", ans_3)