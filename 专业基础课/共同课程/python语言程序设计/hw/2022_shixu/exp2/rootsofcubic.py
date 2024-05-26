'''
rootsofcubic.py
author:张辰旭
date:2023.03.28
description:解一元三次方程
'''
def FindIntRootsOfCubic(a, b, c, d):
    p = -b / (3 * a)
    q = p ** 3 + (b * c - 3 * a * d) / (6 * a ** 2)
    r = c / (3 * a)
    x1 = (q + (q ** 2 + (r - p ** 2) ** 3) ** (1 / 2)) ** (1 / 3) + (q - (q ** 2 + (r - p ** 2) ** 3) ** (1 / 2)) ** (1 / 3) + p
    x2 = (-b-x1*a+(b**2-4*a*c-2*a*b*x1-3*a*a*x1*x1)**(1/2))/(2*a)
    x3 = (-b - x1 * a - (b ** 2 - 4 * a * c - 2 * a * b * x1 - 3 * a * a * x1 * x1) ** (1 / 2)) / (2 * a)
    x_1 = int(round(x1.real))
    x_2 = int(round(x2.real))
    x_3 = int(round(x3.real))
    roots = [x_1, x_2, x_3]
    roots.sort()
    return tuple(roots)

if __name__ == '__main__':
    print(FindIntRootsOfCubic(2,6,12,10))
