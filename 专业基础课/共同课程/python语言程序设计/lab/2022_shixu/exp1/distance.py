"""
distance.py
author:张辰旭
date:2023.03.21
description:计算二维空间内两点间距离
"""
import math
#Enter four numbers separated by “，”
print("Enter four numbers separated by “，”")
x1,y1,x2,y2 = eval(input())
d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print(d)