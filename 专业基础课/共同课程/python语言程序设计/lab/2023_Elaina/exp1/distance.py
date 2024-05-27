"""
distance.py
author:Elaina
date:2023/10/23
description:compute the distance between two points
"""

x1,y1,x2,y2 = map(int, input().split())
print(pow(pow(x1-x2, 2)+pow(y1-y2, 2), 1/2))