"""
calculatefloat.py
author:Elaina
date:2023/10/30
description:Find int roots of cubic equation
"""

import math
import cmath

eps = 1e-6

def zero(x):
    return -eps <= x and x <= eps

def FindIntRootsOfCubic(a,b,c,d):
    p = -((b*b - 3*a*c)/(3*a*a))
    q = (2*b*b*b - 9*a*b*c + 27*a*a*d)/(27*a*a*a)
    w1 = complex(-1/2, math.sqrt(3)/2)
    w2 = complex(-1/2, -math.sqrt(3)/2)
    if (zero(p)):
        if (q <= 0.0):
            y1 = pow(-q, 1.0/3.0)
        else:
    	    y1 = -pow(q, 1.0/3.0)
        y2 = y1 * w1
        y3 = y1 * w2
    else:
        f = q / 2
        g = p / 3
        delta = pow(f,2)+pow(g,3)
        if(delta >= 0.0): 
            u = math.sqrt(delta)
            if (zero(u-f)):
                u = -u-f
            else:
                u = u-f
        else:
            u = cmath.sqrt(delta)-f
        u = pow(u, 1/3)
        v = -g/u
        y1 = u+v
        y2 = u*w1+v*w2
        y3 = u*w2+v*w1
    x1,x2,x3 = y1-b/(3*a),y2-b/(3*a),y3-b/(3*a)
    return (x1,x2,x3)

(x1,x2,x3) = FindIntRootsOfCubic(2,6,12,10)
print(x1,x2,x3)
(x1,x2,x3) = FindIntRootsOfCubic(1,3,3,1)
print(x1,x2,x3)